# Complete the function to combine both dictionaries into one, with each friend listed only once, 
# and the number of guests from Rick's dictionary taking precedence, 
# if a name is included in both dictionaries. Then print the resulting dictionary. This function should:

# accept two dictionaries through the function’s parameters;
# combine both dictionaries into one, with each key listed only once;
# the values from the “guests1” dictionary taking precedence, if a key is included in both dictionaries;
# then print the new dictionary of combined items.

def combine_guests(guests1, guests2):
    guests2.update(guests1)
    return guests2


Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}