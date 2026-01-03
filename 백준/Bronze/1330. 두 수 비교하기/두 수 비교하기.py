input_string = input()
def compare_number(input):
    a, b = input.split(" ")
    a = int(a)
    b = int(b)

    if a > b:
        return print(">")
    elif a < b:
        return print("<")
    else:
        print("==")

    return 

compare_number(input_string)
