# 强化学习的大体知识架构

![[./img/Fig 1-1.png]]

强化学习，起始于**Bellman Equation**，也就是大名鼎鼎的**贝尔曼方程**。
# 每个章节对应的相关强化学习算法
为了方便对每个章节和算法的快速学习，我们做一个表格来总结不同算法的本质基础和特征。有利于在从第四章开始进行算法的分析，也有利于对算法的深刻理解。

| 对应的章节      | 算法的本质基础                                                 | 强化学习算法                                                                      | 核心性质/补充说明                                                                                             |
| :--------- | :------------------------------------------------------ | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| Chapter 4  | **Model-Based** (基于模型)                                  | **动态规划 (DP)**，**Dyna-Q**，**Model-Based RL (MBRL)**                          | 显式建模环境的**转移函数**和**奖励函数**。**DP** 通常不需要经验数据（纯规划）。                                                       |
| Chapter 5  | **Model-Free 细分 1：** **蒙特卡洛 (Monte Carlo)**             | **REINFORCE** (作为策略梯度)，**MC Control** (如 $\epsilon$-greedy MC)              | 使用**完整的回报**（整个回合结束后的累计奖励）来更新价值或策略。**高方差，无偏差**。                                                        |
| Chapter 7  | **Model-Free 细分 2：** **时序差分 (Temporal-Difference, TD)** | **TD(0)**，**TD($\lambda$)**，**SARSA($\lambda$)**，**Q-Learning** (作为 TD 的应用) | 使用**自举 (Bootstrapping)** 思想，用估计的未来价值来更新当前价值。**低方差，有偏差**。                                              |
| Chapter 8  | **Model-Free 细分 3：** **Value-Based (基于价值)**             | **Q-Learning**，**SARSA**，**DQN**，**DDQN**，**C51 (分布RL)**                    | 目标是学习最优的 **Q 函数**。绝大多数此类方法都基于 **TD** 思想。策略是从中学到的价值函数中**隐式导出**的。                                       |
| Chapter 9  | **Model-Free 细分 4：** **Policy-Based (基于策略)**            | **策略梯度 (PG)**，**REINFORCE**，**GPRO**                                        | **直接优化**策略 $\pi(a\|s)$ 的参数。通常是 **On-Policy**，方差较大。                                                    |
| Chapter 10 | **Model-Free 细分 5：** **Actor-Critic (行动者-评判者)**         | **A2C/A3C**，**DDPG**，**TD3**，**TRPO**，**PPO**，**SAC**                       | 结合了上述两种方法：**Actor** 学习策略，**Critic** 学习价值函数来**降低策略梯度的方差**。是现代深度强化学习（Deep Reinforcement Learning）的主流架构。 |

需要注意的是，这些分类维度存在交叉关系：
- **TD** 和 **蒙特卡洛** 描述的是**价值/回报的估计方法**。
- **Value-Based** 和 **Policy-Based** 描述的是**学习的目标**。
- **Actor-Critic** 是**架构**，它结合了 **Policy-Based** 的 Actor 和 **Value-Based** 的 Critic。

# 一、强化学习基本名词

## 1.1-Agent

> [!NOTE] Agent
> **Agent(智能体)**是在环境中通过感知(perception)获取状态、通过决策(policy)选择动作、并通过执行(action)影响环境，进而获得奖励(reward)的实体。

## 1.2-State and State Space
> [!NOTE] State
> **State(状态)**指Agent在环境中能够观测并且量化的变量的集合。

 
> [!NOTE] State Space
> **State Space(状态空间)**指的是在环境中所有$n$个状态$s_i(i=1,2,\dots,n)$的集合，状态空间的表达式：
> $${\mathcal{S}}=\{{s}_{i}\}_{i=1}^{n}$$

## 1.3-Action and Action Space
> [!NOTE] Action
> **Action(动作)**指Agent在特定状态${s_i}{\in}{\mathcal{S}}$可以执行的任意Action，这个过程我们一般用$a$来表示，一般来说任意的State${s_i}{\in}{\mathcal{S}}$有多个Action:
> $$a_k{\quad}(k=1,2,\dots)$$

> [!NOTE] Action Space
> 对于在状态空间中的任意状态$s_i{\in}{\mathcal{S}}$来说，在这个状态能够执行的所有的Acton：
> $$a_k{\quad}(k=1,2,\dots)$$
> 的集合定义为状态$s_i$的**Action Space(动作空间)**：
> $$\{{\mathcal{A}}(s_i)\}=\{a_1,a_2,\dots,a_m\}$$

## 1.4-State transition
> [!NOTE] State transition
> **State transition(状态转移)**指的是状态集合$\{S\}$中的状态$s_i$通过动作集合$\{A(s_i)\}$中的某个动作$a_k$转移到另外的状态$s_j$的过程：
> $$
> {s_i}{\xrightarrow{a_k}}{s_j}
> $$

## 1.5-Policy
> [!NOTE] Policy
> **Policy(策略)** 代表着在环境中的任意给定状态${s}{\in}{\mathcal{S}}$下，采取动作$a_k{\in}{\{{\mathcal{A}}(s_i)\}}$的可能性。Policy可以用以下的形式来表达：
> - **函数形式：** 将策略${\pi}$看作一种函数，函数的输入变量为状态$s{\in}{\mathcal{S}}$，输出变量为在当前需要采取的动作${a}{\in}{\mathcal{A}}\{s\}$，该函数表达如下：$${a}={\pi}({s})$$这种形式可以用于离散或者连续的状态集合$\mathcal{S}$，以及离散或者连续的动作集合${\mathcal{A}}$。
> - **条件概率形式：** 在当前状态$s{\in}{\mathcal{S}}$的情况下，执行动作$a_k{\in}{\{{\mathcal{A}}(s_i)\}}$的概率${\pi}({a_k}|{s})$。这种形式大多数情况下用于离散的动作序列。

强化学习的主要目标，是为了**学习到全局最优的策略${\pi}^{*}$**，我们有**Value-Based**和**Policy-Based**两个方式去学习最优策略${\pi}^{*}$。

> [!NOTE] Value-Based方法和Policy-Based方法
> - **Value-Based方法**：
> 	- 核心思想：首先学习价值函数（Value Function）
> 	- 最优策略是通过**Greedy策略**，也就是在当前的状态下选择能够带来最高价值的动作来间接确定。
> - **Policy-Based方法**：
> 	- 核心思想：直接学习和优化策略函数${\pi}({s})$和${\pi}({a}|{s})$，使之能最大化期望回报。
> 	- 例如：Policy Gradient，Actor-Critic策略。

## 1.6-Reward
> [!NOTE] Reward
> **Reward(奖励)**代表着Agent在某个状态$s{\in}{\mathcal{S}}$下，通过执行动作$a_i{\in}{{\mathcal{A}}(s_i)}$转移到其他状态$s’{\in}{\mathcal{S}}$获得的奖励。这个奖励是可以根据训练目标来人为设定的标量。

在现实生活中，环境是随机的。因此在相同状态执行相同动作，获得的回报也不一定相同，因此，获得回报是个概率性时间
（在现实非理想的环境中，在相同状态，执行相同动作也不一定会收获这个概率，因此，我们在状态$s$，执行动作$a$的时候，获取收益$r$的概率可以表示为$p(r|s,a)$。）
## 1.7-Trajectory和Episode
> [!NOTE] Trajectory
> **Trajectory(轨迹)**是在固定策略 $\pi$ 与环境转移概率 $P(s′|s,a)$ 下，Agent 依次产生的一段状态-动作-奖励链：
> $$
> {s_i}{\xrightarrow[r=r_k]{a_k}}{s_{i+1}}{\xrightarrow[r=r_m]{a_m}}{\dots}
> $$

## 1.8-Return
> [!NOTE] Return
> **Return(回报)**是Agent从当前时间$t$所在的状态$s_i{\in}{\mathcal{S}}$开始，在任意一条可能的Trajectory上从$t+1$时刻开始获得的所有未来奖励的总和。

（直接Return相加只适用于有限步数的，我们更多地使用无限步数的Return，那么所有的Return是无限的，就区分不出来哪个策略是好的或者坏的，我们需要使用一种衰减来让Agent实现策略是可以分辨出好坏的，那么对于没有结束的过程的Return，我们使用Discount Return来实现可量化的Return评估）

> [!NOTE] Discount Return
> **Discount Return(折扣回报)**

> [!question] 为什么在强化学习里面用的最多的是Discount Return
> Contents

## 1.9-Markov Decision Processes
（**未来总回报的价值**只取决于智能体**当前所处的状态**，与过去的历史轨迹无关，这正是MDP的核心马尔可夫性质。因此，智能体为了最大化未来的回报，只需要根据**当前状态**来做出最优决策，从而极大地简化了复杂的学习问题。）
（从我们的Trajectory Chain我们可以发现我们得到的是一系列的）
> [!NOTE] Markov decision processes(重点理解)
> **Markov decision processes(马尔科夫决策过程)**指的是Agent未来的State只与当前时间$t$的State和从$t+1$时刻开始的未来状态有关，与从$t-1$之前的历史状态无关。
