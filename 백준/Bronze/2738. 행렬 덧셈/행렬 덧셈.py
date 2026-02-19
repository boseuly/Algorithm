
n,m = map(int, input().split(" "))
# 첫 번째 행렬
a = []
b = []
for _ in range(n):
    a_data =  input().split()
    a.append(a_data)

# 두 번째 행렬
for _ in range(n):
    b_data = input().split()
    b.append(b_data)

result = ""
for i in range(n):
    for j in range(m):
        result += str(int(a[i][j]) + int(b[i][j]))
        if j != m - 1:
            result += " "
    result += "\n"
print(result)