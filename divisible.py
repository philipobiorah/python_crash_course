# # Should print the sequence 3, 2, 1 two times, as shown above.
#This function should count the number of values from 0 to the “max” 
#parameter that are evenly divisible (no remainder) by the “divisor” parameter. 
#Complete the code so that a function call like “divisible(100,10)” will return the number “10”.


def divisible(max, divisor):
    count = 0
    for x in range(max):
        if x % divisor == 0:
            count += 1
    return count



print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9