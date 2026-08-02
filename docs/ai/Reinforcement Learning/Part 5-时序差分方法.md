## 1.Robbins-Monro算法和Dvoretzky定理
### 1-1.Robbins-Monro算法和均值估计

!!! note "Robbins-Monro算法"
    罗宾斯-蒙罗（Robbins-Monro）算法是一种寻找方程 $g(w) = 0$ 的根 $w^*$ 的迭代方法。
    在第 $k$ 步，我们只能观测到带有随机噪声 $\eta_k$ 的梯度估计值：
    $$
    {\hat{g}(w_k, \eta_k)} = g(w_k) + \eta_k
    $$
    算法使用一个递减的步长 $\gamma_k$ 来更新估计值：
    $$
    w_{k+1} = w_k - \gamma_k \hat{g}(w_k, \eta_k)
    $$
    **关键要求:** 噪声 $\eta_k$ 必须是**无偏**的（$E[\eta_k | w_k] = 0$），并且步长序列$\gamma_k$ 需满足 $\sum \gamma_k = \infty$ 和 $\sum \gamma_k^2 < \infty$，以确保$w_k$ 最终收敛到 $w^*$。


!!! tip "Robbins-Monro算法和梯度下降(Gradient Decrease)"
    我们在机器学习或深度学习中训练神经网络，本质上是寻找一个函数映射 ${f}{:}{{X{\rightarrow}Y}}$，已知一系列数据集 $({x}^{(i)},{y}^{(i)})$，其中 ${{x}{\in}{X}},{{y}{\in}{Y}}$。
    我们假定函数关系为 ${{\hat{y}}^{(i)}}={f}{({x}^{(i)},{\theta})}$，其中 ${\theta}$ 是神经网络的参数。我们通常用均方误差（MSE）等作为损失函数：
    $$
    J={\frac{1}{N}}{\sum_{i=1}^{N}}{{{(}{{{y}}^{(i)}}-f({x}^{(i)},{\theta}){)}}^{2}}
    $$

>**核心优化目标**
>- 我们训练模型的问题转化为：**如何让损失函数 $J(\theta)$ 最小化**。
>- 这等价于寻找最优参数 ${\theta}^{*}$，使得损失函数的梯度（**驻点**）为零    $${{\nabla}_{\theta}}J(\theta^{*})=0$$
>
>**优化方法（随机逼近）**
>- 解决 $\nabla_{\theta}J=0$ 的问题，通常采用**梯度下降 (Gradient Descent)** 算法族。
>- 特别地，对于大规模数据集，我们使用**随机梯度下降 (SGD)**，它通过**小批量数据** $\mathcal{B}$ 计算梯度的**无偏估计** $\hat{\nabla}_{\theta} J$，然后迭代更新参数。
>- SGD 的迭代更新公式可以被视为Robbins-Monro 算法在极小化损失函数（寻找零点）问题上的特定应用：$${{\theta}_{k+1}}={{\theta}_{k}}-{\alpha_k}{\hat{\nabla}_{\theta}}J(\theta_k; \mathcal{B})$$
>- 其中，${\alpha_k}$ 是**学习率（步长）**，它通常会随着训练轮次 $k$ 的增加而衰减。
### 1-2.Dvoretzky定理
**Dvoretzky定理**是随机逼近领域的经典结果。这个定理可以用来分析RM算法和许多强化学习算法的收敛性。

!!! note "Dvoretzky定理"
    考虑到一个随机过程：
    $$
    {{\Delta}_{k+1}}=(1-{{\alpha}_{k}}){{\Delta}_{k}}+{{\beta}_{k}}{{\eta}_{k}}
    $$
    其中${\{{{\alpha}_{k}}\}}_{k=1}^{\infty}$，${\{{{\beta}_{k}}\}}_{k=1}^{\infty}$，${\{{{\eta}_{k}}\}}_{k=1}^{\infty}$都是随机序列，对任意的$k$都存在${{\alpha}_k}{\geq}{0}$和${{\beta}_k}{\geq}{0}$。
    如果满足以下条件，那么序列${{\Delta}_{k}}$基本上会收敛到0：
    - ${\sum_{k=1}^{\infty}}{{\alpha}_k}={\infty}$，${\sum_{k=1}^{\infty}}{{\alpha}^{2}_k}{\lt}{\infty}$和${\sum_{k=1}^{\infty}}{{\beta}_k}{\lt}{\infty}$基本一致。
    - ${\mathbb{E}[{{\eta}_k|\mathcal{H}_k}]}=0$和${\mathbb{E}[{{\eta}^{2}_k|\mathcal{H}_k}]}{\leq}C$基本上确定。
    
    其中：$${\mathcal{H}_k}=\{{{\Delta}_{k}},{{\Delta}_{k-1}},{\dots},{{\eta}_{k-1}},{\dots},{{\alpha}_{k-1}},{\dots},{{\beta}_{k-1}},{\dots}\}$$ 

## 2.使用时序差分方法求解状态值
假设我们有一个策略:${\pi}$，但是我们不知道任何模型和概率的先验知识的情况下，需要我们通过策略${\pi}$来估计当前策略:${\pi}$下每个状态$s{\in}{\mathcal{S}}$的状态值${v_{\pi}}(s)$。
首先我们从贝尔曼方程的定义出发：
$$
\begin{align}
{v_{\pi}}({s})&={\mathbb{E}}[{R_{t+1}}+{\gamma}{G_{t+1}}|{S_t}={s}]\\
&={\mathbb{E}}[{R_{t+1}}|{S_t}={s}]+{\gamma}{\mathbb{E}}[{G_{t+1}}|{S_t}={s}]\\
&={\sum_{{a_t}{\in}{A\{{s}\}}}}{\pi}{({a_t}|{s})}{\sum_{r{\in}{\{R\}}}}p(r|{s},{a_t}){\cdot}{r}+{\gamma}{\sum_{{a_t}{\in}{A\{{s}\}}}}{\pi}{({a_t}|{s})}{\sum_{{s_{t+1}}{\in}{\{S\}}}}{p({{s_{t+1}}}|{s},{a_t})}{v_{\pi}({s_{t+1}})}
\end{align}
$$
其中：
$$
\begin{align}
{\mathbb{E}}[{R_{t+1}}|{S_t}={s}]&={\sum_{{a_t}{\in}{A\{{s}\}}}}{\pi}{({a_t}|{s})}{\sum_{r{\in}{\{R\}}}}p(r|{s},{a_t}){\cdot}{r}\\
{\mathbb{E}}[{G_{t+1}}|{S_t}={s}]&={\sum_{{a_t}{\in}{A\{{s}\}}}}{\pi}{({a_t}|{s})}{\sum_{{s_{t+1}}{\in}{\{S\}}}}{p({{s_{t+1}}}|{s},{a_t})}{v_{\pi}({s_{t+1}})}
\end{align}
$$
我们根据${\sum_{{a_t}{\in}{\mathcal{A}\{s\}}}}{\pi}{({a_t}|{s})}{p({{s_{t+1}}}|{s},{a_t})}={{{P}_{\pi}}({{s_{t+1}}}|{s})}$可以将${\mathbb{E}}[{G_{t+1}}|{S_t}={s}]$写成如下形式：
$$
\begin{align}
{\mathbb{E}}[{G_{t+1}}|{S_t}={s}]&={\sum_{{a_t}{\in}{A\{{s}\}}}}{\pi}{({a_t}|{s})}{\sum_{{s_{t+1}}{\in}{\{S\}}}}{p({{s_{t+1}}}|{s},{a_t})}{v_{\pi}({s_{t+1}})}\\
&={\sum_{{s_{t+1}}{\in}{\{S\}}}}{{{P}_{\pi}}({{s_{t+1}}}|{s})}{v_{\pi}({s_{t+1}})}\\
&={\mathbb{E}}[{v_{\pi}}({S_{t+1}})|{S_t}={s}]
\end{align}
$$
那么我们的贝尔曼方程就能写成如下的形式，这个形式我们称之为**贝尔曼期望方程(Bellman Expectation Function)**：
$$
\begin{align}
{v_{\pi}}({s})={\mathbb{E}}[{R}_{t+1}+{\gamma}{v_{\pi}}({S_{t+1}})|{S_t}={s}]
\end{align}
$$
我们可以像之前的Monte-Carlo方法一样，根据已知的策略$\pi$来生成$N$个长度为$T$（$N$和$T$是足够大的正整数）的Episodes，在这些Episodes中，我们假设一共经过了$n$次状态$s{\in}{\mathcal{S}}$。我们记经过状态的时刻为$t_i(i=1,2{\dots},n)$。我们在$t_i$时刻到达状态$s$后，$t_i+1$时刻的状态$s_{t_i+1}$是随机的。获取的状态值采样即为${{r}_{t_i+1}}+{\gamma}{{v_{\pi}}({s_{t_i+1}})}$，根据大数定律我们在$t_n$时刻的时候，我们估计的状态值如下：$$
\begin{align}
{v_{t_n}}(s)={\frac{1}{n}}{\sum_{i=1}^{n}}({{r}_{t_i+1}}+{\gamma}{{v_{\pi}}({s_{t_i+1}})})
\end{align}
$$当$n$足够大的时候，根据大数定律，我们有：
$$
{{v_{\pi}}(s)}={\mathbb{E}}[R_{t+1}+{\gamma}{v_{\pi}}(S_{t+1})|S_t=s]{\approx}{{v_{t_n}}(s)}={\frac{1}{n}}{\sum_{i=1}^{n}}({{r}_{t_i+1}}+{\gamma}{{v_{\pi}}({s_{t_i+1}})})
$$
但是，上面使用到的例子是一个理想化的例子：当前环境中，仅状态$s$的状态值是未知的。其他状态都是已知的。
但是更普遍的问题是：**我们待求解的状态值都是未知的**。也就是说我们求解的目标就是求解每个状态$s{\in}{\mathcal{S}}$的状态值${{v}_{\pi}}(s)$。那么刚才我们用到的使用随机拟合来求解策略$\pi$下的状态值就无法使用了。
那么首先回顾一下第二章里提到过的用迭代法求解在指定策略${\pi}$下的贝尔曼方程的公式：
$$
{v_{k+1}}={r_\pi}+{\gamma}{P_{\pi}}{v_k}{\quad}(k=0,1,2,\dots,n)
$$
将该元素形式的迭代法方程写成类似于Bellman Expectation Equation的形式如下：
$$
\begin{align}
{v_{k+1}}(s)&={r_{\pi}}(s)+{\gamma}{\sum_{{s_{t+1}}{\in}{\{S\}}}}{{P_{\pi}}({{s_{t+1}}}|{s})}{v_{k}({s_{t+1}})}\\
&={\sum_{{a_t}{\in}{A\{{s}\}}}}{\pi}{({a_t}|{s})}{\sum_{r{\in}{\{R\}}}}p(r|{s},{a_t}){\cdot}{r}+{\gamma}{\sum_{{s_{t+1}}{\in}{\{S\}}}}{{P_{\pi}}({{s_{t+1}}}|{s})}{v_{k}({s_{t+1}})}\\
&={{\mathbb{E}}[{R_{t+1}}|{S_t}={s}]}+{\gamma}{{\mathbb{E}}[{v_k}(S_{t+1})|{S_t}={s}]}\\
&={\mathbb{E}}[{R_{t+1}}+{\gamma}{v_k}(S_{t+1})|{S_t}={s}]{\quad}(k=0,1,2,\dots,n)
\end{align}
$$
后面根据Robbins-Monro方法求解该方程如下：
$$
{v_{k+1}}(s)={v_{k}}(s)-{{\alpha}_{k}}(s)[{v_{k}}(s)-({r_{t+1}}+{\gamma}{v_k}(s_{t+
1}))]
$$
上面公式的$k$代表了我们经过状态$s{\in}{\mathcal{S}}$的次数，我们每经过一次状态$s$，那么状态$s$对应的状态值$v(s)$就更新一次。
那么我们改写一下：当我们按照策略$\pi$生成的轨迹，在时间$t$时刻经过状态$s_t{\in}{\mathcal{S}}$的时候，我们的状态值按照如下形式更新：
$$
\begin{align}
{v_{t+1}}(s_t)&={v_{t}}(s_t)-{{\alpha}_{t}}(s_t)[{v_{t}}(s_t)-({r_{t+1}}+{\gamma}{v_t}(s_{t+1}))]\\
{v_{t+1}}(s)&={v_{t}}(s)&{({\forall}s{\neq}s_t)}
\end{align}
$$
那么我们就推导出来了**时序差分算法（Temporal Difference Algorithm）**：

!!! note "时序差分算法（Temporal Difference Algorithm）"
    


我们将时序差分算法拆解如下：
$$
{\underbrace{v_{t+1}(s_t)}_{\text{new estimate}}}={\underbrace{v_t(s_t)}_{\text{current estimate}}}-{{\alpha}_{t}}(s_t)[{\underbrace{{v_{t}}(s_t)-{\overbrace{({r_{t+1}}+{\gamma}{v_t}(s_{t+1}))}^{\text{TD target}}}}_{\text{TD error } \delta_t}}]
$$
根据拆解，可以分成这四个部分：
- 新的估计(new estimate)：
- 当前估计(current estimate)：
- TD Target：
- TD Error：

!!! tip "时序差分算法的收敛性证明"
    对于时序差分算法最终收敛到$v_{\pi}(s)$的证明，我们可以使用**Dvoretzky定理**来进行证明。


!!! example "值函数时序差分方法的Python程序实现"
    ```
    ```

## 3.SARSA方法

!!! tip "关于SARSA的公式推导与证明"
    - SARSA公式推导：我们首先知道了Action Value的表达形式：$$
    \begin{align}
    {{q}_{\pi}}{({s},{a})}
    &={\mathbb{E}}{[{G_t}{|}{S_t=s},{A_t=a}]}\\
    &={\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{{s_{t+1}}{\in}{\mathcal{S}}}}{p({{s_{t+1}}}|{s},{a})}{\cdot}{v_{\pi}({s_{t+1}})}\\
    &={\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{{s_{t+1}}{\in}{\mathcal{S}}}}{p({{s_{t+1}}}|{s},{a})}{\cdot}{\sum_{{a_{t+1}}{\in}{\mathcal{A}\{{s_{t+1}}\}}}}{\pi}({a_{t+1}}|{s_{t+1}}){{q_{\pi}}({s_{t+1}},{a_{t+1}})}\\
    &={\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\sum_{{s_{t+1}}{\in}{\mathcal{S}}}}{\sum_{{a_{t+1}}{\in}{\mathcal{A}\{{s_{t+1}}\}}}}{{{P}_{\pi}}({{s_{t+1}}},{a_{t+1}}|{s},{a})}{{q_{\pi}}({s_{t+1}},{a_{t+1}})}\\
    &={\sum_{r{\in}{\{R\}}}}p(r|s,a){\cdot}{r}+{\gamma}{\mathbb{E}}[{{q_{\pi}}({S_{t+1}},{A_{t+1}})}|{S_t=s},{A_t=a}]\\
    &={\mathbb{E}}[R+{\gamma}{{q_{\pi}}({S_{t+1}},{A_{t+1}})}|{S_t=s},{A_t=a}]
    \end{align}
    $$然后我们可以根据Robbins-Monro方法求解得到关于Action-Value的迭代求解公式。推导方法和前面提到的求解State-Value的TD算法一样。
    - 关于SARSA的收敛性证明，也可以按照**Dvoretzky定理**来进行证明。


!!! example "SARSA时序差分方法的Python程序实现"
    ```
    ```

## 4.n-step SARSA方法

!!! example "n-step SARSA时序差分方法的Python程序实现"
    ```
    ```

## 5.Q-Learning方法

!!! note "On-Policy和Off-Policy"
    - **On-Policy**：
    - **Off-Policy**：


!!! note "Online Learning和Offline Learning"
    - **Online Learning**：
    - **Offline Learning**：


!!! tip "On-Policy，Off-Policy，Online Learning和Offline Learning之间的关系"
    Contents


!!! example "Q-Learning方法的Python程序实现"
    ```
    ```

