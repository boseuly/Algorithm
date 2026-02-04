
a, x = map(int, input().split())
list = list(map(int, input().split(" ")))
for i in range(a):
    if list[i] < x:
        print(list[i], end=" ")
