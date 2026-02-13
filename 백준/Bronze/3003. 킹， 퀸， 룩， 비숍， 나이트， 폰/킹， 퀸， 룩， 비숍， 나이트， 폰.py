import sys
from collections import deque
chessmen = [1,1,2, 2, 2, 8]
find_chessmen_list = list(map(int, sys.stdin.readline().split()))
result = []
# deque로 변경
deque_chessmen = deque(chessmen)
deque_find_chessmen = deque(find_chessmen_list)

while deque_chessmen.__len__() > 0:
    result.append(deque_chessmen.popleft() - deque_find_chessmen.popleft())
    
for i in range(result.__len__()):
    print(result[i], end=" ")