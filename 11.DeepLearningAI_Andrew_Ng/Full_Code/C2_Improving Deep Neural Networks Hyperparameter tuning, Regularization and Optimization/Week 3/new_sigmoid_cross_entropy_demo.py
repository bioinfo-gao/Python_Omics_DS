"""
Sigmoid Cross Entropy Calculation Demo
演示 sigmoid_cross_entropy_with_logits 的中间计算过程
"""

import tensorflow as tf
import numpy as np

def cost_with_intermediate_values(logits, labels):
    """
    计算 sigmoid cross entropy 并显示中间值
    
    参数:
    logits -- 输入值 (未经过 sigmoid 激活)
    labels -- 真实标签 (0 或 1)
    
    返回:
    cost -- 计算出的损失值
    """
    print("=== Sigmoid Cross Entropy 计算过程 ===")
    print(f"输入 logits: {logits}")
    print(f"输入 labels: {labels}")
    print()
    
    # 转换为 TensorFlow 张量
    z = tf.cast(logits, tf.float32)
    y = tf.cast(labels, tf.float32)
    
    print("转换后的张量:")
    print(f"z (logits): {z.numpy()}")
    print(f"y (labels): {y.numpy()}")
    print()
    
    # 计算 sigmoid cross entropy
    cost_tensor = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
    cost_value = cost_tensor.numpy()
    
    print("计算过程详情:")
    for i in range(len(logits)):
        z_i = z[i].numpy()
        y_i = y[i].numpy()
        
        # 手动计算 sigmoid cross entropy
        # 公式: max(z, 0) - z * y + log(1 + exp(-abs(z)))
        term1 = max(z_i, 0)  # max(z, 0)
        term2 = z_i * y_i    # z * y
        term3 = np.log(1 + np.exp(-abs(z_i)))  # log(1 + exp(-|z|))
        
        manual_cost = term1 - term2 + term3
        
        print(f"样本 {i}:")
        print(f"  z = {z_i:.4f}, y = {y_i:.4f}")
        print(f"  max(z,0) = {term1:.4f}")
        print(f"  z*y = {term2:.4f}")
        print(f"  log(1+exp(-|z|)) = {term3:.4f}")
        print(f"  手动计算 cost = {term1:.4f} - {term2:.4f} + {term3:.4f} = {manual_cost:.4f}")
        print(f"  TensorFlow cost = {cost_value[i]:.4f}")
        print()
    
    return cost_value

def demonstrate_specific_calculation():
    """演示用户指定的具体计算"""
    
    print("=== 用户指定的具体计算 (0.2 和 1) ===")
    
    # 用户提供的输入
    logits = np.array([0.2, 0.4, 0.7, 0.9])
    labels = np.array([0, 0, 1, 1])
    
    print("原始输入:")
    print(f"logits = {logits}")
    print(f"labels = {labels}")
    print()
    
    # 特别关注第0个样本 (0.2 和 0) 和第2个样本 (0.7 和 1)
    print("重点关注样本:")
    print("样本 0: z = 0.2, y = 0")
    print("样本 2: z = 0.7, y = 1")
    print()
    
    # 计算成本
    cost_values = cost_with_intermediate_values(logits, labels)
    
    print("最终结果:")
    print(f"cost = {cost_values}")

def explain_sigmoid_cross_entropy():
    """解释 sigmoid cross entropy 的计算原理"""
    
    print("\n=== Sigmoid Cross Entropy 原理说明 ===")
    print("""
Sigmoid Cross Entropy 的计算公式:
cost = max(z, 0) - z * y + log(1 + exp(-abs(z)))

其中:
- z: 模型的原始输出 (logits，未经过 sigmoid 激活)
- y: 真实标签 (0 或 1)

这个公式的推导:
1. 当 y=1 时: cost = -log(sigmoid(z)) = -log(1/(1+exp(-z))) = log(1+exp(-z))
2. 当 y=0 时: cost = -log(1-sigmoid(z)) = -log(exp(-z)/(1+exp(-z))) = log(1+exp(z))

为了数值稳定性，TensorFlow 使用统一的公式:
cost = max(z, 0) - z * y + log(1 + exp(-abs(z)))
    """)

if __name__ == "__main__":
    demonstrate_specific_calculation()
    explain_sigmoid_cross_entropy()
    
    # 用户提供的原始代码
    print("\n=== 用户原始代码验证 ===")
    def cost(logits, labels):
        z = tf.cast(logits, tf.float32)
        y = tf.cast(labels, tf.float32)
        cost = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
        return cost.numpy()
    
    logits = np.array([0.2, 0.4,0 ,0,0.7, 0.9])
    result = cost(logits, np.array([0, 0,0,1, 1, 1]))
    print("原始代码结果:")
    print(f"cost = {result}")
