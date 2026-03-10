import sys
total_distance = 0
a, b, v = map(int,sys.stdin.readline().split(" "))
required_days = 1
# 새로운 풀이

if a >= v:
    print(required_days)
elif (v - b) % (a - b) == 0:
    print((v - b) // (a - b))
else:
    print((v -b) // (a - b) + 1)