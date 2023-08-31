# Use a dictionary to count the frequency of numbers in the given “text” string. 
# Only numbers should be counted. Do not count blank spaces, letters, or punctuation. 
# Complete the function so that input like "1001000111101" 
# will return a dictionary that holds the count of each number that occurs in the string {'1': 7, '0': 6}. 
# This function should:
# accept a string “text” variable through the function’s parameters;
# initialize an new dictionary;
# iterate over each text character to check if the character is a number’
# count the frequency of numbers in the input string, ignoring all other characters;
# populate the new dictionary with the numbers as keys, ensuring each key is unique, and assign the value for each key with the count of that number;
# return the new dictionary.


def count_numbers(text):
    # Initialize a new dictionary.
    dictionary = {}
    #for loop to iterate through each "text" character.
    for n in text:
        #check if character is a number
        if n.isnumeric():
            #check if the key already exists
            if n in dictionary:
                dictionary[n] += 1
            # add the key to dictionary and initalize the value of the key to 1
            else:
                dictionary[n] = 1    


    return (dictionary)




print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}


genre = "transcendental"
print(genre[:-8])
print(genre[-7:9])