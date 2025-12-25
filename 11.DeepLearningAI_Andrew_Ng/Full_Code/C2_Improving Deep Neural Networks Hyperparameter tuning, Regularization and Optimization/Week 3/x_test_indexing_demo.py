"""
X_test[[1]] 索引演示
解释 NumPy/Python 中 X_test[[1]] 和 X_test[1] 的区别
"""

import numpy as np

def demonstrate_indexing():
    """演示 X_test[[1]] 和 X_test[1] 的区别"""
    
    print("=== X_test[[1]] 索引演示 ===\n")
    
    # 创建示例数据，模拟教程中的 X_test
    # 假设 X_test 形状为 (样本数, 特征数)
    X_test = np.array([
        [0.1, 0.2, 0.3, 0.4],  # 样本 0
        [0.5, 0.6, 0.7, 0.8],  # 样本 1
        [0.9, 1.0, 1.1, 1.2],  # 样本 2
        [1.3, 1.4, 1.5, 1.6]   # 样本 3
    ])
    
    print("原始 X_test 数据:")
    print(f"X_test = \n{X_test}")
    print(f"X_test.shape = {X_test.shape}")
    print()
    
    # 演示不同索引方式
    print("1. X_test[1] (普通索引):")
    result1 = X_test[1]
    print(f"X_test[1] = {result1}")
    print(f"类型: {type(result1)}")
    print(f"形状: {result1.shape}")
    print(f"这是一个 1D 数组，包含样本1的所有特征")
    print()
    
    print("2. X_test[[1]] (花式索引):")
    result2 = X_test[[1]]
    print(f"X_test[[1]] = \n{result2}")
    print(f"类型: {type(result2)}")
    print(f"形状: {result2.shape}")
    print(f"这是一个 2D 数组，保持原始维度结构")
    print()
    
    # 演示多个索引
    print("3. X_test[[0, 2]] (多个索引):")
    result3 = X_test[[0, 2]]
    print(f"X_test[[0, 2]] = \n{result3}")
    print(f"形状: {result3.shape}")
    print(f"选择样本0和样本2")
    print()

def explain_tutorial_context():
    """解释教程中的具体上下文"""
    
    print("=== 教程中的 X_test[[1]] 上下文 ===")
    print("""
在您的 TensorFlow 教程中，X_test 的形状可能是 (120, 12288)，其中：
- 120 是测试样本数量
- 12288 是每个样本的特征数量 (64x64x3 RGB 图像)

当使用 X_test[[1]] 时：
- 选择第1个测试样本（索引为1）
- 保持2D数组结构，形状变为 (1, 12288)
- 这样可以方便地进行批量处理

对比：
- X_test[1] 返回形状 (12288,) 的1D数组
- X_test[[1]] 返回形状 (1, 12288) 的2D数组

在神经网络中，通常使用 X_test[[1]] 来保持批次维度，即使只有一个样本。
""")

def demonstrate_with_realistic_data():
    """使用更真实的数据演示"""
    
    print("=== 使用真实图像数据尺寸演示 ===\n")
    
    # 模拟教程中的真实数据尺寸
    num_test_samples = 120
    num_features = 12288  # 64x64x3
    
    # 创建随机数据模拟图像特征
    X_test_real = np.random.randn(num_test_samples, num_features)
    Y_test_real = np.random.randn(num_test_samples, 6)  # 6个类别
    
    print(f"X_test 真实形状: {X_test_real.shape}")
    print(f"Y_test 真实形状: {Y_test_real.shape}")
    print()
    
    # 演示索引操作
    print("索引操作结果:")
    print(f"X_test[1].shape = {X_test_real[1].shape}")
    print(f"X_test[[1]].shape = {X_test_real[[1]].shape}")
    print(f"Y_test[1].shape = {Y_test_real[1].shape}")
    print(f"Y_test[[1]].shape = {Y_test_real[[1]].shape}")
    print()
    
    # 显示部分数据内容
    print("X_test[[1]] 的部分数据（前10个特征）:")
    print(X_test_real[[1]][0, :10])  # 第一个样本的前10个特征
    print()
    
    print("Y_test[[1]] 的数据:")
    print(Y_test_real[[1]])

if __name__ == "__main__":
    demonstrate_indexing()
    explain_tutorial_context()
    demonstrate_with_realistic_data()
    
    print("\n=== 总结 ===")
    print("""
关键要点:
1. X_test[1] 返回单个样本的1D数组
2. X_test[[1]] 返回包含单个样本的2D数组，保持批次维度
3. 在神经网络中，通常使用 X_test[[1]] 来保持数据结构的完整性
4. 这对于批量处理和维度一致性很重要

在您的 TensorFlow 教程中，使用 X_test[[1]] 是为了调试和查看特定样本的数据，同时保持正确的数组维度。
""")
