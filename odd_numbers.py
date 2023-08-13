def odd_numbers(maximum):
    return_string = ""  #Initialzes variable as a string

    #Complete the for loop with arange that incldues all odd number up to and including the max value
    for x in range(maximum + 1):

        if x % 2 != 0:
            return_string += str(x) + " "

    return return_string.strip() # This .strip command will remove the final " " space at the end of the "return_string"


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed