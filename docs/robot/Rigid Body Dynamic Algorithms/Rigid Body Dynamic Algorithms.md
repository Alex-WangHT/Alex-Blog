# 1-多刚体系统动力学的一般表达形式

!!! note "运动学的任务"
    - **前向动力学（Forward Dynamics）**：根据刚体的受力求解刚体的加速度。
    - **逆向动力学（Inverse Dynamics）**：根据刚体的加速度求解刚体受力。


!!! note "刚体系统的运动方程表达"
    刚体系统的运动方程可以写成以下的**标准形式**：
    ```math
    {\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}
    ```
    其中：
    - ${\mathbf{q}}$，${\mathbf{\dot{q}}}$，${\mathbf{\ddot{q}}}$代表刚体的位置，速度和加速度变量的矢量。
    - ${\boldsymbol{\tau}}$是作用力的矢量。
    - ${\mathbf{H}(\mathbf{q})}$是惯量项矩阵。
    - ${\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}$是力项的矢量，它表示科里奥利力和离心力，重力，以及作用在系统上的除τ中的力以外的任何其他力。

# 2-空间向量及其性质
## 2.1-空间速度向量
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
首先我们可以回顾一下空间坐标变换的表示——齐次矩阵**。
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
- **平移**：首先是坐标系$Frame\{{\mathcal{W}}\}$沿着从坐标系原点$O_W$出发的矢量${\vec{r}}{_{BORG}}$进行平移，平移后的坐标系原点是$O_B$，这个过程可以用下面的矩阵表示：$${
\begin{pmatrix}
{{\mathbf{E}}_{3\times3}}&{{^W}{\vec{r}}{_{BORG}}}\\
{{\mathbf{0}}_{1\times3}}&{1}
\end{pmatrix}
}$$
- **旋转**：在平移之后，我们以平移后的坐标系原点$O_B$为定点进行坐标系的定点旋转，最终得到坐标系$Frame\{{\mathcal{B}}\}$。这个过程可以用下面的矩阵表示：$${
\begin{pmatrix}
{{^W_B}\mathbf{R}}&{{\mathbf{0}}_{3{\times}1}}\\
{{\mathbf{0}}_{1{\times}3}}&{1}
\end{pmatrix}
}$$那么这两个过程可以联合起来表示如下：
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
我们假设有一个空间速度向量，这个空间速度向量相对于固定的世界坐标系$Frame\{{\mathcal{W}}\}$的位置不变，这个空间速度向量在坐标系$Frame\{{\mathcal{B}}\}$的表示如下：$${^{B}}{\hat{m}}=
\begin{pmatrix}
{^{B}}{m}\\
{^{B}}{m_O}
\end{pmatrix}$$首先讨论以下坐标系的两种特殊情况：**仅平移的情况**和**仅旋转的情况**：
- **仅平移的情况**：$Frame\{{\mathcal{B}}\}$沿着从坐标系原点$O_B$为起点的向量$\vec{r}$平移，平移后坐标系是$Frame\{{\mathcal{C}}\}$。首先我们在坐标系$Frame\{{\mathcal{B}}\}$中表示刚体内任意一点$P$的位置：$${^B}{\vec{v}}{_P}={^B}{m}{_O}+{^B}{m}{\times}{^B}{\vec{r}_{BP}}$$然后我们在坐标系$Frame\{{\mathcal{C}}\}$中表示该刚体内任意一点$P$的位置：$${^C}{\vec{v}}{_P}={^C}{m}{_O}+{^C}{m}{\times}{^C}{\vec{r}_{CP}}$$由于坐标系$Frame\{{\mathcal{B}}\}$和$Frame\{{\mathcal{C}}\}$是平移，那么我们可以将上面的式子表示成如下形式：$$\begin{align}{^B}{\vec{v}}{_P}&={^B}{m}{_O}+{^B}{m}{\times}{^B}{\vec{r}_{CP}}\\&={^B}{m}{_O}+{^B}{m}{\times}({{^B}{\vec{r}_{BP}}}-{{^B}{\vec{r}_{BC}}})\end{align}$$由于是平移，那么转换为：$${^{C}_{B}\mathbf{R}}={^{B}_{C}\mathbf{R}}={{\mathbf{E}}_{3\times3}}$$我们有以下等式成立：$$\begin{matrix}{^B}{\vec{v}}{_P}={^C}{\vec{v}}{_P}={\vec{v}}{_P}\\{^{B}}{m}={^{C}}{m}={m}\\{^B}{\vec{r}_{BP}}={^C}{\vec{r}_{BP}}={\vec{r}_{BP}}\\{^B}{\vec{r}_{CP}}={^C}{\vec{r}_{CP}}={\vec{r}_{CP}}\\{^B}{\vec{r}_{BC}}={^C}{\vec{r}_{BC}}={\vec{r}_{BC}}\\\end{matrix}$$那么将前面的式子联立可以得到：$$\begin{align}{^C}{m}{_O}+{m}{\times}({{\vec{r}_{BP}}}-{{\vec{r}_{BC}}})&={^B}{m}{_O}+{m}{\times}{\vec{r}_{BP}}\\{^C}{m}{_O}-{m}{\times}{{\vec{r}_{BC}}}&={^B}{m}{_O}\\{^C}{m}{_O}&={^B}{m}{_O}+{m}{\times}{{\vec{r}_{BC}}}\\{^C}{m}{_O}&={^B}{m}{_O}-{{\vec{r}_{BC}}}{\times}{m}\end{align}$$那么我们的空间速度向量在坐标系$Frame\{{\mathcal{C}}\}$可以表示为：$${^{C}}{\hat{m}}=
\begin{pmatrix}
{^{C}}{m}\\
{^{C}}{m_O}
\end{pmatrix}={
\begin{pmatrix}
{{\mathbf{E}}_{3\times3}}&{0}\\
{-[{^B}{r}{_{CORG}}]_{\times}}&{{\mathbf{E}}_{3\times3}}
\end{pmatrix}
}{^{B}}{\hat{m}}$$对应的空间速度矢量的变换矩阵可以表示如下：$${{^C_B}\mathbf{X}}={
\begin{pmatrix}
{{\mathbf{E}}_{3\times3}}&{0}\\
{-[{^B}{r}{_{CORG}}]_{\times}}&{{\mathbf{E}}_{3\times3}}
\end{pmatrix}
}$$
- **仅旋转的情况**：$Frame\{{\mathcal{B}}\}$以点$O_B$定点旋转一个角度后变成坐标系$Frame\{{\mathcal{C}}\}$，$Frame\{{\mathcal{B}}\}$和$Frame\{{\mathcal{C}}\}$的坐标系是重合的，那么坐标系$Frame\{{\mathcal{C}}\}$相对于$Frame\{{\mathcal{B}}\}$的旋转矩阵记为${_C^B}{R}$。那么我们的空间速度向量在坐标系$Frame\{{\mathcal{C}}\}$可以表示为：$${^{C}}{\hat{m}}=
\begin{pmatrix}
{^{C}}{m}\\
{^{C}}{m_O}
\end{pmatrix}={
\begin{pmatrix}
{{_B^C}\mathbf{R}}&{0}\\
{0}&{{_B^C}\mathbf{R}}
\end{pmatrix}
}{^{B}}{\hat{m}}$$对应的空间速度矢量的变换矩阵可以表示如下：$${{^C_B}\mathbf{X}}={\begin{pmatrix}
{{_B^C}\mathbf{R}}&{0}\\
{0}&{{_B^C}\mathbf{R}}
\end{pmatrix}}$$
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
    ```math
    {{^A_B}\mathbf{X}} = \begin{pmatrix} \mathbf{R} & {\mathbf{0}}_{3{\times}3} \\ [{p}]_{\times} \mathbf{R} & \mathbf{R} \end{pmatrix}
    ```
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

# 3-刚体运动学和刚体动力学
## 3.1-刚体的空间速度 (Spatial Velocity)
在经典力学中，我们通常将角速度 $\omega$ 和线速度 $v$ 分开处理。但在空间矢量代数中，这两者被合成为一个 **6 维矢量**，称为**空间速度（Spatial Velocity）**，通常记为 $\hat{v}$。
### (1)- 定义与构成
对于刚体上的一点 $O$，其空间速度 $\hat{v}_O$ 定义为：
$$
\hat{v}_O = \begin{bmatrix} \omega \\ v_O \end{bmatrix} \in \mathbb{R}^6
$$
- **角速度 $\omega$**：描述刚体整体的旋转。
- **线速度 $v_O$**：描述刚体上选定参考点 $O$ 的瞬时平移速度。
### (2)-坐标变换
如果你需要将速度从坐标系 $B$ 转换到坐标系 $A$，使用变换矩阵 ${^A_B X}$：

$$
{}^A \hat{v} = {^A_B X}^B \hat{v}
$$
展开形式为：
$$
\begin{bmatrix} {}^A \omega \\ {}^A v_A \end{bmatrix} = \begin{bmatrix} \mathbf{E} & \mathbf{0} \\ -\mathbf{E} \mathbf{r}\times & \mathbf{E} \end{bmatrix} \begin{bmatrix} {}^B \omega \\ {}^B v_B \end{bmatrix}
$$
这里反映了一个关键物理事实：**线速度会随着参考点的改变而改变**（即 $v_A = \mathbf{E}(v_B - r \times \omega)$），而角速度在旋转变换下保持几何一致性。
## 3.2-刚体的空间加速度 (Spatial Acceleration)
空间加速度描述了空间速度的变化率。然而，在旋转坐标系下，加速度的定义比速度稍微复杂一些。
### (1)- 经典空间加速度 (Classical Spatial Acceleration)
最直接的定义是对空间速度直接求导：
$$
\hat{a} = \frac{d}{dt} \hat{v} = \begin{bmatrix} \dot{\omega} \\ \dot{v}_O \end{bmatrix}
$$
但在机器人学中，为了方便递归计算（如 RNEA 算法），通常使用**体坐标系下的加速度**。
### (2)- 空间加速度的组成
对于一个在空间中运动的连杆，其加速度通常由两部分组成：
1. **主动加速度**：由关节驱动产生的加速度。
2. **偏置加速度 (Bias Acceleration)**：由于旋转产生的向心加速度和科氏加速度（Coriolis acceleration）。

在空间算子表示法中，连杆 $i$ 的加速度传递方程为：
$$
{}^i \hat{a} = {}^i X_{i-1} {}^{i-1} \hat{a} + \mathbf{S}_i \ddot{q}_i + \hat{v}_i \times \mathbf{S}_i \dot{q}_i
$$
- **${}^i X_{i-1} {}^{i-1} \hat{a}$**：基座/上一个连杆传来的加速度。
- **$\mathbf{S}_i \ddot{q}_i$**：当前关节的加速度映射。
- **$\hat{v}_i \times \mathbf{S}_i \dot{q}_i$**：速度相关的修正项（包含速度积项）。
## 3.3-刚体的空间刚体动量
首先我们已知刚体$B$的质心为刚体内一点$C$，点$C$的质心速度在坐标系坐标系$Frame\{{\mathcal{B}}\}$表示如下：
$$
\begin{align}
{^{B}{\vec{v}}_{C}}&={{^{B}}{v}_{O}}+{{^{B}}{\omega}}{\times}{^{B}{\vec{r}}_{C}}\\
&={{^{B}}{v}_{O}}+{^{B}{\vec{r}}_{CO}}{\times}{{^{B}}{\omega}}\\
\end{align}
$$
已知刚体$B$的质量是$m_B$，刚体$B$关于质心的惯性张量为$I_B$。首先我们可以求得刚体的动量$P_B$如下：
$$
P_B={m_B}{^{B}{\vec{r}}_{CO}}{\times}{{^{B}}{\omega}}+{m_B}{{^{B}}{v}_{O}}
$$
然后我们求刚体$B$的角动量$L_B$如下：
$$
\begin{align}
L_B={I_B}{{^{B}}{\omega}}+{m_B}{^{B}{\vec{r}}_{OC}}{\times}{({^{B}{\vec{r}}_{CO}}{\times}{{^{B}}{\omega}})}+{m_B}{^{B}{\vec{r}}_{OC}}{\times}{{^{B}}{v}_{O}}
\end{align}
$$
我们可以定义刚体$B$在坐标系$Frame\{{\mathcal{B}}\}$的空间动量${\hat{h}}_{B}$：
$$
{\hat{h}_{B}}
={\begin{pmatrix}{L_B}\\ {P_B}\end{pmatrix}}
={\begin{pmatrix}{{I_B}{{^{B}}{\omega}}+{m_B}{^{B}{\vec{r}}_{OC}}{\times}{({^{B}{\vec{r}}_{CO}}{\times}{{^{B}}{\omega}})}+{m_B}{^{B}{\vec{r}}_{OC}}{\times}{{^{B}}{v}_{O}}}\\{{m_B}{^{B}{\vec{r}}_{CO}}{\times}{{^{B}}{\omega}}+{m_B}{{^{B}}{v}_{O}}}\\ \end{pmatrix}}
$$
## 3.4-刚体的空间刚体惯量矩
我们将刚体$B$的空间动量${\hat{h}}_{B}$写成矩阵${^{B}{\hat{I}}}{\in}{\mathbb{R}^{6\times6}}$和空间速度${^{B}}{\hat{v}}$相乘表示形式：
$$
\begin{align}
{{\hat{h}}_{B}}={^{B}{\hat{I}}}{^{B}{\hat{v}}}
={\begin{pmatrix}{I_B}-{m_B}{[{^{B}{\vec{r}}_{CO}}]^{2}_{\times}}&-{{m_B}[{^{B}{\vec{r}}_{CO}}]_{\times}}\\{{m_B}[{^{B}{\vec{r}}_{CO}}]_{\times}}&{{m_B}{\boldsymbol{1}_{3{\times}{3}}}}\end{pmatrix}}{\begin{pmatrix}{^{B}}{\omega}\\ {^{B}}{v_O}
\end{pmatrix}}
\end{align}
$$
其中矩阵${^{B}{\hat{I}}}$即为刚体$B$在坐标系$Frame\{{\mathcal{B}}\}$下定义的空间惯量矩：
$$
{^{B}{\hat{I}}}={\begin{pmatrix}{I_B}-{m_B}{[{^{B}{\vec{r}}_{CO}}]^{2}_{\times}}&-{{m_B}[{^{B}{\vec{r}}_{CO}}]_{\times}}\\{{m_B}[{^{B}{\vec{r}}_{CO}}]_{\times}}&{{m_B}{\boldsymbol{1}_{3{\times}{3}}}}\end{pmatrix}}
$$
## 3.5-刚体的动能
根据柯尼希定理，刚体的动能表示如下：
$$
T={\frac{1}{2}}{m}{\cdot}({{^{B}}{v_C^T}}){\cdot}({{^{B}}{v_C}})+{\frac{1}{2}}{{{{^{B}}{\omega}^T}}{\cdot}{I_B}{\cdot}{{^{B}}{\omega}}}
$$
其中质心速度$v_C = v_O + \omega \times r_{CO}$
改写成空间速度和空间惯量的表达式如下：
$$
\begin{align}
{T}&={\frac{1}{2}}{{\boldsymbol{\hat{v}}}^T}{\boldsymbol{\hat{I}}}{\boldsymbol{\hat{v}}}\\
&={\frac{1}{2}}{\boldsymbol{q}^T}{{\boldsymbol{S}^T}{\boldsymbol{\hat{I}}}{\boldsymbol{S}}}{\boldsymbol{q}}
\\
&={\frac{1}{2}}{\boldsymbol{q}^T}{\boldsymbol{H}}{\boldsymbol{q}}
\end{align}
$$
其中${\boldsymbol{H}}={\boldsymbol{S}^T}{\boldsymbol{\hat{I}}}{\boldsymbol{S}}$。
## 3.6-刚体的空间刚体惯量矩的逆
我们定义$^{B}{\hat{\Phi}}={^{B}{\hat{I}}}^{-1}$，矩阵$^{B}{\hat{\Phi}}={^{B}{\hat{I}}}^{-1}$即为空间刚体惯量矩的逆，该矩阵定义如下：
$$
{^{B}{\hat{\Phi}}} = \begin{pmatrix} I_B^{-1} & -I_B^{-1}[{^{B}{r}_{OC}}]_\times \\ [{^{B}{r}_{OC}}]_\times{I_B}^{-1} & \frac{1}{m}\mathbf{1} - [{^{B}{r}_{OC}}]_\times{I_B}^{-1}[{^{B}{r}_{OC}}]_\times \end{pmatrix}
$$
## 3.7-刚体的空间动力学方程
我们已知刚体$B$的空间动量${\hat{h}}_{B}$如下：$${{\hat{h}}_{B}}={^{B}{\hat{I}}}{^{B}{\hat{v}}}$$我们对空间动量${\hat{h}}_{B}$求导如下，得到空间力${\hat{f}}_{B}$：
$$
\begin{align}
{{\hat{f}}_{B}}&={\frac{d{\hat{h}_B}}{dt}}\\
&={^{B}{\hat{I}}}{^{B}{\hat{a}}}+({\frac{d}{dt}}{^{B}{\hat{I}}}){^{B}{\hat{v}}}\\
&={^{B}{\hat{I}}}{^{B}{\hat{a}}}+({^{B}{\hat{v}}}{\times^*}{^{B}{\hat{I}}}-{^{B}{\hat{I}}}{^{B}{\hat{v}}}{\times}){^{B}{\hat{v}}}\\
&={^{B}{\hat{I}}}{^{B}{\hat{a}}}+{^{B}{\hat{v}}}{\times^*}{^{B}{\hat{I}}}{^{B}{\hat{v}}}
\end{align}
$$
那么我们就能得到刚体的空间动力学方程：
$$
\begin{align}
{^{B}{\hat{f}}}
&={^{B}{\hat{I}}}{^{B}{\hat{a}}}+{^{B}{\hat{v}}}{\times^*}{^{B}{\hat{I}}}{^{B}{\hat{v}}}\\
&={^{B}{\hat{I}}}{^{B}{\hat{a}}}+{^{B}{\hat{p}}}
\end{align}
$$
其中 $\hat{p}_B = \hat{v}_B \times^* \hat{I}_B \hat{v}_B$ 称为**偏置力**。

!!! tip "刚体动力学方程不同形式之间的对比与联系"

>- **刚体动力学方程对比**：空间向量形式 vs. 关节空间标准形式
>
>| 特性 | 空间动力学方程 (Spatial Form) | 关节空间标准形式 (Joint Space/Standard Form) |
> | :--- | :--- | :--- |
> | **数学表达** | $\hat{f} = \hat{I}\hat{a} + \hat{v} \times^* \hat{I}\hat{v}$ | $\mathbf{H}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q}, \dot{\mathbf{q}}) = \boldsymbol{\tau}$ |
> | **描述维度** | $6 \times 1$ 空间向量 | $n \times 1$ 广义坐标向量 ($n$ 为自由度) |
> | **描述对象** | **单个刚体**：描述空间力与空间运动的关系 | **完整系统**：描述关节力矩与关节运动的关系 | 
> | **惯性项** | $\hat{I}$：$6\times6$ 空间惯量阵（在随动坐标系下通常为常数） | $\mathbf{H}(\mathbf{q})$：关节空间惯性矩阵（随姿态 $\mathbf{q}$ 剧烈变化） | 
> | **非线性项** | $\hat{v} \times^* \hat{I}\hat{v}$：空间偏置力（包含向心力和科氏力） | $\mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})$：广义向心力与科氏力项 | 
> | **主要用途** | 动力学算法的底层物理推导与递归实现（如 RNEA） | 控制律设计、仿真、轨迹规划及系统稳定性分析 |
>-  **数学联系（映射关系）**:关节空间的形式本质上是空间动力学方程通过**雅可比矩阵 $J$** 进行投影和聚合的结果：
>	1. **运动学映射**：$\hat{v}_i = \mathbf{J}_i(\mathbf{q})\dot{\mathbf{q}}$
>	2. **惯性映射**：$\mathbf{H}(\mathbf{q}) = \sum_{i=1}^{n} \mathbf{J}_i^T \hat{I}_i \mathbf{J}_i$
>	3. **力矩映射**：$\boldsymbol{\tau} = \sum_{i=1}^{n} \mathbf{J}_i^T \hat{f}_i$

已知空间力$^{B}{\hat{f}}$，我们可以用下式求解刚体$B$的空间加速度${^{B}{\hat{a}}}$：
$$
{^{B}{\hat{a}}}={^{B}{\hat{\Phi}}}{^{B}{\hat{f}}}+{\hat{b}}
$$
其中 ${\hat{b}}=^{B}{\Phi}{\hat{p}_B}$ 。
# 4-带约束的刚体动力学
## 4.1-刚体的运动约束
### (1)-刚体运动约束的显式表达和隐式表达
刚体的运动约束的表达可以分为**显式**和**隐式**：
- **显式表达**：显式表达的数学形式如下：$${\boldsymbol{q}}={\boldsymbol{\gamma}}(\boldsymbol{y})$$其中$\boldsymbol{q}$表示刚体的位置坐标，$\boldsymbol{y}$表示表示系统的 **独立广义坐标**。那么由该显式约束我们可以得到含有速度和加速度的形式：$$\dot{\boldsymbol{q}} = \frac{\partial \boldsymbol{\gamma}}{\partial \boldsymbol{y}} \dot{\boldsymbol{y}} = \mathbf{G}(\boldsymbol{y}) \dot{\boldsymbol{y}}{\quad}{{\boldsymbol{\ddot{q}}}={\boldsymbol{G}(\boldsymbol{y}) }\boldsymbol{\ddot{y}}}+{\boldsymbol{g}}$$其中$\boldsymbol{G}$为雅各比矩阵，$\boldsymbol{g}$的定义如下：$${{\boldsymbol{g}}={\boldsymbol{\dot{G}}}}({\boldsymbol{y}}){{\boldsymbol{\dot{y}}}}$$
- **隐式表达**：隐式表达的数学形式定义如下：$${\boldsymbol{\phi}}({\boldsymbol{q}})=0$$这里的${\boldsymbol{q}}$表示刚体的位置坐标，该方程在空间中定义了一个几何流形，**限制了刚体所有可能的位形（Position/Orientation）**，即刚体只能在满足该等式的空间内运动。我们可以将隐式约束求导，得到以下含有速度和加速度的形式：$${{\boldsymbol{K}}{\boldsymbol{\dot{q}}}={\boldsymbol{0}}}{\quad}{{\boldsymbol{K}}{\boldsymbol{\ddot{q}}}={\boldsymbol{k}}}$$其中：$${\boldsymbol{K}}={\frac{\partial{\boldsymbol{\phi}}}{\partial{\boldsymbol{q}}}}{\quad}{{\boldsymbol{k}}=-{\boldsymbol{\dot{K}}}{\boldsymbol{\dot{q}}}}$$
### (2)-刚体约束的分类
我们在理论力学里面已经提到过约束的分类，这些分类都有一个特点：**约束的类型都是类似于${\boldsymbol{\phi}}({\boldsymbol{q}})=0$的隐式约束的形式**，对于隐式约束形式 （或不等式形式），我们可以将其分为以下三大类：
- **单边约束 (Unilateral)与双边约束(Bilateral)**：这是根据约束对系统运动方向的**限制范围**来划分的：
	- **单边约束 (Unilateral)**：
	    * **数学形式**：$f(q_1, q_2, \dots, q_n, t) \ge 0$ （不等式约束）。
	    * **物理意义**：质点可以在某一区域内运动，但不能穿过边界，且在某些条件下可以脱离边界。
	    * **例子**：放在桌面上的小球 ($z \ge 0$)，用软绳悬挂的单摆 ($l \le L$)。
	* **双边约束 (Bilateral)**：
	    * **数学形式**：$f(q_1, q_2, \dots, q_n, t) = 0$ （等式约束）。
	    * **物理意义**：质点必须在指定的曲面或曲线上运动，不能离开。
	    * **例子**：圆锥摆中的刚性细杆，滑块在固定的导轨上运动。
- **完整约束(Holonomic)与非完整约束(Non-holonomic)**：这是根据约束方程是否限制了系统的**位形空间（坐标可达性）** 来划分的：
	* **完整约束 (Holonomic)**：
	    * **定义**：只限制系统的位置坐标，其方程可表示为 $f(\boldsymbol{q}, t) = 0$。如果约束包含速度但可以积分还原为坐标关系，也属于完整约束。
	    * **特点**：独立广义坐标的数目等于系统的自由度。
	* **非完整约束 (Non-holonomic)**：
	    * **定义**：约束方程中含有不可积分的速度项，或者约束为单边约束（不等式）。
	    * **例子**：硬币在地面上纯滚动而不打滑。虽然它限制了瞬时速度方向，但并没有限制硬币最终能到达桌面的哪个位置。
- **稳定约束(Scleronomic)与不稳定约束(Rheonomic)**：这是根据约束条件是否随**时间显式变化**来划分的：
	- **稳定约束 (Scleronomic Constraints)**：
		* **定义**：约束条件不随时间改变，约束方程中不显式包含时间 $t$。 
		* **数学表达式**： $$\boldsymbol{\phi}(q_1, q_2, \dots, q_n) = 0$$
		* **物理直观**：质点运动的轨道、容器或支座在空间中是固定不动的。 
		* **例子**： 
			* 固定在墙上的单摆（摆长 $l$ 不变）。 
			* 小球在固定的碗内滚动。 
			* 刚体各点之间的距离保持不变（$|r_i - r_j| = d_{ij}$）
	- **不稳定约束 (Rheonomic Constraints)**：
		* **定义**：约束条件随时间显式变化，约束方程中显式包含时间 $t$。 
		* **数学表达式**： $$\boldsymbol{\phi}(q_1, q_2, \dots, q_n, t) = 0$$
		* **物理直观**：限制质点运动的物体本身就在运动或发生形变。 
		* **例子**： 
			* 单摆的悬点正在做周期性上下振动（悬点位置 $y_0 = A \sin(\omega t)$）。 
			* 质点在一段长度随时间不断增长的绳索上运动。 
			* 小球在旋转的直杆上滑动。
我们可以将不同的约束按照**限制范围**，**坐标依赖**和**时间依赖**三点来划分：

| 维度       | 对立类型 A             | 对立类型 B                 |
| :------- | :----------------- | :--------------------- |
| **限制范围** | **双边约束** (等式 $=0$) | **单边约束** (不等式 $\ge 0$) |
| **坐标依赖** | **完整约束** (位置限制)    | **非完整约束** (不可积速度限制)    |
| **时间依赖** | **稳定约束** (不随时间变)   | **不稳定约束** (随时间变)       |


## 4.2-带约束的刚体动力学
### (1)-带约束力的刚体动力学方程

!!! note "带约束的刚体系统的动力学方程表达"
    带约束的刚体系统的动力学方程可以写成以下的**标准形式**：
    ```math
    {\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}+{\boldsymbol{\tau_c}}
    ```
    其中：
    - ${\mathbf{q}}$，${\mathbf{\dot{q}}}$，${\mathbf{\ddot{q}}}$代表刚体的位置，速度和加速度。
    - ${\boldsymbol{\tau}}$是作用力的矢量，${\boldsymbol{\tau_c}}$是约束力的矢量
    - ${\mathbf{H}(\mathbf{q})}$是惯量矩阵。
    - ${\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}$是力项的矢量，它表示科里奥利力和离心力，重力，以及作用在系统上的除τ中的力以外的任何其他力。


### (2)-约束力在不同约束下的表示
首先我们回顾一下**若尔当变分定理**：

!!! note "若尔当变分定理"
    对于受理想约束的系统，在给定时刻 $t$ 和给定位置 $\mathbf{r}$，系统的真实运动满足：主动力与惯性力在**虚速度**（速度变分 $\delta \mathbf{v}$）上所作的**虚功率**之和为零，其数学表达式为：
    ```math
    \sum_{i=1}^{n} \mathbf{R}_i \cdot \delta \mathbf{v}_i = \sum_{i=1}^{n} (\mathbf{F}_i - m_i \dot{\mathbf{v}}_i) \cdot \delta \mathbf{v}_i = 0
    ```


我们设约束力为$\boldsymbol{\tau_c}$，那么我们根据若尔当变分原理可以得到约束力的功率${\boldsymbol{\tau_c}}{\cdot}{\boldsymbol{\dot{q}}}=0$。我们分别使用显式约束和隐式约束来表示约束力${\boldsymbol{\tau_c}}$：
- **显式约束**：我们根据等式$\dot{\boldsymbol{q}} = \mathbf{G}(\boldsymbol{y}) \dot{\boldsymbol{y}}$以及矢量点乘的交换性质${\boldsymbol{\tau_c}}{\cdot}{\boldsymbol{\dot{q}}}={\boldsymbol{\dot{q}}}{\cdot}{\boldsymbol{\tau_c}}=0$可以得到：$${\boldsymbol{\dot{q}}}{\cdot}{\boldsymbol{\tau_c}}={\boldsymbol{\dot{q}}}^{T}{\boldsymbol{\tau_c}}=\dot{\boldsymbol{y}}^{T}\mathbf{G}(\boldsymbol{y})^{T}{\boldsymbol{\tau_c}}=0 $$那么对于任意的$\boldsymbol{y}$来说我们都有：$$\mathbf{G}^{T}{\boldsymbol{\tau_c}}=0$$
- **隐式约束**：给定不含时间的隐式约束：$$\boldsymbol{\phi}(\boldsymbol{q}) = 0$$对其求全导数，得到速度约束方程：$$\frac{d}{dt}\boldsymbol{\phi}(\boldsymbol{q}) = \frac{\partial \boldsymbol{\phi}}{\partial \boldsymbol{q}} \dot{\boldsymbol{q}} = \mathbf{K} \dot{\boldsymbol{q}} = 0$$其中 $\mathbf{K}_{m \times n}$ 便是系统的约束雅可比矩阵。在若尔当原理中，我们考虑的是在当前位形 $\boldsymbol{q}$ 和当前速度 $\dot{\boldsymbol{q}}$ 保持不变的情况下，对速度进行变分。受约束的虚速度 $\delta \dot{\boldsymbol{q}}$ 必须满足：$$\mathbf{K} \delta \dot{\boldsymbol{q}} = 0$$这意味着虚速度 $\delta \dot{\boldsymbol{q}}$ 必须位于雅可比矩阵 $\mathbf{K}$ 的**零空间（Null Space）**，由若尔当原理我们可以知道：$${\boldsymbol{\tau_c^{T}}}\delta \dot{\boldsymbol{q}} = 0$$根据线性代数中的引理（一个向量如果正交于另一个矩阵的零空间，则该向量必然属于该矩阵转置的列空间）：$\boldsymbol{\tau_c}$ 必须能表示为 $\mathbf{K}$ 转置矩阵的线性组合。因此，引入拉格朗日乘子向量 $\boldsymbol{\lambda} = [\lambda_1, \dots, \lambda_m]^T$，得到：$$\boldsymbol{\tau_c} = \mathbf{K}^T \boldsymbol{\lambda}$$
### (3)-不同约束形式下的刚体运动学方程
- **隐式约束**：我们有约束方程如下：$${\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}+{\boldsymbol{\tau_c}}$$其中$\boldsymbol{\tau_c} = \mathbf{K}^T \boldsymbol{\lambda}$，并且带加速度项的约束如下：$$\mathbf{K} \dot{\boldsymbol{q}} = {\boldsymbol{k}}$$那么我们将约束联立可得如下动力学方程，该动力学方程即为在**隐式约束形式的动力学方程**：$$\begin{bmatrix}
\boldsymbol{H} & \boldsymbol{K}^{\mathrm{T}} \\
\boldsymbol{K} & 0
\end{bmatrix}
\begin{bmatrix}
\ddot{\boldsymbol{q}} \\
-\boldsymbol{\lambda}
\end{bmatrix} =
\begin{bmatrix}
\boldsymbol{\tau} - \boldsymbol{C} \\
\boldsymbol{k}
\end{bmatrix}$$其中
- **显式约束**：我们有约束方程如下：$${\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}+{\boldsymbol{\tau_c}}$$其中$\mathbf{G}^{T}{\boldsymbol{\tau_c}}=0$，并且带加速度项的约束如下：$${{\boldsymbol{\ddot{q}}}={\boldsymbol{G}(\boldsymbol{y}) }\boldsymbol{\ddot{y}}}+{\boldsymbol{g}}$$我们联立可得以下的约束方程：$$\begin{bmatrix}
\boldsymbol{H} & -\boldsymbol{1} & 0 \\
-\boldsymbol{1} & 0 & \boldsymbol{G} \\
0 & \boldsymbol{G}^{\mathrm{T}} & 0
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{\ddot{q}} \\
\boldsymbol{\tau_c} \\
\boldsymbol{\ddot{y}}
\end{bmatrix} =
\begin{bmatrix}
\boldsymbol{\tau} - \boldsymbol{C }\\
-\boldsymbol{g} \\
0
\end{bmatrix}$$将左侧的约束矩阵使用高斯消元法化简成上三角的形式，可以得到**显式约束形式的动力学方程**：$$\begin{bmatrix}
\boldsymbol{H} & -\boldsymbol{1} & 0 \\
0 & \boldsymbol{H}^{\mathrm{-1}} & \boldsymbol{G} \\
0 & 0 & -{\boldsymbol{G}^{\mathrm{T}}}{\boldsymbol{H}}{\boldsymbol{G}}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{\ddot{q}} \\
\boldsymbol{\tau_c} \\
\boldsymbol{\ddot{y}}
\end{bmatrix} =
\begin{bmatrix}
\boldsymbol{\tau} - \boldsymbol{C }\\
{\boldsymbol{H}}^{-1}(\boldsymbol{\tau} - \boldsymbol{C}) - \boldsymbol{g} \\ -\boldsymbol{G}^{\mathrm{T}}(\boldsymbol{\tau} - \boldsymbol{C} - \boldsymbol{Hg})
\end{bmatrix}$$我们可以从最后一项中得到一个表达式：$$\boldsymbol{G}^{\mathrm{T}}\boldsymbol{HG} \boldsymbol{\ddot{y}} = \boldsymbol{G}^{\mathrm{T}}(\boldsymbol{\tau} - \boldsymbol{C} - \boldsymbol{Hg})$$化简成如下形式，我们就得到了显式约束的：$$\boldsymbol{H_G \ddot{y}} + \boldsymbol{C_G} = \boldsymbol{u}$$其中$${{\boldsymbol{u}}={\boldsymbol{G}^{\mathrm{T}}}{\boldsymbol{\tau}}}{\quad}\boldsymbol{H_G} = \boldsymbol{G^{\mathrm{T}}HG} {\quad} \boldsymbol{C_G} = \boldsymbol{G^{\mathrm{T}}(C + Hg)}$$
## 4.3-刚体的关节约束
### (1)-矢量子空间的相关知识概念

!!! note "矢量子空间"
    假设我们有一个$n$维的矢量空间$V$，我们定义一个$m$维的子空间${S}{\subseteq}{V}$，那么该子空间$S$的定义如下：
    ```math
    {\mathcal{S}}={\{{\mathbf{s}_1},{\mathbf{s}_2},{\mathbf{s}_3},{\dots},{\mathbf{s}_m}\}}
    ```
    


!!! note "向量分解"
    Contents


!!! note "向量空间的正交补"
    Contents

### (2)-运动子空间和约束力子空间

!!! note "矢量子空间在关节动力学的应用"
    - **空间运动学**：我们已知空间约束的两种形式：显式约束和隐式约束，那么对于这两种约束来说，关节运动的子空间$S$的定义如下：
    	- 对隐式约束来说，关节运动的子空间$\boldsymbol{S}$就是隐式约束的Jacobians矩阵$\boldsymbol{K}$的零空间：$$\boldsymbol{S}=null(\boldsymbol{K}){\subseteq}{M^6}$$
    	- 对显式约束来说，关节运动的子空间$\boldsymbol{S}$就是显式约束的Jacobians矩阵$\boldsymbol{G}$的列空间：$$\boldsymbol{S}=range(\boldsymbol{G}){\subseteq}{M^6}$$
    	- 如果矩阵$\boldsymbol{K}_1$和$\boldsymbol{K}_2$表示同一个约束，那么$null(\boldsymbol{K}_1)=null(\boldsymbol{K}_2)=\boldsymbol{S}$。同理，如果矩阵$\boldsymbol{G}_1$和$\boldsymbol{G}_2$表示同一个约束，那么$range(\boldsymbol{G}_1)=range(\boldsymbol{G}_2)=\boldsymbol{S}$。
    - **空间动力学**：我们定义关节的空间约束力所在的子空间$\boldsymbol{T}={\boldsymbol{S}}^{\perp}$，并且定义关节的空间驱动力$\boldsymbol{T}_a$满足${\boldsymbol{T}}{\oplus}{\boldsymbol{T}_a}={F^{6}}$


### (3)-常见关节类型及其子空间
常见的关节类型以及其对应的变换矩阵，关节位移向量，运动子空间矩阵和约束力子空间矩阵如下：

| 关节类型 (Joint Type)      | 关节变换矩阵 $\mathbf{E}$       | 关节位移向量 $\mathbf{r}$                                                     | 运动子空间矩阵 ($\mathbf{S}$)                                                                                     | 约束力子空间矩阵 ($\mathbf{T}$)                                                                                                                                    |
| :--------------------- | :------------------------ | :---------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **转动关节 (Revolute)**    | $rz(q_1)$                 | $\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$                             | $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}$                                                 | $\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 &0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}$  |
| **移动关节 (Prismatic)**   | $\mathbf{1}_{3 \times 3}$ | $\begin{bmatrix} 0 \\ 0 \\ q_1 \end{bmatrix}$                           | $\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}$                                                 | $\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ |
| **螺旋关节 (Helical)**     | $rz(q_1)$                 | $\begin{bmatrix} 0 \\ 0 \\ h q_1 \end{bmatrix}$                         | $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ h \end{bmatrix}$                                                 | $\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & -h \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0\end{bmatrix}$ |
| **圆柱关节 (Cylindrical)** | $rz(q_1)$                 | $\begin{bmatrix} 0 \\ 0 \\ q_2 \end{bmatrix}$                           | $\begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 0 \\ 0 & 1 \end{bmatrix}$                         | $\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$                           |
| **平面关节 (Planar)**      | $rz(q_1)$                 | $\begin{bmatrix} c_1q_2 - s_1q_3 \\ s_1q_2 + c_1q_3 \\ 0 \end{bmatrix}$ | $\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$                                                 |
| **球关节 (Spherical)**    | 见 Eq. 4.12                | $\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$                             | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$                                                 |
| **6-DoF 关节 (Free)**    | 见 Eq. 4.12                | $\mathbf{E}^{-1} \begin{bmatrix} q_5 \\ q_6 \\ q_7 \end{bmatrix}$       | $\mathbf{1}_{6 \times 6}$                                                                                  | (空)                                                                                                                                                        |
**Notes:**
* $c_1 = \cos(q_1)$, $s_1 = \sin(q_1)$
* $^{s}X_{p} = \text{rot}(\mathbf{E}) \text{xlt}(\mathbf{r})$
### (4)-球形关节的位姿描述方式
球形关节具有定点旋转的三个自由度，我们一般用**欧拉角**和**四元数**来表示球形关节的位置：

!!! note "欧拉角"
    欧拉角（Euler Angles）是描述刚体在三维空间中取向的最直观方式。其核心思想是将一个复杂的旋转拆解为绕三个坐标轴的连续三次旋转。
    欧拉角通过三个角度（如 $\alpha, \beta, \gamma$）来定义物体坐标系相对于参考坐标系的姿态。
    
    - **旋转顺序**：顺序至关重要（如 $Z-Y-X$ 或 $X-Y-Z$），不同的顺序会导致完全不同的最终姿态。
    - **内在旋转 (Intrinsic)**：绕物体自身的动态轴旋转。
    - **外在旋转 (Extrinsic)**：绕固定的参考坐标轴旋转。
    - **万向节锁 (Gimbal Lock)**：当第二次旋转为 $90^\circ$ 时，第一轴与第三轴重合，丢失一个自由度。
    
    以最常用的 **$Z-Y-X$ 顺规**（常用于航空航天的 Roll-Pitch-Yaw）为例，假设旋转角度分别为 $\phi$ (绕 $z$)、$\theta$ (绕 $y$)、$\psi$ (绕 $x$)：
    单个轴的旋转矩阵为：
    ```math
    R_z(\phi) = \begin{bmatrix} \cos\phi & -\sin\phi & 0 \\ \sin\phi & \cos\phi & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}, \quad R_x(\psi) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\psi & -\sin\psi \\ 0 & \sin\psi & \cos\psi \end{bmatrix}
    ```
    组合后的旋转矩阵 $R = R_z R_y R_x$：
    ```math
    R = \begin{bmatrix} c_\phi c_\theta & c_\phi s_\theta s_\psi - s_\phi c_\psi & c_\phi s_\theta c_\psi + s_\phi s_\psi \\ s_\phi c_\theta & s_\phi s_\theta s_\psi + c_\phi c_\psi & s_\phi s_\theta c_\psi - c_\phi s_\psi \\ -s_\theta & c_\theta s_\psi & c_\theta c_\psi \end{bmatrix}
    ```
    (注：$c$ 代表 $\cos$，$s$ 代表 $\sin$)


!!! note "四元数"
    在使用欧拉角描述刚体在空间的姿态的时候，难免会引入奇异值。为了解决描述空间姿态出现的奇异值问题，我们引入**四元数**来描述刚体的姿态。
    首先介绍一下四元数(Quaternions)，一个四元数$q$可以表示为一个实数和三个虚数单位$i$，$j$，$k$的线性组合：
    ```math
    q=a+bi+cj+dk
    ```
    其中$a$，$b$，$c$，$d$是实数，$a$为实部，$bi+cj+dk$为虚部。四元数的矩阵分别表示左乘矩阵表示$L(q)$和右乘矩阵表示$R(q)$：
    $$ L(q) = 
    \begin{pmatrix} 
    a & -b & -c & -d \\ b & a & -d & c \\ c & d & a & -b \\d & -c & b & a
    \end{pmatrix} 
    \quad
    R(q) = 
    \begin{pmatrix} 
    a & -b & -c & -d \\ b & a & d & -c \\ c & -d & a & b \\d & c & -b & a
    \end{pmatrix}
    ```math
    如图所示，刚体在绕着过点$O$的旋转轴做定轴旋转运动，向量$\vec{n}$是旋转轴的方向向量，$\theta$是刚体在这段时间内绕轴旋转的角度。我们可以使用下面的单位四元数来表述刚体的姿态：
    ```
    \begin{align}q&=[cos(\frac{\theta}{2}),sin(\frac{\theta}{2}){\vec{n}}]\\&=cos(\frac{\theta}{2})+sin(\frac{\theta}{2}){{n}_{x}}{i}+sin(\frac{\theta}{2}){{n}_{y}}{j}+sin(\frac{\theta}{2}){{n}_{z}}{k}\end{align}
    $$
    ![[Fig 1-1-9.png]]


!!! note "四元数的运算性质"
    四元数满足的运算包括**加法，减法，乘法，共轭，范数和逆**：
    - **加法**：如果 $q_1 = w_1 + x_1i + y_1j + z_1k$ 和 $q_2 = w_2 + x_2i + y_2j + z_2k$，那么它们的和是：$$ q_1 + q_2 = (w_1 + w_2) + (x_1 + x_2)i + (y_1 + y_2)j + (z_1 + z_2)k $$
    - **减法**：如果 $q_1 = w_1 + x_1i + y_1j + z_1k$ 和 $q_2 = w_2 + x_2i + y_2j + z_2k$，那么它们的差是：$$ q_1 - q_2 = (w_1 - w_2) + (x_1 - x_2)i + (y_1 - y_2)j + (z_1 - z_2)k $$
    - **乘法**：两个四元数${q_1}$和${q_2}$相乘分为左乘和右乘，左乘的形式如下：$${{q_1}{\cdot}{q_2}}=L({q_1}){\mathbf{q_2}}$$右乘的形式如下：$${{q_2}{\cdot}{q_1}}=R({q_1}){\mathbf{q_2}}$$四元数的乘法满足结合律$({q_1}{\cdot}{q_2}){\cdot}{q_3}={q_1}{\cdot}({q_2}{\cdot}{q_3})$和分配律$({q_1}+{q_2}){\cdot}{q_3}={q_1}{\cdot}{q_3}+{q_2}{\cdot}{q_3}$。
    - **共轭**：四元数 $q = w + xi + yj + zk$ 的共轭为： $$ q^* = w - xi - yj - zk $$
    - **范数**：四元数的范数是其大小的度量： $$ \|q\| = \sqrt{w^2 + x^2 + y^2 + z^2} $$ 范数的平方与共轭乘积的关系： $$ qq^* = w^2 + x^2 + y^2 + z^2 = \|q\|^2 $$
    - **逆**：四元数的逆 $q^{-1}$ 的计算公式为： $$ q^{-1} = \frac{q^*}{\|q\|^2} $$


!!! note "欧拉角和四元数之间的相互转换"
    1. 欧拉角 (Z-Y-X) $\rightarrow$ 四元数 设 $\phi, \theta, \psi$ 分别为 Roll, Pitch, Yaw，四元数 $q = [w, x, y, z]$： $$ \begin{cases} w = \cos\frac{\phi}{2}\cos\frac{\theta}{2}\cos\frac{\psi}{2} + \sin\frac{\phi}{2}\sin\frac{\theta}{2}\sin\frac{\psi}{2} \\ x = \sin\frac{\phi}{2}\cos\frac{\theta}{2}\cos\frac{\psi}{2} - \cos\frac{\phi}{2}\sin\frac{\theta}{2}\sin\frac{\psi}{2} \\ y = \cos\frac{\phi}{2}\sin\frac{\theta}{2}\cos\frac{\psi}{2} + \sin\frac{\phi}{2}\cos\frac{\theta}{2}\sin\frac{\psi}{2} \\ z = \cos\frac{\phi}{2}\cos\frac{\theta}{2}\sin\frac{\psi}{2} - \sin\frac{\phi}{2}\sin\frac{\theta}{2}\cos\frac{\psi}{2} \end{cases} $$ 
    2. 四元数 $\rightarrow$ 欧拉角 (Z-Y-X) $$ \begin{bmatrix} \phi \\ \theta \\ \psi \end{bmatrix} = \begin{bmatrix} \operatorname{atan2}(2(wx + yz), 1 - 2(x^2 + y^2)) \\ \arcsin(2(wy - zx)) \\ \operatorname{atan2}(2(wz + xy), 1 - 2(y^2 + z^2)) \end{bmatrix} $$


### (5)-关节空间速度
我们定义关节空间速度是父连杆(Predecessor)在关节连接处的空间速度与子连杆(Successor)在关节连接处的空间速度之差：
$$
\boldsymbol{v_{\mathrm{J}}} = \boldsymbol{v_s - v_p}
$$
关节空间速度可以写为：
$$
\boldsymbol{v_{\mathrm{J}}} = \boldsymbol{S(q, t) \dot{q} + \sigma(q, t)}
$$
其中：
- $\boldsymbol{S}$是关节运动的子空间矩阵
- $\boldsymbol{\sigma}$是关节运动的偏置速度，也就是当$\boldsymbol{q}=0$时的刚体速度
- $\boldsymbol{q}$和$\boldsymbol{\dot{q}}$是关节的转动角度和转动角度变化率。
如果矩阵$\boldsymbol{S}$不随时间而改变，我们可以将关节的空间速度直接写为：
$$
\boldsymbol{v_{\mathrm{J}}} = \boldsymbol{S(q) \dot{q}}
$$
!!! example "以2-DOF平面机械臂来理解关节空间速度"
    

### (6)-关节空间力
我们让关节的空间约束力所在的子空间$\boldsymbol{T}={\boldsymbol{S}}^{\perp}$，并且定义关节的空间驱动力$\boldsymbol{T}_a$满足${\boldsymbol{T}}{\oplus}{\boldsymbol{T}_a}={F^{6}}$，那么关节的空间力如下：
$$
{\boldsymbol{f}_J}={\boldsymbol{T}_a}{\boldsymbol{\tau}}+{\boldsymbol{T}}{\boldsymbol{\lambda}}
$$
其中${\boldsymbol{\tau}}$为关节驱动力向量，${\boldsymbol{\lambda}}$为关节约束力向量。并且，子空间$\boldsymbol{T}$和$\boldsymbol{T}_a$需要满足以下性质：
$$
\begin{align}
{\boldsymbol{T}^{T}_a}{\boldsymbol{S}}=1\\
{\boldsymbol{T}^{T}}{\boldsymbol{S}}=0
\end{align}
$$
我们令关节空间里的等式两边同时乘以$\boldsymbol{S}^{T}$，那么我们可以得到：
$$
\begin{align}
{\boldsymbol{S}^{T}}{\boldsymbol{f}_J}&={\boldsymbol{S}^{T}}{\boldsymbol{T}_a}{\boldsymbol{\tau}}+{\boldsymbol{S}^{T}}{\boldsymbol{T}}{\boldsymbol{\lambda}}\\
{\boldsymbol{S}^{T}}{\boldsymbol{f}_J}&={\boldsymbol{\tau}}
\end{align}
$$

!!! tip
    因为在关节空间力两边同时乘以关节运动空间${\boldsymbol{S}}$之后，关节空间的约束力一项等于0，因此在后续的建模中，我们只考虑到关节空间的作用力，不考虑关节空间的约束力。


## 4.4-受约束的刚体动力学方程
在一个受约束的刚体中，刚体$i$受到以下几个力：
- 父关节对当前连杆的作用力${\boldsymbol{f}_{Bi}}$
- 所有子连杆对当前连杆的反作用力${\sum}{\boldsymbol{f}_j}$
- 刚体的空间约束内力${\boldsymbol{f}_{ci}}$
- 刚体受到的来自外部的合力${\boldsymbol{f}_{xi}}$（包括重力）
那么我们可以列写出来刚体的空间运动方程如下：
$$
{\boldsymbol{f}_{Bi}}+{\boldsymbol{f}_{ci}}+{\boldsymbol{f}_{xi}}+{{\sum}{\boldsymbol{f}_{j}}}={\boldsymbol{{{\hat{I}}}{{\hat{a}}}+{\hat{v}\times^* \hat{I} \hat{v}}}}
$$
等式两边同时减去外力项$\boldsymbol{f}_{xi}$，可以得到：$$
{\boldsymbol{f}_{Bi}}+{\boldsymbol{f}_{ci}}+{{\sum}{\boldsymbol{f}_{j}}}={\boldsymbol{{{\hat{I}}}{{\hat{a}}}+{\hat{p}}}}
$$其中$\boldsymbol{\hat{p}}=\boldsymbol{{\hat{v}\times^* \hat{I} \hat{v}}-{f_{xi}}}$。
# 5-多刚体系统建模
## 5.1-拓扑结构与表示
首先刚体的拓扑结构可以用具有以下性质的**连接图**来表示：
- 节点代表刚体
- 边代表关节
- 只有一个节点代表刚体的固定基座，其余节点代表刚体的移动刚体
- 该连接图是无向图
- 图是连接的
让我们用$G$来代表任意连接图，连接图$G$的生成树用$G_t$来表示。$G_t$是$G$的一个包含所有节点的子图。每个连接图$G$包含至少一个生成树$G_t$。
如果连接图的拓扑结构是树结构，我们也可以称这个连接图为**连接树**。那么$G_t=G$。
如果对于连接图$G$来说，$N_J{\gt}N_B$的情况下，连接图会有闭环，闭环的数量$N_L=N_J-N_B$。如果系统又运动环，那么就称为**闭环系统**，否则就是**开环系统**。

!!! tip "如果多体系统的连接图$G$的边是有向的，代表什么？"
    - 刚体系统连接图$G$的边有向，在计算上代表从节点的一端到另外一端的顺序，那么在有向连接图$G$中，每条边的起点为父节点，终点为子节点。
    - 如果刚体系统的连接图$G$是无向图，默认关节$i$从刚体$i$的父节点到刚体$i$
    - 在运动学算法中的有向图$G$中，图$G$的边是从父节点指向子节点
    - 在动力学算法中的有向图$G$中，图$G$的边是从子节点指向父节点。 


我们从$0$到$N_B$来编号刚体（其中编号$0$为基座），使用$1$到$N_J$来编号关节，编号规则如下：
- 首先选择一个连接树$G_t$
- 我们让表示基座的刚体节点定义为编号$0$，这个节点作为连接树$G_t$的根节点
- 从$1$到$N_B$来编号剩余的刚体，但是要求节点的编号比父节点的编号要大
- 从$1$到$N_B$来编号边，其中边$i$连接着节点$i$及其父节点
- 使用任意顺序来给剩余的边来编号，从$N_B+1$到$N_J$
- 确保每个刚体获得与其节点编号相同的编号，并且每个关节的编号与边的编号相对应

!!! example "刚体编号的例子"
    Contents


每个关节$i$连接两个刚体，我们认定其中一个刚体作为父连杆，另外一个刚体是作为子连杆。关节本身是从父连杆连接到子连杆。
- 定义关节和刚体变量的关系
- 去分辨关节在系统的连接方式
分辨两个刚体是通过什么方式连接到关节称为**关节的极性**。在结构图中，我们认定关节的极性是从关节的父节点引出箭头到关节的子节点。

首先我们可以用**父连杆表格和子连杆表格**来表示连接图$G$中关节和刚体之间的连接关系：列出父连杆表格$p(i)$和子连杆表格$s(i)$，其中$i$为关节编号。
然后我们从父连杆表格$p(i)$和子连杆表格$s(i)$中可以提取出来以下的量：
- **父母表格**：根据父连杆表格$p(i)$和子连杆表格$s(i)$来推导出父节点列表$\lambda(i)$:$$\lambda(i)={\min}(p(i),s(i)){\quad}{(1{\leq}i{\leq}N_B)}$$如果$i=s(i)$，那么我们认定在连接树中式前向传播的，如果$i=p(i)$，那么关节$i$是反向传播的。
- **刚体$i$路径集合${\kappa}(i)$**：除了基座($i=0$)，${\kappa}(i)$是连接树$G_t$里从基座到刚体$i$的路径上所有的节点的集合。
- **刚体$i$的子刚体集合${\mu}(i)$**：刚体$i$的子刚体节点集合
- **刚体$i$的子树节点集合${\nu}(i)$**：以刚体$i$为根节点的子树的所有节点的集合
## 5.2-Modified D-H表达法
Modified D-H表达法常用于开链的机械臂结构的运动学几何描述，首先我们按照如下步骤来为机械臂上面的$n$个关节创建坐标系：
1. 首先我们需要定义好$\mathcal{Frame}\{0\}$坐标系和$\mathcal{Frame}\{n+1\}$坐标系，其中$\mathcal{Frame}\{0\}$坐标系是**基座坐标系**$\mathcal{Frame}\{B\}$，$\mathcal{Frame}\{n+1\}$坐标系是**工具坐标系**$\mathcal{Frame}\{T\}$。
2. 按照关节标号$1$到$n$来依次建立$\mathcal{Frame}\{1\}$坐标系和$\mathcal{Frame}\{n\}$坐标系，首先我们需要定义好$z_i$，$z_i$的位置与关节运动的轴线重合，$z_i$的方向以关节的旋转方向为右手旋转方向，右手大拇指的朝向即为关节的朝向。
3. 然后定义关节坐标系$\mathcal{Frame}\{i\}$的$x_i$方向，有以下三种情况：
	- **$z_i$ 与 $z_{i+1}$ 相交**：
	    - **定义**：$x_i$ 轴取在两条轴线交点处，且垂直于 $z_i$ 和 $z_{i+1}$ 所在的平面。    
	    - **方向**：通常选为 $x_i = z_i \times z_{i+1}$ 或 $x_i = z_{i+1} \times z_i$（需保持全机建模方向的一致性）。   
	- **$z_i$ 与 $z_{i+1}$ 平行**：
	    - **定义**：由于平行线之间有无数条公垂线，$x_i$ 的位置不唯一。
	    - **方向**：通常选择 $x_i$ 位于通过前一个坐标系原点且垂直于 $z_{i+1}$ 的公垂线上。为了简化计算，常令 $x_i$ 的方向与 $x_{i-1}$ 保持一致，从而使连杆偏移量 $d_i = 0$。
	- **$z_i$ 与 $z_{i+1}$ 异面（既不平行也不相交）**：
	    - **定义**：$x_i$ 轴严格重合于 $z_i$ 与 $z_{i+1}$ 之间唯一的公垂线。
	    - **方向**：方向定义为从 $z_i$ 指向 $z_{i+1}$，其矢量方向满足 $x_i = z_i \times z_{i+1}$ 的几何指向。
4. 最后根据右手定则$y_i=z_i\times x_i$来确定关节坐标系$\mathcal{Frame}\{i\}$的$y_i$方向
接下来我们可以使用Modified D-H参数来描述上面定义的坐标系统，在 **Modified D-H (改进型 D-H)** 表达法中，两个相邻坐标系 $\mathcal{Frame}\{i-1\}$ 到 $\mathcal{Frame}\{i\}$ 之间的相对位置关系由以下四个参数定义：
- **连杆转角 $\alpha_{i-1}$ (Link Twist)**：绕 $x_{i-1}$ 轴，从 $z_{i-1}$ 旋转到 $z_i$ 的角度。
- **连杆长度 $a_{i-1}$ (Link Length)**：沿 $x_{i-1}$ 轴，从 $z_{i-1}$ 到 $z_i$ 的距离（即两轴线之间的公垂线长度）。
- **关节角 $\theta_i$ (Joint Angle)**：绕 $z_i$ 轴，从 $x_{i-1}$ 旋转到 $x_i$ 的角度。
- **连杆偏移 $d_i$ (Link Offset)**：沿 $z_i$ 轴，从 $x_{i-1}$ 到 $x_i$ 的距离。
## 5.3-多刚体运动学方程
### (1)-关节空间基向量的坐标变换
我们定义空间中有一个坐标系${\mathcal{Frame}\{i\}}$，关节$i$的中心点即为坐标系${\mathcal{Frame}\{i\}}$的原点。并且关节$i$的关节运动子空间的基向量在坐标系${\mathcal{Frame}\{i\}}$中定义为$^{i}\mathbf{S}_i$。我们在另外的坐标系${\mathcal{Frame}\{W\}}$中可以得到关节$i$的空间基向量可以表示为
$$
{{^{W}\mathbf{S}}_i}={{^{W}_i\mathbf{X}}}{{^{i}\mathbf{S}}_i}
$$
其中${{^{W}_i\mathbf{X}}}$是从${\mathcal{Frame}\{i\}}$到${\mathcal{Frame}\{W\}}$的空间坐标转换矩阵
### (2)-多刚体系统的速度表示
我们定义刚体$i$的空间速度为$\boldsymbol{v}_i$，刚体关节$i$的空间速度$\boldsymbol{v}_{Ji}$。首先我们可以在坐标系${\mathcal{Frame}\{W\}}$定义刚体$\boldsymbol{v}_i$的速度如下：
$$
{\boldsymbol{^{W}{v}}_i}=\boldsymbol{^{W}{v}}_{{\lambda}(i)}+\boldsymbol{^{W}{v}}_{Ji}
$$
我们默认$i=0$的时候，刚体$0$为固定基座，因此$\boldsymbol{v}_0=0$，那么上式可以写成如下形式：
$$
\boldsymbol{^{W}{v}}_i = \sum_{j \in \kappa(i)} \boldsymbol{^{W}{v}}_{\mathrm{J}j}
$$

我们定义刚体$i$的速度如下：
$$
{\boldsymbol{{^{W}{v}}_i}}={\boldsymbol{{{^{W}{J}}_{i}}(q)}}{\dot{\boldsymbol{q}}}
$$
### (3)-多刚体系统的加速度表示
我们在坐标系${\mathcal{Frame}\{W\}}$定义刚体$i$的加速度如下：
$$
{\boldsymbol{{^{W}{a}}_i}}={\boldsymbol{{{^{W}\dot{J}}_{i}}(q)}}{\dot{\boldsymbol{q}}}+{\boldsymbol{{{^{W}{J}}_{i}}(q)}}{\ddot{\boldsymbol{q}}}
$$
## 5.4-多刚体动力学方程
### (1)-带空间约束的力学方程推导
- **单独列出来n个刚体的独立动力学方程**：我们已知有$N_B$个刚体，其中每个刚体的独立表达式为${\boldsymbol{{f}}_i}={\boldsymbol{{I_i}{{a}}}_i}+{\boldsymbol{{p}}_i}$。那么我们先将这$N_B$个独立的刚体的表达式写作一整个表达式：$$\begin{bmatrix}
\boldsymbol{f}_1 \\
\boldsymbol{f}_2 \\
\vdots \\
\boldsymbol{f}_{N_B}
\end{bmatrix}
=
\begin{bmatrix}
\boldsymbol{I}_1 & \mathbf{0} & \cdots & \mathbf{0} \\
\mathbf{0} & \boldsymbol{I}_2 & \cdots & \mathbf{0} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{0} & \mathbf{0} & \cdots & \boldsymbol{I}_{N_B}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{a}_1 \\
\boldsymbol{a}_2 \\
\vdots \\
\boldsymbol{a}_{N_B}
\end{bmatrix}
+
\begin{bmatrix}
\boldsymbol{p}_1 \\
\boldsymbol{p}_2 \\
\vdots \\
\boldsymbol{p}_{N_B}
\end{bmatrix}$$上式也可以直接写成如下的运动学形式：$${\boldsymbol{{f}}}={\boldsymbol{{I}{{a}}}}+{\boldsymbol{{p}}}$$
- **由刚体关节角度表达到刚体空间运动表达**：
- **从刚体的空间力到关节的空间力**：
- **加入运动约束**：
- **列出约束力**：
最终，这种带有约束项的多刚体系统动力学方程的形式如下：$$\begin{bmatrix}
\boldsymbol{I} & \boldsymbol{P} \boldsymbol{T} \\
\boldsymbol{T}^{\text{T}} \boldsymbol{P}^{\text{T}} & \boldsymbol{0}
\end{bmatrix} 
\begin{bmatrix}
\boldsymbol{a} \\
-\boldsymbol{\lambda}
\end{bmatrix} = 
\begin{bmatrix}
\boldsymbol{P} \boldsymbol{T}_{\boldsymbol{a}} \boldsymbol{\tau} - \boldsymbol{p} \\
-\dot{\boldsymbol{T}}^{\text{T}} \boldsymbol{P}^{\text{T}} \boldsymbol{v}
\end{bmatrix}$$
### (2)-求解多刚体系统动力学的一般步骤
如果我们已知下面的条件：
- 刚体系统连接图$G$的拓扑结构。
- 刚体系统的Modified D-H参数。
- 刚体系统中每个刚体的质心相对于关节连接处的位置，刚体相对于质心的惯量矩和刚体重量。
那么我们可以列写出来不受约束的多刚体系统的动力学方程，可以分为以下几个步骤：
- **根据拓扑结构和Modified D-H参数写出各个关节相对于参考坐标系的转换矩阵**
- **写出来每个刚体关于参考坐标系的空间惯量矩阵**
- **根据空间惯量矩阵写出Jacobians矩阵，并且求解速度和加速度**
- **根据空间惯量矩阵，速度，加速度来列些动力学方程${\boldsymbol{{f}}}={\boldsymbol{{I}{{a}}}}+{\boldsymbol{{p}}}$**
- **将带Jacobians项的速度，加速度方程以及力的映射$\boldsymbol{f}=\boldsymbol{J}(\boldsymbol{q})\dot{\boldsymbol{q}}$导入空间动力学方程${\boldsymbol{{f}}}={\boldsymbol{{I}{{a}}}}+{\boldsymbol{{p}}}$，最终求解动力学方程${\boldsymbol{H}}{\ddot{\boldsymbol{q}}}+{\boldsymbol{C}}={\boldsymbol{\tau}}$**
## 5.5-多刚体系统的总动能
首先，多刚体系统的动能表示如下：
$$
{T}={\frac{1}{2}}{\sum_{k=1}^{N_B}}{{\boldsymbol{\hat{v_k}}}^T}{\boldsymbol{\hat{I_k}}}{\boldsymbol{\hat{v_k}}}
$$
并且根据多刚体运动学方程，我们有：
$$
{\boldsymbol{\hat{v}}_k}={\sum_{{i}{\in}{{\kappa}(k)}}}{\boldsymbol{S}_i}{\boldsymbol{\dot{q_i}}}
$$
那么代入上式我们表达多刚体系统的动能如下：
$$
\begin{align}
{T}&={\frac{1}{2}}{\sum_{k=1}^{N_B}}{\sum_{{j}{\in}{{\kappa}(k)}}}{\sum_{{i}{\in}{{\kappa}(k)}}}{{\boldsymbol{\dot{q}_i^T}}{\boldsymbol{S}_i^T}}{\boldsymbol{\hat{I_k}}}{\boldsymbol{S}_j}{\boldsymbol{\dot{q}_j}}\\
&={\frac{1}{2}}{\sum_{i=1}^{N_B}}{\sum_{j=1}^{N_B}}{\boldsymbol{\dot{q}_i^T}}({\sum_{k{\in}{\nu}(i){\cap}{\nu}(j)}}{\boldsymbol{S}_i^T}{\boldsymbol{\hat{I_k}}}{\boldsymbol{S}_j}){\boldsymbol{\dot{q}_j}}\\
&={\frac{1}{2}}{\sum_{i=1}^{N_B}}{\sum_{j=1}^{N_B}}{\boldsymbol{\dot{q}_i^T}}{\boldsymbol{H}_{ij}}{\boldsymbol{\dot{q}_j}}
\end{align}
$$
其中：
$$
{\boldsymbol{H}_{ij}}={\sum_{k{\in}{\nu}(i){\cap}{\nu}(j)}}{\boldsymbol{S}_i^T}{\boldsymbol{\hat{I_k}}}{\boldsymbol{S}_j}{\quad}{\quad}
{\nu(i) \cap \nu(j) = \begin{cases} \nu(i) & \text{if } i \in \nu(j) \\ \nu(j) & \text{if } j \in \nu(i) \\ \emptyset & \text{otherwise} \end{cases}}
$$
## 5.6-多刚体系统的复合惯性矩
在多体动力学中，**复合刚体惯量 $\boldsymbol{I}_i^c$** 指的是：假设刚体 $i$ 及其所有子孙节点（Descendants）所属的刚体全部“固连”在一起，形成一个单一的复合刚体时，该整体在空间中相对于刚体 $i$ 坐标系的等效空间惯量。
根据 5.5 节中推导出的 $\boldsymbol{H}_{ij}$，我们可以定义复合刚体惯量矩阵 $\boldsymbol{I}_i^c$ 为：
$$
{\boldsymbol{I}_i^c} = \sum_{k \in \nu(i)} \boldsymbol{\hat{I}}_k
$$
其中 $\nu(i)$ 是以 $i$ 为根节点的子树中所有节点的集合。这意味着 $\boldsymbol{H}_{ij}$ 的计算可以简化为：
- 若 $i$ 是 $j$ 的祖先（$i \in \kappa(j)$），则有：$$\boldsymbol{H}_{ij} = \boldsymbol{S}_i^T \left( \sum_{k \in \nu(j)} \boldsymbol{\hat{I}}_k \right) \boldsymbol{S}_j = \boldsymbol{S}_i^T \boldsymbol{I}_j^c \boldsymbol{S}_j$$
- 利用对称性，若 $j$ 是 $i$ 的祖先，则 $\boldsymbol{H}_{ij} = \boldsymbol{H}_{ji}^T$。
那么${\boldsymbol{H}_{ij}}$表示如下：
$$
\boldsymbol{H}_{ij} = \begin{cases} 
\boldsymbol{S}_i^{\mathrm{T}} \boldsymbol{I}_i^{\mathrm{c}} \boldsymbol{S}_j & \text{if } i \in \nu(j) \\ 
\boldsymbol{S}_i^{\mathrm{T}} \boldsymbol{I}_j^{\mathrm{c}} \boldsymbol{S}_j & \text{if } j \in \nu(i) \\ 
\mathbf{0} & \text{otherwise.} 
\end{cases}
$$
## 5.7-浮动基座系统的动力学建模方法
### (1)-浮动基座系统的运动学
首先，我们将浮动基座系统的浮动基座记为刚体$1$，剩下的刚体的编号是从$2$到$N_B+1$。
### (2)-浮动基座的动力学建模
首先，我们可以仿照固定基座的多体动力学的形式，将浮动基座动力学的一般形式如下：
$$
\begin{bmatrix}
\mathbf{H}_{11} & \mathbf{H}_{1*} \\
\mathbf{H}_{*1} & \mathbf{H}_{**}
\end{bmatrix}
\begin{bmatrix}
\mathbf{\ddot{q}}_1 \\
\mathbf{\ddot{q}}_*
\end{bmatrix} +
\begin{bmatrix}
\mathbf{C}_1 \\
\mathbf{C}_*
\end{bmatrix}
 =
\begin{bmatrix}
\mathbf{\tau}_1 \\
\mathbf{\tau}_*
\end{bmatrix}
$$
在前面推导浮动基座系统的运动学的时候，我们推导出来如下的规律：
$$
\begin{matrix}
{\boldsymbol{\dot{{q}}_1}={\boldsymbol{v_1}}}&{\boldsymbol{\ddot{{q}}_1}={\boldsymbol{a_1}}}
\end{matrix}
$$
由于虚拟关节$1$的运动子空间$\boldsymbol{S}_1={\boldsymbol{1}_{6\times6}}$，那么虚拟关节$1$的关节力$\boldsymbol{f}_1$和$\boldsymbol{\tau}_1$的关系如下：
$$
{\boldsymbol{\tau}_1}={\boldsymbol{S}^{T}_{1}}{\boldsymbol{f}_1}={\boldsymbol{f}_1}
$$
对于浮动基座来说，在本质上虚拟关节的空间关节力${\boldsymbol{f}_1}$和刚体本身受到的其它外部力组成的合力$\boldsymbol{f}_{ext1}$一样都是由刚体外部施加的外力。我们可以将其合并为整体的外力项${\boldsymbol{f}_{x1}}={\boldsymbol{f}_1}+\boldsymbol{f}_{ext1}$。但是等式右边的关节力$\tau_1$作为基座$0$通过刚体向基座$1$传递力，并且在实际物理系统中，${\boldsymbol{f}_{1}}$只是外力的一部分，那么我们令关节力$\tau_1$为0。
我们假设浮动基座的复合刚体空间惯量为${\boldsymbol{I}^{c}_1}$，那么${\boldsymbol{H}_{11}}$和如下：
$$
{\boldsymbol{H}_{11}}={\boldsymbol{S}^{T}_{1}}{\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{1}}={\boldsymbol{I}^{c}_1}{\quad}{{\boldsymbol{H}_{1i}}={\boldsymbol{S}^{T}_{1}}{\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{i}}={\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{i}}
}
$$
我们将上面的$\boldsymbol{H}_{1*}$改写成$\boldsymbol{F}$，其中：
$$
{\boldsymbol{F}}=[{\boldsymbol{F}_1},{\boldsymbol{F}_2},{\boldsymbol{F}_3},{\cdots}{\boldsymbol{F}_{N_B}}]
$$
其中${\boldsymbol{F}_{i}}={\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{i}}$，$\boldsymbol{F}_i$代表
然后，我们将基座的空间惯量，加速度和偏置力重新写为$\boldsymbol{I}_0^c$，$\boldsymbol{a}_0$和$\boldsymbol{p}_0^c$。那么浮动基座的多体动力学如下：
$$
\begin{bmatrix}
\boldsymbol{I}_{0}^{c} & \boldsymbol{F} \\
\boldsymbol{F}^{T} & \boldsymbol{H}_{**}
\end{bmatrix} \begin{bmatrix}
\boldsymbol{a}_{0} \\
\ddot{\boldsymbol{q}}_{*}
\end{bmatrix} + \begin{bmatrix}
\boldsymbol{p}_{0}^{c} \\
\boldsymbol{C}_{*}
\end{bmatrix} = \begin{bmatrix}
\mathbf{0} \\
\boldsymbol{\tau}_{*}
\end{bmatrix}
$$
我们将浮动基座的多体动力学方程组写成如下形式：
$$
\left\{
{\begin{align}
&{\boldsymbol{I}_0^c}{{\boldsymbol{a}_0}}+{\boldsymbol{F}}{\boldsymbol{\ddot{q}}}+{\boldsymbol{p}_0^c}=\boldsymbol{0}\\
&{\boldsymbol{F}^T}{{\boldsymbol{a}_0}}+{\boldsymbol{H}_{**}}{\boldsymbol{\ddot{q}}_*}+{\boldsymbol{C}_*}=\boldsymbol{\tau}_{*}\\
\end{align}}
\right.
$$
方程组中的第一个方程是**浮动基座的动力学方程**，其中：
- ${\boldsymbol{I}_0^c}{{\boldsymbol{a}_0}}$表示浮动基座平台的加速度合力，该项是将整个系统（基座+机械臂）视为一个瞬时刚体时，产生整体空间加速度 $\boldsymbol{a}_0$ 所需的惯性力/力矩。
- ${\boldsymbol{F}}{\boldsymbol{\ddot{q}}}$代表着机械臂的关节加速度传导到浮动基座平台上的合力。
- ${\boldsymbol{p}_0^c}$代表浮动基座平台的偏置力，包括重力，科氏力，浮动基座的驱动力以及其他外部的干扰合力，这里的力都是非加速度项。
方程组中的第二个方程是**机械臂本身的动力学方程**，其中：
- ${\boldsymbol{F}^T}{\boldsymbol{a}_0}$是浮动基座在加速运动的时候传导到机械臂各个刚体上的空间力
- ${\boldsymbol{H}_{**}}{\boldsymbol{\ddot{q}}_*}$是机械臂各个刚体转动的的力
- ${\boldsymbol{C}_*}$是机械臂每个刚体的偏置力
- ${\boldsymbol{\tau}_*}$是机械臂上各个关节提供的空间力
# 6-闭环机器人动力学

# 7-接触动力学

# 8-刚体系统的逆动力学求解

!!! tip "内容概要"
    机器人的逆动力学，即**已知速度，加速度等信息求解力**。在这一章节中，我们主要介绍机器人求解逆动力学的**迭代牛顿-欧拉算法（Recurrence Newton-Euler Algorithm）**


## 8.1-固定基座系统的牛顿-欧拉法

!!! example "迭代牛顿-欧拉算法的伪代码"
    
    $$
    \begin{array}{@{}l@{\hspace{5.5em}}l@{}}
    \hline \\[-0.9em]
    \begin{array}{l}
    \underline{\text{Basic Equations:}} \\[0.5em]
    \boldsymbol{v}_0 = \boldsymbol{0} \\[0.35em]
    \boldsymbol{a}_0 = -\boldsymbol{a}_g \\[0.7em]
    \boldsymbol{v}_i
    =
    \boldsymbol{v}_{\lambda(i)}
    +
    \boldsymbol{S}_i \dot q_i \\[0.35em]
    \boldsymbol{a}_i
    =
    \boldsymbol{a}_{\lambda(i)}
    +
    \boldsymbol{S}_i \ddot q_i
    +
    \dot{\boldsymbol{S}}_i \dot q_i \\[0.35em]
    \boldsymbol{f}_i^B
    =
    \boldsymbol{I}_i \boldsymbol{a}_i
    +
    \boldsymbol{v}_i \times^{*}
    \boldsymbol{I}_i \boldsymbol{v}_i \\[0.35em]
    \boldsymbol{f}_i
    =
    \boldsymbol{f}_i^B
    -
    \boldsymbol{f}_i^x
    +
    \sum_{j \in \mu(i)}
    \boldsymbol{f}_j \\[0.7em]
    \tau_i
    =
    \boldsymbol{S}_i^T \boldsymbol{f}_i \\[1em]
    \underline{\text{Equations in Body Coordinates:}} \\[0.5em]
    \boldsymbol{v}_0 = \boldsymbol{0} \\[0.35em]
    \boldsymbol{a}_0 = -\boldsymbol{a}_g \\[0.7em]
    \boldsymbol{v}_{J_i}
    =
    \boldsymbol{S}_i \dot q_i \\[0.35em]
    \boldsymbol{c}_{J_i}
    =
    \dot{\boldsymbol{S}}_i \dot q_i \\[0.35em]
    \boldsymbol{v}_i
    =
    {}^i\boldsymbol{X}_{\lambda(i)}
    \boldsymbol{v}_{\lambda(i)}
    +
    \boldsymbol{v}_{J_i} \\[0.35em]
    \boldsymbol{a}_i
    =
    {}^i\boldsymbol{X}_{\lambda(i)}
    \boldsymbol{a}_{\lambda(i)}
    +
    \boldsymbol{S}_i \ddot q_i
    +
    \boldsymbol{c}_{J_i}
    +
    \boldsymbol{v}_i \times \boldsymbol{v}_{J_i} \\[0.35em]
    \boldsymbol{f}_i^B
    =
    \boldsymbol{I}_i \boldsymbol{a}_i
    +
    \boldsymbol{v}_i \times^{*}
    \boldsymbol{I}_i \boldsymbol{v}_i \\[0.35em]
    \boldsymbol{f}_i
    =
    \boldsymbol{f}_i^B
    -
    {}^i\boldsymbol{X}_0^{*}
    \boldsymbol{f}_i^x
    +
    \sum_{j \in \mu(i)}
    {}^i\boldsymbol{X}_j^{*}
    \boldsymbol{f}_j \\[0.7em]
    \tau_i
    =
    \boldsymbol{S}_i^T \boldsymbol{f}_i
    \end{array}
    &
    \begin{array}{l}
    \underline{\text{Algorithm:}} \\[0.5em]
    \boldsymbol{v}_0 = \boldsymbol{0} \\[0.35em]
    \boldsymbol{a}_0 = -\boldsymbol{a}_g \\[0.35em]
    \mathbf{for}\ i = 1\ \mathbf{to}\ N_B\ \mathbf{do} \\[0.35em]
    \quad
    [\boldsymbol{X}_J,\boldsymbol{S}_i,\boldsymbol{v}_J,\boldsymbol{c}_J]
    = \\[-0.1em]
    \qquad\qquad
    \operatorname{jcalc}
    (
    \operatorname{jtype}(i),
    q_i,
    \dot q_i
    ) \\[0.35em]
    \quad
    {}^i\boldsymbol{X}_{\lambda(i)}
    =
    \boldsymbol{X}_J
    \boldsymbol{X}_T(i) \\[0.35em]
    \quad
    \mathbf{if}\ \lambda(i) \neq 0\ \mathbf{then} \\[0.35em]
    \qquad
    {}^i\boldsymbol{X}_0
    =
    {}^i\boldsymbol{X}_{\lambda(i)}
    {}^{\lambda(i)}\boldsymbol{X}_0 \\[0.35em]
    \quad
    \mathbf{end} \\[0.35em]
    \quad
    \boldsymbol{v}_i
    =
    {}^i\boldsymbol{X}_{\lambda(i)}
    \boldsymbol{v}_{\lambda(i)}
    +
    \boldsymbol{v}_J \\[0.35em]
    \quad
    \boldsymbol{a}_i
    =
    {}^i\boldsymbol{X}_{\lambda(i)}
    \boldsymbol{a}_{\lambda(i)}
    +
    \boldsymbol{S}_i \ddot q_i \\[-0.1em]
    \qquad\qquad
    +
    \boldsymbol{c}_J
    +
    \boldsymbol{v}_i \times \boldsymbol{v}_J \\[0.35em]
    \quad
    \boldsymbol{f}_i
    =
    \boldsymbol{I}_i \boldsymbol{a}_i
    +
    \boldsymbol{v}_i \times^{*}
    \boldsymbol{I}_i \boldsymbol{v}_i
    -
    {}^i\boldsymbol{X}_0^{*}
    \boldsymbol{f}_i^x \\[0.35em]
    \mathbf{end} \\[0.5em]
    \mathbf{for}\ i = N_B\ \mathbf{to}\ 1\ \mathbf{do} \\[0.35em]
    \quad
    \tau_i
    =
    \boldsymbol{S}_i^T
    \boldsymbol{f}_i \\[0.35em]
    \quad
    \mathbf{if}\ \lambda(i) \neq 0\ \mathbf{then} \\[0.35em]
    \qquad
    \boldsymbol{f}_{\lambda(i)}
    =
    \boldsymbol{f}_{\lambda(i)}
    +
    {}^{\lambda(i)}\boldsymbol{X}_i^{*}
    \boldsymbol{f}_i \\[0.35em]
    \quad
    \mathbf{end} \\[0.35em]
    \mathbf{end}
    \end{array}
    \\[0.4em]
    \hline
    \end{array}
    $$

## 8.2-浮动基座系统的牛顿-欧拉法

!!! example "迭代牛顿-欧拉算法的伪代码"
    $$
    \begin{array}{@{}l@{\qquad\qquad}l@{}}
    \hline \\[-8pt]
    \begin{array}{l}
    \underline{\text{Pass 1}} \\[6pt]
    a_{0}^{r}=-{}^{0}a_{g} \\[8pt]
    v_{Ji}=S_{i}\dot{q}_{i} \\[8pt]
    v_{i}={}^{i}X_{\lambda(i)}v_{\lambda(i)}+v_{Ji} \\[8pt]
    c_{i}=\dot{S}_{i}\dot{q}_{i}+v_{i}\times v_{Ji} \\[8pt]
    a_{i}^{r}={}^{i}X_{\lambda(i)}a_{\lambda(i)}+c_{i}+S_{i}\ddot{q}_{i} \\[8pt]
    p_{i}=I_{i}a_{i}^{r}+v_{i}\times^{*}I_{i}v_{i}-{}^{i}X_{0}^{*}{}^{0}f_{i}^{x} \\[14pt]
    
    \underline{\text{Pass 2}} \\[6pt]
    I_{i}^{c}=I_{i}+\displaystyle\sum_{j\in\mu(i)}{}^{i}X_{j}^{*}I_{j}^{c}{}^{j}X_{i} \\[16pt]
    p_{i}^{c}=p_{i}+\displaystyle\sum_{j\in\mu(i)}{}^{i}X_{j}^{*}p_{j}^{c} \\[16pt]
    
    \underline{\text{Pass 3}} \\[6pt]
    {}^{0}a_{0}=-(I_{0}^{c})^{-1}p_{0}^{c} \\[8pt]
    {}^{i}a_{0}={}^{i}X_{\lambda(i)}{}^{\lambda(i)}a_{0} \\[8pt]
    \tau_{i}=S_{i}^{T}\left(I_{i}^{c}{}^{i}a_{0}+p_{i}^{c}\right)
    \end{array}
    &
    \begin{array}{l}
    a_{0}^{r}=-{}^{0}a_{g} \\[2pt]
    \textbf{for } i=1 \textbf{ to } N_{B} \textbf{ do} \\[2pt]
    \quad [X_{J},S_{i},v_{J},c_{J}]
    =\operatorname{jcalc}(\operatorname{jtype}(i),q_{i},\dot{q}_{i}) \\[2pt]
    \quad {}^{i}X_{\lambda(i)}=X_{J}X_{T(i)} \\[2pt]
    \quad \textbf{if } \lambda(i)\neq 0 \textbf{ then} \\[2pt]
    \qquad {}^{i}X_{0}={}^{i}X_{\lambda(i)}{}^{\lambda(i)}X_{0} \\[2pt]
    \quad \textbf{end} \\[2pt]
    \quad v_{i}={}^{i}X_{\lambda(i)}v_{\lambda(i)}+v_{J} \\[2pt]
    \quad a_{i}^{r}={}^{i}X_{\lambda(i)}a_{\lambda(i)}^{r}
    +c_{J}+v_{i}\times v_{J}+S_{i}\ddot{q}_{i} \\[2pt]
    \quad I_{i}^{c}=I_{i} \\[2pt]
    \quad p_{i}^{c}=I_{i}a_{i}^{r}+v_{i}\times^{*}I_{i}v_{i}
    -{}^{i}X_{0}^{*}{}^{0}f_{i}^{x} \\[2pt]
    \textbf{end} \\[2pt]
    I_{0}^{c}=I_{0} \\[2pt]
    p_{0}^{c}=I_{0}a_{0}^{r}+v_{0}\times^{*}I_{0}v_{0}-{}^{0}f_{0}^{x} \\[2pt]
    \textbf{for } i=N_{B} \textbf{ to } 1 \textbf{ do} \\[2pt]
    \quad I_{\lambda(i)}^{c}
    =I_{\lambda(i)}^{c}
    +{}^{\lambda(i)}X_{i}^{*}I_{i}^{c}{}^{i}X_{\lambda(i)} \\[2pt]
    \quad p_{\lambda(i)}^{c}
    =p_{\lambda(i)}^{c}
    +{}^{\lambda(i)}X_{i}^{*}p_{i}^{c} \\[2pt]
    \textbf{end} \\[2pt]
    {}^{0}a_{0}=-(I_{0}^{c})^{-1}p_{0}^{c} \\[2pt]
    \textbf{for } i=1 \textbf{ to } N_{B} \textbf{ do} \\[2pt]
    \quad {}^{i}a_{0}={}^{i}X_{\lambda(i)}{}^{\lambda(i)}a_{0} \\[2pt]
    \quad \tau_{i}=S_{i}^{T}\left(I_{i}^{c}{}^{i}a_{0}+p_{i}^{c}\right) \\[2pt]
    \textbf{end}
    \end{array}
    \\[-2pt] \hline
    \end{array}
    $$


# 9-刚体系统的正动力学求解

!!! tip "内容概要"
    机器人的正动力学，即为已知力求解加速度等信息。在这一章节中，我们主要介绍机器人的正动力学的两种算法：
    - **惯量矩阵方法（Inertia Matrix Methods）**：复合刚体算法(CRBA)就是基于惯量矩阵方法的正动力学求解算法
    - **传播法（Propagation Methods）**：(ABA)算法就是基于惯量矩阵方法的正动力学求解算法

## 9.1-复合刚体算法(CRBA)求解正动力学
首先，求解复合刚体动力学的方程，就是求解以下几个矩阵：
- 偏置力矩阵$\mathbf{C}$
- 惯性张量矩阵$\mathbf{H}$
首先，在Chapter-8中，我们计算的逆动力学如下：
$$
\begin{align}
\tau&=ID({model},\mathbf{q},\mathbf{\dot{q}},\mathbf{\ddot{q}},\mathbf{f^x})
\end{align}
$$
当$,\mathbf{\ddot{q}}=0$的时候，我们有：
$$
\mathbf{C}=ID({model},\mathbf{q},\mathbf{\dot{q}},\mathbf{0},\mathbf{f^x})
$$
也就是说对于偏置力矩阵$\mathbf{C}$来说，只需要调用求解逆动力学的方式就能得到，然后我们就可以得到：
$$
{\mathbf{H}}{\mathbf{\ddot{q}}}=\mathbf{\tau}-ID({model},\mathbf{q},\mathbf{\dot{q}},\mathbf{0},\mathbf{f^x})
$$
（过渡）
因此，求解正动力学的重中之重，是求解惯性张量矩阵$\mathbf{H}$。接下来就要用**复合刚体算法**来求解矩阵$\mathbf{H}$。
!!! example "复合刚体算法的伪代码"
    
    $$
    \begin{array}{@{}l@{\hspace{6em}}l@{}}
    \hline \\[-0.8em]
    \begin{array}{l}
    \underline{\text{Basic Equations:}} \\[0.8em]
    \boldsymbol{I}_i^c
    =
    \boldsymbol{I}_i
    +
    \displaystyle\sum_{j \in \mu(i)}
    \boldsymbol{I}_j^c \\[1.2em]
    
    \boldsymbol{H}_{ij}
    =
    \left\{
    \begin{array}{ll}
    \boldsymbol{S}_i^T
    \boldsymbol{I}_i^c
    \boldsymbol{S}_j
    & \text{if } i \in \nu(j) \\[0.25em]
    
    \boldsymbol{S}_i^T
    \boldsymbol{I}_j^c
    \boldsymbol{S}_j
    & \text{if } j \in \nu(i) \\[0.25em]
    
    \boldsymbol{0}
    & \text{otherwise}
    \end{array}
    \right. \\[2.2em]
    
    \underline{\text{Equations for Body-Coordinates}} \\[-0.1em]
    \underline{\text{Algorithm:}} \\[1em]
    
    \boldsymbol{I}_i^c
    =
    \boldsymbol{I}_i
    +
    \displaystyle\sum_{j \in \mu(i)}
    {}^i\boldsymbol{X}_j^{*}
    \boldsymbol{I}_j^c
    {}^j\boldsymbol{X}_i \\[1.2em]
    
    {}^{\lambda(j)}\boldsymbol{F}_i
    =
    {}^{\lambda(j)}\boldsymbol{X}_j^{*}
    {}^j\boldsymbol{F}_i
    \qquad
    \left(
    {}^i\boldsymbol{F}_i
    =
    \boldsymbol{I}_i^c
    \boldsymbol{S}_i
    \right) \\[1.2em]
    
    \boldsymbol{H}_{ij}
    =
    \left\{
    \begin{array}{ll}
    {}^j\boldsymbol{F}_i^T
    \boldsymbol{S}_j
    & \text{if } i \in \nu(j) \\[0.25em]
    
    \boldsymbol{H}_{ji}^T
    & \text{if } j \in \nu(i) \\[0.25em]
    
    \boldsymbol{0}
    & \text{otherwise}
    \end{array}
    \right.
    \end{array}
    &
    \begin{array}{l}
    \underline{\text{Algorithm:}} \\[0.6em]
    
    \boldsymbol{H} = \boldsymbol{0} \\[0.35em]
    
    \mathbf{for}\ i = 1\ \mathbf{to}\ N_B\ \mathbf{do} \\[0.25em]
    \qquad
    \boldsymbol{I}_i^c
    =
    \boldsymbol{I}_i \\[0.25em]
    \mathbf{end} \\[0.45em]
    
    \mathbf{for}\ i = N_B\ \mathbf{to}\ 1\ \mathbf{do} \\[0.25em]
    \qquad
    \mathbf{if}\ \lambda(i) \neq 0\ \mathbf{then} \\[0.25em]
    \qquad\qquad
    \boldsymbol{I}_{\lambda(i)}^c
    =
    \boldsymbol{I}_{\lambda(i)}^c
    +
    {}^{\lambda(i)}\boldsymbol{X}_i^{*}
    \boldsymbol{I}_i^c
    {}^i\boldsymbol{X}_{\lambda(i)} \\[0.25em]
    \qquad
    \mathbf{end} \\[0.35em]
    
    \qquad
    \boldsymbol{F}
    =
    \boldsymbol{I}_i^c
    \boldsymbol{S}_i \\[0.35em]
    
    \qquad
    \boldsymbol{H}_{ii}
    =
    \boldsymbol{S}_i^T
    \boldsymbol{F} \\[0.35em]
    
    \qquad
    j = i \\[0.35em]
    
    \qquad
    \mathbf{while}\ \lambda(j) \neq 0\ \mathbf{do} \\[0.25em]
    \qquad\qquad
    \boldsymbol{F}
    =
    {}^{\lambda(j)}\boldsymbol{X}_j^{*}
    \boldsymbol{F} \\[0.25em]
    
    \qquad\qquad
    j = \lambda(j) \\[0.25em]
    
    \qquad\qquad
    \boldsymbol{H}_{ij}
    =
    \boldsymbol{F}^T
    \boldsymbol{S}_j \\[0.25em]
    
    \qquad\qquad
    \boldsymbol{H}_{ji}
    =
    \boldsymbol{H}_{ij}^T \\[0.25em]
    
    \qquad
    \mathbf{end} \\[0.25em]
    
    \mathbf{end}
    \end{array}
    \\[0.4em]
    \hline
    \end{array}
    $$

## 9.2-铰接体算法(ABA)求解正动力学
# 10-多刚体系统的混合动力学求解
