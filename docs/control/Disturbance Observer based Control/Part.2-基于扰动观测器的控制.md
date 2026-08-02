
!!! note "参考书目"
    - S. Li, J. Yang, W. H. Chen, and X. Chen, _Disturbance Observer-Based Control: Methods and Applications_.

## 1-基于扰动观测器的非线性系统设计
首先我们有SISO非线性系统如下：

$$
\left\{
{\begin{align}
& {\dot{x}}=f(x)+{g_1}(x)u+{g_2}(x)d\\
&y=h(x)
\end{align}}
\right.
$$

其中$x{\in}{\mathbb{R}^n}$是状态向量，$u{\in}{\mathbb{R}}$为控制输入，$d{\in}{\mathbb{R}}$为扰动，$y{\in}{\mathbb{R}}$为系统输出。
非线性系统的框图如下：

**首先，是关于扰动观测器的两个定理**：

!!! note "定理1"
    Contents


!!! note "定理2"
    Contents


这两个定理告诉我们：扰动观测器能够收敛到信号
**针对Matched Disturbance的NDOBC**

!!! note "定理3"
    Contents


**针对Mismatched Disturbance的NDOBC**

!!! note "定义：输入状态稳定性（ISS）"


!!! note "局部 ISS 的一个充分条件引理"


