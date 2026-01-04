input = input()

def check_leap_year (input):
    year = int(input)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return print(1)

    return print(0)

check_leap_year(input)