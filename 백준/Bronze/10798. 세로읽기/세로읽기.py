str_list = [[""] * 15 for _ in range(5)] # 초기화를 먼저 해줘서 index out of range 에러 방지

for i in range(5):
    input_data = input()
    for j in range(len(input_data)):
        str_list[i][j] = input_data[j]          # 데이터를 하나씩 추가해준다. 

for i in range(15):  # 5개니까 5번 반복
    for j in range(5):
        print(str_list[j][i], end="")
