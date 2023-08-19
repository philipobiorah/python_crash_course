def reverse_digits(number):
    if number <= 0:
        return "Enter positive integer"
    
    reverse_number = ""

    while(number > 0):
        digit = number % 10
        reverse_number  +=  str(digit)
        number = number // 10

    return reverse_number        


print(reverse_digits(54399))