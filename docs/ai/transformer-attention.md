---
title: "Transformer 注意力机制数学推导"
date: "2024-07-20"
tags: [深度学习, Transformer, 注意力机制, 数学]
description: "从零推导 Self-Attention 的数学公式，理解 Q/K/V 的直觉含义。"
---

# Transformer 注意力机制数学推导

Transformer 架构的核心是**自注意力机制（Self-Attention）**，它允许模型在处理序列时直接关注任意位置的信息。

## 基本定义

给定输入序列的嵌入矩阵 $X \in \mathbb{R}^{n \times d_{model}}$，通过三个线性投影得到 Query、Key、Value：

$$Q = X W_Q, \quad K = X W_K, \quad V = X W_V$$

其中 $W_Q, W_K \in \mathbb{R}^{d_{model} \times d_k}$，$W_V \in \mathbb{R}^{d_{model} \times d_v}$。

## Scaled Dot-Product Attention

注意力输出定义为：

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

### 缩放因子 $\sqrt{d_k}$ 的作用

当 $d_k$ 较大时，$QK^T$ 的点积值会呈指数级增长，导致 softmax 进入梯度极小的饱和区。除以 $\sqrt{d_k}$ 可以保持方差稳定：

$$\text{Var}\left(\frac{q \cdot k}{\sqrt{d_k}}\right) = \frac{d_k \cdot \sigma^2}{d_k} = \sigma^2$$

## Multi-Head Attention

使用 $h$ 组不同的投影矩阵并行计算注意力：

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W_O$$

其中每个 head 的维度为 $d_k = d_{model} / h$。

---

> 后续将补充位置编码和 Layer Normalization 的详细推导。
