
# 4-带约束的刚体动力学
## 4.1-刚体的运动约束
### (1)-刚体运动约束的显式表达和隐式表达
刚体的运动约束的表达可以分为**显式**和**隐式**：

- **显式表达**：显式表达的数学形式如下：

$$
{\boldsymbol{q}}={\boldsymbol{\gamma}}(\boldsymbol{y})
$$

其中$\boldsymbol{q}$表示刚体的位置坐标，$\boldsymbol{y}$表示表示系统的 **独立广义坐标**。那么由该显式约束我们可以得到含有速度和加速度的形式：

$$
\dot{\boldsymbol{q}} = \frac{\partial \boldsymbol{\gamma}}{\partial \boldsymbol{y}} \dot{\boldsymbol{y}} = \mathbf{G}(\boldsymbol{y}) \dot{\boldsymbol{y}}{\quad}{{\boldsymbol{\ddot{q}}}={\boldsymbol{G}(\boldsymbol{y}) }\boldsymbol{\ddot{y}}}+{\boldsymbol{g}}
$$

其中$\boldsymbol{G}$为雅各比矩阵，$\boldsymbol{g}$的定义如下：

$$
{{\boldsymbol{g}}={\boldsymbol{\dot{G}}}}({\boldsymbol{y}}){{\boldsymbol{\dot{y}}}}
$$

- **隐式表达**：隐式表达的数学形式定义如下：

$$
{\boldsymbol{\phi}}({\boldsymbol{q}})=0
$$

这里的${\boldsymbol{q}}$表示刚体的位置坐标，该方程在空间中定义了一个几何流形，**限制了刚体所有可能的位形（Position/Orientation）**，即刚体只能在满足该等式的空间内运动。我们可以将隐式约束求导，得到以下含有速度和加速度的形式：

$$
{{\boldsymbol{K}}{\boldsymbol{\dot{q}}}={\boldsymbol{0}}}{\quad}{{\boldsymbol{K}}{\boldsymbol{\ddot{q}}}={\boldsymbol{k}}}
$$

其中：

$$
{\boldsymbol{K}}={\frac{\partial{\boldsymbol{\phi}}}{\partial{\boldsymbol{q}}}}{\quad}{{\boldsymbol{k}}=-{\boldsymbol{\dot{K}}}{\boldsymbol{\dot{q}}}}
$$

### (2)-刚体约束的分类
我们在理论力学里面已经提到过约束的分类，这些分类都有一个特点：**约束的类型都是类似于${\boldsymbol{\phi}}({\boldsymbol{q}})=0$的隐式约束的形式**，对于隐式约束形式 （或不等式形式），我们可以将其分为以下三大类：

- **单边约束 (Unilateral)与双边约束(Bilateral)**：这是根据约束对系统运动方向的**限制范围**来划分的：
	- **单边约束 (Unilateral)**：
	    * **数学形式**：$f(q_1, q_2, \dots, q_n, t) \ge 0$ （不等式约束）。
	    * **物理意义**：质点可以在某一区域内运动，但不能穿过边界，且在某些条件下可以脱离边界。
	    * **例子**：放在桌面上的小球 ($z \ge 0$)，用软绳悬挂的单摆 ($l \le L$)。
	* **双边约束 (Bilateral)**：
	    * **数学形式**：$f(q_1, q_2, \dots, q_n, t) = 0$ （等式约束）。
	    * **物理意义**：质点必须在指定的曲面或曲线上运动，不能离开。
	    * **例子**：圆锥摆中的刚性细杆，滑块在固定的导轨上运动。
- **完整约束(Holonomic)与非完整约束(Non-holonomic)**：这是根据约束方程是否限制了系统的**位形空间（坐标可达性）** 来划分的：
	* **完整约束 (Holonomic)**：
	    * **定义**：只限制系统的位置坐标，其方程可表示为 $f(\boldsymbol{q}, t) = 0$。如果约束包含速度但可以积分还原为坐标关系，也属于完整约束。
	    * **特点**：独立广义坐标的数目等于系统的自由度。
	* **非完整约束 (Non-holonomic)**：
	    * **定义**：约束方程中含有不可积分的速度项，或者约束为单边约束（不等式）。
	    * **例子**：硬币在地面上纯滚动而不打滑。虽然它限制了瞬时速度方向，但并没有限制硬币最终能到达桌面的哪个位置。
- **稳定约束(Scleronomic)与不稳定约束(Rheonomic)**：这是根据约束条件是否随**时间显式变化**来划分的：
	- **稳定约束 (Scleronomic Constraints)**：
		* **定义**：约束条件不随时间改变，约束方程中不显式包含时间 $t$。 
		* **数学表达式**： 
        $$
        \boldsymbol{\phi}(q_1, q_2, \dots, q_n) = 0
        $$
		* **物理直观**：质点运动的轨道、容器或支座在空间中是固定不动的。 
		* **例子**： 
			* 固定在墙上的单摆（摆长 $l$ 不变）。 
			* 小球在固定的碗内滚动。 
			* 刚体各点之间的距离保持不变（$|r_i - r_j| = d_{ij}$）
	- **不稳定约束 (Rheonomic Constraints)**：
		* **定义**：约束条件随时间显式变化，约束方程中显式包含时间 $t$。 
		* **数学表达式**： 
        $$
        \boldsymbol{\phi}(q_1, q_2, \dots, q_n, t) = 0
        $$
		* **物理直观**：限制质点运动的物体本身就在运动或发生形变。 
		* **例子**： 
			* 单摆的悬点正在做周期性上下振动（悬点位置 $y_0 = A \sin(\omega t)$）。 
			* 质点在一段长度随时间不断增长的绳索上运动。 
			* 小球在旋转的直杆上滑动。
我们可以将不同的约束按照**限制范围**，**坐标依赖**和**时间依赖**三点来划分：

| 维度       | 对立类型 A             | 对立类型 B                 |
| :------- | :----------------- | :--------------------- |
| **限制范围** | **双边约束** (等式 $=0$) | **单边约束** (不等式 $\ge 0$) |
| **坐标依赖** | **完整约束** (位置限制)    | **非完整约束** (不可积速度限制)    |
| **时间依赖** | **稳定约束** (不随时间变)   | **不稳定约束** (随时间变)       |


## 4.2-带约束的刚体动力学
### (1)-带约束力的刚体动力学方程

!!! note "带约束的刚体系统的动力学方程表达"
    带约束的刚体系统的动力学方程可以写成以下的**标准形式**：

    $$
    {\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}+{\boldsymbol{\tau_c}}
    $$

    其中：

    - ${\mathbf{q}}$，${\mathbf{\dot{q}}}$，${\mathbf{\ddot{q}}}$代表刚体的位置，速度和加速度。
    - ${\boldsymbol{\tau}}$是作用力的矢量，${\boldsymbol{\tau_c}}$是约束力的矢量
    - ${\mathbf{H}(\mathbf{q})}$是惯量矩阵。
    - ${\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}$是力项的矢量，它表示科里奥利力和离心力，重力，以及作用在系统上的除τ中的力以外的任何其他力。


### (2)-约束力在不同约束下的表示
首先我们回顾一下**若尔当变分定理**：

!!! note "若尔当变分定理"
    对于受理想约束的系统，在给定时刻 $t$ 和给定位置 $\mathbf{r}$，系统的真实运动满足：主动力与惯性力在**虚速度**（速度变分 $\delta \mathbf{v}$）上所作的**虚功率**之和为零，其数学表达式为：

    $$
    \sum_{i=1}^{n} \mathbf{R}_i \cdot \delta \mathbf{v}_i = \sum_{i=1}^{n} (\mathbf{F}_i - m_i \dot{\mathbf{v}}_i) \cdot \delta \mathbf{v}_i = 0
    $$


我们设约束力为$\boldsymbol{\tau_c}$，那么我们根据若尔当变分原理可以得到约束力的功率${\boldsymbol{\tau_c}}{\cdot}{\boldsymbol{\dot{q}}}=0$。我们分别使用显式约束和隐式约束来表示约束力${\boldsymbol{\tau_c}}$：
- **显式约束**：我们根据等式$\dot{\boldsymbol{q}} = \mathbf{G}(\boldsymbol{y}) \dot{\boldsymbol{y}}$以及矢量点乘的交换性质${\boldsymbol{\tau_c}}{\cdot}{\boldsymbol{\dot{q}}}={\boldsymbol{\dot{q}}}{\cdot}{\boldsymbol{\tau_c}}=0$可以得到：

$$
{\boldsymbol{\dot{q}}}{\cdot}{\boldsymbol{\tau_c}}={\boldsymbol{\dot{q}}}^{T}{\boldsymbol{\tau_c}}=\dot{\boldsymbol{y}}^{T}\mathbf{G}(\boldsymbol{y})^{T}{\boldsymbol{\tau_c}}=0 
$$

那么对于任意的$\boldsymbol{y}$来说我们都有：

$$
\mathbf{G}^{T}{\boldsymbol{\tau_c}}=0
$$

- **隐式约束**：给定不含时间的隐式约束：

$$
\boldsymbol{\phi}(\boldsymbol{q}) = 0
$$

对其求全导数，得到速度约束方程：

$$
\frac{d}{dt}\boldsymbol{\phi}(\boldsymbol{q}) = \frac{\partial \boldsymbol{\phi}}{\partial \boldsymbol{q}} \dot{\boldsymbol{q}} = \mathbf{K} \dot{\boldsymbol{q}} = 0
$$

其中 $\mathbf{K}_{m \times n}$ 便是系统的约束雅可比矩阵。在若尔当原理中，我们考虑的是在当前位形 $\boldsymbol{q}$ 和当前速度 $\dot{\boldsymbol{q}}$ 保持不变的情况下，对速度进行变分。受约束的虚速度 $\delta \dot{\boldsymbol{q}}$ 必须满足：$$\mathbf{K} \delta \dot{\boldsymbol{q}} = 0$$这意味着虚速度 $\delta \dot{\boldsymbol{q}}$ 必须位于雅可比矩阵 $\mathbf{K}$ 的**零空间（Null Space）**，由若尔当原理我们可以知道：

$$
{\boldsymbol{\tau_c^{T}}}\delta \dot{\boldsymbol{q}} = 0
$$

根据线性代数中的引理（一个向量如果正交于另一个矩阵的零空间，则该向量必然属于该矩阵转置的列空间）：$\boldsymbol{\tau_c}$ 必须能表示为 $\mathbf{K}$ 转置矩阵的线性组合。因此，引入拉格朗日乘子向量 $\boldsymbol{\lambda} = [\lambda_1, \dots, \lambda_m]^T$，得到：

$$
\boldsymbol{\tau_c} = \mathbf{K}^T \boldsymbol{\lambda}
$$

### (3)-不同约束形式下的刚体运动学方程
- **隐式约束**：我们有约束方程如下：

$$
{\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}+{\boldsymbol{\tau_c}}
$$

其中$\boldsymbol{\tau_c} = \mathbf{K}^T \boldsymbol{\lambda}$，并且带加速度项的约束如下：$$\mathbf{K} \dot{\boldsymbol{q}} = {\boldsymbol{k}}$$那么我们将约束联立可得如下动力学方程，该动力学方程即为在**隐式约束形式的动力学方程**：

$$
\begin{bmatrix}
\boldsymbol{H} & \boldsymbol{K}^{\mathrm{T}} \\
\boldsymbol{K} & 0
\end{bmatrix}
\begin{bmatrix}
\ddot{\boldsymbol{q}} \\
-\boldsymbol{\lambda}
\end{bmatrix} =
\begin{bmatrix}
\boldsymbol{\tau} - \boldsymbol{C} \\
\boldsymbol{k}
\end{bmatrix}
$$
其中

- **显式约束**：我们有约束方程如下：$${\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}+{\boldsymbol{\tau_c}}$$其中$\mathbf{G}^{T}{\boldsymbol{\tau_c}}=0$，并且带加速度项的约束如下：

$$
{{\boldsymbol{\ddot{q}}}={\boldsymbol{G}(\boldsymbol{y}) }\boldsymbol{\ddot{y}}}+{\boldsymbol{g}}
$$

我们联立可得以下的约束方程：

$$
\begin{bmatrix}
\boldsymbol{H} & -\boldsymbol{1} & 0 \\
-\boldsymbol{1} & 0 & \boldsymbol{G} \\
0 & \boldsymbol{G}^{\mathrm{T}} & 0
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{\ddot{q}} \\
\boldsymbol{\tau_c} \\
\boldsymbol{\ddot{y}}
\end{bmatrix} =
\begin{bmatrix}
\boldsymbol{\tau} - \boldsymbol{C }\\
-\boldsymbol{g} \\
0
\end{bmatrix}
$$

将左侧的约束矩阵使用高斯消元法化简成上三角的形式，可以得到**显式约束形式的动力学方程**：

$$
\begin{bmatrix}
\boldsymbol{H} & -\boldsymbol{1} & 0 \\
0 & \boldsymbol{H}^{\mathrm{-1}} & \boldsymbol{G} \\
0 & 0 & -{\boldsymbol{G}^{\mathrm{T}}}{\boldsymbol{H}}{\boldsymbol{G}}
\end{bmatrix}
\begin{bmatrix}
\boldsymbol{\ddot{q}} \\
\boldsymbol{\tau_c} \\
\boldsymbol{\ddot{y}}
\end{bmatrix} =
\begin{bmatrix}
\boldsymbol{\tau} - \boldsymbol{C }\\
{\boldsymbol{H}}^{-1}(\boldsymbol{\tau} - \boldsymbol{C}) - \boldsymbol{g} \\ -\boldsymbol{G}^{\mathrm{T}}(\boldsymbol{\tau} - \boldsymbol{C} - \boldsymbol{Hg})
\end{bmatrix}
$$

我们可以从最后一项中得到一个表达式：

$$
\boldsymbol{G}^{\mathrm{T}}\boldsymbol{HG} \boldsymbol{\ddot{y}} = \boldsymbol{G}^{\mathrm{T}}(\boldsymbol{\tau} - \boldsymbol{C} - \boldsymbol{Hg})
$$

化简成如下形式，我们就得到了显式约束的：

$$
\boldsymbol{H_G \ddot{y}} + \boldsymbol{C_G} = \boldsymbol{u}
$$

其中

$$
{{\boldsymbol{u}}={\boldsymbol{G}^{\mathrm{T}}}{\boldsymbol{\tau}}}{\quad}\boldsymbol{H_G} = \boldsymbol{G^{\mathrm{T}}HG} {\quad} \boldsymbol{C_G} = \boldsymbol{G^{\mathrm{T}}(C + Hg)}
$$

## 4.3-刚体的关节约束
### (1)-矢量子空间的相关知识概念

!!! note "矢量子空间"
    假设我们有一个$n$维的矢量空间$V$，我们定义一个$m$维的子空间${S}{\subseteq}{V}$，那么该子空间$S$的定义如下：
    $${\mathcal{S}}={\{{\mathbf{s}_1},{\mathbf{s}_2},{\mathbf{s}_3},{\dots},{\mathbf{s}_m}\}}$$
    


!!! note "向量分解"
    Contents


!!! note "向量空间的正交补"
    Contents

### (2)-运动子空间和约束力子空间

!!! note "矢量子空间在关节动力学的应用"
    - **空间运动学**：我们已知空间约束的两种形式：显式约束和隐式约束，那么对于这两种约束来说，关节运动的子空间$S$的定义如下：
    	- 对隐式约束来说，关节运动的子空间$\boldsymbol{S}$就是隐式约束的Jacobians矩阵$\boldsymbol{K}$的零空间：$$\boldsymbol{S}=null(\boldsymbol{K}){\subseteq}{M^6}$$
    	- 对显式约束来说，关节运动的子空间$\boldsymbol{S}$就是显式约束的Jacobians矩阵$\boldsymbol{G}$的列空间：$$\boldsymbol{S}=range(\boldsymbol{G}){\subseteq}{M^6}$$
    	- 如果矩阵$\boldsymbol{K}_1$和$\boldsymbol{K}_2$表示同一个约束，那么$null(\boldsymbol{K}_1)=null(\boldsymbol{K}_2)=\boldsymbol{S}$。同理，如果矩阵$\boldsymbol{G}_1$和$\boldsymbol{G}_2$表示同一个约束，那么$range(\boldsymbol{G}_1)=range(\boldsymbol{G}_2)=\boldsymbol{S}$。
    - **空间动力学**：我们定义关节的空间约束力所在的子空间$\boldsymbol{T}={\boldsymbol{S}}^{\perp}$，并且定义关节的空间驱动力$\boldsymbol{T}_a$满足${\boldsymbol{T}}{\oplus}{\boldsymbol{T}_a}={F^{6}}$


### (3)-常见关节类型及其子空间
常见的关节类型以及其对应的变换矩阵，关节位移向量，运动子空间矩阵和约束力子空间矩阵如下：

| 关节类型 (Joint Type)      | 关节变换矩阵 $\mathbf{E}$       | 关节位移向量 $\mathbf{r}$                                                     | 运动子空间矩阵 ($\mathbf{S}$)                                                                                     | 约束力子空间矩阵 ($\mathbf{T}$)                                                                                                                                    |
| :--------------------- | :------------------------ | :---------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **转动关节 (Revolute)**    | $rz(q_1)$                 | $\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$                             | $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}$                                                 | $\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 &0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}$  |
| **移动关节 (Prismatic)**   | $\mathbf{1}_{3 \times 3}$ | $\begin{bmatrix} 0 \\ 0 \\ q_1 \end{bmatrix}$                           | $\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}$                                                 | $\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$ |
| **螺旋关节 (Helical)**     | $rz(q_1)$                 | $\begin{bmatrix} 0 \\ 0 \\ h q_1 \end{bmatrix}$                         | $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ h \end{bmatrix}$                                                 | $\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & -h \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0\end{bmatrix}$ |
| **圆柱关节 (Cylindrical)** | $rz(q_1)$                 | $\begin{bmatrix} 0 \\ 0 \\ q_2 \end{bmatrix}$                           | $\begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 1 & 0 \\ 0 & 0 \\ 0 & 0 \\ 0 & 1 \end{bmatrix}$                         | $\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0\\ 0 & 0 & 0 & 0\\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$                           |
| **平面关节 (Planar)**      | $rz(q_1)$                 | $\begin{bmatrix} c_1q_2 - s_1q_3 \\ s_1q_2 + c_1q_3 \\ 0 \end{bmatrix}$ | $\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$                                                 |
| **球关节 (Spherical)**    | 见 Eq. 4.12                | $\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$                             | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ | $\begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$                                                 |
| **6-DoF 关节 (Free)**    | 见 Eq. 4.12                | $\mathbf{E}^{-1} \begin{bmatrix} q_5 \\ q_6 \\ q_7 \end{bmatrix}$       | $\mathbf{1}_{6 \times 6}$                                                                                  | (空)                                                                                                                                                        |

**Notes:**

* $c_1 = \cos(q_1)$, $s_1 = \sin(q_1)$
* $^{s}X_{p} = \text{rot}(\mathbf{E}) \text{xlt}(\mathbf{r})$
### (4)-球形关节的位姿描述方式
球形关节具有定点旋转的三个自由度，我们一般用**欧拉角**和**四元数**来表示球形关节的位置：

!!! note "欧拉角"
    欧拉角（Euler Angles）是描述刚体在三维空间中取向的最直观方式。其核心思想是将一个复杂的旋转拆解为绕三个坐标轴的连续三次旋转。
    欧拉角通过三个角度（如 $\alpha, \beta, \gamma$）来定义物体坐标系相对于参考坐标系的姿态。
    
    - **旋转顺序**：顺序至关重要（如 $Z-Y-X$ 或 $X-Y-Z$），不同的顺序会导致完全不同的最终姿态。
    - **内在旋转 (Intrinsic)**：绕物体自身的动态轴旋转。
    - **外在旋转 (Extrinsic)**：绕固定的参考坐标轴旋转。
    - **万向节锁 (Gimbal Lock)**：当第二次旋转为 $90^\circ$ 时，第一轴与第三轴重合，丢失一个自由度。
    
    以最常用的 **$Z-Y-X$ 顺规**（常用于航空航天的 Roll-Pitch-Yaw）为例，假设旋转角度分别为 $\phi$ (绕 $z$)、$\theta$ (绕 $y$)、$\psi$ (绕 $x$)：
    单个轴的旋转矩阵为：

    $$
    R_z(\phi) = \begin{bmatrix} \cos\phi & -\sin\phi & 0 \\ \sin\phi & \cos\phi & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}, \quad R_x(\psi) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\psi & -\sin\psi \\ 0 & \sin\psi & \cos\psi \end{bmatrix}
    $$

    组合后的旋转矩阵 $R = R_z R_y R_x$：

    $$
    R = \begin{bmatrix} c_\phi c_\theta & c_\phi s_\theta s_\psi - s_\phi c_\psi & c_\phi s_\theta c_\psi + s_\phi s_\psi \\ s_\phi c_\theta & s_\phi s_\theta s_\psi + c_\phi c_\psi & s_\phi s_\theta c_\psi - c_\phi s_\psi \\ -s_\theta & c_\theta s_\psi & c_\theta c_\psi \end{bmatrix}
    $$

    (注：$c$ 代表 $\cos$，$s$ 代表 $\sin$)


!!! note "四元数"
    在使用欧拉角描述刚体在空间的姿态的时候，难免会引入奇异值。为了解决描述空间姿态出现的奇异值问题，我们引入**四元数**来描述刚体的姿态。
    首先介绍一下四元数(Quaternions)，一个四元数$q$可以表示为一个实数和三个虚数单位$i$，$j$，$k$的线性组合：

    $$
    q=a+bi+cj+dk
    $$

    其中$a$，$b$，$c$，$d$是实数，$a$为实部，$bi+cj+dk$为虚部。四元数的矩阵分别表示左乘矩阵表示$L(q)$和右乘矩阵表示$R(q)$：

    $$ 
    L(q) = 
    \begin{pmatrix} 
    a & -b & -c & -d \\ b & a & -d & c \\ c & d & a & -b \\d & -c & b & a
    \end{pmatrix} 
    \quad
    R(q) = 
    \begin{pmatrix} 
    a & -b & -c & -d \\ b & a & d & -c \\ c & -d & a & b \\d & c & -b & a
    \end{pmatrix}
    $$
    
    如图所示，刚体在绕着过点$O$的旋转轴做定轴旋转运动，向量$\vec{n}$是旋转轴的方向向量，$\theta$是刚体在这段时间内绕轴旋转的角度。我们可以使用下面的单位四元数来表述刚体的姿态：
    
    $$
    \begin{align}q&=[cos(\frac{\theta}{2}),sin(\frac{\theta}{2}){\vec{n}}]\\&=cos(\frac{\theta}{2})+sin(\frac{\theta}{2}){{n}_{x}}{i}+sin(\frac{\theta}{2}){{n}_{y}}{j}+sin(\frac{\theta}{2}){{n}_{z}}{k}\end{align}
    $$

    ![Fig 1-1-9](../../physics/理论力学/img/Fig%201-1-9.png)


!!! note "四元数的运算性质"
    四元数满足的运算包括**加法，减法，乘法，共轭，范数和逆**：
    - **加法**：如果 $q_1 = w_1 + x_1i + y_1j + z_1k$ 和 $q_2 = w_2 + x_2i + y_2j + z_2k$，那么它们的和是：$$ q_1 + q_2 = (w_1 + w_2) + (x_1 + x_2)i + (y_1 + y_2)j + (z_1 + z_2)k $$
    - **减法**：如果 $q_1 = w_1 + x_1i + y_1j + z_1k$ 和 $q_2 = w_2 + x_2i + y_2j + z_2k$，那么它们的差是：$$ q_1 - q_2 = (w_1 - w_2) + (x_1 - x_2)i + (y_1 - y_2)j + (z_1 - z_2)k $$
    - **乘法**：两个四元数${q_1}$和${q_2}$相乘分为左乘和右乘，左乘的形式如下：$${{q_1}{\cdot}{q_2}}=L({q_1}){\mathbf{q_2}}$$右乘的形式如下：$${{q_2}{\cdot}{q_1}}=R({q_1}){\mathbf{q_2}}$$四元数的乘法满足结合律$({q_1}{\cdot}{q_2}){\cdot}{q_3}={q_1}{\cdot}({q_2}{\cdot}{q_3})$和分配律$({q_1}+{q_2}){\cdot}{q_3}={q_1}{\cdot}{q_3}+{q_2}{\cdot}{q_3}$。
    - **共轭**：四元数 $q = w + xi + yj + zk$ 的共轭为： $$ q^* = w - xi - yj - zk $$
    - **范数**：四元数的范数是其大小的度量： $$ \|q\| = \sqrt{w^2 + x^2 + y^2 + z^2} $$ 范数的平方与共轭乘积的关系： $$ qq^* = w^2 + x^2 + y^2 + z^2 = \|q\|^2 $$
    - **逆**：四元数的逆 $q^{-1}$ 的计算公式为： $$ q^{-1} = \frac{q^*}{\|q\|^2} $$


!!! note "欧拉角和四元数之间的相互转换"
    1. 欧拉角 (Z-Y-X) $\rightarrow$ 四元数 设 $\phi, \theta, \psi$ 分别为 Roll, Pitch, Yaw，四元数 $q = [w, x, y, z]$： 
    
    $$ 
    \begin{cases} w = \cos\frac{\phi}{2}\cos\frac{\theta}{2}\cos\frac{\psi}{2} + \sin\frac{\phi}{2}\sin\frac{\theta}{2}\sin\frac{\psi}{2} \\ x = \sin\frac{\phi}{2}\cos\frac{\theta}{2}\cos\frac{\psi}{2} - \cos\frac{\phi}{2}\sin\frac{\theta}{2}\sin\frac{\psi}{2} \\ y = \cos\frac{\phi}{2}\sin\frac{\theta}{2}\cos\frac{\psi}{2} + \sin\frac{\phi}{2}\cos\frac{\theta}{2}\sin\frac{\psi}{2} \\ z = \cos\frac{\phi}{2}\cos\frac{\theta}{2}\sin\frac{\psi}{2} - \sin\frac{\phi}{2}\sin\frac{\theta}{2}\cos\frac{\psi}{2} \end{cases} 
    $$ 
    
    2. 四元数 $\rightarrow$ 欧拉角 (Z-Y-X) 

    $$ 
    \begin{bmatrix} \phi \\ \theta \\ \psi \end{bmatrix} = \begin{bmatrix} \operatorname{atan2}(2(wx + yz), 1 - 2(x^2 + y^2)) \\ \arcsin(2(wy - zx)) \\ \operatorname{atan2}(2(wz + xy), 1 - 2(y^2 + z^2)) \end{bmatrix} 
    $$


### (5)-关节空间速度
我们定义关节空间速度是父连杆(Predecessor)在关节连接处的空间速度与子连杆(Successor)在关节连接处的空间速度之差：
$$
\boldsymbol{v_{\mathrm{J}}} = \boldsymbol{v_s - v_p}
$$
关节空间速度可以写为：
$$
\boldsymbol{v_{\mathrm{J}}} = \boldsymbol{S(q, t) \dot{q} + \sigma(q, t)}
$$
其中：

- $\boldsymbol{S}$是关节运动的子空间矩阵
- $\boldsymbol{\sigma}$是关节运动的偏置速度，也就是当$\boldsymbol{q}=0$时的刚体速度
- $\boldsymbol{q}$和$\boldsymbol{\dot{q}}$是关节的转动角度和转动角度变化率。
如果矩阵$\boldsymbol{S}$不随时间而改变，我们可以将关节的空间速度直接写为：
$$
\boldsymbol{v_{\mathrm{J}}} = \boldsymbol{S(q) \dot{q}}
$$

!!! example "以2-DOF平面机械臂来理解关节空间速度"
    

### (6)-关节空间力
我们让关节的空间约束力所在的子空间$\boldsymbol{T}={\boldsymbol{S}}^{\perp}$，并且定义关节的空间驱动力$\boldsymbol{T}_a$满足${\boldsymbol{T}}{\oplus}{\boldsymbol{T}_a}={F^{6}}$，那么关节的空间力如下：

$$
{\boldsymbol{f}_J}={\boldsymbol{T}_a}{\boldsymbol{\tau}}+{\boldsymbol{T}}{\boldsymbol{\lambda}}
$$

其中${\boldsymbol{\tau}}$为关节驱动力向量，${\boldsymbol{\lambda}}$为关节约束力向量。并且，子空间$\boldsymbol{T}$和$\boldsymbol{T}_a$需要满足以下性质：

$$
\begin{align}
{\boldsymbol{T}^{T}_a}{\boldsymbol{S}}=1\\
{\boldsymbol{T}^{T}}{\boldsymbol{S}}=0
\end{align}
$$

我们令关节空间里的等式两边同时乘以$\boldsymbol{S}^{T}$，那么我们可以得到：

$$
\begin{align}
{\boldsymbol{S}^{T}}{\boldsymbol{f}_J}&={\boldsymbol{S}^{T}}{\boldsymbol{T}_a}{\boldsymbol{\tau}}+{\boldsymbol{S}^{T}}{\boldsymbol{T}}{\boldsymbol{\lambda}}\\
{\boldsymbol{S}^{T}}{\boldsymbol{f}_J}&={\boldsymbol{\tau}}
\end{align}
$$

!!! tip
    因为在关节空间力两边同时乘以关节运动空间${\boldsymbol{S}}$之后，关节空间的约束力一项等于0，因此在后续的建模中，我们只考虑到关节空间的作用力，不考虑关节空间的约束力。


## 4.4-受约束的刚体动力学方程
在一个受约束的刚体中，刚体$i$受到以下几个力：

- 父关节对当前连杆的作用力${\boldsymbol{f}_{Bi}}$
- 所有子连杆对当前连杆的反作用力${\sum}{\boldsymbol{f}_j}$
- 刚体的空间约束内力${\boldsymbol{f}_{ci}}$
- 刚体受到的来自外部的合力${\boldsymbol{f}_{xi}}$（包括重力）
那么我们可以列写出来刚体的空间运动方程如下：

$$
{\boldsymbol{f}_{Bi}}+{\boldsymbol{f}_{ci}}+{\boldsymbol{f}_{xi}}+{{\sum}{\boldsymbol{f}_{j}}}={\boldsymbol{{{\hat{I}}}{{\hat{a}}}+{\hat{v}\times^* \hat{I} \hat{v}}}}
$$

等式两边同时减去外力项$\boldsymbol{f}_{xi}$，可以得到：

$$
{\boldsymbol{f}_{Bi}}+{\boldsymbol{f}_{ci}}+{{\sum}{\boldsymbol{f}_{j}}}={\boldsymbol{{{\hat{I}}}{{\hat{a}}}+{\hat{p}}}}
$$

其中$\boldsymbol{\hat{p}}=\boldsymbol{{\hat{v}\times^* \hat{I} \hat{v}}-{f_{xi}}}$。
