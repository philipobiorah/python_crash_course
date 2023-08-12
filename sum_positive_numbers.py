def sum_positive_numbers(n):
    # the base case is n being smaller than 1
    print("Calling sum_positive_numbers() for" + str(n))
    if n < 1:
        print("Returing 0 ..... ")
        return 0
    
    #recusive case
    print("Returning " + str(n) + " for " + str(n-1))
    return n + sum_positive_numbers(n-1)



print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15