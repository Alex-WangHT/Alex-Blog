#!/usr/bin/env python3
"""
将 Markdown 中的单行/多行 $$...$$ 块级公式规范化。

在 admonition (!!! note 等) 内部，$$...$$ 容易被 Markdown 解析器错误处理
（如下划线 _ 被转义为 <em>）。本脚本将 admonition 内部的 $$...$$ 转换为
```math fenced code block 格式，确保公式内容被完全保护。

admonition 外部的 $$...$$ 保持多行格式即可（arithmatex 能正确处理）。

用法:
    python scripts/reshape_math.py
"""
import re
from pathlib import Path

DOCS_DIR = Path('docs')

# 匹配 admonition 内部的块级 $$...$$（捕获缩进和公式内容）
# 要求 $$ 独占一行，内容在 $$ 和 $$ 之间
ADMONITION_BLOCK_MATH = re.compile(
    r'^([ \t]+)\$\$\n((?:(?!\1\$\$).)*?)\n\1\$\$',
    re.MULTILINE
)

# 匹配单行 $$...$$（同一行内）
SINGLELINE_BLOCK_RE = re.compile(r'^(\s*)\$\$(.*?)\$\$\s*$')


def is_inside_admonition(lines, line_idx):
    """检查给定行是否在 admonition 块内部。"""
    # 向上查找最近的 admonition 标记或空行
    for i in range(line_idx - 1, -1, -1):
        stripped = lines[i].strip()
        if stripped.startswith('!!! ') or stripped.startswith('??? '):
            return True
        # 如果遇到一个非缩进行（且不是 admonition 继续标记），说明不在 admonition 内
        if lines[i] and not lines[i].startswith(' ') and not lines[i].startswith('\t'):
            return False
        # 如果行不缩进且为空行，继续向上检查
    return False


def reshape_math_in_file(md_file: Path):
    """修复单个文件中的公式格式。"""
    content = md_file.read_text(encoding='utf-8')
    original = content

    lines = content.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = SINGLELINE_BLOCK_RE.match(line)
        if m:
            indent = m.group(1)
            formula = m.group(2).strip()
            # 检查是否在 admonition 内部
            if is_inside_admonition(lines, i):
                # 转换为 fenced code block math
                out.append(f'{indent}```math')
                out.append(f'{indent}{formula}')
                out.append(f'{indent}```')
            else:
                # admonition 外部：转换为多行格式
                out.append(f'{indent}$$')
                out.append(f'{indent}{formula}')
                out.append(f'{indent}$$')
        else:
            out.append(line)
        i += 1

    # 处理 admonition 内部的多行 $$...$$
    content = '\n'.join(out)

    def replace_admonition_math(m):
        indent = m.group(1)
        formula = m.group(2).rstrip('\n')
        lines_out = [f'{indent}```math']
        for fl in formula.split('\n'):
            lines_out.append(f'{indent}{fl.lstrip()}')
        lines_out.append(f'{indent}```')
        return '\n'.join(lines_out)

    content = ADMONITION_BLOCK_MATH.sub(replace_admonition_math, content)

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
    print(f"✅ 转换公式格式: {fixed} 个文件")


if __name__ == '__main__':
    main()
