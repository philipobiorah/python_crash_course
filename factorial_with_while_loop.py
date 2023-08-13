def factorial(n):
    result = n
    start = n
    n = n - 1

    while n > 0: # the while loop should execure as long as n is greater than 0
        result *= n  # Multipley the current result by the currnt value of n
        n -= 1 # Decrement the n by -1
    return result




print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1
