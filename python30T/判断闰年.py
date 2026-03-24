# 输入一个年份，判断是否为闰年（能被四整除且不能被100整除，或能被400整除）
# 输入：一个整数year
# 输出：“是闰年”或“不是闰年”
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年。")
else:
    print(f"{year}年不是闰年。")
