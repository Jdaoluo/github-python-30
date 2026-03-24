# 输入一个字符串，统计其中数字字符的个数
# 输入：一个字符串s
# 输出：数字字符的个数
s = input()
count = 0
for c in s:
    if c.isdigit():
        count += 1
print(count)
