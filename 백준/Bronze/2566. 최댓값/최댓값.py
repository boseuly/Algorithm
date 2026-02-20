
import sys
data_list = []
for _ in range(9):
    data_list.append(list(map(int, sys.stdin.readline().split(" ")))) 


max_value = 0
position = ""
for i in range(9):
    for j in range(9):
        if max_value <= data_list[i][j]: 
            max_value = data_list[i][j] 
            position = str(i + 1) + " " + str(j + 1)
print(max_value)
print(position)
