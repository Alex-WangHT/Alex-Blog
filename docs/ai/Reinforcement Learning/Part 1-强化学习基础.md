# 一、强化学习基本名词

## 1.1-Agent

!!! note "Agent"
    **Agent(智能体)**是在环境中通过感知(perception)获取状态、通过决策(policy)选择动作、并通过执行(action)影响环境，进而获得奖励(reward)的实体。


## 1.2-State and State Space

!!! note "State"
    **State(状态)**指Agent在环境中能够观测并且量化的变量的集合。


 
!!! note "State Space"
    **State Space(状态空间)**指的是在环境中所有$n$个状态$s_i(i=1,2,\dots,n)$的集合，状态空间的表达式：
    $${\mathcal{S}}=\{{s}_{i}\}_{i=1}^{n}$$


## 1.3-Action and Action Space

!!! note "Action"
    **Action(动作)**指Agent在特定状态${s_i}{\in}{\mathcal{S}}$可以执行的任意Action，这个过程我们一般用$a$来表示，一般来说任意的State${s_i}{\in}{\mathcal{S}}$有多个Action:
    $$a_k{\quad}(k=1,2,\dots)$$


!!! note "Action Space"
    对于在状态空间中的任意状态$s_i{\in}{\mathcal{S}}$来说，在这个状态能够执行的所有的Acton：
    $$a_k{\quad}(k=1,2,\dots)$$
    的集合定义为状态$s_i$的**Action Space(动作空间)**：
    $$\{{\mathcal{A}}(s_i)\}=\{a_1,a_2,\dots,a_m\}$$


## 1.4-State transition

!!! note "State transition"
    **State transition(状态转移)**指的是状态集合$\{S\}$中的状态$s_i$通过动作集合$\{A(s_i)\}$中的某个动作$a_k$转移到另外的状态$s_j$的过程：
    $${s_i}{\xrightarrow{a_k}}{s_j}$$


## 1.5-Policy

!!! note "Policy"
    **Policy(策略)** 代表着在环境中的任意给定状态${s}{\in}{\mathcal{S}}$下，采取动作$a_k{\in}{\{{\mathcal{A}}(s_i)\}}$的可能性。Policy可以用以下的形式来表达：
    - **函数形式：** 将策略${\pi}$看作一种函数，函数的输入变量为状态$s{\in}{\mathcal{S}}$，输出变量为在当前需要采取的动作${a}{\in}{\mathcal{A}}\{s\}$，该函数表达如下：
    $${a}={\pi}({s})$$这种形式可以用于离散或者连续的状态集合$\mathcal{S}$，以及离散或者连续的动作集合${\mathcal{A}}$。
    - **条件概率形式：** 在当前状态$s{\in}{\mathcal{S}}$的情况下，执行动作$a_k{\in}{\{{\mathcal{A}}(s_i)\}}$的概率${\pi}({a_k}|{s})$。这种形式大多数情况下用于离散的动作序列。


强化学习的主要目标，是为了**学习到全局最优的策略${\pi}^{*}$**，我们有**Value-Based**和**Policy-Based**两个方式去学习最优策略${\pi}^{*}$。

!!! note "Value-Based方法和Policy-Based方法"
    - **Value-Based方法**：
    	- 核心思想：首先学习价值函数（Value Function）
    	- 最优策略是通过**Greedy策略**，也就是在当前的状态下选择能够带来最高价值的动作来间接确定。
    - **Policy-Based方法**：
    	- 核心思想：直接学习和优化策略函数${\pi}({s})$和${\pi}({a}|{s})$，使之能最大化期望回报。
    	- 例如：Policy Gradient，Actor-Critic策略。


## 1.6-Reward

!!! note "Reward"
    **Reward(奖励)**代表着Agent在某个状态$s{\in}{\mathcal{S}}$下，通过执行动作$a_i{\in}{{\mathcal{A}}(s_i)}$转移到其他状态$s’{\in}{\mathcal{S}}$获得的奖励。这个奖励是可以根据训练目标来人为设定的标量。


在现实生活中，环境是随机的。因此在相同状态执行相同动作，获得的回报也不一定相同，因此，获得回报是个概率性时间
（在现实非理想的环境中，在相同状态，执行相同动作也不一定会收获这个概率，因此，我们在状态$s$，执行动作$a$的时候，获取收益$r$的概率可以表示为$p(r|s,a)$。）
## 1.7-Trajectory和Episode

!!! note "Trajectory"
    **Trajectory(轨迹)**是在固定策略 $\pi$ 与环境转移概率 $P(s′|s,a)$ 下，Agent 依次产生的一段状态-动作-奖励链：
    $${s_i}{\xrightarrow[r=r_k]{a_k}}{s_{i+1}}{\xrightarrow[r=r_m]{a_m}}{\dots}$$


## 1.8-Return

!!! note "Return"
    **Return(回报)**是Agent从当前时间$t$所在的状态$s_i{\in}{\mathcal{S}}$开始，在任意一条可能的Trajectory上从$t+1$时刻开始获得的所有未来奖励的总和。


（直接Return相加只适用于有限步数的，我们更多地使用无限步数的Return，那么所有的Return是无限的，就区分不出来哪个策略是好的或者坏的，我们需要使用一种衰减来让Agent实现策略是可以分辨出好坏的，那么对于没有结束的过程的Return，我们使用Discount Return来实现可量化的Return评估）


!!! note "Discount Return"
    **Discount Return(折扣回报)**



!!! question "为什么在强化学习里面用的最多的是Discount Return"
    Contents



## 1.9-Markov Decision Processes

（**未来总回报的价值**只取决于智能体**当前所处的状态**，与过去的历史轨迹无关，这正是MDP的核心马尔可夫性质。因此，智能体为了最大化未来的回报，只需要根据**当前状态**来做出最优决策，从而极大地简化了复杂的学习问题。）
（从我们的Trajectory Chain我们可以发现我们得到的是一系列的）

!!! note "Markov decision processes(重点理解)"
    **Markov decision processes(马尔科夫决策过程)**指的是Agent未来的State只与当前时间$t$的State和从$t+1$时刻开始的未来状态有关，与从$t-1$之前的历史状态无关。

