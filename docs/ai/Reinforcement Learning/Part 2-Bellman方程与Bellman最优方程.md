# 二、贝尔曼方程(Bellman Equation)

首先我们的Agent面对的状态以及各个状态对应的不同动作及其回报如图所示：

我们
（为什么Return是非常重要的）

> [!NOTE] State Value
> 我们有如下形式的Trajectory：
> $${S}_{t}{\xrightarrow{{a{\in}{\{A{(S_t})\}}}}}{{R}_{t+1}},{{S}_{t+1}}{\xrightarrow{{a{\in}{\{A{(S_{t+1}})\}}}}}{{R}_{t+2}},{{S}_{t+2}}{\cdots}$$
> 我们计算这个策略对应轨迹的Return：
> $$G_t={R_{t+1}}+{\gamma}{R_{t+2}}+{\gamma^{2}}{R_{t+3}}+{\cdots}$$
> 由于在当前策略$s_t$执行的下一步动作不确定
> 我们定义在时间$t$上，状态${s}{\in}{\{S\}}$的Return期望就是**State Value**：
> $${{v}_{\pi}}(s)={\mathbb{E}}{[{G_t}{|}{S_t=s}]}$$

首先我们将Return的公式写作如下形式：
$$
{G_t}={R_{t+1}}+{\gamma}{G_{t+1}}
$$
根据State Value的定义，我们将上面的式子写成期望的形式：
$$
\begin{align}
{\mathbb{E}}[{G_t}|{S_t}={s}]
&={\mathbb{E}}[{R_{t+1}}+{\gamma}{G_{t+1}}|{S_t}={s}]\\
&={\mathbb{E}}[{R_{t+1}}|{S_t}={s}]+{\gamma}{\mathbb{E}}[{G_{t+1}}|{S_{t}}={s}]
\end{align}
$$
那么在当前时间$t$下，我们的State Value可以写成两种形式，分别是在当前时刻$t$下在任意状态$s{\in}{\mathcal{S}}$，$t+1$时刻获得的Return的数学期望${\mathbb{E}}[{R_{t+1}}|{S_t}={s}]$和下一时刻$t+1$能够获得的数学期望两个部分。
首先是等式的第一项，也就是在当前状态$S_t$的时候，我们执行动作获得回报的期望值：
$$
\begin{align}
{\mathbb{E}}[{R_{t+1}}|{S_t}={s}]
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{\mathbb{E}}{(R_{t+1}|{S_t}={s},{A_t}={a})}\\
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}
\end{align}
$$
然后是等式的第二项，也就是当前Agent在$t$时刻的状态$S_t$的时候，下一时刻$t+1$能够得到的State Value的期望值：
$$
\begin{align}
{\mathbb{E}}[{G_{t+1}}|{S_{t}}={s}]
&={\sum_{{s^{'}}{\in}{\{S\}}}}{\mathbb{E}}[{G_{t+1}}|{S_{t}}={s},{S_{t+1}}={s'}]{\cdot}p({s^{'}}|{s})\\
&={\sum_{{s^{'}}{\in}{\{S\}}}}{\mathbb{E}}[{G_{t+1}}|{S_{t+1}}={s'}]{\cdot}p({s^{'}}|{s})\\
&={\sum_{{s^{'}}{\in}{\{S\}}}}{\mathbb{E}}[{G_{t+1}}|{S_{t+1}}={s'}]{\cdot}{\sum_{a{\in}{A\{s\}}}}{\pi}(a|s){\cdot}{p({s^{'}}|{s},{a})}\\
&={\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{\sum_{a{\in}{A\{s\}}}}{\pi}(a|s){\cdot}{p({s^{'}}|{s},{a})}\\
\end{align}
$$
将第一项和第二项联立起来：
$$
v_{\pi}({s})={\mathbb{E}}[{G_t}|{S_t}={s}]={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{a{\in}{A\{s\}}}}{\pi}(a|s){\cdot}{\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{p({s^{'}}|{s},{a})}\\
$$
上式结果就是**贝尔曼方程**的一般形式。

> [!NOTE] Bellman Equation
> $$
> v_{\pi}({s})={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{a{\in}{A\{s\}}}}{\pi}(a|s){\cdot}{\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{p({s^{'}}|{s},{a})}\\
> $$

我们设Agent在当前的环境中有一系列的State：
$${s_i}{\in}{\mathcal{S}}{\quad}(i=1,2,3,\dots,n)$$
我们将每个状态的State Value写作${v_{\pi}}({s_i})(i=1,2,3,\dots)$。然后我们将Bellman等式写作如下形式：
$$
\begin{align}
v_{\pi}({s}_{i})
&={r_{\pi}}({s}_{i})+{\gamma}{\sum_{{s_k}{\in}{\{S\}}}}{p({{s}_{k}}|{s}_{i})}{\cdot}{v_{\pi}({s_k})}
\end{align}
$$
其中：
$$
\begin{align}
{r_{\pi}}(s_i)={\sum_{a{\in}{A\{s_{i}\}}}}{\pi}{(a|{s}_{i})}{\cdot}{\sum_{r{\in}{\{R\}}}}p(r|{s_i},a){\cdot}{r}\\
{p({{s}_{k}}|{s}_{i})}={\sum_{a{\in}{A\{s_{i}\}}}}{\pi}{(a|{s}_{i})}{\cdot}{p({{s}_{k}}|{{s}_{i}},{a})}\\
\end{align}
$$
然后我们定义State Value矩阵$v_{\pi}$，回报期望矩阵$r_{\pi}$和状态转移概率矩阵$P_{\pi}$：
$$
\begin{matrix}
v_{\pi}={
\begin{pmatrix}
{v_{\pi}}({s_1})\\
{v_{\pi}}({s_2})\\
{\vdots}\\
{v_{\pi}}({s_n})\\
\end{pmatrix}
}{\quad}
r_{\pi}={
\begin{pmatrix}
{r_{\pi}}({s_1})\\
{r_{\pi}}({s_2})\\
{\vdots}\\
{r_{\pi}}({s_n})\\
\end{pmatrix}
}{\quad}
{P_{\pi}}={
\begin{pmatrix}
{p_{\pi}}({s_1}|{s_1})&{\dots}&{p_{\pi}}({s_1}|{s_n})\\
{\vdots}&{\quad}&{\vdots}\\
{p_{\pi}}({s_n}|{s_1})&{\dots}&{p_{\pi}}({s_n}|{s_n})\\
\end{pmatrix}
}{\quad}
\end{matrix}
$$
那么在这个Environment中，Bellman Equation方程的矩阵表达式为：
$$
{v_{\pi}}={r_{\pi}}+{\gamma}{P_{\pi}}{v_{\pi}}
$$
通过移项之后就得到了更容易计算的形式：
$$
(I-{\gamma}{P}){v_{\pi}}={r_{\pi}}
$$

> [!question] 我们为什么要求解State Value？
> 

因为State Value对于我们做强化学习评估Policy效果非常重要，因此我们求解各个状态对应的State Value有以下两种方式：
- **矩阵求解**：这是State Value的Closed form解，我们已知状态转移矩阵$P$，每个状态的回报期望值矩阵$R_{\pi}$和折扣系数${\gamma}$。我们可以通过矩阵求逆的形式求解：$${v_{\pi}}={(I-{\gamma}{P_{\pi}})}^{-1}{r_{\pi}}$$这种方式可以一次性求解所有状态的State Value并且显得更直观一些，但是这种方式的局限性在于状态过多导致矩阵维数过大，求解的复杂度增大。
- **迭代求解**：迭代求解是先预设一个State Value矩阵的初始值${v_{0}}$，使用下面的迭代方式直到第$n$步求出最终的状态值矩阵：$${v_{k+1}}={r_\pi}+{\gamma}{P_{\pi}}{v_k}{\quad}(k=0,1,2,\dots,n)$$我们可以证明为什么能够迭代法能够在$n$步之后实现满足误差范围的$v_{\pi}$，首先我们令：$${\delta}_{k}=v_{k}-v_{\pi}{\quad}(k=0,1,2,\dots,n)$$代入上面的迭代式子，我们可以得到：$$\begin{align}{{\delta}_{k+1}}&={r_\pi}+{\gamma}{P}({{\delta}_{k}}+{v_{\pi}})-{v_{\pi}}\\&={r_\pi}+{\gamma}{P}{{\delta}_{k}}-(I-{\gamma}{P}){{v}_{\pi}}\\&={\gamma}{P}{{\delta}_{k}}\end{align}$$然后我们从$k=0$开始迭代，我们最终得到：$${{\delta}_{k+1}}=({\gamma}{P})^{k+1}{{\delta}_{0}}$$那么随着迭代次数$k$的不断增大，$\delta$也逐渐趋近于0。因此迭代方法能够实现对任意初始值$v_0$，只要迭代次数$k$足够多，结果一定收敛到$v_{\pi}$。

> [!TIP] State Value的Close Form Solution和Iteration Form Solution的算法复杂度对比
> 从算法复杂度的角度来评判当前的算法复杂度
> - 使用Close Form求解State Value：我们假设有$n$个状态，我们矩阵求逆的算法复杂度是${O}({n^3})$。
> - 使用Iteration Form来求解State Value：我们假设有$n$个状态，我们使用迭代方法求解矩阵的算法复杂度仅仅是$O({n^2})$

（Action Value：我们选择最优的序列，看那个Action Value能达到最优解）
我们在前面主要对State Value进行讨论，因为在强化学习中，State Value是至关重要的。
我们回到前面推到的贝尔曼方程，我们将Policy项提取出来：
$$
\begin{align}
v_{\pi}({s})={\mathbb{E}}[{G_t}|{S_t}={s}]
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{a{\in}{A\{s\}}}}{\pi}(a|s){\cdot}{\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{p({s^{'}}|{s},{a})}\\
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}({\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{p({s^{'}}|{s},{a})})\\
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{{q}_{\pi}}{({s},{a})}
\end{align}
$$
上式右侧的第二项我们称之为**Action Value**：

> [!NOTE] Action Value
> $$
> \begin{align}
> {{q}_{\pi}}{({s},{a})}
> &={\mathbb{E}}{[{G_t}{|}{S_t=s},{A_t=a}]}\\
> &={\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{p({s^{'}}|{s},{a})}
> \end{align}
> $$

> [!TIP] Action Value和State Value的求解关系
> - 根据Action Value求解State Value
> - 根据State Value求解Action Value

> [!WARNING] 求解Action Value的出错点
> Contents

(写成缩写的形式)
首先我们根据Action Value的公式我们可以定义当处于状态$S_t=s$的时候，所有动作的Action Value矩阵$q_{\pi}$，当执行动作$A_t=a{\in}A(s)$的时候获取的收益矩阵${\tilde{r}}$，概率转移矩阵$P$和Policy矩阵${\pi}$如下：
$$
\begin{matrix}
q_{\pi}={
\begin{pmatrix}
[{q_{\pi}}]_{({s,a_1})}\\
[{q_{\pi}}]_{({s,a_2})}\\
{\vdots}\\
[{q_{\pi}}]_{({s,a_m})}\\
\end{pmatrix}
}{\quad}
{\tilde{r}}={
\begin{pmatrix}
[{\tilde{r}}]_{({s,a_1})}\\
[{\tilde{r}}]_{({s,a_2})}\\
{\vdots}\\
[{\tilde{r}}]_{({s,a_m})}\\
\end{pmatrix}
}{\quad}
P={
\begin{pmatrix}
p({s_1}|{s},{a_1})&{\dots}&p({s_1}|{s},{a_m})\\
{\vdots}&{\quad}&{\vdots}\\
p({s_n}|{s},{a_1})&{\dots}&p({s_n}|{s},{a_m})\\
\end{pmatrix}
}{\quad}
{\Pi}={
\begin{pmatrix}
{\pi}{({s|a_1})}\\
{\pi}{({s|a_2})}\\
{\vdots}\\
{\pi}{({s|a_m})}\\
\end{pmatrix}}
\end{matrix}
$$
那么我们可以求解出来Action Value的矩阵形式：
$$
{q_{\pi}}={\tilde{r}}+{\gamma}{P}{\Pi}{q_{\pi}}
$$
这也就是贝尔曼方程的Action Value方式，对于此表达我们依然可以用Closed-Form方法和Iteration-Form方法求解，求解的方法本质上和State-Value的方法是一致的。

> [!TIP] Action Value和State Value的对比
> - 根据Action Value求解State Value
> - 根据State Value求解Action Value

# 三、贝尔曼优化方程(Bellman Optimal Equation)

（Examples,我们为什么使用State Value？原因是State Value是能够评价哪个可能的Policy更好。）
## 3-1.最优状态值和最优策略

> [!NOTE] Optimal State Value和Optimal Policy
> 对于在任意状态中的State:$s{\in}{\{S\}}$来说，任意可能Policy的集合为${\mathbb{\Pi}}$。我们可以有如下的定义：
> 对于${\forall}{\pi}{\in}{\mathbb{\Pi}}$，总是存在一个策略${\pi}^{*}$使得${{v}_{{\pi}^{*}}(s)}{\geq}{{v}_{\pi}(s)}$。我们称${{v}_{{\pi}^{*}}(s)}$为**Optimal State Value(最优状态值)**，对应的${\pi}^{*}$就是**Optimal Policy(最优策略)**。

## 3-2.贝尔曼最优方程的两种表达形式
### 3-2-1.元素形式的贝尔曼最优方程
那么在一个未知的环境中，我们的问题就从所有的量都已知来求解State Value，变成了在任意状态${s}{\in}{\mathcal{S}}$中所有可能的Policy中找到Policy来使得State Value达到最优。从本质上来讲这就是求解一个最优化问题。
首先我们回顾一下贝尔曼方程：
$$
\begin{align}
v_{\pi}({s})={\mathbb{E}}[{G_t}|{S_t}={s}]
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{a{\in}{A\{s\}}}}{\pi}(a|s){\cdot}{\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{p({s^{'}}|{s},{a})}\\
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}({\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{{s^{'}}{\in}{\{S\}}}}{v_{\pi}(s^{'})}{\cdot}{p({s^{'}}|{s},{a})})\\
&={\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{{q}_{\pi}}{({s},{a})}
\end{align}
$$
我们是已知在状态${s}{\in}{\mathcal{S}}$中的策略${\pi}$，进而求解策略${\pi}$对应的State Value：$v_{\pi}(s)$。那么我们在前面的定义中提到找到State Value的最优解的前提就是寻找到最优的Policy。因此我们将贝尔曼方程改写成下面的**贝尔曼最优方程**的元素形式：
$$
\begin{align}
v({s})
&={\underset{{\pi}{\in}{\mathbb{\Pi}}}{\max}}{\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{{q}_{\pi}}{({s},{a})}\\
&={\underset{{\pi}{\in}{\mathbb{\Pi}}}{\max}}{\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}({\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{{s^{'}}{\in}{\{S\}}}}{p({s^{'}}|{s},{a})}{\cdot}{v(s^{'})})\\
&={\underset{{\pi}{\in}{\mathbb{\Pi}}}{\max}}{\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}([r]_{(s,a)}+{\gamma}{\sum_{{s^{'}}{\in}{\{S\}}}}{p({s^{'}}|{s},{a})}{\cdot}{v(s^{'})})\\
\end{align}
$$
那么在元素形式中，我们有两个未知数$v(s)$和$\pi$，但是我们还需要求解State Value:$v(s)$的最大值。那么我们首先就需要从Policy:${\pi}$来入手求解元素形式的贝尔曼方程。
首先我们看贝尔曼最优方程的元素形式，我们发现我们有策略:$\pi$和State Value:$v({s})$两个未知的变量。但是我们只求解其中一个变量$v({s})$的最大值。

> [!EXAMPLE] 求解最大值
> 我们假设有两组数列，其中有一组数列$q_k=\{{q_1},{q_2},{q_3},{\dots},{q_k}\}$我们仅仅知道里面有最大值。另外一组数列$c_k=\{{c_1},{c_2},{c_3},{\dots},{c_k}\}$是未知的，我们只知道数列$c_k$的数列和：
> $${\sum_{i=1}^{k}}c_i=1$$
> 那么我们需要求解当数列$c_k$满足什么条件的时候能够让下面的式子取得最大值：
> $${\sum_{i=1}^{k}}{c_i}{\cdot}{q_i}$$
> 我们只需要知道数列$q_k$的最大值$q_m$，然后我们让对应的$c_m=1$，其余项为0，那么我们的最大值就是${c_m}{\cdot}{q_m}$

那么对于贝尔曼最优方程的元素形式来说，我们只需要找到在任意状态$s{\in}{\{S\}}$对应的动作$a{\in}{A\{s\}}$中找到能够让${{q}_{\pi}}{({s},{a})}$取得最大值的${{q}_{\pi}}{({s},{{a}^{*}})}$对应的动作$a^{*}$，并且让这个最大值对应策略${\pi}{({a}^{*}|s)}=1$，其余项等于0，于是我们就可以得到$v({s})$的最大值如下：
$$
\begin{align}
v({s})
&={\underset{{\pi}{\in}{\mathbb{\Pi}}}{\max}}{\sum_{a{\in}{A\{s\}}}}{\pi}{(a|s)}{\cdot}{{q}_{\pi}}{({s},{a})}\\
&={\underset{{{a}{\in}{A\{s\}}}}{\max}}([r]_{(s,{{a}^{*}})}+{\gamma}{\sum_{{s^{'}}{\in}{\{S\}}}}{p({s^{'}}|{s},{{a}^{*}})}{\cdot}{v(s^{'})})\\
\end{align}
$$
那么对于元素形式的贝尔曼最优方程的实际意义，就是对于任意状态$s{\in}{\mathcal{S}}$，我们要在该状态对应的Action Space:$a{\in}{\mathcal{A}}\{{s}\}$中寻找能够使得Action Value:${{q}_{\pi}}{({s},{a})}$最大的动作${a}^{*}$并且执行。我们无需进行复杂的规划，**最优策略${\pi}^{*}({s})$仅需要进行一步贪婪搜索（Greedy Search）**。
$$
{a}^{*}={\arg}{\underset{{{a}{\in}{\mathcal{A}\{s\}}}}{\max}}{q_{\pi}(s,a)}
$$
### 3-2-2.矩阵形式的贝尔曼最优方程
我们将贝尔曼方程的矩阵形式改写为贝尔曼最优方程的矩阵形式，那么我们可以得到：
$$
{v}={\underset{{\pi}{\in}{\mathbb{\Pi}}}{\max}}({r_{\pi}}+{\gamma}{P_{\pi}}{v})
$$
矩阵形式的贝尔曼方程的意义就是为了证明贝尔曼方程是否具有唯一的最值。
> [!question] 接下来要讨论什么问题？
> - 是否存在最优解？
> - 这个最优解是否是唯一的？
> - 如何求解这个最优解？
> - 贝尔曼最优方程的最优解是怎么和最优策略结合起来的?
## 3-3.Bellman最优方程的一些性质
### 3-3-1.Bellman最优方程存在唯一的最优解
首先来介绍**不动点和收缩映射的定义**以及**收缩映射定理**：

> [!NOTE] 不动点和收缩映射的定义
> - **不动点**：对变量$x{\in}{\mathbb{R}^{n}}$和函数$f(x){\in}{\mathbb{R}^{n}}$来说，如果我们满足以下关系$$x^{*}=f(x^{*})$$那么$x^{*}$称为函数的**不动点**，这个方程也叫做不动点方程。
> - **收缩映射**：一个映射 $f: \mathbb{R}^n \rightarrow \mathbb{R}^n$ 被称为**收缩映射**，如果存在一个常数 $L \in [0, 1)$，使得对于任意两个点 $x, y \in \mathbb{R}^n$，都有： $$ \|f(x) - f(y)\| \le L\|x - y\| $$ 其中，$\|\cdot\|$ 表示欧几里得范数（距离）。

> [!NOTE] 收缩映射定理
> 对于任意一个具有$x=f(x)$形式的方程来说，其中${x}{\in}{\mathbb{R}^{n}}$，$f:{\mathbb{R}^{n}}{\rightarrow}{\mathbb{R}^{n}}$，如果$f$是收缩映射，那么遵守以下的性质：
> - **存在性**：有且仅有一个不动点${x}^{*}$满足${{x}^{*}}=f({{x}^{*}})$
> - **唯一性**：不动点${x}^{*}$是唯一的
> - **算法**：设定一个初始的点${x}_{0}$，我们使用以下方式来进行迭代：$$x_{k+1}=f({x_{k}}){\quad}k{\in}{\mathbb{Z}}$$当$k{\rightarrow}{\infty}$的时候$x_k{\rightarrow}x^{*}$

接下来我们来证明**Bellman最优方程存在唯一的最优解**：
- 首先，由于我们在最初就定义了以下形式的贝尔曼优化方程：$$v=f(v)={\underset{{\pi}{\in}{\mathbb{\Pi}}}{\max}}({r_{\pi}}+{\gamma}{P}{v})$$因此我们的这个形式自然满足**不动点方程**的形式。
- 我们任意设定两个Optimal State Value:$v_1$和$v_2$。对应的Optimal Policy分别是${\pi}^{*}_{1}$和${\pi}^{*}_{2}$。对应的贝尔曼最优方程可以写成如下的形式：$$\begin{align}f(v_{1})={r_{\pi^{*}_{1}}}+{\gamma}{P_{\pi^{*}_{1}}}{v_1}{\geq}{r_{\pi^{*}_{2}}}+{\gamma}{P_{\pi^{*}_{2}}}{v_1}\\f(v_{2})={r_{\pi^{*}_{2}}}+{\gamma}{P_{\pi^{*}_{2}}}{v_2}{\geq}{r_{\pi^{*}_{1}}}+{\gamma}{P_{\pi^{*}_{1}}}{v_2}\end{align}$$那么我们先写出${f(v_{1})-f(v_{2})}$的形式：$$\begin{align}{f(v_{1})-f(v_{2})}={{{r_{\pi^{*}_{1}}}+{\gamma}{P_{\pi^{*}_{1}}}{v_1}}-{r_{\pi^{*}_{2}}}-{\gamma}{P_{\pi^{*}_{2}}}{v_2}}{\leq}{{{r_{\pi^{*}_{1}}}+{\gamma}{P_{\pi^{*}_{1}}}{v_1}}-{r_{\pi^{*}_{1}}}-{\gamma}{P_{\pi^{*}_{1}}}{v_2}}={\gamma}{P_{{\pi}^{*}_{1}}}{(v_1-v_2)}\\{f(v_{1})-f(v_{2})}={{{r_{\pi^{*}_{1}}}+{\gamma}{P_{\pi^{*}_{1}}}{v_1}}-{r_{\pi^{*}_{2}}}-{\gamma}{P_{\pi^{*}_{2}}}{v_2}}{\geq}{{{r_{\pi^{*}_{2}}}+{\gamma}{P_{\pi^{*}_{2}}}{v_1}}-{r_{\pi^{*}_{2}}}-{\gamma}{P_{\pi^{*}_{2}}}{v_2}}={\gamma}{P_{{\pi}^{*}_{2}}}{(v_1-v_2)}\end{align}$$我们因此也就得到了：$${\gamma}{P_{{\pi}^{*}_{2}}}{(v_1-v_2)}{\leq}{f(v_{1})-f(v_{2})}{\leq}{\gamma}{P_{{\pi}^{*}_{1}}}{(v_1-v_2)}$$接下来我们定义一个最大值：$$z={\max}{\{}{\gamma}{P_{{\pi}^{*}_{1}}}{(v_1-v_2)}|{\gamma}{P_{{\pi}^{*}_{2}}}{(v_1-v_2)}\}$$那么上面的不等式我们也可以写为：$${-z}{\leq}{\gamma}{P_{{\pi}^{*}_{2}}}{(v_1-v_2)}{\leq}{(f(v_{1})-f(v_{2}))}{\leq}{\gamma}{P_{{\pi}^{*}_{1}}}{(v_1-v_2)}{\leq}{z}$$我们可以得出如下结论：$${\|}f(v_1)-f(v_2){\|}_{\infty}{\leq}{\|}z{\|}_{\infty}$$接下来我们需要证明存在一个${\gamma}{\in}{[0,1)}$使得$\|z\|{\leq}{\gamma}\|(v_1-v_2)\|$。对$z$中的各个元素来说，都有$$[z]_{i}={\max}{\{}{({\gamma}{p}^{T}(v_1-v_2)|{\gamma}{q}^{T}(v_1-v_2))}{\}}{\leq}[{{\gamma}{(v_1-v_2)}}]_{i}$$那么整体的$\|z\|_{\infty}{\leq}{\gamma}\|(v_1-v_2)\|_{\infty}$，联立可得：$${\|}f(v_1)-f(v_2){\|}_{\infty}{\leq}{\gamma}\|(v_1-v_2)\|_{\infty}$$贝尔曼最优方程的**收缩映射**性质得证。
- 根据
因此，**贝尔曼最优方程本身就具有唯一的最优解**，问题得证。并且我们可以通过迭代算法来求解贝尔曼最优方程的最优解。
对于求解最优解，我们有两种方式来求解：**价值迭代**和**策略迭代**。
### 3-3-2.最优策略的贝尔曼优化方程的结果对应最优状态值

我们已经证明了贝尔曼最优方程是能够通过收缩映射定理能够求最优解的，那么我们需要证明一件事情，那就是**Optimal State Value和Optimal Policy**是否是一一对应的，也就是说我们的最优策略是否一定对应最优解。