# 输入一个字符串，统计其中元音字母（a,e,i,o,u，不区分大小写）的个数
# 输入：一个字符串s
# 输出：元音字母个数
s = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for c in s:
    if c in vowels:
        count += 1
print(count)
