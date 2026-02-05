
import sys
list = [int(input()) for _ in range(9)]
max_value = max(list)

for i in range(list.__len__()):
    if list[i] == max_value:
        print(max_value)
        print(i+1)
