n, q = map(int, input().split(" "))
def solution(n,q):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J','K','L', 'M','N','O', 'P','Q', 'R', 'S', 'T','U','V', 'W', 'X', 'Y', 'Z']
    rev_base = ''
    while n > 0:
        n, mod = divmod(n,q)    # 몫과 나머지를 한 번에 가져올 수 있음
        if mod >= 10: 
            rev_base += alphabet[mod - 10]
        else : rev_base += str(mod)
        
    return rev_base[::-1]       # 리스트를 [::-1] 역순으로 반환하는 방법



print(solution(n, q))
