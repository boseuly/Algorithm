
n = int(input())
not_prime_number = 0
for num in list(map(int,input().split(" "))):
    # 숫자를 하나씩 가져와서 해당 숫자가 만약 
    # 2,3,5,7 로 나눴을 때 나누어 떨어지면 소수가 아니다
    # 제곱근을 구한다. 
    square = int(num**(1/2))
    if num > 1:
        for divisor in range(2, square+1):
            if num % divisor == 0:
                not_prime_number += 1
                break
    else: not_prime_number += 1
print(n - not_prime_number)