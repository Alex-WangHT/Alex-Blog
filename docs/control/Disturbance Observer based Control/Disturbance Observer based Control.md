# Part.1-扰动观测器设计

> [!NOTE] 参考书目
>- K. Ohnishi, W. Chen, and J. Yang, _Disturbance Observer for Advanced Motion Control with MATLAB / Simulink_.
> - S. Li, J. Yang, W. H. Chen, and X. Chen, _Disturbance Observer-Based Control: Methods and Applications_.
## 1-扰动观测器工作原理

## 2-线性扰动观测器设计

## 3-非线性扰动观测器设计
首先我们有非线性系统如下：
$$
\left\{
{\begin{align}
& {\dot{x}}=f(x)+{g_1}(x)u+{g_2}(x)d\\
&y=h(x)
\end{align}}
\right.
$$
其中$x{\in}{\mathbb{R}^n}$是状态向量，$u{\in}{\mathbb{R}^m}$为控制输入，$d{\in}{\mathbb{R}^l}$为扰动，$y{\in}{\mathbb{R}^s}$为系统输出。$f(x),{g_1}(x),{g_2}(x),h(x)$都是只和$x$有关的非线性平滑函数，扰动我们是未知的。
根据非线性系统的数学表达式，我们可以得到**基本扰动观测器**的形式如下：
$$\dot{\hat{d}} = l(x)[\dot{x} - f(x) - g_1(x)u - g_2(x)\hat{d}]$$
我们可以定义一个**增强扰动观测器**来估计慢变的扰动，这种类型的观测器定义如下：
$$
\begin{cases} 
\dot{z} = -l(x)g_2(x)z - l(x)[g_2(x)p(x) + f(x) + g_1(x)u] \\ 
\hat{d} = z + p(x) 
\end{cases} 
$$
其中：
- **$z$**: 观测器的内部状态变量。
- **$\hat{d}$**: 扰动的估计值（Disturbance estimate）。
- **$f(x), g_1(x), g_2(x)$**: 系统动力学模型中的已知非线性函数。
- **$p(x)$**: 为自定义的非线性函数
- **$l(x)$**: 观测器增益函数，满足 $$l(x) = \frac{\partial p(x)}{\partial x}$$
那么该增强观测器的框图如下：
![增强非线性扰动观测器](NDO-1.png)

> [!NOTE] 内模原理
> Contents

针对于谐波扰动的扰动观测器的框图如下
![增强非线性扰动观测器](NDO-2.png)

## 4-数字扰动观测器设计

## 5-基于卡尔曼滤波器的扰动观测器

## 6-自适应扰动观测器设计

# Part.2-基于扰动观测器的控制

> [!NOTE] 参考书目
> - S. Li, J. Yang, W. H. Chen, and X. Chen, _Disturbance Observer-Based Control: Methods and Applications_.
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

> [!NOTE] 定理1
> Contents

> [!NOTE] 定理2
> Contents

这两个定理告诉我们：扰动观测器能够收敛到信号
**针对Matched Disturbance的NDOBC**

> [!NOTE] 定理3
> Contents

**针对Mismatched Disturbance的NDOBC**
> [!NOTE] 定义：输入状态稳定性（ISS）

> [!NOTE] 局部 ISS 的一个充分条件引理

