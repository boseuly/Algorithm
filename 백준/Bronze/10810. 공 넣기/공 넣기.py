n, m = map(int , input().split(" "))
basketList = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split(" "))
    # i ~ j 번째 바구니에 k를 넣어야 한다. 
    for index in range(i-1, j, 1):
        basketList[index] = k

for e in range(n):
    print(basketList[e], end=" ")