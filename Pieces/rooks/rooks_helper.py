def direction_to_go(from_y, from_x, to_y, to_x):
    if (from_y == to_y):
        change = from_x
        #checks to see if we increment or decrement
        if (change < to_x):
            value_change = 1
        else:
            value_change = -1
    else:
        change = from_y #will be used to see to head toward to_y
        #checks to see if we increment or decrement
        if (change < to_y):
             value_change = 1
        else:
            value_change = -1
    return  change, value_change