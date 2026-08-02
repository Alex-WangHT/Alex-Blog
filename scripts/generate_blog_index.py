#!/usr/bin/env python3
"""
自动生成博客系统：为所有分类生成 index.md + 导航配置

技术博客（tech-blog）已迁移到 Material 官方 blog 插件：
- 文章位于 docs/tech-blog/posts/，由 blog 插件生成索引/标签/分类/归档页
- 本脚本仅扫描 tech-blog 文章用于首页"最新文章"列表

功能：
1. 扫描 docs/ 下所有文章（递归子目录），提取 front matter
2. 为每个分类生成 docs/<cat>/index.md（按子目录分组，H2 标题；tech-blog 除外）
3. 为每个子目录生成 index.md（解决导入文件夹后 404 问题；tech-blog 除外）
4. 生成 _includes/latest_posts.md（首页最新文章列表，含 tech-blog）
5. 复制根目录 mathjax.js 到 docs/javascripts/
6. 自动更新 mkdocs.yml 中的 nav 配置（左侧栏展开显示子目录和文件）
7. 转换 Obsidian ![[...]] WikiLink 图片嵌入为标准 Markdown
8. 转换 Obsidian > [!NOTE] callout 为标准 admonition 语法

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


def generate_subdir_index(subdir_path: Path, articles_in_subdir):
    """为单个子目录生成 index.md"""
    subdir_name = subdir_path.name
    lines = [f'# {subdir_name}', '', '## 文章列表', '']
    for art in sorted(articles_in_subdir, key=lambda x: x['date'] or '0000-00-00', reverse=True):
        date_str = f" ({art['date']})" if art['date'] else ''
        rel_path = Path(art['path']).name
        lines.append(f"- **[{art['title']}]({rel_path})**{date_str}")
        if art['description']:
            lines.append(f"  > {art['description']}")
        lines.append('')
    return '\n'.join(lines)


def generate_all_subdir_indices(articles):
    """为所有包含文章的子目录生成 index.md"""
    subdirs = defaultdict(list)
    for art in articles:
        path = Path(art['path'])
        if path.parts[0] == 'tech-blog':
            continue  # tech-blog 由官方 blog 插件托管
        if len(path.parts) > 2:
            subdirs[path.parent].append(art)
    for subdir, arts in subdirs.items():
        subdir_path = DOCS_DIR / subdir
        if subdir_path.exists():
            (subdir_path / 'index.md').write_text(
                generate_subdir_index(subdir_path, arts), encoding='utf-8'
            )
    return len(subdirs)


def generate_category_index(cat_dir, cat_name, articles):
    """生成分类 index.md：按子目录分组，每个子目录/文件作为 H2 标题"""
    cat_articles = [a for a in articles if a['category_dir'] == cat_dir]
    lines = [f'# {cat_name}', '']
    if not cat_articles:
        lines.append('> 暂无文章，敬请期待。')
        return '\n'.join(lines)

    groups = defaultdict(list)
    for art in cat_articles:
        path = Path(art['path'])
        if len(path.parts) == 2:
            groups[art['title']].append(art)
        else:
            groups[path.parts[1]].append(art)

    for group_name in sorted(groups.keys(), key=str.lower):
        arts = groups[group_name]
        lines.append(f'## {group_name}')
        lines.append('')
        for art in sorted(arts, key=lambda x: x['date'] or '0000-00-00', reverse=True):
            date_str = f" ({art['date']})" if art['date'] else ''
            tags_str = ' '.join(f'`#{t}`' for t in art['tags']) if art['tags'] else ''
            rel_path = art['path'].replace(f'{cat_dir}/', '')
            lines.append(f"- **[{art['title']}]({rel_path})**{date_str}")
            if tags_str:
                lines.append(f"  {tags_str}")
            if art['description']:
                lines.append(f"  > {art['description']}")
            lines.append('')
    return '\n'.join(lines)


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


def update_mkdocs_nav(articles):
    """更新 mkdocs.yml 中的 nav 配置（左侧栏展开显示子目录和文件）"""
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

        for md_file in sorted(cat_path.glob('*.md')):
            if md_file.name == 'index.md':
                continue
            file_content = md_file.read_text(encoding='utf-8')
            meta = parse_front_matter(file_content)
            title = meta.get('title', md_file.stem)
            rel_path = md_file.relative_to(DOCS_DIR).as_posix()
            other_nav += f'    - {title}: {rel_path}\n'

        for subdir in sorted(cat_path.iterdir()):
            if not subdir.is_dir() or subdir.name in ('tags', 'img'):
                continue
            if list(subdir.rglob('*.md')):
                other_nav += f'    - {subdir.name}: {cat_dir}/{subdir.name}/index.md\n'

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

    # 1. 为每个分类生成 index.md（tech-blog 由官方 blog 插件托管，跳过）
    for cat_dir, cat_name in CATEGORIES.items():
        if cat_dir == 'tech-blog':
            continue
        cat_path = DOCS_DIR / cat_dir
        if cat_path.exists():
            (cat_path / 'index.md').write_text(
                generate_category_index(cat_dir, cat_name, articles), encoding='utf-8'
            )

    # 2. 为包含文章的子目录生成 index.md
    subdir_count = generate_all_subdir_indices(articles)

    # 3. 生成首页最新文章列表（含 tech-blog 文章）
    latest_md = generate_latest_posts(articles)
    INCLUDES_DIR.mkdir(exist_ok=True)
    (INCLUDES_DIR / 'latest_posts.md').write_text(latest_md, encoding='utf-8')

    # 4. 复制 MathJax 配置
    copy_mathjax_config()

    # 5. 更新 mkdocs.yml nav（展开子目录）
    update_mkdocs_nav(articles)

    print(f"✅ Callout 转换: {callout_count} 个文件")
    print(f"✅ WikiLink 转换: {wikilink_count} 个文件")
    print(f"✅ 扫描到 {len(articles)} 篇文章")
    print(f"✅ 生成分类主页: {len(CATEGORIES) - 1} 个（tech-blog 由 blog 插件托管）")
    print(f"✅ 生成子目录索引: {subdir_count} 个")
    print(f"✅ 更新首页文章列表: _includes/latest_posts.md")
    print(f"✅ 更新导航配置: mkdocs.yml")


if __name__ == '__main__':
    main()
