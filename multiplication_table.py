#The function accepts a variable number through its parameter. This number shoulb e be 
#multiplied by the numbers 1 through 5, and printed in a formart similar to
# 1 x 6 = 6. The code should aslo limit the resutl to not exceed 25. 

def multiplication_table(number):

    multiplier = 1

    #while multiplier is <= 5
    while(multiplier <= 5):

        result = number * multiplier
        #multiplier > 25
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result)) 
        #increment multiplier
        multiplier = multiplier + 1

    


multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15

multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24
