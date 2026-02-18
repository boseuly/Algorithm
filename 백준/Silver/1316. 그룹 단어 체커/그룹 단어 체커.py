
n = int(input())
total_repeat_cnt = n
for _ in range(n):
    
    find_words = []
    for s in input():
        if s not in find_words:
            find_words.append(s)
        else:
            if s != find_words[-1]:
                total_repeat_cnt -= 1
                break
print(total_repeat_cnt)
