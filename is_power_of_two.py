#!/usr/bin/env python3

def is_power_of_two(number):
    #if num is zero return false
    if number == 0:
        return False
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder.
    while(number % 2 == 0 and number > 1):
        number = number // 2
    
    #after each iterative division and the number is 1 return true
    if(number == 1):
        return True
    return False    

         
    
  




# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False