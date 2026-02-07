import sys
n = 10
list = [sys.stdin.readline().strip() for _ in range(n)] # 10개 자연수
divide_list = []

for data in list:
    divide_list.append(int(data) % 42)

# 1. set을 사용할 경우
result_set = set(divide_list)
print(result_set.__len__())

# 저장된 나머지 중에서 서로 다른 값이 몇 개인지 확인한다. 
# 2. for를 사용할 경우
# result_list = []
# for data in divide_list: #[1,2,3,4,5,6,7,8,9,1]
#     if data not in result_list:
#         result_list.append(data)
