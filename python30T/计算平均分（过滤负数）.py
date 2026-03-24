# 输入若干整数（含负数），过滤掉负数后输出平均分，（若全为负数，输出为0）
# 输入：多个整数
# 输出：平均分（保留2位小数）
nums = list(map(int, input().split()))
positive = [x for x in nums if x >= 0]
if not positive:
    print("0.00")
else:
    print(f"{sum(positive)/len(positive):.2f}")
