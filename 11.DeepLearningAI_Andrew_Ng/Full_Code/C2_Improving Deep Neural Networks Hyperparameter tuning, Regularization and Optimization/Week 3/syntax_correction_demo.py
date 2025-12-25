"""
语法纠正演示 - X_test[:, [1]] 的正确写法
演示 NumPy 数组索引的正确语法
"""

import numpy as np

def demonstrate_correct_syntax():
    """演示正确的索引语法"""
    
    print("=== 数组索引语法纠正演示 ===\n")
    
    # 创建示例数据
    X_test = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    
    print("原始数据:")
    print(f"X_test = \n{X_test}")
    print(f"X_test.shape = {X_test.shape}")
    print()
    
    # 演示正确语法
    print("1. 正确语法 - X_test[:, [1]]:")
    try:
        result_correct = X_test[:, [1]]
        print(f"X_test[:, [1]] = \n{result_correct}")
        print(f"形状: {result_correct.shape}")
        print("✅ 语法正确，执行成功")
    except Exception as e:
        print(f"❌ 错误: {e}")
    print()
    
    # 演示错误语法
    print("2. 错误语法 - X_test[, [1]]:")
    print("   这种写法在 Python 中是无效语法")
    print("   Python 解释器会报语法错误")
    print("   原因: 缺少必要的冒号(:)")
    print()
    
    # 解释语法规则
    print("3. 语法规则解释:")
    print("   NumPy 数组索引语法: array[行选择, 列选择]")
    print("   - 行选择部分不能为空")
    print("   - 冒号(:)表示'选择所有行'")
    print("   - 逗号(,)分隔行选择和列选择")
    print()
    
    # 展示其他正确写法
    print("4. 其他正确的索引写法:")
    
    # 选择所有行，第二列
    print("   X_test[:, 1] - 选择所有行，第二列(1D):")
    print(f"   结果: {X_test[:, 1]}")
    print(f"   形状: {X_test[:, 1].shape}")
    print()
    
    # 选择第一行，所有列
    print("   X_test[0, :] - 选择第一行，所有列:")
    print(f"   结果: {X_test[0, :]}")
    print(f"   形状: {X_test[0, :].shape}")
    print()
    
    # 选择第一行，第二列
    print("   X_test[0, 1] - 选择第一行，第二列(标量):")
    print(f"   结果: {X_test[0, 1]}")
    print(f"   类型: {type(X_test[0, 1])}")
    print()

def explain_why_colon_is_required():
    """解释为什么冒号是必需的"""
    
    print("=== 为什么冒号(:)是必需的？ ===\n")
    
    print("""
在 Python 的索引语法中，逗号(,)用于分隔不同维度的索引。

正确的语法结构:
array[行索引表达式, 列索引表达式]

其中:
- 行索引表达式: 指定要选择哪些行
- 列索引表达式: 指定要选择哪些列

冒号(:)的作用:
- : 表示"选择该维度的所有元素"
- X_test[:, [1]] 意思是"选择所有行，以及索引为1的列"

如果省略冒号:
- X_test[, [1]] 在语法上是错误的
- Python 不知道您想要选择哪些行
- 逗号前面必须有行选择表达式

类比理解:
- 就像在函数调用中: function(arg1, arg2)
- 不能写成 function(, arg2) - 必须提供第一个参数
""")

def demonstrate_valid_alternatives():
    """演示有效的替代写法"""
    
    print("=== 有效的替代写法 ===\n")
    
    X_test = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    
    print("如果您想简化语法，可以使用以下写法:")
    print()
    
    # 方法1: 使用切片对象
    print("1. 使用 slice(None) 代替冒号:")
    all_rows = slice(None)
    result1 = X_test[all_rows, [1]]
    print(f"   X_test[slice(None), [1]] = \n{result1}")
    print()
    
    # 方法2: 使用省略号
    print("2. 使用省略号 (...) 选择所有前面的维度:")
    result2 = X_test[..., [1]]
    print(f"   X_test[..., [1]] = \n{result2}")
    print("   (注意: 这只有在列是最后一个维度时才有效)")
    print()
    
    # 方法3: 直接使用列索引
    print("3. 如果只需要列，可以直接索引:")
    result3 = X_test.T[1]  # 转置后选择行
    print(f"   X_test.T[1] = {result3}")
    print(f"   形状: {result3.shape}")
    print()

def common_mistakes_and_corrections():
    """常见错误和纠正"""
    
    print("=== 常见错误和纠正 ===\n")
    
    X_test = np.array([[1, 2, 3], [4, 5, 6]])
    
    mistakes = [
        ("X_test[, 1]", "X_test[:, 1]", "缺少行选择表达式"),
        ("X_test[1, ]", "X_test[1, :]", "缺少列选择表达式"), 
        ("X_test[1]", "X_test[1, :] 或 X_test[1]", "单索引选择行"),
        ("X_test[: 1]", "X_test[:, 1]", "冒号后不应有空格")
    ]
    
    for wrong, correct, reason in mistakes:
        print(f"错误: {wrong}")
        print(f"纠正: {correct}")
        print(f"原因: {reason}")
        print()

if __name__ == "__main__":
    demonstrate_correct_syntax()
    explain_why_colon_is_required()
    demonstrate_valid_alternatives()
    common_mistakes_and_corrections()
    
    print("=== 总结 ===")
    print("""
关键要点:
1. ✅ 正确语法: X_test[:, [1]] 
2. ❌ 错误语法: X_test[, [1]] (无效语法)

记住:
- 冒号(:)表示"选择所有"
- 逗号(,)分隔不同维度的索引
- 行选择和列选择都不能省略

在您的代码中，请始终使用正确的语法: X_test[:, [1]]
""")
