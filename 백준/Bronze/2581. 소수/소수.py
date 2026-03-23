import sys
M,N = map(int, sys.stdin.read().split())
# 2~제곱근의 수까지 나누었을 때 나누어지는 수는 소수가 아니다. 
# 소수인지 검증하는 함수
# 소수라면 list에 값을 넣는다. 

def find_prime_number(number): 
    # number의 제곱근
    square = int(number**(1/2))
    if number <= 1:
        return False
    if number == 2: # 2는 예외
        return True
    
    # square가 소수인지 확인하는 로직
    # 2~제곱근까지의 수로 나눠지면 소수가 아니다. 
    for num in range(2, square + 1):
        if (number % num == 0):
            return False
    return True

# m~n까지의 수를 함수에 넣어서 소수인지 여부를 확인하고 만약 해당 수가 소수라면 리스트에 넣는다. 
# 그리고 sum을 통해서 리스트 총계를 구하고, min함수를 통해서 최솟값을 구한다. 
prime_list = []
for number in range(M, N + 1):
    if find_prime_number(number): prime_list.append(number)
if len(prime_list) != 0:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)