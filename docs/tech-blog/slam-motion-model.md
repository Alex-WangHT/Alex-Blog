---
title: "SLAM 中的概率运动模型"
date: "2024-07-25"
tags: [SLAM, 概率论, 机器人]
description: "推导移动机器人里程计运动模型的概率形式，为粒子滤波做准备。"
---

# SLAM 中的概率运动模型

在基于粒子滤波的 SLAM 算法（如 FastSLAM）中，准确的**运动模型**是采样有效粒子的关键。

## 里程计运动模型

给定机器人上一时刻位姿 $x_{t-1} = [x, y, \theta]^T$ 和里程计读数 $u_t = [\delta_{rot1}, \delta_{trans}, \delta_{rot2}]$，预测当前位姿：

$$
\hat{x}_t = x_{t-1} + \delta_{trans} \cos(\theta + \delta_{rot1})
$$

$$
\hat{y}_t = y_{t-1} + \delta_{trans} \sin(\theta + \delta_{rot1})
$$

$$
\hat{\theta}_t = \theta_{t-1} + \delta_{rot1} + \delta_{rot2}
$$

## 概率采样

由于里程计存在噪声，真实位姿服从以预测值为中心的高斯分布：

$$
x_t \sim \mathcal{N}(\hat{x}_t, \Sigma)
$$

其中协方差 $\Sigma$ 通常取对角矩阵，各分量与运动距离成正比。

---

> 下一篇将介绍观测模型和 FastSLAM 算法原理。
