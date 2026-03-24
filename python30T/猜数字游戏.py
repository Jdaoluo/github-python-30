# 系统随机生成1-10之间的整数，用户输入猜测的数字，若属地则输出“恭喜猜对！”，否则输出“猜错了，正确答案是X”（X为随机数）
# 输入：一个整数（1-10）
# 输出：猜测结果
import random
target = random.randint(1, 10)
guess = int(input())
if guess == target:
    print("恭喜猜对！")
else:
    print(f"猜错了，正确答案是{target}")