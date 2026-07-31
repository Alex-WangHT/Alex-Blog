#!/usr/bin/env python3
"""
自动生成博客系统：标签页 + 文章列表 + 动态导航

功能：
1. 扫描 docs/ 下所有文章，提取 front matter
2. 生成 docs/tech-blog/index.md（标题 + 技术分类文章列表，右侧 TOC 只显示技术分类）
3. 生成 docs/tech-blog/tags/<tag>.md（各标签文章列表，右侧 TOC 只显示文章列表）
4. 自动更新 mkdocs.yml 中的 nav 配置

使用方式：
    python scripts/generate_blog_index.py
"""
import re
import yaml
from pathlib import Path
from collections import defaultdict

DOCS_DIR = Path('docs')
INCLUDES_DIR = Path('_includes')
MKDOCS_FILE = Path('mkdocs.yml')
TECH_BLOG_DIR = DOCS_DIR / 'tech-blog'
TAGS_DIR = TECH_BLOG_DIR / 'tags'

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
    """扫描所有文章"""
    articles = []
    for cat_dir, cat_name in CATEGORIES.items():
        cat_path = DOCS_DIR / cat_dir
        if not cat_path.exists():
            continue
        for md_file in sorted(cat_path.glob('*.md')):
            if md_file.name == 'index.md':
                continue
            content = md_file.read_text(encoding='utf-8')
            meta = parse_front_matter(content)
            if meta.get('draft'):
                continue
            rel_path = md_file.relative_to(DOCS_DIR).as_posix()
            articles.append({
                'title': meta.get('title', md_file.stem),
                'date': meta.get('date', ''),
                'tags': meta.get('tags', []),
                'description': meta.get('description', ''),
                'category': cat_name,
                'category_dir': cat_dir,
                'path': rel_path,
            })
    articles.sort(key=lambda x: x['date'] or '0000-00-00', reverse=True)
    return articles

def get_relative_path_from_tech_blog(art_path):
    """获取从 tech-blog/index.md 出发的相对路径"""
    if art_path.startswith('tech-blog/'):
        return art_path.replace('tech-blog/', '')
    return f'../{art_path}'

def get_relative_path_from_tag_page(art_path):
    """获取从 tech-blog/tags/*.md 出发的相对路径"""
    if art_path.startswith('tech-blog/'):
        return art_path.replace('tech-blog/', '../')
    return f'../../{art_path}'

def generate_tech_blog_home(articles):
    """生成技术博客主页：标题 + 技术分类文章列表，右侧 TOC 只显示技术分类"""
    lines = [
        '# 技术博客',
        '',
        '## 技术分类',
        '',
    ]

    for art in articles:
        date_str = f" ({art['date']})" if art['date'] else ''
        tags_str = ' '.join(f'`#{t}`' for t in art['tags']) if art['tags'] else ''
        rel_path = get_relative_path_from_tech_blog(art['path'])
        lines.append(f"- **[{art['title']}]({rel_path})**{date_str} — *{art['category']}*")
        if tags_str:
            lines.append(f"  {tags_str}")
        if art['description']:
            lines.append(f"  > {art['description']}")
        lines.append('')

    if not articles:
        lines.append('> 暂无文章，敬请期待。')

    return '\n'.join(lines)

def generate_tag_page(tag, articles):
    """生成单个标签的页面，右侧 TOC 只显示文章列表"""
    lines = [
        f'# 标签：#{tag}',
        '',
        f'以下是包含标签 **#{tag}** 的所有文章。',
        '',
        '## 文章列表',
        '',
    ]
    for art in sorted(articles, key=lambda x: x['date'] or '0000-00-00', reverse=True):
        date_str = f" ({art['date']})" if art['date'] else ''
        rel_path = get_relative_path_from_tag_page(art['path'])
        lines.append(f"- **[{art['title']}]({rel_path})**{date_str} — *{art['category']}*")
        if art['description']:
            lines.append(f"  > {art['description']}")
        lines.append('')
    return '\n'.join(lines)

def generate_tag_pages(articles):
    """为每个标签生成独立页面"""
    TAGS_DIR.mkdir(exist_ok=True)

    tags_dict = defaultdict(list)
    for art in articles:
        for tag in art['tags']:
            tags_dict[tag].append(art)

    for old_file in TAGS_DIR.glob('*.md'):
        old_file.unlink()

    for tag, arts in tags_dict.items():
        tag_file = TAGS_DIR / f"{tag}.md"
        tag_file.write_text(generate_tag_page(tag, arts), encoding='utf-8')

    return sorted(tags_dict.keys(), key=str.lower)

def generate_latest_posts(articles, max_count=10):
    """生成首页最新文章列表"""
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
    lines.append(f"[查看更多 →](tech-blog/index.md)")
    lines.append('')
    return '\n'.join(lines)

def update_mkdocs_nav(all_tags):
    """更新 mkdocs.yml 中的 nav 配置（左侧栏只保留标签分类）"""
    content = MKDOCS_FILE.read_text(encoding='utf-8')

    # 启用 navigation.indexes 后，父项自动链接到同目录 index.md
    # 不需要在子菜单中显式列出 tech-blog/index.md
    tech_blog_nav = "  - 技术博客:\n"
    tech_blog_nav += "    - 标签分类:\n"
    for tag in sorted(all_tags, key=str.lower):
        tech_blog_nav += f'      - "#{tag}": tech-blog/tags/{tag}.md\n'

    other_nav = """  - 机器人: robot/index.md
  - 人工智能: ai/index.md
  - 控制理论: control/index.md
  - 计算机: computer/index.md
  - 电子设计: electronics/index.md
  - 数学知识: math/index.md
  - 物理知识: physics/index.md
"""

    nav_start = content.find('nav:')
    gh_start = content.find('\n# GitHub Pages')
    if nav_start != -1 and gh_start != -1:
        new_content = (
            content[:nav_start] +
            f"nav:\n{tech_blog_nav}{other_nav}" +
            content[gh_start:]
        )
        MKDOCS_FILE.write_text(new_content, encoding='utf-8')
    else:
        print("⚠️  无法定位 nav 区域，请手动更新 mkdocs.yml")

def main():
    articles = scan_articles()

    all_tags = generate_tag_pages(articles)

    tech_blog_home = generate_tech_blog_home(articles)
    (TECH_BLOG_DIR / 'index.md').write_text(tech_blog_home, encoding='utf-8')

    latest_md = generate_latest_posts(articles)
    INCLUDES_DIR.mkdir(exist_ok=True)
    (INCLUDES_DIR / 'latest_posts.md').write_text(latest_md, encoding='utf-8')

    update_mkdocs_nav(all_tags)

    print(f"✅ 扫描到 {len(articles)} 篇文章")
    print(f"✅ 生成标签页面: {len(all_tags)} 个")
    print(f"✅ 更新技术博客主页: docs/tech-blog/index.md")
    print(f"✅ 更新首页文章列表: _includes/latest_posts.md")
    print(f"✅ 更新导航配置: mkdocs.yml")

if __name__ == '__main__':
    main()
