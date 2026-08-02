
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
