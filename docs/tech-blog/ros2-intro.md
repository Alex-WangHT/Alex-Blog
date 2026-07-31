---
title: "ROS2 入门笔记：从节点到话题"
date: "2024-07-28"
tags: [ROS2, 机器人, Python]
description: "记录ROS2基础概念与常用命令，适合初学者快速上手。"
---

# ROS2 入门笔记：从节点到话题

ROS2（Robot Operating System 2）是目前机器人开发中最广泛使用的中间件框架。本文记录一些核心概念和常用命令。

## 核心概念

- **Node（节点）**：ROS2 中最小的计算单元
- **Topic（话题）**：节点间发布/订阅消息的通道
- **Service（服务）**：请求/响应式的同步通信
- **Action（动作）**：适合长时间任务的异步通信

## 常用命令

```bash
# 查看话题列表
ros2 topic list

# 查看节点列表
ros2 node list

# 发布测试消息
ros2 topic pub /chatter std_msgs/String "data: Hello"
```

## 节点示例

```python
import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
```

---

> 后续会补充 launch 文件编写和参数配置等内容。
