# 输入3个整数，按从小到大的顺序输出
# 输入：3个整数（以空格分隔）
# 输出：排序后的整数（以空格分隔）
nums = list(map(int, input().split()))
nums.sort()
print(' '.join(map(str, nums)))
