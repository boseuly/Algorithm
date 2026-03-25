
N = int(input())
quo = []
def num_mod(n):
    if n <= 1:  # 1일 경우 그냥 return
        return 
    # 몫을 다시 재귀함수의 인수로 전달한다.
    # 나누어지지 않는 경우 나누어질 때까지 반복한다.
    for i in range(2, n + 1):
        if n % i == 0:
            quo.append(i)
            n = n // i
            if n == 1:
                break
            num_mod(n)
            return

num_mod(N)   # 제수, 피제수
print('\n'.join(str(i) for i in quo))