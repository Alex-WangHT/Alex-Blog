## 1.大数定理和蒙特卡洛采样
首先介绍一下**大数定理**：

!!! note "大数定理"
    设 $X_1, X_2, \ldots, X_n$ 是独立同分布（i.i.d.）的随机变量序列，且它们具有有限的期望值（或均值）$\mu$:
    $$E[X_i] = \mu$$
    定义这 $n$ 个随机变量的样本均值 $\bar{X}_n$ 为：
    $$\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$$
    **大数定理**断言：随着样本数量 $n$ 趋于无穷大，样本均值 $\bar{X}_n$ 将**收敛**于期望值 $\mu$。


假设我们开始扔硬币，每次扔完硬币之后，我们都记录下来扔的是正面还是反面，记正面为1，反面为0。在第k次扔硬币的时候，我们都会将前面k次所有的结果取平均值。我们会发现随着我们扔硬币次数k的不断增加，我们前面k次扔硬币的平均值也会回归到扔硬币对应数学期望值。这就是大数定理。
## 2.MC-Based算法
**蒙特卡洛 (MC-Based) 算法**通过**完整的试验 (Episode)** 进行学习。在每个试验结束后，算法会计算**实际获得的**总回报 $G_t$ 作为状态-动作对 $(s, a)$ 价值的样本，并用它来**更新** $Q(s, a)$ 的估计值。由于它使用实际回报而非对未来状态的估计（不自举），因此学习过程具备低偏差性。随后，算法根据更新后的 $Q$ 值，通过**贪婪 (Greedy) 策略**来改进当前的行动策略 $\pi(s) = \arg\max_a Q(s, a)$，并结合 $\epsilon$-贪婪机制来确保对环境的持续探索，如此往复，直至 $Q$ 值和策略收敛到最优。

!!! example "MC Based算法的Python程序实现"
    ```
    ```

## 3.MC-Exploring算法
前面提到的**MC-Based算法**提供了一个很简单的方式去理解在Model-Free的情况下如何求解Action-Value。
但是MC-Based这种方法有一个致命的缺点，就是我从某一个键值对$({s},{a})$开始遍历一整个Episode之后才能返回一个Action-Value。这样大大降低了采样效率。
假设我们根据策略$\pi$有以下的一个采样的Episode：

$$
{s_1}{\xrightarrow[]{a_2}}{s_2}{\xrightarrow[]{a_4}}{s_1}{\xrightarrow[]{a_2}}{s_3}{\xrightarrow[]{a_3}}{s_6}{\xrightarrow[]{a_4}}{s_5}{\xrightarrow[]{a_3}}{\cdots}
$$

我们可以像如下所示这样将上面的Episode分解成多个子Episode，每个子Episode可以看作是一个新的Episode。在走完第一个状态-动作对$(s_1,a_2)$之后，我们以下一个状态-动作对$(s_2,a_4)$为起点的Episode作为一个新的Episode来看待。这些Episode能够用来估计更多的Action-Value。这样我们能够更有效地利用整个Episode的样本。

$$
\begin{align}
{s_1}{\xrightarrow[]{a_2}}{s_2}{\xrightarrow[]{a_4}}{s_1}{\xrightarrow[]{a_2}}{s_3}{\xrightarrow[]{a_3}}{s_6}{\xrightarrow[]{a_4}}{s_5}{\xrightarrow[]{a_3}}{\cdots}&{\quad}{\text{[original episode starting from}(s_1,a_2)]}\\
{s_2}{\xrightarrow[]{a_4}}{s_1}{\xrightarrow[]{a_2}}{s_3}{\xrightarrow[]{a_3}}{s_6}{\xrightarrow[]{a_4}}{s_5}{\xrightarrow[]{a_3}}{\cdots}&{\quad}{\text{[subepisode starting from}(s_2,a_4)]}\\
{s_1}{\xrightarrow[]{a_2}}{s_3}{\xrightarrow[]{a_3}}{s_6}{\xrightarrow[]{a_4}}{s_5}{\xrightarrow[]{a_3}}{\cdots}&{\quad}{\text{[subepisode starting from}(s_1,a_2)]}\\
{s_3}{\xrightarrow[]{a_3}}{s_6}{\xrightarrow[]{a_4}}{s_5}{\xrightarrow[]{a_3}}{\cdots}&{\quad}{\text{[subepisode starting from}(s_3,a_3)]}\\
{s_6}{\xrightarrow[]{a_4}}{s_5}{\xrightarrow[]{a_3}}{\cdots}&{\quad}{\text{[subepisode starting from}(s_6,a_4)]}\\
{s_5}{\xrightarrow[]{a_3}}{\cdots}&{\quad}{\text{[subepisode starting from}(s_5,a_3)]}\\
\end{align}
$$

!!! note "一次访问策略和多次访问策略"
    - **一次访问策略(first-visit strategy)**：一次访问策略就是说，在策略评估步骤中，收集从相同状态-动作对开始的所有事件，然后使用这些事件的平均回报近似动作值。
    - **多次访问策略(every-visit strategy)**：


（引入MC-Exploring算法）

!!! example "MC Exploring算法的Python程序实现"
    ```
    ```

## 4.MC ${\epsilon}$-greedy算法

接下来我们来讨论一下探索性和利用性：

!!! note "Expectation和Exploitation"
    Contents


!!! example "MC ${\epsilon}$-greedy算法的Python程序实现"
    ```
    ```

