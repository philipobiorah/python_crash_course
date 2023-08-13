for outer_loop in range(10):


    #using the outer_loop variable as the endof range for the
    # inner loop means the end of range index will be 9. value of incdx 9 wil be 9-1 or 8

    for inner_loop in range(outer_loop):
        print(inner_loop, end=" ")

    print()