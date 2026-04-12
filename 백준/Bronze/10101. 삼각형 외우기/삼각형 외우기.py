import sys
tri_list = list(map(int, sys.stdin.read().splitlines()))

def find_tri(tri_list):
    if sum(tri_list) != 180:
        return print("Error")
    cnt = 0
    for i in range(tri_list.__len__()-1):
        for j in range(i+1, tri_list.__len__()):
            if tri_list[i] == tri_list[j]:
                cnt +=1
    if cnt == 0:
        print('Scalene')
    elif cnt == 1:
        print("Isosceles")
    else:
        print("Equilateral")

find_tri(tri_list)