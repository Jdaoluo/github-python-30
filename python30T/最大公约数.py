# 输入两个正整数，计算它们的最大公约数（辗转相除法）
# 输入：两个正整数a,b
# 输出：最大公约数
a, b = map(int, input().split())
while b != 0:
    a, b = b, a % b
print(a)
