def X_figure(salary):

    tally = 0;
    #base case
    if salary == 0:
        tally += 1


    while salary >= 1:
        #keep dividing the salary by 10 and count how many times is possible 
        # to divide it by 10
        salary = salary/10

        tally += 1


    return tally


print(X_figure(300000))
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")