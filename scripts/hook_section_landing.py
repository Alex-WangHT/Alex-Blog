"""MkDocs hook：为分类/子目录生成虚拟落地页（不写入 docs/）。

效果：
- 点击左侧任一文件夹（分类或子目录），中间直接跳转到该文件夹下的第一篇文章
- 落地页是构建期虚拟生成的 index.md（meta refresh + JS 重定向），docs/ 目录保持纯净
- 没有文章的一级分类显示「暂无文章」占位页

排序规则与 scripts/generate_blog_index.py 的 nav 生成保持一致（按路径名字典序）。
"""
import os
import posixpath
from urllib.parse import quote

from mkdocs.structure.files import File

# 不生成落地页的顶层目录（tech-blog 由 blog 插件托管，javascripts 是资源目录）
EXCLUDE_TOP_LEVEL = {'tech-blog', 'javascripts'}
# 任何层级都不视为内容目录的名字
EXCLUDE_DIR_NAMES = {'img', 'tags'}

REDIRECT_TEMPLATE = """<meta http-equiv="refresh" content="0; url={url}">
<script>window.location.replace("{url}");</script>

正在跳转到第一篇文章： [{title}]({target})
"""

EMPTY_TEMPLATE = """> 暂无文章，敬请期待。
"""


def _article_sort_key(src_uri: str):
    return src_uri.lower()


def on_files(files, config, **kwargs):
    docs_pages = [f for f in files if f.is_documentation_page()]
    existing = {f.src_uri for f in docs_pages}

    # 1. 收集每个目录下（递归）的第一篇文章，按路径字典序
    dir_first_article = {}
    for f in sorted(docs_pages, key=lambda f: _article_sort_key(f.src_uri)):
        src = f.src_uri
        parts = src.split('/')
        if parts[-1] == 'index.md':
            continue
        if parts[0] in EXCLUDE_TOP_LEVEL:
            continue
        if len(parts) < 2:
            continue  # 根目录首页
        if any(p in EXCLUDE_DIR_NAMES for p in parts[:-1]):
            continue
        for depth in range(1, len(parts)):
            dir_path = '/'.join(parts[:depth])
            dir_first_article.setdefault(dir_path, src)

    # 2. 遍历磁盘，找出一级分类（含空目录），保证空分类也有占位页
    docs_dir = config.docs_dir
    top_level_dirs = set()
    for entry in sorted(os.listdir(docs_dir)):
        full = os.path.join(docs_dir, entry)
        if os.path.isdir(full) and entry not in EXCLUDE_TOP_LEVEL and not entry.startswith('.'):
            top_level_dirs.add(entry)

    target_dirs = set(dir_first_article) | top_level_dirs

    # 3. 为缺少物理 index.md 的目录注入虚拟落地页
    for dir_path in sorted(target_dirs):
        src_uri = f'{dir_path}/index.md'
        if src_uri in existing:
            continue  # 磁盘上已有 index.md，不覆盖

        first = dir_first_article.get(dir_path)
        if first:
            rel_target = posixpath.relpath(first, dir_path)
            # 文章输出 URL（use_directory_urls: xxx.md -> xxx/）
            url = quote(rel_target[:-3], safe='/') + '/'
            title = os.path.splitext(os.path.basename(first))[0]
            content = REDIRECT_TEMPLATE.format(url=url, title=title, target=rel_target)
        else:
            content = EMPTY_TEMPLATE

        files.append(File.generated(config, src_uri, content=content))

    return files
