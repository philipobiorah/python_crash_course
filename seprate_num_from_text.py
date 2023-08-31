def sales_prices(item_and_price):
    item = ""
    price = ""

    #Create a variable "item_or_price" to hold the result of the split
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price"
    for x in item_or_price:
        #check if its alpha
        if x.isalpha():
            # If true, assign the element to the "item" string variable and add a space 
            # for any item names containing multiple words, like "Winter fleece jacket".


            item += x + " "

        else:
            price = x

    #Strip the extra space to the right of the last "item" word
    item = item.strip()   

    # Return the item name and price formatted in a sentence 
    return "{} are on sale for ${}".format(item,price)

     
#Call to the function
print(sales_prices("Winter fleece jackets 49.99"))
# Should print "Winter fleece jackets are on sale for $49.99"