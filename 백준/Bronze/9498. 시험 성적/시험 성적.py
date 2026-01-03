a = input()
def grading(input):

    grade = int(input)
    if 90 <= grade and grade <= 100:
        return print("A")
    elif 80 <= grade and grade <= 89:
        return print("B")
    elif 70 <= grade and grade <= 79:
        return print("C")
    elif 60 <= grade and grade <= 69:
        return print("D")
    else:
        return print("F")
    
grading(a)