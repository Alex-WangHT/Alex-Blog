#!/usr/bin/env python3
"""
自动生成博客系统：为所有分类生成 index.md + 标签页

功能：
1. 扫描 docs/ 下所有文章（递归子目录），提取 front matter
2. 为每个分类生成 docs/<cat>/index.md（该分类的文章列表）
3. 为每个子目录生成 index.md（解决导入文件夹后 404 问题）
4. 为技术博客生成 docs/tech-blog/index.md（全部文章列表，作为博客主页）
5. 生成 docs/tech-blog/tags/<tag>.md（各标签文章列表）
6. 生成 _includes/latest_posts.md（首页最新文章列表）
7. 复制根目录 mathjax.js 到 docs/javascripts/
8. 自动更新 mkdocs.yml 中的 nav 配置

使用方式：
    python scripts/generate_blog_index.py
"""
import shutil
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
    """扫描所有文章（递归子目录）"""
    articles = []
    for cat_dir, cat_name in CATEGORIES.items():
        cat_path = DOCS_DIR / cat_dir
        if not cat_path.exists():
            continue
        # 使用 rglob 递归扫描所有子目录
        for md_file in sorted(cat_path.rglob('*.md')):
            if md_file.name == 'index.md':
                continue
            # 跳过 tech-blog/tags 目录（标签页单独管理）
            if 'tags' in md_file.relative_to(DOCS_DIR).parts:
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


def generate_subdir_index(subdir_path: Path, articles_in_subdir):
    """为单个子目录生成 index.md，添加 H2 让右侧 TOC 有内容"""
    subdir_name = subdir_path.name
    lines = [
        f'# {subdir_name}',
        '',
        '## 文章列表',
        '',
    ]

    for art in sorted(articles_in_subdir, key=lambda x: x['date'] or '0000-00-00', reverse=True):
        date_str = f" ({art['date']})" if art['date'] else ''
        # 从子目录 index.md 到同目录文章的相对路径就是文件名
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
        # 只处理嵌套在分类目录下的子目录，如 robot/subdir/file.md
        if len(path.parts) > 2:
            subdir = path.parent  # e.g., robot/subdir
            subdirs[subdir].append(art)

    for subdir, arts in subdirs.items():
        subdir_path = DOCS_DIR / subdir
        if not subdir_path.exists():
            continue
        index_md = generate_subdir_index(subdir_path, arts)
        (subdir_path / 'index.md').write_text(index_md, encoding='utf-8')

    return len(subdirs)


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


def generate_category_index(cat_dir, cat_name, articles):
    """生成某个分类的 index.md，添加 H2 让右侧 TOC 有内容"""
    cat_articles = [a for a in articles if a['category_dir'] == cat_dir]

    lines = [
        f'# {cat_name}',
        '',
    ]

    if cat_articles:
        lines.append('## 文章列表')
        lines.append('')
        for art in cat_articles:
            date_str = f" ({art['date']})" if art['date'] else ''
            tags_str = ' '.join(f'`#{t}`' for t in art['tags']) if art['tags'] else ''
            rel_path = art['path'].replace(f'{cat_dir}/', '')
            lines.append(f"- **[{art['title']}]({rel_path})**{date_str}")
            if tags_str:
                lines.append(f"  {tags_str}")
            if art['description']:
                lines.append(f"  > {art['description']}")
            lines.append('')
    else:
        lines.append('> 暂无文章，敬请期待。')

    return '\n'.join(lines)


def generate_tech_blog_home(articles):
    """生成技术博客主页：显示全部文章（作为博客总览）"""
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
    """生成单个标签的页面"""
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


def copy_mathjax_config():
    """将根目录的 mathjax.js 复制到 docs/javascripts/"""
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
    articles = scan_articles()

    # 1. 为每个分类生成 index.md
    for cat_dir, cat_name in CATEGORIES.items():
        cat_path = DOCS_DIR / cat_dir
        if cat_path.exists():
            index_md = generate_category_index(cat_dir, cat_name, articles)
            (cat_path / 'index.md').write_text(index_md, encoding='utf-8')

    # 2. 为包含文章的子目录生成 index.md（解决导入文件夹后 404 问题）
    subdir_count = generate_all_subdir_indices(articles)

    # 3. 技术博客主页（显示所有文章）
    tech_blog_home = generate_tech_blog_home(articles)
    (TECH_BLOG_DIR / 'index.md').write_text(tech_blog_home, encoding='utf-8')

    # 4. 生成标签页面
    all_tags = generate_tag_pages(articles)

    # 5. 生成首页最新文章列表
    latest_md = generate_latest_posts(articles)
    INCLUDES_DIR.mkdir(exist_ok=True)
    (INCLUDES_DIR / 'latest_posts.md').write_text(latest_md, encoding='utf-8')

    # 6. 复制 MathJax 配置
    copy_mathjax_config()

    # 7. 更新 mkdocs.yml nav
    update_mkdocs_nav(all_tags)

    print(f"✅ 扫描到 {len(articles)} 篇文章")
    print(f"✅ 生成分类主页: {len(CATEGORIES)} 个")
    print(f"✅ 生成子目录索引: {subdir_count} 个")
    print(f"✅ 生成标签页面: {len(all_tags)} 个")
    print(f"✅ 更新首页文章列表: _includes/latest_posts.md")
    print(f"✅ 更新导航配置: mkdocs.yml")


if __name__ == '__main__':
    main()
