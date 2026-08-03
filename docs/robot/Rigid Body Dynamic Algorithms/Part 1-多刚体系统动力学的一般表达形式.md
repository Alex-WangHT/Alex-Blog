# 1-多刚体系统动力学的一般表达形式

!!! note "运动学的任务"
    - **前向动力学（Forward Dynamics）**：根据刚体的受力求解刚体的加速度。
    - **逆向动力学（Inverse Dynamics）**：根据刚体的加速度求解刚体受力。


!!! note "刚体系统的运动方程表达"
    刚体系统的运动方程可以写成以下的**标准形式**：
    
    $$
    {\mathbf{H}(\mathbf{q})}{\mathbf{\ddot{q}}}+{\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}={\boldsymbol{\tau}}
    $$
    
    其中：
    
    - ${\mathbf{q}}$，${\mathbf{\dot{q}}}$，${\mathbf{\ddot{q}}}$代表刚体的位置，速度和加速度变量的矢量。
    - ${\boldsymbol{\tau}}$是作用力的矢量。
    - ${\mathbf{H}(\mathbf{q})}$是惯量项矩阵。
    - ${\mathbf{C}(\mathbf{q},\mathbf{\dot{q}})}$是力项的矢量，它表示科里奥利力和离心力，重力，以及作用在系统上的除τ中的力以外的任何其他力。
