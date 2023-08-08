def sum_divisors(number):
    #initialze the variables 
    total = 0
    divisor = 1


    #Avoid dividing by 0 and negative numbers
    if number < 1:
        return 0
    
    while(divisor != number):
        if(number % divisor == 0):
            total += divisor

        divisor += 1

    return total         


print(sum_divisors(0)) # Should print 0
print(sum_divisors(3)) # Should print 1
# 1
print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# 114
