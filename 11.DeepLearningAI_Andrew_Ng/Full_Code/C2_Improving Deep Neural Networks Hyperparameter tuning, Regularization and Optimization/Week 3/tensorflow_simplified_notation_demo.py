"""
TensorFlow Simplified Notation Demo by Fitten Code 2025 
演示如何简化 TensorFlow 公式书写 

当前写法: result = tf.add(tf.matmul(W, X), b)
简化写法: result = W @ X + b
"""

import tensorflow as tf
import numpy as np

def demonstrate_simplified_notation():
    """演示 TensorFlow 简化记法"""
    
    print("=== TensorFlow 简化记法演示 ===\n")
    
    # 创建示例数据
    W = tf.constant([[1.0, 2.0], [3.0, 4.0]])  # 2x2 矩阵
    X = tf.constant([[5.0], [6.0]])            # 2x1 矩阵  
    b = tf.constant([[0.1], [0.2]])            # 2x1 偏置
    
    print("权重 W:")
    print(W.numpy())
    print("\n输入 X:")
    print(X.numpy())
    print("\n偏置 b:")
    print(b.numpy())
    print()
    
    # 传统写法 (verbose)
    print("1. 传统写法:")
    result_verbose = tf.add(tf.matmul(W, X), b)
    print(f"result = tf.add(tf.matmul(W, X), b)")
    print(f"结果: {result_verbose.numpy()}")
    print()
    
    # 简化写法 (simplified)
    print("2. 简化写法:")
    result_simple = W @ X + b
    print(f"result = W @ X + b")
    print(f"结果: {result_simple.numpy()}")
    print()
    
    # 验证结果相同
    print("3. 验证结果相同:")
    print(f"结果是否相同: {tf.reduce_all(tf.equal(result_verbose, result_simple)).numpy()}")
    print()

def simplified_forward_propagation(X, parameters):
    """
    使用简化记法的前向传播函数
    
    参数:
    X -- 输入数据
    parameters -- 参数字典 {'W1': ..., 'b1': ..., 'W2': ..., 'b2': ..., 'W3': ..., 'b3': ...}
    
    返回:
    Z3 -- 输出层的线性激活值
    """
    
    # 提取参数
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    W3 = parameters['W3']
    b3 = parameters['b3']
    
    # 使用简化记法实现前向传播
    Z1 = W1 @ X + b1      # 等价于 tf.add(tf.matmul(W1, X), b1)
    A1 = tf.nn.relu(Z1)   # ReLU 激活函数
    
    Z2 = W2 @ A1 + b2     # 等价于 tf.add(tf.matmul(W2, A1), b2)
    A2 = tf.nn.relu(Z2)   # ReLU 激活函数
    
    Z3 = W3 @ A2 + b3     # 等价于 tf.add(tf.matmul(W3, A2), b3)
    
    return Z3

def compare_implementations():
    """比较传统写法和简化写法的前向传播函数"""
    
    print("=== 前向传播函数比较 ===\n")
    
    # 创建测试数据
    X_test = tf.constant(np.random.randn(12288, 1), dtype=tf.float32)
    
    # 初始化参数 (使用 Xavier 初始化)
    initializer = tf.keras.initializers.GlorotNormal(seed=1)
    parameters = {
        "W1": tf.Variable(initializer(shape=(25, 12288))),
        "b1": tf.Variable(tf.zeros(shape=(25, 1))),
        "W2": tf.Variable(initializer(shape=(12, 25))),
        "b2": tf.Variable(tf.zeros(shape=(12, 1))),
        "W3": tf.Variable(initializer(shape=(6, 12))),
        "b3": tf.Variable(tf.zeros(shape=(6, 1)))
    }
    
    print("输入数据形状:", X_test.shape)
    print("参数形状:")
    for key, value in parameters.items():
        print(f"  {key}: {value.shape}")
    print()
    
    # 传统写法 (原代码)
    def original_forward_propagation(X, parameters):
        Z1 = tf.add(tf.matmul(parameters['W1'], X), parameters['b1'])
        A1 = tf.nn.relu(Z1)
        Z2 = tf.add(tf.matmul(parameters['W2'], A1), parameters['b2'])
        A2 = tf.nn.relu(Z2)
        Z3 = tf.add(tf.matmul(parameters['W3'], A2), parameters['b3'])
        return Z3
    
    # 运行两种实现
    result_original = original_forward_propagation(X_test, parameters)
    result_simplified = simplified_forward_propagation(X_test, parameters)
    
    print("传统写法结果形状:", result_original.shape)
    print("简化写法结果形状:", result_simplified.shape)
    print()
    
    # 验证结果相同
    are_equal = tf.reduce_all(tf.abs(result_original - result_simplified) < 1e-6)
    print(f"两种实现结果是否相同: {are_equal.numpy()}")
    print()

def additional_simplifications():
    """展示更多简化记法示例"""
    
    print("=== 更多简化记法示例 ===\n")
    
    # 创建示例张量
    a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    b = tf.constant([[5.0, 6.0], [7.0, 8.0]])
    c = tf.constant(2.0)
    
    print("示例张量:")
    print(f"a = {a.numpy()}")
    print(f"b = {b.numpy()}")
    print(f"c = {c.numpy()}")
    print()
    
    # 各种操作的简化记法
    operations = [
        ("矩阵乘法", "a @ b", a @ b),
        ("逐元素加法", "a + b", a + b),
        ("逐元素减法", "a - b", a - b),
        ("逐元素乘法", "a * b", a * b),
        ("标量乘法", "a * c", a * c),
        ("转置", "tf.transpose(a)", tf.transpose(a)),
        ("求和", "tf.reduce_sum(a)", tf.reduce_sum(a)),
        ("平均值", "tf.reduce_mean(a)", tf.reduce_mean(a)),
    ]
    
    for desc, expr, result in operations:
        print(f"{desc}: {expr}")
        print(f"结果: {result.numpy()}")
        print()

if __name__ == "__main__":
    demonstrate_simplified_notation()
    compare_implementations()
    additional_simplifications()
    
    print("=== 总结 ===")
    print("""
TensorFlow 支持以下简化记法:
- 矩阵乘法: W @ X 代替 tf.matmul(W, X)
- 加法: a + b 代替 tf.add(a, b)
- 减法: a - b 代替 tf.subtract(a, b)
- 乘法: a * b 代替 tf.multiply(a, b)
- 除法: a / b 代替 tf.divide(a, b)

这使得代码更简洁、更易读，同时保持相同的功能。
    """)
