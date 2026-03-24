# 输入一个正整数n,计算n的阶乘（n!=1*2*...*n）
# 输入：正整数n
# 输出：n的阶乘
n = int(input())
result = 1
for i in range(1, n + 1):
    result = result * i
print(result)
