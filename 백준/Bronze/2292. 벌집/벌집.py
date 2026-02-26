# a = n * 6의 누적합
prefix_sum = 0      # 누적합 < target_num <= 누적합 + (n * 6)
next_num = 1        # 1부터 시작
target_num = int(input())    # 타겟이 되는 방
n = 0                        # 몇 개의 방을 지나는지 저장 

# target_num이 
while True:
    if target_num > prefix_sum and target_num <= next_num:
        print(n+1)
        break
    else:
        prefix_sum += n * 6     
        n += 1
        next_num += n * 6