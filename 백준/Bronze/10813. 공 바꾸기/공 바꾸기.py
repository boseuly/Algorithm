n, m = map(int, input().split())
list = [0] * n
for index in range(list.__len__()):
    list[index] = index + 1
for _ in range(m):
    i, j = map(int, input().split(" "))
    list[i - 1], list[j - 1] = list[j - 1], list[i - 1]

for print_index in range(list.__len__()):
    print(list[print_index], end=" ")