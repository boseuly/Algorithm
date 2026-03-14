import sys

cnt = 0
result = 0
N, K = map(int, sys.stdin.readline().split())

for n in range(1, N + 1):  # N은 피제수, n은 제수
    result = n
    if N % (n) == 0:
        cnt += 1
        if K == cnt:
            print(n)
            break

if K > cnt:
    print(0)