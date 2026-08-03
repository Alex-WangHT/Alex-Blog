
## 1-空间速度向量
首先我们在空间中有一个刚体$B$和空间内任意一点$O_W$，我们以点$O_W$为原点建立参考坐标系$Frame\{{\mathcal{W}}\}$，以刚体$B$内任意一点$O_B$为原点建立坐标系$Frame\{{\mathcal{B}}\}$如下：

我们可以在坐标系$Frame\{{\mathcal{W}}\}$中表示刚体内一点$P$的位置如下：

$$
{^{W}{\vec{r}}_{P}}={^{W}{\vec{r}}_{BORG}}+{^{W}_{B}{R}}{^{B}{\vec{r}}_{P}}
$$

我们可以在坐标系$Frame\{{\mathcal{W}}\}$中得到点$P$的瞬时速度如下：

$$
\begin{align}
{^{W}{\vec{v}}_{P}}&={^{W}{\dot{\vec{r}}}_{BORG}}+{^{W}_{B}{\dot{R}}}{^{B}{\vec{r}}_{P}}\\
&={^{W}{\dot{\vec{r}}}_{BORG}}+{^{W}_{B}{\dot{R}}}({^{W}_{B}{R}^{T}}{^{W}_{B}{R}}){^{B}{\vec{r}}_{P}}\\
&={^{W}{\dot{\vec{r}}}_{BORG}}+({^{W}_{B}{\dot{R}}}{^{W}_{B}{R}^{T}})({^{W}_{B}{R}}{^{B}{\vec{r}}_{P}})\\
&={^{W}{\vec{v}}_{BORG}}+{^{W}{\vec{\omega}}_{B}}{\times}{^{W}{\vec{r}}_{{O_B}{P}}}
\end{align}
$$

我们在理论力学的知识中学过：角速度是不变量。即刚体运动的角速度**不依赖于**刚体坐标系原点 $O_B$的选取而改变。
我们可以换个思路，如果我们在刚体$B$的外面有一个能够随着刚体运动的点$O_B$，该点$O_B$**只随着刚体$\boldsymbol{B}$平动**，并且点$O_B$和刚体内任意一点的距离都是恒定不变的，那么这个点$O_B$也可以作为坐标系$Frame\{{\mathcal{B}}\}$的原点。那么在坐标系$Frame\{{\mathcal{W}}\}$中的速度依然可以表示为：

$$
\begin{align}
{^{W}{\vec{v}}_{P}}={^{W}{\vec{v}}_{BORG}}+{^{W}{\vec{\omega}}_{B}}{\times}{^{W}{\vec{r}}_{{O_B}{P}}}
\end{align}
$$

那么在刚体$B$的本体坐标系$Frame\{{\mathcal{B}}\}$中的表述如下：

$$
\begin{align}
{^{B}{\vec{v}}_{P}}&={^{B}{\vec{v}}_{BORG}}+{^{B}_{W}R}({^{W}{\vec{\omega}}_{B}}{\times}{^{W}{\vec{r}}_{{O_B}{P}}})\\
&={^{B}{\vec{v}}_{BORG}}+{^{B}{\vec{\omega}}_{B}}{\times}{^{B}{\vec{r}}_{P}}\\
\end{align}
$$

在坐标系$Frame\{{\mathcal{B}}\}$中，如果我们用${^{B}}{v}_{O}$表示${^{B}{\vec{v}}_{BORG}}$，然后我们用${^{B}}{\omega}$来表示${^{B}{\vec{\omega}}_{B}}$，那么我们在刚体$B$内部的任意一点$P$的速度可以表示为：

$$
{^{B}{\vec{v}}_{P}}={{^{B}}{v}_{O}}+{{^{B}}{\omega}}{\times}{^{B}{\vec{r}}_{P}}
$$

我们可以知道在空间坐标系$Frame\{{\mathcal{B}}\}$中，我们的刚体$B$上任意一点的速度都可以用角速度${\omega}$和${{v}_{O}}$一起表示。那么我们就可以使用如下的方式来一起表示：

$$
{^{B}}{\hat{v}}=
\begin{pmatrix}
{^{B}}{\omega}\\
{^{B}}{v_O}
\end{pmatrix}
{\in}{\mathbb{R}^{6}}
$$

这里就是刚体$B$的**空间速度向量**。

!!! note "空间速度向量"
    Contents


## 2.2-空间力向量

在前面我们设定了**空间速度向量**，接下来我们在空间坐标系$Frame\{{\mathcal{B}}\}$上表示刚体$B$受到的力和力矩。我们假设有一个力$f$施加在刚体上，并且力$f$的方向沿着从刚体到坐标系$Frame\{{\mathcal{B}}\}$的原点$O_B$的方向。与此同时刚体$B$还受到过点$O$的力矩$n_O$的作用，那么对刚体上的任意一点$P$来说，表示其力矩如下：

$$
{\vec{n}}_{P}={\vec{n}}_{O}+{\vec{f}}{\times}{\vec{OP}}
$$

我们可以使用以下的方式来表示刚体$B$的力：

$$
{^{B}}{\hat{f}}=
\begin{pmatrix}
{^{B}}{n_O}\\
{^{B}}{f}
\end{pmatrix}
{\in}{\mathbb{R}^{6}}
$$

这里就是刚体刚体$B$的**空间力向量**。

!!! note "空间力向量"
    Contents


## 2.3-Plücker坐标，线矢量和自由矢量


!!! note "线矢量"
    线矢量$L$是一个依附在空间某一直线上的六维向量，含有**主部（原部）**和**副部（对偶部）**两个部分。主部是矢量的轴线$\vec{l}$，也是空间直线的姿态向量。副部为该轴线相对原点的矢矩$\vec{l_0}$，线矢量写作如下形式：

    $$
    {\mathbf{L}}=
    \begin{pmatrix}
    {\vec{l}}\\
    {\vec{l_0}}
    \end{pmatrix}=
    \begin{pmatrix}
    {\vec{l}}\\
    {\vec{r}{\times}{\vec{l}}}
    \end{pmatrix} 
    $$


## 2.4-坐标变换
首先我们可以回顾一下空间坐标变换的表示——**齐次矩阵**。
我们有两个坐标系$Frame\{{\mathcal{W}}\}$和$Frame\{{\mathcal{B}}\}$如下：

其中$Frame\{{\mathcal{B}}\}$的原点坐标$O_B$在坐标系$Frame\{{\mathcal{W}}\}$中的位置表示我们可以表示为${^W}{\vec{r}}{_{BORG}}$。如果我们表达空间中某一个点$P$的坐标，我们用${^B}{\vec{r}}{_{P}}$表示点$P$相对于$Frame\{{\mathcal{B}}\}$的位置，我们用${^W_B}{R}$表示坐标系$Frame\{{\mathcal{B}}\}$的旋转矩阵，那么我们用齐次坐标表示的矩阵转换如下：

$$
{{^W_B}\mathbf{T}}=
{
\begin{pmatrix}
{{^W_B}\mathbf{R}}&{{^W}{\vec{r}}{_{BORG}}}\\
{{\mathbf{0}}_{1{\times}3}}&{1}
\end{pmatrix}
}
$$

这个就是针对空间三维坐标系的**齐次变换矩阵**。我们可以把从坐标系$Frame\{{\mathcal{W}}\}$到$Frame\{{\mathcal{B}}\}$的变换看作**平移**和**旋转**两个过程组合后的结果：

- **平移**：首先是坐标系$Frame\{{\mathcal{W}}\}$沿着从坐标系原点$O_W$出发的矢量${\vec{r}}{_{BORG}}$进行平移，平移后的坐标系原点是$O_B$，这个过程可以用下面的矩阵表示：

$$
{
\begin{pmatrix}
{{\mathbf{E}}_{3\times3}}&{{^W}{\vec{r}}{_{BORG}}}\\
{{\mathbf{0}}_{1\times3}}&{1}
\end{pmatrix}
}
$$

- **旋转**：在平移之后，我们以平移后的坐标系原点$O_B$为定点进行坐标系的定点旋转，最终得到坐标系$Frame\{{\mathcal{B}}\}$。这个过程可以用下面的矩阵表示：

$$
{
\begin{pmatrix}
{{^W_B}\mathbf{R}}&{{\mathbf{0}}_{3{\times}1}}\\
{{\mathbf{0}}_{1{\times}3}}&{1}
\end{pmatrix}
}
$$

那么这两个过程可以联合起来表示如下：

$$
{{^W_B}\mathbf{T}}=
{
\begin{pmatrix}
{{^W_B}\mathbf{R}}&{{^W}{\vec{r}}{_{BORG}}}\\
{{\mathbf{0}}_{1{\times}3}}&{1}
\end{pmatrix}
}={
\begin{pmatrix}
{{^W_B}\mathbf{R}}&{{\mathbf{0}}_{3{\times}1}}\\
{{\mathbf{0}}_{1{\times}3}}&{1}
\end{pmatrix}
}{
\begin{pmatrix}
{{\mathbf{E}}_{3\times3}}&{{^W}{\vec{r}}{_{BORG}}}\\
{{\mathbf{0}}_{1\times3}}&{1}
\end{pmatrix}
}
$$

接下来，我们也可以类比上面的齐次坐标矩阵的推导方式来推导**空间速度向量的空间速度向量变换矩阵**${X}$：
我们假设有一个空间速度向量，这个空间速度向量相对于固定的世界坐标系$Frame\{{\mathcal{W}}\}$的位置不变，这个空间速度向量在坐标系$Frame\{{\mathcal{B}}\}$的表示如下：

$$
{^{B}}{\hat{m}}=
\begin{pmatrix}
{^{B}}{m}\\
{^{B}}{m_O}
\end{pmatrix}
$$

首先讨论以下坐标系的两种特殊情况：**仅平移的情况**和**仅旋转的情况**：
- **仅平移的情况**：$Frame\{{\mathcal{B}}\}$沿着从坐标系原点$O_B$为起点的向量$\vec{r}$平移，平移后坐标系是$Frame\{{\mathcal{C}}\}$。首先我们在坐标系$Frame\{{\mathcal{B}}\}$中表示刚体内任意一点$P$的位置：

$$
{^B}{\vec{v}}{_P}={^B}{m}{_O}+{^B}{m}{\times}{^B}{\vec{r}_{BP}}
$$

然后我们在坐标系$Frame\{{\mathcal{C}}\}$中表示该刚体内任意一点$P$的位置：

$$
{^C}{\vec{v}}{_P}={^C}{m}{_O}+{^C}{m}{\times}{^C}{\vec{r}_{CP}}
$$

由于坐标系$Frame\{{\mathcal{B}}\}$和$Frame\{{\mathcal{C}}\}$是平移，那么我们可以将上面的式子表示成如下形式：

$$
\begin{align}{^B}{\vec{v}}{_P}&={^B}{m}{_O}+{^B}{m}{\times}{^B}{\vec{r}_{CP}}\\&={^B}{m}{_O}+{^B}{m}{\times}({{^B}{\vec{r}_{BP}}}-{{^B}{\vec{r}_{BC}}})\end{align}
$$

由于是平移，那么转换为：

$$
{^{C}_{B}\mathbf{R}}={^{B}_{C}\mathbf{R}}={{\mathbf{E}}_{3\times3}}
$$

我们有以下等式成立：

$$
\begin{matrix}{^B}{\vec{v}}{_P}={^C}{\vec{v}}{_P}={\vec{v}}{_P}\\{^{B}}{m}={^{C}}{m}={m}\\{^B}{\vec{r}_{BP}}={^C}{\vec{r}_{BP}}={\vec{r}_{BP}}\\{^B}{\vec{r}_{CP}}={^C}{\vec{r}_{CP}}={\vec{r}_{CP}}\\{^B}{\vec{r}_{BC}}={^C}{\vec{r}_{BC}}={\vec{r}_{BC}}\\\end{matrix}
$$

那么将前面的式子联立可以得到：

$$
\begin{align}{^C}{m}{_O}+{m}{\times}({{\vec{r}_{BP}}}-{{\vec{r}_{BC}}})&={^B}{m}{_O}+{m}{\times}{\vec{r}_{BP}}\\{^C}{m}{_O}-{m}{\times}{{\vec{r}_{BC}}}&={^B}{m}{_O}\\{^C}{m}{_O}&={^B}{m}{_O}+{m}{\times}{{\vec{r}_{BC}}}\\{^C}{m}{_O}&={^B}{m}{_O}-{{\vec{r}_{BC}}}{\times}{m}\end{align}
$$

那么我们的空间速度向量在坐标系$Frame\{{\mathcal{C}}\}$可以表示为：

$$
{^{C}}{\hat{m}}=
\begin{pmatrix}
{^{C}}{m}\\
{^{C}}{m_O}
\end{pmatrix}={
\begin{pmatrix}
{{\mathbf{E}}_{3\times3}}&{0}\\
{-[{^B}{r}{_{CORG}}]_{\times}}&{{\mathbf{E}}_{3\times3}}
\end{pmatrix}
}{^{B}}{\hat{m}}
$$

对应的空间速度矢量的变换矩阵可以表示如下：

$$
{{^C_B}\mathbf{X}}={
\begin{pmatrix}
{{\mathbf{E}}_{3\times3}}&{0}\\
{-[{^B}{r}{_{CORG}}]_{\times}}&{{\mathbf{E}}_{3\times3}}
\end{pmatrix}
}
$$

- **仅旋转的情况**：$Frame\{{\mathcal{B}}\}$以点$O_B$定点旋转一个角度后变成坐标系$Frame\{{\mathcal{C}}\}$，$Frame\{{\mathcal{B}}\}$和$Frame\{{\mathcal{C}}\}$的坐标系是重合的，那么坐标系$Frame\{{\mathcal{C}}\}$相对于$Frame\{{\mathcal{B}}\}$的旋转矩阵记为${_C^B}{R}$。那么我们的空间速度向量在坐标系$Frame\{{\mathcal{C}}\}$可以表示为：

$$
{^{C}}{\hat{m}}=
\begin{pmatrix}
{^{C}}{m}\\
{^{C}}{m_O}
\end{pmatrix}={
\begin{pmatrix}
{{_B^C}\mathbf{R}}&{0}\\
{0}&{{_B^C}\mathbf{R}}
\end{pmatrix}
}{^{B}}{\hat{m}}
$$

对应的空间速度矢量的变换矩阵可以表示如下：

$$
{{^C_B}\mathbf{X}}={\begin{pmatrix}
{{_B^C}\mathbf{R}}&{0}\\
{0}&{{_B^C}\mathbf{R}}
\end{pmatrix}}
$$

那么根据三维坐标系的坐标系变换，我们也可以将空间速度矢量的坐标转换看作是坐标系的先平移后旋转的一个过程，那么我们就可以将从坐标系$Frame\{{\mathcal{B}}\}$到$Frame\{{\mathcal{C}}\}$的更一般的空间速度矢量的转换矩阵如下：

$$
{{^C_B}\mathbf{X}}={\begin{pmatrix}
{{_B^C}\mathbf{R}}&{0}\\
{-{{_B^C}\mathbf{R}}{[^{B}{\vec{r}}{_{CORG}}}]_{\times}}&{{_B^C}\mathbf{R}}
\end{pmatrix}}
$$

这样，我们就得到了**空间变换矩阵**：

!!! note "空间变换矩阵(Spatial Transformation Matrix)"
    假设有两个坐标系 $Frame{\{\mathcal{A}\}}$ 和 $Frame{\{\mathcal{B}\}}$ 。$Frame{\{\mathcal{B}\}}$ 坐标系相对于 $Frame{\{\mathcal{A}\}}$ 坐标系的几何关系由旋转矩阵 $\mathbf{R} = {^A_B \mathbf{R}}$ 和位置向量 ${p} = {^A\vec{p}_{BORG}}$ (即$Frame{\{\mathcal{B}\}}$原点在$Frame{\{\mathcal{A}\}}$中的位置) 确定。
    **空间变换矩阵 ${{^A_B}\mathbf{X}}$** 用于将空间矢量从$Frame{\{\mathcal{B}\}}$ 坐标系转换到 $Frame{\{\mathcal{A}\}}$ 坐标系， 的定义如下：

    $$
    {{^A_B}\mathbf{X}} = \begin{pmatrix} \mathbf{R} & {\mathbf{0}}_{3{\times}3} \\ [{p}]_{\times} \mathbf{R} & \mathbf{R} \end{pmatrix}
    $$

    其中：
    - $\mathbf{R} = {^A_B\mathbf{ R}}$ 是 $3 \times 3$ **旋转矩阵**。
    -  ${p} = {^A\vec{p}_{BORG}}$ 是 $3 \times 1$ **位置向量**
    - $[{p}]_{\times}$ 是位置向量 ${p}$ 对应的 $3 \times 3$ **斜对称叉乘矩阵**。


!!! note "空间变换矩阵的性质"
    Contents


!!! note "空间变换矩阵的对偶形式"
    Contents

## 2.5-空间向量的标量积

!!! note "空间向量的标量积"
    基于空间矢量我们定义标量积，这个标量积的其中一个参数为**空间速度向量**，另外一个参数是**空间力向量**。两者相乘的结果是一个**表示能量，功率或者类似的物理量**。
    我们给定一个空间速度向量${\mathbf{m}}{\in}{{M}^{6}}$和一个空间力向量${\mathbf{f}}{\in}{{F}^{6}}$，我们将这两个向量进行点乘运算，点乘运算可以表示为${\mathbf{m}}{\cdot}{\mathbf{f}}$或者${\mathbf{f}}{\cdot}{\mathbf{m}}$，**这两者等价**。


!!! warning "空间向量的标量积的物理含义"
    - 空间向量的标量积只有${\mathbf{m}}{\cdot}{\mathbf{f}}$或者${\mathbf{f}}{\cdot}{\mathbf{m}}$才具有物理含义，这个运算表示的是刚体运动的功率，能量等类似物理量。
    - 运算${\mathbf{f}}{\cdot}{\mathbf{f}}$或者${\mathbf{m}}{\cdot}{\mathbf{m}}$没有任何物理含义。

## 2.6-空间向量叉乘

!!! note "空间向量的叉乘"
    Contents

## 2.7-空间向量求导

!!! note "空间向量的求导"
    Contents
