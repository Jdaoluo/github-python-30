# 输入矩形的长和宽，计算周长
# 输入：两个数（长，宽，以空格分隔）
# 输出：矩形的周长
length, width = map(float, input().split())
perimeter = 2 * (length + width)
print(perimeter)
