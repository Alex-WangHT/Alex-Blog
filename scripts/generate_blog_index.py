#!/usr/bin/env python3
"""
自动维护博客站点：首页最新文章列表 + 完整导航树

技术博客（tech-blog）由 Material 官方 blog 插件托管；
各分类/子目录的落地页（点击后跳转到第一篇文章）由
scripts/hook_section_landing.py 在构建期虚拟生成，本脚本不写入 docs/。

功能：
1. 扫描 docs/ 下所有文章（递归子目录），提取 front matter
2. 生成 _includes/latest_posts.md（首页最新文章列表，含 tech-blog）
3. 复制根目录 mathjax.js 到 docs/javascripts/
4. 自动更新 mkdocs.yml 中的 nav 配置（左侧栏显示完整文章树）
5. 转换 Obsidian ![[...]] WikiLink 图片嵌入为标准 Markdown
6. 转换 Obsidian > [!NOTE] callout 为标准 admonition 语法

使用方式：
    python scripts/generate_blog_index.py
"""
import re
import shutil
import yaml
from pathlib import Path
from collections import defaultdict

DOCS_DIR = Path('docs')
INCLUDES_DIR = Path('_includes')
MKDOCS_FILE = Path('mkdocs.yml')

CATEGORIES = {
    'tech-blog': '技术博客',
    'robot': '机器人',
    'ai': '人工智能',
    'control': '控制理论',
    'computer': '计算机',
    'electronics': '电子设计',
    'math': '数学知识',
    'physics': '物理知识',
}


# ── Obsidian Callout → Admonition 转换 ───────────────────────────

CALLOUT_RE = re.compile(r'^>\s*\[!\s*(\w+)\s*\]\s*(.*?)$')

CALLOUT_TYPE_MAP = {
    'note': 'note', 'tip': 'tip', 'warning': 'warning',
    'danger': 'danger', 'question': 'question', 'info': 'info',
    'important': 'important', 'success': 'success', 'failure': 'failure',
    'example': 'example', 'abstract': 'abstract', 'summary': 'summary',
    'quote': 'quote', 'bug': 'bug',
}


def convert_callouts(content: str) -> str:
    """将 Obsidian 风格的 > [!NOTE] 引用块转换为标准 admonition 语法。"""
    lines = content.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = CALLOUT_RE.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        obs_type = m.group(1).strip().lower()
        title = m.group(2).strip()
        ad_type = CALLOUT_TYPE_MAP.get(obs_type, 'note')

        # 收集 callout 内容行（> 开头的连续行）
        body_lines = []
        i += 1
        while i < len(lines):
            if lines[i].startswith('> '):
                body_lines.append(lines[i][2:])
                i += 1
            elif lines[i] == '>':
                body_lines.append('')
                i += 1
            else:
                break

        # 输出 admonition
        if title:
            out.append(f'!!! {ad_type} "{title}"')
        else:
            out.append(f'!!! {ad_type}')
        for bl in body_lines:
            out.append('    ' + bl)
        out.append('')

    return '\n'.join(out)


def convert_callouts_in_file(md_file: Path):
    """转换单个文件中的 Obsidian callout。"""
    content = md_file.read_text(encoding='utf-8')
    converted = convert_callouts(content)
    if converted != content:
        md_file.write_text(converted, encoding='utf-8')
        return True
    return False


def convert_all_callouts():
    """扫描 docs/ 下所有 .md，转换 Obsidian callout。"""
    converted = 0
    for md_file in DOCS_DIR.rglob('*.md'):
        if md_file.name == 'index.md':
            continue
        if 'tags' in md_file.relative_to(DOCS_DIR).parts:
            continue
        if convert_callouts_in_file(md_file):
            converted += 1
    return converted


# ── Obsidian WikiLink 转换 ───────────────────────────────────────

WIKILINK_IMG_RE = re.compile(r'!\[\[([^\]]+)\]\]')


def _resolve_wikilink(md_file: Path, link: str):
    """
    把 Obsidian 的 ![[...]] 链接解析为相对于 md_file 的图片路径。
    返回标准 Markdown 图片语法，找不到则返回 None。
    """
    raw = link.lstrip('./')

    # 1) 直接路径（如 img/Fig.png）
    candidate = md_file.parent / raw
    if candidate.exists() and candidate.is_file():
        rel = candidate.relative_to(md_file.parent).as_posix()
        return f'![{candidate.stem}]({rel})'

    # 2) 同级 img/ 目录中查找（Obsidian 常见做法）
    name = Path(raw).name
    candidate = md_file.parent / 'img' / name
    if candidate.exists() and candidate.is_file():
        return f'![{name}](img/{name})'

    return None


def convert_wikilinks_in_file(md_file: Path):
    """把单个 .md 文件中的 ![[...]] 转换为标准 Markdown 图片语法。"""
    content = md_file.read_text(encoding='utf-8')
    original = content

    def replacer(m: re.Match) -> str:
        link = m.group(1).strip()
        resolved = _resolve_wikilink(md_file, link)
        if resolved:
            return resolved
        print(f"⚠️  图片未找到: {md_file} -> ![[{link}]]")
        return m.group(0)

    content = WIKILINK_IMG_RE.sub(replacer, content)

    if content != original:
        md_file.write_text(content, encoding='utf-8')
        return True
    return False


def convert_all_wikilinks():
    """扫描 docs/ 下所有 .md，转换 Obsidian WikiLink 图片嵌入。"""
    converted = 0
    for md_file in DOCS_DIR.rglob('*.md'):
        if md_file.name == 'index.md':
            continue
        if 'tags' in md_file.relative_to(DOCS_DIR).parts:
            continue
        if convert_wikilinks_in_file(md_file):
            converted += 1
    return converted


# ── 原有函数 ─────────────────────────────────────────────────────

def parse_front_matter(content: str):
    """从 markdown 内容中提取 YAML front matter"""
    if not content.startswith('---'):
        return {}
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def scan_articles():
    """扫描所有文章（递归子目录）"""
    articles = []
    for cat_dir, cat_name in CATEGORIES.items():
        cat_path = DOCS_DIR / cat_dir
        if not cat_path.exists():
            continue
        for md_file in sorted(cat_path.rglob('*.md')):
            if md_file.name == 'index.md':
                continue
            if 'tags' in md_file.relative_to(DOCS_DIR).parts:
                continue
            content = md_file.read_text(encoding='utf-8')
            meta = parse_front_matter(content)
            if meta.get('draft'):
                continue
            # blog 插件的 date 是 {created: ..., updated: ...} 字典，统一取 created
            date = meta.get('date', '')
            if isinstance(date, dict):
                date = date.get('created', '')
            rel_path = md_file.relative_to(DOCS_DIR).as_posix()
            articles.append({
                'title': meta.get('title', md_file.stem),
                'date': str(date) if date else '',
                'tags': meta.get('tags', []),
                'description': meta.get('description', ''),
                'category': cat_name,
                'category_dir': cat_dir,
                'path': rel_path,
            })
    articles.sort(key=lambda x: x['date'] or '0000-00-00', reverse=True)
    return articles


def generate_latest_posts(articles, max_count=10):
    if not articles:
        return '## 最新文章\n\n> 暂无文章，敬请期待。\n'
    lines = ['## 最新文章', '']
    for art in articles[:max_count]:
        date_str = f" ({art['date']})" if art['date'] else ''
        tags_str = ' '.join(f'`#{t}`' for t in art['tags']) if art['tags'] else ''
        lines.append(f"- **[{art['title']}]({art['path']})**{date_str} — *{art['category']}*")
        if tags_str:
            lines.append(f"  {tags_str}")
        if art['description']:
            lines.append(f"  > {art['description']}")
        lines.append('')
    lines.append('[查看更多 →](tech-blog/index.md)')
    lines.append('')
    return '\n'.join(lines)


def _yaml_quote(text: str) -> str:
    """标题含 YAML 特殊字符时加引号"""
    if any(c in text for c in ':#"\'') or text != text.strip():
        return '"' + text.replace('"', '\\"') + '"'
    return text


def build_nav_tree(dir_path: Path, level: int) -> str:
    """递归生成某个目录的 nav 子树：文章全部列出，子目录展开为分区。

    level: 缩进层级（每级 2 空格），目录自身的 index.md 由调用方处理。
    """
    indent = '  ' * level
    nav = ""

    # 1. 直接文章文件
    for md_file in sorted(dir_path.glob('*.md'), key=lambda p: p.name.lower()):
        if md_file.name == 'index.md':
            continue
        meta = parse_front_matter(md_file.read_text(encoding='utf-8'))
        title = _yaml_quote(meta.get('title', md_file.stem))
        rel_path = md_file.relative_to(DOCS_DIR).as_posix()
        nav += f"{indent}- {title}: {rel_path}\n"

    # 2. 递归子目录（含 .md 的内容目录）
    for subdir in sorted(dir_path.iterdir(), key=lambda p: p.name.lower()):
        if not subdir.is_dir() or subdir.name in ('tags', 'img'):
            continue
        if not list(subdir.rglob('*.md')):
            continue
        rel = subdir.relative_to(DOCS_DIR).as_posix()
        name = _yaml_quote(subdir.name)
        nav += f"{indent}- {name}:\n"
        nav += f"{indent}  - {name}: {rel}/index.md\n"
        nav += build_nav_tree(subdir, level + 1)

    return nav


def update_mkdocs_nav(articles):
    """更新 mkdocs.yml 中的 nav 配置（左侧栏显示完整文章树）。

    各目录的 index.md 由 scripts/hook_section_landing.py 在构建期虚拟生成
    （重定向到该目录第一篇文章），docs/ 目录保持纯净。
    """
    content = MKDOCS_FILE.read_text(encoding='utf-8')

    # tech-blog 由官方 blog 插件托管，nav 只保留插件索引页与标签索引页
    tech_blog_nav = "  - 技术博客:\n"
    tech_blog_nav += "    - 全部文章: tech-blog/index.md\n"
    tech_blog_nav += "    - 标签索引: tech-blog/tags.md\n"

    other_nav = ""
    for cat_dir, cat_name in CATEGORIES.items():
        if cat_dir == 'tech-blog':
            continue
        cat_path = DOCS_DIR / cat_dir
        if not cat_path.exists():
            other_nav += f"  - {cat_name}: {cat_dir}/index.md\n"
            continue

        other_nav += f"  - {cat_name}:\n"
        other_nav += f"    - {cat_name}: {cat_dir}/index.md\n"
        other_nav += build_nav_tree(cat_path, 2)

    nav_start = content.find('nav:')
    gh_start = content.find('\n# GitHub Pages')
    if nav_start != -1 and gh_start != -1:
        new_content = content[:nav_start] + f"nav:\n{tech_blog_nav}{other_nav}" + content[gh_start:]
        MKDOCS_FILE.write_text(new_content, encoding='utf-8')
    else:
        print("⚠️  无法定位 nav 区域，请手动更新 mkdocs.yml")


def copy_mathjax_config():
    js_dir = DOCS_DIR / 'javascripts'
    js_dir.mkdir(exist_ok=True)
    src = Path('mathjax.js')
    dst = js_dir / 'mathjax.js'
    if src.exists():
        shutil.copy2(src, dst)
        print("✅ 复制 MathJax 配置到 docs/javascripts/mathjax.js")
    else:
        print("⚠️  根目录 mathjax.js 未找到")


def main():
    # 0a. 转换 Obsidian callout 为 admonition
    callout_count = convert_all_callouts()

    # 0b. 转换 Obsidian WikiLink 图片嵌入为标准 Markdown
    wikilink_count = convert_all_wikilinks()

    articles = scan_articles()

    # 1. 生成首页最新文章列表（含 tech-blog 文章）
    latest_md = generate_latest_posts(articles)
    INCLUDES_DIR.mkdir(exist_ok=True)
    (INCLUDES_DIR / 'latest_posts.md').write_text(latest_md, encoding='utf-8')

    # 2. 复制 MathJax 配置
    copy_mathjax_config()

    # 3. 更新 mkdocs.yml nav（左侧栏完整文章树；
    #    各目录 index.md 落地页由 scripts/hook_section_landing.py 构建期虚拟生成）
    update_mkdocs_nav(articles)

    print(f"✅ Callout 转换: {callout_count} 个文件")
    print(f"✅ WikiLink 转换: {wikilink_count} 个文件")
    print(f"✅ 扫描到 {len(articles)} 篇文章")
    print(f"✅ 更新首页文章列表: _includes/latest_posts.md")
    print(f"✅ 更新导航配置: mkdocs.yml（完整文章树）")


if __name__ == '__main__':
    main()
