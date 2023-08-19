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


for x in range(1, 10, 3):
    print(x)



print()


num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print("The reuslt of {} + {} is {}".format(num1, num2, num1 + num2))