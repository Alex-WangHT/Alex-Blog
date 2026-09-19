# Alex Blog

## 本地 MkDocs 环境（Windows PowerShell）

使用 Python 3.11 或以上版本，在仓库根目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

本机已使用 `C:\ProgramData\miniconda3\python.exe` 创建 `.venv`。
无需激活环境，可直接调用其中的 Python；本地和 CI 使用同一份依赖清单。

生成导航、图片引用和 MathJax 配置，然后启动预览：

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/generate_blog_index.py
.\.venv\Scripts\python.exe -X utf8 -m mkdocs serve -a 127.0.0.1:8000
```

打开 <http://127.0.0.1:8000/Alex-Blog/>，按 `Ctrl+C` 停止。
生成脚本会更新导航并转换文档中的 Obsidian 语法，提交前请检查 `git diff`。

仅构建：

```powershell
.\.venv\Scripts\python.exe -X utf8 -m mkdocs build
```

## 公式和图片

中文文档保存为 UTF-8。行内公式使用 `$...$`；块公式的 `$$` 独占一行，且公式块前后必须留空行，矩阵内部不能插入空行：

```markdown
正文。

$$
L=\begin{pmatrix}
l\\
l_0
\end{pmatrix}
$$

下一段。
```

图片路径的大小写必须与 Git 中的文件名完全一致，GitHub Pages 的 Linux 构建环境区分大小写。
