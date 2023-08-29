# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the 
# element and adds a dash between the element and the moved character. 
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):
    elem_list = given_string.split()
    new_string = ""
    for element in elem_list:
        new_string += element[1:]+ "-"+element[0] +" "
    return new_string


print(change_string("1one 2two 3three 4four 5five")) 