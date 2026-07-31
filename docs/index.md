# Welcome to Alex Blog

这是一个基于 MkDocs + Material 主题的个人博客站点，支持 MathJax 数学公式渲染。

## 数学公式示例

### 行内公式 (Inline Math)

行内公式使用单个美元符号包裹，例如：质能方程 $E = mc^2$ 由爱因斯坦提出。

### 独立公式 (Display Math)

独立公式使用双美元符号包裹，例如：

$$\int_{-\infty}^{+\infty} e^{-x^2} dx = \sqrt{\pi}$$

### 更复杂的公式

$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$

$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$

### 矩阵示例

$$
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

## 站点命令

- `mkdocs serve` - 启动本地预览服务器
- `mkdocs build` - 构建文档站点
- `mkdocs gh-deploy` - 部署到 GitHub Pages

## 项目结构

```
mkdocs.yml    # 配置文件
docs/
    index.md          # 首页
    javascripts/      # 自定义 JS（MathJax 配置）
        mathjax.js    # MathJax 配置：仅支持 $...$ 和 $$...$$
```
