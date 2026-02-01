import sys
t = int(input())

for n in range(1, t+ 1):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(f"Case #{n}: {a} + {b} = {a+b}")
    