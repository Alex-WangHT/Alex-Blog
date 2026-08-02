# scripts 目录说明

| 脚本 | 状态 | 运行时机 | 用途 |
|---|---|---|---|
| `generate_blog_index.py` | ✅ 必备 | **CI 自动**（每次 push，见 `.github/workflows/deploy.yml`）；本地改动结构后可手动跑 | 站点维护主脚本 |
| `hook_section_landing.py` | ✅ 必备 | **构建自动**（`mkdocs.yml` 的 `hooks` 引用，本地/CI 构建都会触发） | 虚拟生成目录落地页 |
| `reshape_math.py` | 🔧 按需 | **手动**，仅在 Obsidian 导入的笔记公式渲染异常时运行 | 公式格式规范化工具 |

---

## generate_blog_index.py —— 站点维护主脚本

每次 push 后由 CI 自动运行，日常写作**无需手动执行**。

功能：

1. 扫描 `docs/` 下所有文章，提取 front matter
2. 生成 `_includes/latest_posts.md`（首页"最新文章"列表）
3. 复制根目录 `mathjax.js` 到 `docs/javascripts/`
4. 重写 `mkdocs.yml` 的 `nav` 段（左侧栏完整文章树）
5. 转换 Obsidian `![[...]]` WikiLink 图片为标准 Markdown
6. 转换 Obsidian `> [!NOTE]` callout 为标准 admonition

> 注意：本脚本会重写 `mkdocs.yml` 中 `nav:` 到 `# GitHub Pages` 之间的内容，
> 手动改 nav 会被覆盖；nav 之外的部分（theme、plugins、hooks 等）不受影响。

手动运行：

```bash
python scripts/generate_blog_index.py
```

## hook_section_landing.py —— 目录落地页（MkDocs hook）

由 `mkdocs.yml` 的 `hooks:` 注册，每次 `mkdocs build` / `mkdocs serve` 自动触发，**不要手动运行**。

功能：为每个分类/子目录在构建期**虚拟生成** `index.md` 落地页
（meta refresh + JS 重定向到该目录下按文件名排序的第一篇文章），
实现"点击左侧目录 → 中间直接显示第一篇文章"。

- 文件只存在于构建产物中，`docs/` 目录保持纯净
- 空分类生成"暂无文章"占位页
- `tech-blog/`（blog 插件托管）与 `javascripts/` 不参与

## reshape_math.py —— 公式修复工具（按需）

一次性修复工具，**不在 CI 流程中**。

用途：Obsidian 导入的笔记中，admonition（`!!! note` 等）内部的
`$$...$$` 公式可能被 Markdown 解析器错误处理（下划线 `_` 被误认为斜体）。
本脚本把 admonition 内的 `$$...$$` 转成 ```` ```math ```` 围栏格式加以保护。

仅在发现某篇笔记的公式在网站上渲染错乱时运行：

```bash
python scripts/reshape_math.py
```
