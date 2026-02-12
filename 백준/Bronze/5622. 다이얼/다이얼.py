str_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
alphabet_list = list(input())
total_seconds = 0

for alphabet in alphabet_list:
    for index in range(len(str_list)):
        if alphabet in str_list[index]:
            total_seconds += index + 3

print(total_seconds)