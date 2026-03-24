# 输入三角形的底和高，计算面积（面积=底*高/2）
# 输入：两个数（底，高，以空格分隔）
# 输出：三角形的面积
base, height = map(float,input().split())
area = base * height / 2
print(area)
