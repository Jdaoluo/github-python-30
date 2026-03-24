# 输出九九乘法表（格式：1*1=1 1*2=2...9*9=81，每行以制表符分隔）
# 输入：无
# 输出：九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}", end='\t')
    print()