def factorial(n):
    print("Factorial call with  " + str(n))
    #base case
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result



value = factorial(4)
print("value", value)