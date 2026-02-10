alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' , 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = [-1] * 26 
str_list = list(input())
position = 0
for str_value in str_list:
    for i in range(alphabet.__len__()):
        if str_value == alphabet[i] and result[i] == -1:  # 둘이 서로 같다면 
            result[i] = position
            break
    position += 1
print(' '.join(map(str, result)))
