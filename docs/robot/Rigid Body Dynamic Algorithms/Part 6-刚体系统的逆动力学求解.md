
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
