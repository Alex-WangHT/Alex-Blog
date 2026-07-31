#!/usr/bin/env python3
"""
自动生成博客首页文章列表和标签索引页
扫描 docs/ 下各分类目录中的文章，提取 YAML front matter，生成：
- _includes/latest_posts.md  （首页最新文章列表）
- docs/tags.md               （标签索引页）

使用方式：
    python scripts/generate_blog_index.py
"""
import yaml
from pathlib import Path
from collections import defaultdict

DOCS_DIR = Path('docs')
INCLUDES_DIR = Path('_includes')
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
    # 按日期降序排列（无日期排最后）
    articles.sort(key=lambda x: x['date'] or '0000-00-00', reverse=True)
    return articles

def generate_latest_posts(articles, max_count=10):
    """生成最新文章列表的 markdown"""
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

def generate_tags_page(articles):
    """生成标签索引页"""
    tags_dict = defaultdict(list)
    for art in articles:
        for tag in art['tags']:
            tags_dict[tag].append(art)

    lines = [
        '# 标签索引',
        '',
        '点击标签可查看对应文章。',
        '',
    ]

    # 标签云 / 列表
    for tag in sorted(tags_dict.keys(), key=str.lower):
        count = len(tags_dict[tag])
        lines.append(f"## #{tag} ({count})")
        lines.append('')
        for art in sorted(tags_dict[tag], key=lambda x: x['date'] or '0000', reverse=True):
            date_str = f" ({art['date']})" if art['date'] else ''
            lines.append(f"- [{art['title']}]({art['path']}){date_str} — *{art['category']}*")
        lines.append('')

    if not tags_dict:
        lines.append('> 暂无标签。')

    return '\n'.join(lines)

def main():
    articles = scan_articles()

    # 生成最新文章列表
    latest_md = generate_latest_posts(articles)

    # 生成标签页面
    tags_md = generate_tags_page(articles)

    # 确保目录存在
    INCLUDES_DIR.mkdir(exist_ok=True)

    # 写入文件
    (INCLUDES_DIR / 'latest_posts.md').write_text(latest_md, encoding='utf-8')
    (DOCS_DIR / 'tags.md').write_text(tags_md, encoding='utf-8')

    print(f"✅ 扫描到 {len(articles)} 篇文章")
    print(f"✅ 生成标签: {len(set(t for a in articles for t in a['tags']))} 个")
    print(f"✅ 写入 _includes/latest_posts.md")
    print(f"✅ 写入 docs/tags.md")

if __name__ == '__main__':
    main()
