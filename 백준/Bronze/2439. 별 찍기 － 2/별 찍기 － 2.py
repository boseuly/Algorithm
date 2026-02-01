t = int(input())
a = 0
for n in range(t, 0, -1):
    a += 1
    print(" " * (n-1) + "*" * a)
    