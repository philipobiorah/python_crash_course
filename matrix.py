def matrix(initial_number, end_of_first_row):
    #optioanal code stye to assign long var name to short var name
    n1 = initial_number
    n2 = end_of_first_row + 1


    #the fist for loop will create the colums
    for column in range(n1, n2):


        #The  nested for loop will create the rows
        for row in range(n1, n2):
            print(f"[{column}][{row}]" , end=" ")
        print()    





matrix(1,4)

        
    