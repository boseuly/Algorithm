import sys
result = ""
divisors = [25, 10, 5, 1]   # 1센트 = 100달러 
for _ in range(int(input())):
    return_money = int(sys.stdin.readline().strip())
    for divisor in divisors:
        quotient, return_money = divmod(return_money, divisor)
        result += str(quotient) + " "
    result += "\n"
print(result)