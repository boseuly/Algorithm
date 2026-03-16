import sys
while True:
    # 약수를 담을 리스트
    factor_list = []
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    # 제수가 약수 리스트에 이미 존재하면 해당값을 반환하고 break
    for divisor in range(1, n+1):
        # if any(str(divisor) in str(factor) for factor in factor_list):
        if divisor in factor_list:
            break

        if n % divisor == 0 and n != divisor:
            # 나눴을 때 0이라면 divisor은 n의 약수에 해당함
            # 제수와 몫을 저장한다. 그리고 자기 자신은 들어가면 안 된다
            factor_list.append(divisor)         # 제수
            if n != (n // divisor) and divisor != (n // divisor):               
                factor_list.append(n // divisor) # 몫

    if sum(factor_list) == n:
        factor_list.sort()
        # 1. 만약 완전수라면 약수들의 합 
        factor_list = list(map(str, factor_list))
        print(f'{n} =', ' + '.join(factor_list))                               
    else:
        # 2. 만약 완전수가 아니라면 {n} is NOT perfect.
        print(f'{n} is NOT perfect.')
