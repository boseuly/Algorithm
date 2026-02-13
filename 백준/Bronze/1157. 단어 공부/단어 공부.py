import sys
str_list = list(sys.stdin.readline().strip().upper())
set_list = set(str_list)
deduplication_list = list(set_list)   # set 사용해서 중복제거

dict_alphabet = {}
for index in range(len(deduplication_list)):
    dict_alphabet[deduplication_list[index]] = 0

for key, value in dict_alphabet.items(): # key, value를 가져온다.
    for alphabet in str_list: 
        if alphabet == key: # alphabet이랑 key가 같다면 해당 값을 dictionary[key] = dict_alphabet[key] + 1 해준다.
            dict_alphabet[key] = dict_alphabet[key] + 1

a = [k for k, v in dict_alphabet.items() if max(dict_alphabet.values()) == v]
if a.__len__() > 1:
    print('?')
else:
    print(a.pop())