# 输入5个整数，过滤掉负数后输出平均分，（保留1位小数）
# 输入：多个整数
# 输出：平均分
scores = list(map(int, input().split()))
avg = sum(scores) / 5
print(f"{avg:.1f}")
