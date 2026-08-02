#!/usr/bin/env python3
"""
将 Markdown 中的单行 $$...$$ 转换为多行格式，保留原始缩进。

转换前:
        $$公式内容$$

转换后:
        $$
        公式内容
        $$

用法:
    python scripts/reshape_math.py
"""
import re
from pathlib import Path

DOCS_DIR = Path('docs')

# 匹配单行 $$...$$，捕获前导空白和公式内容
SINGLELINE_BLOCK_RE = re.compile(r'^(\s*)\$\$(.*?)\$\$\s*$')


def reshape_math_in_file(md_file: Path):
    """修复单个文件中的公式格式。"""
    content = md_file.read_text(encoding='utf-8')
    original = content

    lines = content.split('\n')
    out = []
    for line in lines:
        m = SINGLELINE_BLOCK_RE.match(line)
        if m:
            indent = m.group(1)
            formula = m.group(2).strip()
            out.append(f'{indent}$$')
            out.append(f'{indent}{formula}')
            out.append(f'{indent}$$')
        else:
            out.append(line)

    content = '\n'.join(out)

    if content != original:
        md_file.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    fixed = 0
    for md_file in DOCS_DIR.rglob('*.md'):
        if md_file.name == 'index.md':
            continue
        if 'tags' in md_file.relative_to(DOCS_DIR).parts:
            continue
        if reshape_math_in_file(md_file):
            fixed += 1
    print(f"✅ 转换单行公式: {fixed} 个文件")


if __name__ == '__main__':
    main()
