import sys
t = int(sys.stdin.readline().strip())
result = ""
def mod_num(dividend, divisor):    # dividend: 피제수(나뉨수), divisor: 제수(나눔수)
    # 몫        나머지
    quotient, dividend = divmod(dividend, divisor)   # 나누고 남은 값을 전달해준다. 
    return quotient, dividend
    

divisors = [25, 10, 5, 1]   # 1센트 = 100달러 
for _ in range(t):
    return_money = int(sys.stdin.readline().strip())
    for divisor in divisors:
        quotient, return_money = mod_num(return_money, divisor)
        result += str(quotient) + " "
        
    result += "\n"
print(result)
    