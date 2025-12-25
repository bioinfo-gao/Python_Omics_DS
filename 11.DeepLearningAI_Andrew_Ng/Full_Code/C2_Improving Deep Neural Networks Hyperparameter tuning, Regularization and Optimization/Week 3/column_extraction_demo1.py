"""
列提取演示 - 如何取第二列
演示 NumPy/Python 中提取特定列的方法
"""

import numpy as np

def demonstrate_column_extraction():
    """演示如何提取第二列"""
    
    print("=== 列提取演示 - 如何取第二列 ===\n")
    
    # 创建示例数据
    data = np.array([
        [1, 2, 3, 4],    # 第0行
        [5, 6, 7, 8],    # 第1行  
        [9, 10, 11, 12], # 第2行
        [13, 14, 15, 16] # 第3行
    ])
    
    print("原始数据:")
    print(f"data = \n{data}")
    print(f"data.shape = {data.shape}")
    print()
    
    # 演示不同列提取方法
    print("1. 提取第二列 (索引为1):")
    print("   data[:, 1] - 返回1D数组")
    col_1d = data[:, 1]
    print(f"   data[:, 1] = {col_1d}")
    print(f"   形状: {col_1d.shape}")
    print(f"   类型: {type(col_1d)}")
    print()
    
    print("2. 提取第二列并保持2D结构:")
    print("   data[:, [1]] - 返回2D数组")
    col_2d = data[:, [1]]
    print(f"   data[:, [1]] = \n{col_2d}")
    print(f"   形状: {col_2d.shape}")
    print(f"   类型: {type(col_2d)}")
    print()
    
    # 演示多列提取
    print("3. 提取多列 (第二列和第三列):")
    print("   data[:, [1, 2]] - 返回包含两列的2D数组")
    multi_cols = data[:, [1, 2]]
    print(f"   data[:, [1, 2]] = \n{multi_cols}")
    print(f"   形状: {multi_cols.shape}")
    print()

def demonstrate_with_tensorflow_data():
    """使用 TensorFlow 教程中的数据尺寸演示"""
    
    print("=== 使用 TensorFlow 教程数据尺寸演示 ===\n")
    
    # 模拟教程中的 X_test 数据
    # 形状: (120, 12288) - 120个样本，每个样本12288个特征
    X_test = np.random.randn(120, 12288)
    
    print(f"X_test 形状: {X_test.shape}")
    print(f"- 120 个样本")
    print(f"- 每个样本 12288 个特征")
    print()
    
    # 演示提取第二列（第二个特征）
    print("提取第二列（索引为1的特征）:")
    second_feature = X_test[:, 1]
    print(f"X_test[:, 1].shape = {second_feature.shape}")
    print(f"包含所有120个样本的第二个特征值")
    print()
    
    # 显示部分数据
    print("前10个样本的第二个特征值:")
    print(second_feature[:10])
    print()
    
    # 演示保持2D结构的提取
    print("提取第二列并保持2D结构:")
    second_feature_2d = X_test[:, [1]]
    print(f"X_test[:, [1]].shape = {second_feature_2d.shape}")
    print(f"形状为 (120, 1) - 适合神经网络输入")
    print()

def explain_indexing_syntax():
    """解释索引语法"""
    
    print("=== 索引语法解释 ===")
    print("""
NumPy 数组索引语法: data[行索引, 列索引]

1. 提取单列:
   - data[:, 1]     # 提取第二列，返回1D数组
   - data[:, [1]]   # 提取第二列，返回2D数组

2. 冒号(:)的含义:
   - : 表示"所有行"或"所有列"
   - data[:, 1] 意思是"所有行的第1列"

3. 索引从0开始:
   - 第0列: data[:, 0]
   - 第1列: data[:, 1] (第二列)
   - 第2列: data[:, 2] (第三列)

4. 在神经网络中的应用:
   - 通常使用 data[:, [1]] 保持批次维度
   - 便于进行矩阵运算和批量处理
""")

def practical_examples():
    """实用示例"""
    
    print("=== 实用示例 ===")
    
    # 创建更真实的数据
    student_scores = np.array([
        [85, 90, 78],  # 学生1: 数学, 英语, 物理
        [92, 88, 95],  # 学生2
        [78, 85, 80],  # 学生3
        [95, 92, 88]   # 学生4
    ])
    
    print("学生成绩数据:")
    print("行: 学生, 列: 科目 (数学, 英语, 物理)")
    print(f"数据: \n{student_scores}")
    print()
    
    # 提取英语成绩（第二列）
    print("提取所有学生的英语成绩（第二列）:")
    english_scores = student_scores[:, 1]
    print(f"英语成绩: {english_scores}")
    print(f"平均英语成绩: {np.mean(english_scores):.2f}")
    print()

if __name__ == "__main__":
    demonstrate_column_extraction()
    demonstrate_with_tensorflow_data()
    explain_indexing_syntax()
    practical_examples()
    
    print("=== 总结 ===")
    print("""
提取第二列的方法:
1. data[:, 1]    - 返回1D数组，形状 (n,)
2. data[:, [1]]  - 返回2D数组，形状 (n, 1)

在您的 TensorFlow 工作中:
- 使用 X_test[:, 1] 查看所有样本的第二个特征
- 使用 X_test[:, [1]] 进行神经网络处理（保持维度）

记住: Python 索引从0开始，所以第二列的索引是1。
""")
