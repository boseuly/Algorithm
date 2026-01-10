
input1 = int(input())

def plus_function (param):
    for num in range(param):
        first_number, second_number = input().split(" ")
        first_number = int(first_number)
        second_number = int(second_number)

        print(first_number + second_number)
    return
        
plus_function(input1)
