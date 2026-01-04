
x_coordinate = input()
y_coordinate = input()

def print_quadrant(x_coordinate, y_coordinate):
    x_coordinate = int(x_coordinate)
    y_coordinate = int(y_coordinate)
    # 1: +, +
    # 2: -, +
    # 3: _, _
    # 4: +, -
    
    if x_coordinate > 0 and y_coordinate > 0:
        return print(1)
    elif x_coordinate < 0 and y_coordinate > 0:
        return print(2)
    elif x_coordinate < 0 and y_coordinate < 0:
        return print(3)
    else:
        return print(4)
    
print_quadrant(x_coordinate, y_coordinate)