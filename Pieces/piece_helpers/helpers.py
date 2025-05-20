def check_to_see_direction_Q_B(from_x, from_y, to_x, to_y):
        change_x = from_x
        change_y = from_y
        #if we don't move on the x cordinate
        value_change_x = 0
        #if we don't move on the y cordinate
        value_change_y = 0
        #when we do move on the spefic coordinates
        if (change_x < to_x):
            value_change_x = 1

        if (change_x > to_x):
            value_change_x = -1

        if change_y < to_y:  
            value_change_y = 1

        if (change_y > to_y):
            value_change_y = -1

        return change_y, change_x, value_change_y, value_change_x