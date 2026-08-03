## 1-刚体的空间速度 (Spatial Velocity)
在经典力学中，我们通常将角速度 $\omega$ 和线速度 $v$ 分开处理。但在空间矢量代数中，这两者被合成为一个 **6 维矢量**，称为**空间速度（Spatial Velocity）**，通常记为 $\hat{v}$。
### (1)- 定义与构成
对于刚体上的一点 $O$，其空间速度 $\hat{v}_O$ 定义为：

$$
\hat{v}_O = 
\begin{bmatrix} 
\omega \\ 
v_O 
\end{bmatrix} \in \mathbb{R}^6
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
## 2-刚体的空间加速度 (Spatial Acceleration)
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
## 3-刚体的空间刚体动量
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

## 4-刚体的空间刚体惯量矩
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

## 5-刚体的动能
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
## 6-刚体的空间刚体惯量矩的逆
我们定义$^{B}{\hat{\Phi}}={^{B}{\hat{I}}}^{-1}$，矩阵$^{B}{\hat{\Phi}}={^{B}{\hat{I}}}^{-1}$即为空间刚体惯量矩的逆，该矩阵定义如下：

$$
{^{B}{\hat{\Phi}}} = \begin{pmatrix} I_B^{-1} & -I_B^{-1}[{^{B}{r}_{OC}}]_\times \\ [{^{B}{r}_{OC}}]_\times{I_B}^{-1} & \frac{1}{m}\mathbf{1} - [{^{B}{r}_{OC}}]_\times{I_B}^{-1}[{^{B}{r}_{OC}}]_\times \end{pmatrix}
$$

## 7-刚体的空间动力学方程
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
    **刚体动力学方程对比**：空间向量形式 vs. 关节空间标准形式
    
    | 特性 | 空间动力学方程 (Spatial Form) | 关节空间标准形式 (Joint Space/Standard Form) |
    | :--- | :--- | :--- |
    | **数学表达** | $\hat{f} = \hat{I}\hat{a} + \hat{v} \times^* \hat{I}\hat{v}$ | $\mathbf{H}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q}, \dot{\mathbf{q}}) = \boldsymbol{\tau}$ |
    | **描述维度** | $6 \times 1$ 空间向量 | $n \times 1$ 广义坐标向量 ($n$ 为自由度) |
    | **描述对象** | **单个刚体**：描述空间力与空间运动的关系 | **完整系统**：描述关节力矩与关节运动的关系 | 
    | **惯性项** | $\hat{I}$：$6\times6$ 空间惯量阵（在随动坐标系下通常为常数） | $\mathbf{H}(\mathbf{q})$：关节空间惯性矩阵（随姿态 $\mathbf{q}$ 剧烈变化） | 
    | **非线性项** | $\hat{v} \times^* \hat{I}\hat{v}$：空间偏置力（包含向心力和科氏力） | $\mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})$：广义向心力与科氏力项 | 
    | **主要用途** | 动力学算法的底层物理推导与递归实现（如 RNEA） | 控制律设计、仿真、轨迹规划及系统稳定性分析 |
    
    **数学联系（映射关系）**:关节空间的形式本质上是空间动力学方程通过**雅可比矩阵 $J$** 进行投影和聚合的结果：

    1. **运动学映射**：$\hat{v}_i = \mathbf{J}_i(\mathbf{q})\dot{\mathbf{q}}$
    2. **惯性映射**：$\mathbf{H}(\mathbf{q}) = \sum_{i=1}^{n} \mathbf{J}_i^T \hat{I}_i \mathbf{J}_i$
    3. **力矩映射**：$\boldsymbol{\tau} = \sum_{i=1}^{n} \mathbf{J}_i^T \hat{f}_i$

已知空间力$^{B}{\hat{f}}$，我们可以用下式求解刚体$B$的空间加速度${^{B}{\hat{a}}}$：

$$
{^{B}{\hat{a}}}={^{B}{\hat{\Phi}}}{^{B}{\hat{f}}}+{\hat{b}}
$$

其中 ${\hat{b}}=^{B}{\Phi}{\hat{p}_B}$ 。