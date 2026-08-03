
# 5-多刚体系统建模

## 5.1-拓扑结构与表示

首先刚体的拓扑结构可以用具有以下性质的**连接图**来表示：

- 节点代表刚体
- 边代表关节
- 只有一个节点代表刚体的固定基座，其余节点代表刚体的移动刚体
- 该连接图是无向图
- 图是连接的

让我们用$G$来代表任意连接图，连接图$G$的生成树用$G_t$来表示。$G_t$是$G$的一个包含所有节点的子图。每个连接图$G$包含至少一个生成树$G_t$。
如果连接图的拓扑结构是树结构，我们也可以称这个连接图为**连接树**。那么$G_t=G$。
如果对于连接图$G$来说，$N_J{\gt}N_B$的情况下，连接图会有闭环，闭环的数量$N_L=N_J-N_B$。如果系统又运动环，那么就称为**闭环系统**，否则就是**开环系统**。

!!! tip "如果多体系统的连接图$G$的边是有向的，代表什么？"

    - 刚体系统连接图$G$的边有向，在计算上代表从节点的一端到另外一端的顺序，那么在有向连接图$G$中，每条边的起点为父节点，终点为子节点。
    - 如果刚体系统的连接图$G$是无向图，默认关节$i$从刚体$i$的父节点到刚体$i$
    - 在运动学算法中的有向图$G$中，图$G$的边是从父节点指向子节点
    - 在动力学算法中的有向图$G$中，图$G$的边是从子节点指向父节点。 


我们从$0$到$N_B$来编号刚体（其中编号$0$为基座），使用$1$到$N_J$来编号关节，编号规则如下：

- 首先选择一个连接树$G_t$
- 我们让表示基座的刚体节点定义为编号$0$，这个节点作为连接树$G_t$的根节点
- 从$1$到$N_B$来编号剩余的刚体，但是要求节点的编号比父节点的编号要大
- 从$1$到$N_B$来编号边，其中边$i$连接着节点$i$及其父节点
- 使用任意顺序来给剩余的边来编号，从$N_B+1$到$N_J$
- 确保每个刚体获得与其节点编号相同的编号，并且每个关节的编号与边的编号相对应

!!! example "刚体编号的例子"
    Contents


每个关节$i$连接两个刚体，我们认定其中一个刚体作为父连杆，另外一个刚体是作为子连杆。关节本身是从父连杆连接到子连杆。

- 定义关节和刚体变量的关系
- 去分辨关节在系统的连接方式
分辨两个刚体是通过什么方式连接到关节称为**关节的极性**。在结构图中，我们认定关节的极性是从关节的父节点引出箭头到关节的子节点。

首先我们可以用**父连杆表格和子连杆表格**来表示连接图$G$中关节和刚体之间的连接关系：列出父连杆表格$p(i)$和子连杆表格$s(i)$，其中$i$为关节编号。
然后我们从父连杆表格$p(i)$和子连杆表格$s(i)$中可以提取出来以下的量：

- **父母表格**：根据父连杆表格$p(i)$和子连杆表格$s(i)$来推导出父节点列表$\lambda(i)$:

$$
\lambda(i)={\min}(p(i),s(i)){\quad}{(1{\leq}i{\leq}N_B)}
$$

如果$i=s(i)$，那么我们认定在连接树中式前向传播的，如果$i=p(i)$，那么关节$i$是反向传播的。

- **刚体$i$路径集合${\kappa}(i)$**：除了基座($i=0$)，${\kappa}(i)$是连接树$G_t$里从基座到刚体$i$的路径上所有的节点的集合。
- **刚体$i$的子刚体集合${\mu}(i)$**：刚体$i$的子刚体节点集合
- **刚体$i$的子树节点集合${\nu}(i)$**：以刚体$i$为根节点的子树的所有节点的集合

## 5.2-Modified D-H表达法
Modified D-H表达法常用于开链的机械臂结构的运动学几何描述，首先我们按照如下步骤来为机械臂上面的$n$个关节创建坐标系：

1. 首先我们需要定义好$\mathcal{Frame}\{0\}$坐标系和$\mathcal{Frame}\{n+1\}$坐标系，其中$\mathcal{Frame}\{0\}$坐标系是**基座坐标系**$\mathcal{Frame}\{B\}$，$\mathcal{Frame}\{n+1\}$坐标系是**工具坐标系**$\mathcal{Frame}\{T\}$。
2. 按照关节标号$1$到$n$来依次建立$\mathcal{Frame}\{1\}$坐标系和$\mathcal{Frame}\{n\}$坐标系，首先我们需要定义好$z_i$，$z_i$的位置与关节运动的轴线重合，$z_i$的方向以关节的旋转方向为右手旋转方向，右手大拇指的朝向即为关节的朝向。
3. 然后定义关节坐标系$\mathcal{Frame}\{i\}$的$x_i$方向，有以下三种情况：

	- **$z_i$ 与 $z_{i+1}$ 相交**：
	    - **定义**：$x_i$ 轴取在两条轴线交点处，且垂直于 $z_i$ 和 $z_{i+1}$ 所在的平面。    
	    - **方向**：通常选为 $x_i = z_i \times z_{i+1}$ 或 $x_i = z_{i+1} \times z_i$（需保持全机建模方向的一致性）。   
	- **$z_i$ 与 $z_{i+1}$ 平行**：
	    - **定义**：由于平行线之间有无数条公垂线，$x_i$ 的位置不唯一。
	    - **方向**：通常选择 $x_i$ 位于通过前一个坐标系原点且垂直于 $z_{i+1}$ 的公垂线上。为了简化计算，常令 $x_i$ 的方向与 $x_{i-1}$ 保持一致，从而使连杆偏移量 $d_i = 0$。
	- **$z_i$ 与 $z_{i+1}$ 异面（既不平行也不相交）**：
	    - **定义**：$x_i$ 轴严格重合于 $z_i$ 与 $z_{i+1}$ 之间唯一的公垂线。
	    - **方向**：方向定义为从 $z_i$ 指向 $z_{i+1}$，其矢量方向满足 $x_i = z_i \times z_{i+1}$ 的几何指向。
4. 最后根据右手定则$y_i=z_i\times x_i$来确定关节坐标系$\mathcal{Frame}\{i\}$的$y_i$方向
接下来我们可以使用Modified D-H参数来描述上面定义的坐标系统，在 **Modified D-H (改进型 D-H)** 表达法中，两个相邻坐标系 $\mathcal{Frame}\{i-1\}$ 到 $\mathcal{Frame}\{i\}$ 之间的相对位置关系由以下四个参数定义：
- **连杆转角 $\alpha_{i-1}$ (Link Twist)**：绕 $x_{i-1}$ 轴，从 $z_{i-1}$ 旋转到 $z_i$ 的角度。
- **连杆长度 $a_{i-1}$ (Link Length)**：沿 $x_{i-1}$ 轴，从 $z_{i-1}$ 到 $z_i$ 的距离（即两轴线之间的公垂线长度）。
- **关节角 $\theta_i$ (Joint Angle)**：绕 $z_i$ 轴，从 $x_{i-1}$ 旋转到 $x_i$ 的角度。
- **连杆偏移 $d_i$ (Link Offset)**：沿 $z_i$ 轴，从 $x_{i-1}$ 到 $x_i$ 的距离。

## 5.3-多刚体运动学方程
### (1)-关节空间基向量的坐标变换
我们定义空间中有一个坐标系${\mathcal{Frame}\{i\}}$，关节$i$的中心点即为坐标系${\mathcal{Frame}\{i\}}$的原点。并且关节$i$的关节运动子空间的基向量在坐标系${\mathcal{Frame}\{i\}}$中定义为$^{i}\mathbf{S}_i$。我们在另外的坐标系${\mathcal{Frame}\{W\}}$中可以得到关节$i$的空间基向量可以表示为

$$
{{^{W}\mathbf{S}}_i}={{^{W}_i\mathbf{X}}}{{^{i}\mathbf{S}}_i}
$$

其中${{^{W}_i\mathbf{X}}}$是从${\mathcal{Frame}\{i\}}$到${\mathcal{Frame}\{W\}}$的空间坐标转换矩阵
### (2)-多刚体系统的速度表示
我们定义刚体$i$的空间速度为$\boldsymbol{v}_i$，刚体关节$i$的空间速度$\boldsymbol{v}_{Ji}$。首先我们可以在坐标系${\mathcal{Frame}\{W\}}$定义刚体$\boldsymbol{v}_i$的速度如下：

$$
{\boldsymbol{^{W}{v}}_i}=\boldsymbol{^{W}{v}}_{{\lambda}(i)}+\boldsymbol{^{W}{v}}_{Ji}
$$

我们默认$i=0$的时候，刚体$0$为固定基座，因此$\boldsymbol{v}_0=0$，那么上式可以写成如下形式：

$$
\boldsymbol{^{W}{v}}_i = \sum_{j \in \kappa(i)} \boldsymbol{^{W}{v}}_{\mathrm{J}j}
$$

我们定义刚体$i$的速度如下：

$$
{\boldsymbol{{^{W}{v}}_i}}={\boldsymbol{{{^{W}{J}}_{i}}(q)}}{\dot{\boldsymbol{q}}}
$$

### (3)-多刚体系统的加速度表示
我们在坐标系${\mathcal{Frame}\{W\}}$定义刚体$i$的加速度如下：

$$
{\boldsymbol{{^{W}{a}}_i}}={\boldsymbol{{{^{W}\dot{J}}_{i}}(q)}}{\dot{\boldsymbol{q}}}+{\boldsymbol{{{^{W}{J}}_{i}}(q)}}{\ddot{\boldsymbol{q}}}
$$

## 5.4-多刚体动力学方程
### (1)-带空间约束的力学方程推导
- **单独列出来n个刚体的独立动力学方程**：我们已知有$N_B$个刚体，其中每个刚体的独立表达式为${\boldsymbol{{f}}_i}={\boldsymbol{{I_i}{{a}}}_i}+{\boldsymbol{{p}}_i}$。那么我们先将这$N_B$个独立的刚体的表达式写作一整个表达式：

$$
\begin{bmatrix}
\boldsymbol{f}_1 \\
\boldsymbol{f}_2 \\
\vdots \\
\boldsymbol{f}_{N_B}
\end{bmatrix}
=
\begin{bmatrix}
\boldsymbol{I}_1 & \mathbf{0} & \cdots & \mathbf{0} \\
\mathbf{0} & \boldsymbol{I}_2 & \cdots & \mathbf{0} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{0} & \mathbf{0} & \cdots & \boldsymbol{I}_{N_B}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{a}_1 \\
\boldsymbol{a}_2 \\
\vdots \\
\boldsymbol{a}_{N_B}
\end{bmatrix}
+
\begin{bmatrix}
\boldsymbol{p}_1 \\
\boldsymbol{p}_2 \\
\vdots \\
\boldsymbol{p}_{N_B}
\end{bmatrix}
$$

上式也可以直接写成如下的运动学形式：

$$
{\boldsymbol{{f}}}={\boldsymbol{{I}{{a}}}}+{\boldsymbol{{p}}}
$$

- **由刚体关节角度表达到刚体空间运动表达**：
- **从刚体的空间力到关节的空间力**：
- **加入运动约束**：
- **列出约束力**：
最终，这种带有约束项的多刚体系统动力学方程的形式如下：

$$
\begin{bmatrix}
\boldsymbol{I} & \boldsymbol{P} \boldsymbol{T} \\
\boldsymbol{T}^{\text{T}} \boldsymbol{P}^{\text{T}} & \boldsymbol{0}
\end{bmatrix} 
\begin{bmatrix}
\boldsymbol{a} \\
-\boldsymbol{\lambda}
\end{bmatrix} = 
\begin{bmatrix}
\boldsymbol{P} \boldsymbol{T}_{\boldsymbol{a}} \boldsymbol{\tau} - \boldsymbol{p} \\
-\dot{\boldsymbol{T}}^{\text{T}} \boldsymbol{P}^{\text{T}} \boldsymbol{v}
\end{bmatrix}
$$

### (2)-求解多刚体系统动力学的一般步骤
如果我们已知下面的条件：

- 刚体系统连接图$G$的拓扑结构。
- 刚体系统的Modified D-H参数。
- 刚体系统中每个刚体的质心相对于关节连接处的位置，刚体相对于质心的惯量矩和刚体重量。
那么我们可以列写出来不受约束的多刚体系统的动力学方程，可以分为以下几个步骤：

- **根据拓扑结构和Modified D-H参数写出各个关节相对于参考坐标系的转换矩阵**
- **写出来每个刚体关于参考坐标系的空间惯量矩阵**
- **根据空间惯量矩阵写出Jacobians矩阵，并且求解速度和加速度**
- **根据空间惯量矩阵，速度，加速度来列些动力学方程${\boldsymbol{{f}}}={\boldsymbol{{I}{{a}}}}+{\boldsymbol{{p}}}$**
- **将带Jacobians项的速度，加速度方程以及力的映射$\boldsymbol{f}=\boldsymbol{J}(\boldsymbol{q})\dot{\boldsymbol{q}}$导入空间动力学方程${\boldsymbol{{f}}}={\boldsymbol{{I}{{a}}}}+{\boldsymbol{{p}}}$，最终求解动力学方程${\boldsymbol{H}}{\ddot{\boldsymbol{q}}}+{\boldsymbol{C}}={\boldsymbol{\tau}}$**
## 5.5-多刚体系统的总动能
首先，多刚体系统的动能表示如下：

$$
{T}={\frac{1}{2}}{\sum_{k=1}^{N_B}}{{\boldsymbol{\hat{v_k}}}^T}{\boldsymbol{\hat{I_k}}}{\boldsymbol{\hat{v_k}}}
$$

并且根据多刚体运动学方程，我们有：

$$
{\boldsymbol{\hat{v}}_k}={\sum_{{i}{\in}{{\kappa}(k)}}}{\boldsymbol{S}_i}{\boldsymbol{\dot{q_i}}}
$$

那么代入上式我们表达多刚体系统的动能如下：

$$
\begin{align}
{T}&={\frac{1}{2}}{\sum_{k=1}^{N_B}}{\sum_{{j}{\in}{{\kappa}(k)}}}{\sum_{{i}{\in}{{\kappa}(k)}}}{{\boldsymbol{\dot{q}_i^T}}{\boldsymbol{S}_i^T}}{\boldsymbol{\hat{I_k}}}{\boldsymbol{S}_j}{\boldsymbol{\dot{q}_j}}\\
&={\frac{1}{2}}{\sum_{i=1}^{N_B}}{\sum_{j=1}^{N_B}}{\boldsymbol{\dot{q}_i^T}}({\sum_{k{\in}{\nu}(i){\cap}{\nu}(j)}}{\boldsymbol{S}_i^T}{\boldsymbol{\hat{I_k}}}{\boldsymbol{S}_j}){\boldsymbol{\dot{q}_j}}\\
&={\frac{1}{2}}{\sum_{i=1}^{N_B}}{\sum_{j=1}^{N_B}}{\boldsymbol{\dot{q}_i^T}}{\boldsymbol{H}_{ij}}{\boldsymbol{\dot{q}_j}}
\end{align}
$$

其中：

$$
{\boldsymbol{H}_{ij}}={\sum_{k{\in}{\nu}(i){\cap}{\nu}(j)}}{\boldsymbol{S}_i^T}{\boldsymbol{\hat{I_k}}}{\boldsymbol{S}_j}{\quad}{\quad}
{\nu(i) \cap \nu(j) = \begin{cases} \nu(i) & \text{if } i \in \nu(j) \\ \nu(j) & \text{if } j \in \nu(i) \\ \emptyset & \text{otherwise} \end{cases}}
$$

## 5.6-多刚体系统的复合惯性矩
在多体动力学中，**复合刚体惯量 $\boldsymbol{I}_i^c$** 指的是：假设刚体 $i$ 及其所有子孙节点（Descendants）所属的刚体全部“固连”在一起，形成一个单一的复合刚体时，该整体在空间中相对于刚体 $i$ 坐标系的等效空间惯量。
根据 5.5 节中推导出的 $\boldsymbol{H}_{ij}$，我们可以定义复合刚体惯量矩阵 $\boldsymbol{I}_i^c$ 为：

$$
{\boldsymbol{I}_i^c} = \sum_{k \in \nu(i)} \boldsymbol{\hat{I}}_k
$$

其中 $\nu(i)$ 是以 $i$ 为根节点的子树中所有节点的集合。这意味着 $\boldsymbol{H}_{ij}$ 的计算可以简化为：
- 若 $i$ 是 $j$ 的祖先（$i \in \kappa(j)$），则有：

$$
\boldsymbol{H}_{ij} = \boldsymbol{S}_i^T \left( \sum_{k \in \nu(j)} \boldsymbol{\hat{I}}_k \right) \boldsymbol{S}_j = \boldsymbol{S}_i^T \boldsymbol{I}_j^c \boldsymbol{S}_j
$$

- 利用对称性，若 $j$ 是 $i$ 的祖先，则 $\boldsymbol{H}_{ij} = \boldsymbol{H}_{ji}^T$。
那么${\boldsymbol{H}_{ij}}$表示如下：

$$
\boldsymbol{H}_{ij} = \begin{cases} 
\boldsymbol{S}_i^{\mathrm{T}} \boldsymbol{I}_i^{\mathrm{c}} \boldsymbol{S}_j & \text{if } i \in \nu(j) \\ 
\boldsymbol{S}_i^{\mathrm{T}} \boldsymbol{I}_j^{\mathrm{c}} \boldsymbol{S}_j & \text{if } j \in \nu(i) \\ 
\mathbf{0} & \text{otherwise.} 
\end{cases}
$$

## 5.7-浮动基座系统的动力学建模方法
### (1)-浮动基座系统的运动学
首先，我们将浮动基座系统的浮动基座记为刚体$1$，剩下的刚体的编号是从$2$到$N_B+1$。
### (2)-浮动基座的动力学建模
首先，我们可以仿照固定基座的多体动力学的形式，将浮动基座动力学的一般形式如下：

$$
\begin{bmatrix}
\mathbf{H}_{11} & \mathbf{H}_{1*} \\
\mathbf{H}_{*1} & \mathbf{H}_{**}
\end{bmatrix}
\begin{bmatrix}
\mathbf{\ddot{q}}_1 \\
\mathbf{\ddot{q}}_*
\end{bmatrix} +
\begin{bmatrix}
\mathbf{C}_1 \\
\mathbf{C}_*
\end{bmatrix}
 =
\begin{bmatrix}
\mathbf{\tau}_1 \\
\mathbf{\tau}_*
\end{bmatrix}
$$

在前面推导浮动基座系统的运动学的时候，我们推导出来如下的规律：

$$
\begin{matrix}
{\boldsymbol{\dot{{q}}_1}={\boldsymbol{v_1}}}&{\boldsymbol{\ddot{{q}}_1}={\boldsymbol{a_1}}}
\end{matrix}
$$

由于虚拟关节$1$的运动子空间$\boldsymbol{S}_1={\boldsymbol{1}_{6\times6}}$，那么虚拟关节$1$的关节力$\boldsymbol{f}_1$和$\boldsymbol{\tau}_1$的关系如下：

$$
{\boldsymbol{\tau}_1}={\boldsymbol{S}^{T}_{1}}{\boldsymbol{f}_1}={\boldsymbol{f}_1}
$$

对于浮动基座来说，在本质上虚拟关节的空间关节力${\boldsymbol{f}_1}$和刚体本身受到的其它外部力组成的合力$\boldsymbol{f}_{ext1}$一样都是由刚体外部施加的外力。我们可以将其合并为整体的外力项${\boldsymbol{f}_{x1}}={\boldsymbol{f}_1}+\boldsymbol{f}_{ext1}$。但是等式右边的关节力$\tau_1$作为基座$0$通过刚体向基座$1$传递力，并且在实际物理系统中，${\boldsymbol{f}_{1}}$只是外力的一部分，那么我们令关节力$\tau_1$为0。
我们假设浮动基座的复合刚体空间惯量为${\boldsymbol{I}^{c}_1}$，那么${\boldsymbol{H}_{11}}$和如下：

$$
{\boldsymbol{H}_{11}}={\boldsymbol{S}^{T}_{1}}{\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{1}}={\boldsymbol{I}^{c}_1}{\quad}{{\boldsymbol{H}_{1i}}={\boldsymbol{S}^{T}_{1}}{\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{i}}={\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{i}}
}
$$

我们将上面的$\boldsymbol{H}_{1*}$改写成$\boldsymbol{F}$，其中：

$$
{\boldsymbol{F}}=[{\boldsymbol{F}_1},{\boldsymbol{F}_2},{\boldsymbol{F}_3},{\cdots}{\boldsymbol{F}_{N_B}}]
$$

其中${\boldsymbol{F}_{i}}={\boldsymbol{I}^{c}_1}{\boldsymbol{S}_{i}}$，$\boldsymbol{F}_i$代表
然后，我们将基座的空间惯量，加速度和偏置力重新写为$\boldsymbol{I}_0^c$，$\boldsymbol{a}_0$和$\boldsymbol{p}_0^c$。那么浮动基座的多体动力学如下：

$$
\begin{bmatrix}
\boldsymbol{I}_{0}^{c} & \boldsymbol{F} \\
\boldsymbol{F}^{T} & \boldsymbol{H}_{**}
\end{bmatrix} \begin{bmatrix}
\boldsymbol{a}_{0} \\
\ddot{\boldsymbol{q}}_{*}
\end{bmatrix} + \begin{bmatrix}
\boldsymbol{p}_{0}^{c} \\
\boldsymbol{C}_{*}
\end{bmatrix} = \begin{bmatrix}
\mathbf{0} \\
\boldsymbol{\tau}_{*}
\end{bmatrix}
$$

我们将浮动基座的多体动力学方程组写成如下形式：

$$
\left\{
{\begin{align}
&{\boldsymbol{I}_0^c}{{\boldsymbol{a}_0}}+{\boldsymbol{F}}{\boldsymbol{\ddot{q}}}+{\boldsymbol{p}_0^c}=\boldsymbol{0}\\
&{\boldsymbol{F}^T}{{\boldsymbol{a}_0}}+{\boldsymbol{H}_{**}}{\boldsymbol{\ddot{q}}_*}+{\boldsymbol{C}_*}=\boldsymbol{\tau}_{*}\\
\end{align}}
\right.
$$

方程组中的第一个方程是**浮动基座的动力学方程**，其中：

- ${\boldsymbol{I}_0^c}{{\boldsymbol{a}_0}}$表示浮动基座平台的加速度合力，该项是将整个系统（基座+机械臂）视为一个瞬时刚体时，产生整体空间加速度 $\boldsymbol{a}_0$ 所需的惯性力/力矩。
- ${\boldsymbol{F}}{\boldsymbol{\ddot{q}}}$代表着机械臂的关节加速度传导到浮动基座平台上的合力。
- ${\boldsymbol{p}_0^c}$代表浮动基座平台的偏置力，包括重力，科氏力，浮动基座的驱动力以及其他外部的干扰合力，这里的力都是非加速度项。
方程组中的第二个方程是**机械臂本身的动力学方程**，其中：
- ${\boldsymbol{F}^T}{\boldsymbol{a}_0}$是浮动基座在加速运动的时候传导到机械臂各个刚体上的空间力
- ${\boldsymbol{H}_{**}}{\boldsymbol{\ddot{q}}_*}$是机械臂各个刚体转动的的力
- ${\boldsymbol{C}_*}$是机械臂每个刚体的偏置力
- ${\boldsymbol{\tau}_*}$是机械臂上各个关节提供的空间力