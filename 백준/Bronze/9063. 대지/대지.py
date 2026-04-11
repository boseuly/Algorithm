import sys

coor_x = []
coor_y = []

n = int(input())
for i in range(n):
    coor_x_y = list(map(int, sys.stdin.readline().strip().split(" ")))
    coor_x.append(coor_x_y[0])
    coor_y.append(coor_x_y[1])
# 큰 것에서 작은 걸 빼줘야 한다.
x_value = max(coor_x) - min(coor_x)
y_value = max(coor_y) - min(coor_y)
print(x_value * y_value)