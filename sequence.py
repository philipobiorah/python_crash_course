def sequence(low, high):
    #Complete the outer loop range to make the loop run twice
    # to create tow rows
    for x in range(high - 1):
        #Complete the inner loop range to print the given arialb enubers starting rom hight to low
        for y in range(high, low-1, -1):
            if y == low:
                print(str(y))

            else:
                    # Print a comma and a aspace bwtween umbers
                    print(str(y), end=",")



sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.                