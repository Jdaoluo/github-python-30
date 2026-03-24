# 输入若干整数（以空格分隔），去除重复元素后，按原顺序输出
# 输入：多个整数
# 输入：去重后的整数（以空格分隔）
nums = list(map(int, input().split()))
seen = set()
result = []
for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(str(num))
print(" ".join(result))
