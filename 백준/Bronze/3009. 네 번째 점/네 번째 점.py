
coor_list = [[], []]
for i in range(3):
    data = input().split(" ")    
    coor_list[0].append(data[0]) # x축
    coor_list[1].append(data[1]) # y축
result = ""
coor_list[0].sort()
coor_list[1].sort()
if coor_list[0][0] == coor_list[0][1]:    
    result += coor_list[0][2]
else:
    result += coor_list[0][0]

if coor_list[1][0] == coor_list[1][1]:
    result += " " + coor_list[1][2]
else:
    result +=  " " + coor_list[1][0]

print(result)
