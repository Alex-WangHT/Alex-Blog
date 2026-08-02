# 1-2、刚体一般运动学方程
#### 1-刚体定点运动的无限小量
我们假设在1-1的第四部分描述的刚体旋转了一个很小的角度$\Delta{\theta}{\to}{0}$，根据三角函数在原点附近的一阶泰勒展开$cos({\Delta{\theta}}){\sim}{1}$和$\sin({\Delta{\theta}}){\sim}{\Delta{\theta}}$，可以将罗德里格斯公式写成以下形式：
$$
{R}={I}+{\Delta{\theta}}{[p{\times}]}={I}+[{\omega}{\times}]
$$
我们在这里暂时将$[{{\omega}}{\times}]$记作刚体定点运动的无限小量，其中：
$$
[{\omega}{\times}]=
\begin{pmatrix}
{0}&-{\Delta{\theta}}{p_z}&{\Delta{\theta}}{p_y}\\
{\Delta{\theta}}{p_z}&0&-{\Delta{\theta}}{p_x}\\
-{\Delta{\theta}}{p_y}&{\Delta{\theta}}{p_x}&0\\
\end{pmatrix}
$$
#### 2-刚体定点运动的角速度和角加速度
我们假设在很短的时间$\Delta{t}$内转动了一个很小的角度$\Delta{\theta}$，即：
$$
{\lim_{\Delta{t}{\to}{0}}}{\frac{\Delta{\theta}}{\Delta{t}}}=\dot{\theta}
$$
那么刚体定点运动的无穷小量可以写为：
$$
[{\omega}{\times}]=
\begin{pmatrix}
{0}&-{\dot{\theta}}{p_z}&{\dot{\theta}}{p_y}\\
{\dot{\theta}}{p_z}&0&-{\dot{\theta}}{p_x}\\
-{\dot{\theta}}{p_y}&{\dot{\theta}}{p_x}&0\\
\end{pmatrix}={[{\dot{\theta}}p{\times}]}
$$
根据上式我们可以得到刚体的角速度如下，其中${\vec{p}}$是刚体定点旋转的瞬时旋转单位轴：
$$
\vec{\omega}={\dot{\theta}}{\vec{p}}
$$
对刚体角速度求导，得到加速度如下：
$$
\vec{\epsilon}=\dot{\vec{\omega}}={\ddot{\theta}}{\vec{p}}+{\dot{\theta}}{\dot{\vec{p}}}
$$

!!! tip "刚体的角速度在刚体有限转动的不同表示下的描述"
    - **旋转矩阵**：我们设旋转前刚体B的固连坐标系$\{B\}$的基向量为$\vec{x}$，$\vec{y}$，$\vec{z}$，在以固连坐标系原点$O_B$做很短时间定点运动后的基向量为$\dot{\vec{x}}$，$\dot{\vec{y}}$，$\dot{\vec{z}}$。我们可以得到：$$\left\{ \begin{align}&{\dot{\vec{x}}}={[\omega{\times}]}{\vec{x}}\\&{\dot{\vec{y}}}={[\omega{\times}]}{\vec{y}}\\&{\dot{\vec{z}}}={[\omega{\times}]}{\vec{z}}\end{align}\right.$$根据旋转矩阵的定义我们可以得到：$$\dot{R}={[\omega{\times}]}{R}$$根据旋转矩阵正交的性质$R{R^T}=I$我们可以得到：$${\dot{R}}{R^T}={[\omega{\times}]}$$
    - **欧拉角和卡尔丹角**
    - **四元数**

#### 3-刚体定点运动的线速度和线加速度
在刚体绕着定点转动的时候，刚体上的某一点在惯性参考坐标系上的绕着转动前的向量$\vec{r}$和转动后的向量$\vec{r}^{'}$的关系如下：
$$
\vec{r}^{'}=R\vec{r}={\vec{r}}+{[\omega{\times}]}{\vec{r}}
$$
即：
$$
\Delta{\vec{r}}=\vec{r}^{'}-\vec{r}={[\omega{\times}]}{\vec{r}}
$$
因为在很短的时间$\Delta{t}{\to}{0}$运动的，因此我们可以得到刚体的某一点绕定点运动的线速度如下：
$$
\vec{v}=\dot{\vec{r}}={\vec{\omega}}{\times}{\vec{r}}
$$
对上面绕定点运动的线速度进行求导即可获得绕定点运动的加速度：
$$
\vec{a}=\ddot{\vec{r}}=\dot{\vec{\omega}}{\times}{\vec{r}}+{\vec{\omega}}{\times}{\dot{\vec{r}}}={\vec{\epsilon}}{\times}{\vec{r}}+{\vec{\omega}}{\times}({\vec{\omega}}{\times}{\vec{r}})
$$
#### 4-刚体一般运动的描述
我们在理论力学里面有一个结论：**刚体一般运动是由刚体平动和刚体绕某个点做定点运动合成得到的**。那么根据这个结论，我们将刚体的一般运动分为刚体质心在空间的平动以及刚体绕着质心定点运动。
刚体在空间相对于惯性参考坐标系$\{O\}$进行一般运动如上图所示，其中坐标系$\{B\}$是刚体的固连坐标系，$O_{C}$是刚体的质心。刚体内一点P在参考坐标系$\{O\}$的位置表示如下：
$$
{^{O}}{\vec{r}}_{P}={^{O}}{\vec{r}}_{C}+{^{O}}{R}{_{B}}{^{B}}{\vec{\rho_{P}}}
$$
我们对上面的式子进行求导，可以得到刚体内某一点的线速度：
$$
{^{O}}{\vec{v}}_{P}={^{O}}{\dot{\vec{r}}}_{P}={^{O}}{\dot{\vec{r}}}_{C}+{^{O}}{\vec{\omega}_{B}}{\times}{^{O}}{\vec{\rho_{P}}}
$$
对上面的式子再次求导，我们可以得到刚体内某一点的加速度：
$$
{^{O}}{\vec{a}}_{P}={^{O}}{\ddot{\vec{r}}}_{P}={^{O}}{\ddot{\vec{r}}}_{C}+{^{O}}{\vec{\epsilon}_{B}}{\times}{^{O}}{\vec{\rho_{P}}}+{^{O}}{\vec{\omega}_{B}}{\times}({^{O}}{\vec{\omega}_{B}}{\times}{^{O}}{\vec{\rho_{P}}})
$$

!!! tip "刚体各个运动类型的运动描述"
    我们已知刚体的运动类型包括平动，定轴转动，平面运动，定点运动和一般运动五类，其中：
    - 定轴运动是定点运动的特例
    - 平面运动是一般运动的特例
    - 平动是平面运动的特例

#### 5-多刚体的复合运动描述
【使用旋转矩阵的相关性质来证明角速度复合定理】
【1.罗德里格斯推导角速度矩阵和旋转矩阵的关系】
【2.罗德里格斯推导角速度矩阵与旋转矩阵的乘法】
【3.用性质证明角速度合成定理】

# 二、多体系统的动力学分析

## 2-2、动力学普遍方程
### 2-2-1、微分变分原理

### 2-2-2、达朗贝尔-拉格朗日原理

### 2-2-3、若尔当原理

!!! example "使用若尔当定理来推导刚体定点运动的欧拉方程"
    Contents

### 2-2-4、高斯原理