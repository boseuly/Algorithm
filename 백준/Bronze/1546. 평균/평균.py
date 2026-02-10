
n = int(input())
subject_list = list(map(int, input().split(" ")))
max_score = max(subject_list)
for i in range(n):
    subject_list[i] = subject_list[i] / max_score * 100

total_sum = 0
for data in subject_list:
    total_sum += data

print(round(total_sum / n, 3))