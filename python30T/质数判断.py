# 输入一个大于1的整数，判断其是否为质数（仅能被1和自身整除）
# 输入：整数n(n>1)
# 输出：“是质数”或“不是质数”
n = int(input())
is_prime = True
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print("是质数" if is_prime else "不是质数")
