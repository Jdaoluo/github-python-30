# 输入n，输出斐波那契数列的第n项（F（0）=0，F（1）=1，F（n）=F（n-1）+F（n-2））。
# 输入：非负整数n
# 输出：第n项的值
n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(a)
