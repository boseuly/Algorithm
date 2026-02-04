
a, x = input().split()
x= int(x)
list = list(map(int, input().split(" ")))

def findUnderList(x, list):
    result = []
    for data in list:
        if data < x:
            result.append(data)
    
    new_result = " ".join(map(str, result))
    
    print(new_result)

findUnderList(x, list)