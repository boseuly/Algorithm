import sys
n = 28 # 과제를 낸 학생 수만큼 리스트를 생성해야 한다. 

homework_completed_stu_list = [sys.stdin.readline().strip() for _ in range(n)] # 과제를 낸 학생 리스트
total_stu_list = [0] * 30 # 전체 학생 리스트 0과 1로 과제를 낸 학생을 걸러낸다.
for stu_seq in homework_completed_stu_list: 
    total_stu_list[int(stu_seq) - 1] = 1 # 만약 과제를 했다면 1로 변경

for stu_seq in range(total_stu_list.__len__()):
    if total_stu_list[stu_seq] == 0:
        print(stu_seq + 1) # 학생 번호는 1번부터 시작하니까 + 1을 해줘야 함
    