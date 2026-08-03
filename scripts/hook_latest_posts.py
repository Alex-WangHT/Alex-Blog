"""MkDocs hook：自动扫描博客文章，生成首页最新推文列表。

在 docs/index.md 中插入 <!-- LATEST_POSTS --> 占位符，
构建时自动替换为按日期排序的文章卡片 HTML。
"""

import os
import re
from datetime import datetime

import yaml

POSTS_DIR = "tech-blog/posts"
PLACEHOLDER = "<!-- LATEST_POSTS -->"
MAX_POSTS = 5


def _parse_front_matter(content: str):
    """解析 YAML front matter，返回 (meta_dict, markdown_body)。"""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                meta = {}
            return meta, parts[2]
    return {}, content


def _extract_title(md_body: str) -> str:
    """从 Markdown 正文中提取第一个 H1 标题。"""
    for line in md_body.split("\n"):
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return "Untitled"


def _extract_excerpt(md_body: str) -> str:
    """提取文章摘要（<!-- more --> 之前或第一段非空非标题文本）。"""
    if "<!-- more -->" in md_body:
        text = md_body.split("<!-- more -->")[0]
    else:
        text = md_body

    # 在目标区域内找第一个非空、非标题、非分隔符的行
    for line in text.split("\n"):
        s = line.strip()
        if s and not s.startswith("#") and not s.startswith("---"):
            part = s
            break
    else:
        part = ""

    # 清理 Markdown 标记
    excerpt = re.sub(r'[#*>`~\[\]\(\)!]', "", part).strip()
    if len(excerpt) > 120:
        excerpt = excerpt[:120] + "..."
    return excerpt


def _slugify(text: str) -> str:
    """生成 URL slug，与 Material blog 插件的行为保持一致。"""
    text = text.lower()
    # 移除中文/英文冒号
    text = re.sub(r"[：:]", "", text)
    # 移除其他标点，保留字母数字中文和空格
    text = re.sub(r"[^\w\s-]", "", text)
    # 空白字符替换为 -
    text = re.sub(r"[\s]+", "-", text)
    # 去掉首尾 -
    text = text.strip("-")
    return text


def _read_posts(config):
    """扫描博客文章目录，返回按日期倒序排列的文章列表。"""
    docs_dir = config.docs_dir
    posts_path = os.path.join(docs_dir, POSTS_DIR)

    if not os.path.isdir(posts_path):
        return []

    posts = []
    for filename in os.listdir(posts_path):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(posts_path, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        meta, md_body = _parse_front_matter(content)
        title = _extract_title(md_body)

        # 解析日期
        date_raw = meta.get("date")
        if isinstance(date_raw, dict):
            date_raw = date_raw.get("created", "")
        if isinstance(date_raw, datetime):
            date = date_raw
        else:
            try:
                date = datetime.strptime(str(date_raw), "%Y-%m-%d")
            except (ValueError, TypeError):
                date = datetime.fromtimestamp(os.path.getmtime(filepath))

        excerpt = _extract_excerpt(md_body)
        tags = meta.get("tags", []) or []

        posts.append(
            {
                "title": title,
                "date": date,
                "excerpt": excerpt,
                "tags": tags,
                "slug": _slugify(title),
            }
        )

    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts[:MAX_POSTS]


def _render_post_card(post: dict) -> str:
    """渲染单篇文章的 HTML 卡片。"""
    date_str = post["date"].strftime("%Y-%m-%d")
    url = f"tech-blog/{post['date'].strftime('%Y/%m/%d')}/{post['slug']}/"

    tags_html = "\n".join(
        f'<span style="font-size:.75rem;padding:.15rem .5rem;border-radius:999px;background:var(--md-default-fg-color--lightest);color:var(--md-default-fg-color--light);">{tag}</span>'
        for tag in post["tags"]
    )

    return f"""<a href="{url}" class="post-item" style="display:block;padding:1.25rem 1.5rem;border-radius:.5rem;border:1px solid var(--md-default-fg-color--lightest);text-decoration:none;color:inherit;transition:transform .15s,box-shadow .15s,background .15s;box-shadow:0 1px 3px rgba(0,0,0,.04);">
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.5rem;">
    <h3 style="margin:0;font-size:1.05rem;font-weight:600;">{post["title"]}</h3>
    <time style="font-size:.8rem;color:var(--md-default-fg-color--light);white-space:nowrap;">{date_str}</time>
  </div>
  <p style="margin:.35rem 0 0;font-size:.9rem;color:var(--md-default-fg-color--light);line-height:1.5;">{post["excerpt"]}</p>
  <div style="margin-top:.5rem;display:flex;gap:.4rem;flex-wrap:wrap;">
    {tags_html}
  </div>
</a>"""


def on_page_markdown(markdown, page, config, files):
    """MkDocs hook：处理 index.md 时替换 LATEST_POSTS 占位符。"""
    if page.file.src_uri != "index.md":
        return markdown

    if PLACEHOLDER not in markdown:
        return markdown

    posts = _read_posts(config)
    if not posts:
        return markdown.replace(
            PLACEHOLDER,
            '<p style="text-align:center;color:var(--md-default-fg-color--light);">暂无文章</p>',
        )

    cards = "\n".join(_render_post_card(p) for p in posts)
    html = f"""<div class="post-list" style="margin-top:1.5rem;display:flex;flex-direction:column;gap:1rem;">
{cards}
</div>

<div style="text-align:center;margin-top:1.5rem;">
  <a href="tech-blog/" style="font-size:.9rem;color:var(--md-default-fg-color--light);text-decoration:none;transition:color .2s;">
    查看更多 →
  </a>
</div>"""

    return markdown.replace(PLACEHOLDER, html)
