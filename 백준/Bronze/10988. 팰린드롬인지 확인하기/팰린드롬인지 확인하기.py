import sys
alphabet_list = sys.stdin.readline().strip()
alphabet_list = list(alphabet_list)
is_palindrome = True

for i in range(alphabet_list.__len__() // 2):  
    front_pointer = alphabet_list[i]
    end_pointer = alphabet_list[len(alphabet_list) - i - 1]
    if front_pointer != end_pointer :
        is_palindrome = False
        break
    # 프론트 pointer와 엔드 pointer가 서로 같아지면 break 해준다.
    if i == len(alphabet_list) - i -1:
        break

if is_palindrome:
    print(1)
else:
    print(0)