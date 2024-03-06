# Instructions 

# Top border containing Title and *
print ("*" * 40)

# Name of coffee shop
txt = "My Coffee and Muffin Shop"
title = txt.center(41)
print(title)

# Make a space
print (" " * 41)

# Number of Coffee question
print ("Number of coffees bought?")

# Amount of coffee displayed
numberOfCoffee = input('Enter amount of coffees: ')
numberOfCoffee = int(numberOfCoffee)
print(numberOfCoffee)

# Number of Muffin question
print ("Number of muffins bought?")

# Amount of Muffin displayed
numberOfMuffin = input('Enter amount of muffins: ')
numberOfMuffin = int(numberOfMuffin)
print(numberOfMuffin)

# Number of Tea question
print ("Number of tea bought?")

# Amount of Tea displayed
numberOfTea = input('Enter amount of tea: ')
numberOfTea = int(numberOfTea)
print(numberOfTea)

# Number of Boba question
print ("Number of boba bought?")

# Amount of Tea displayed
numberOfBoba = input('Enter amount of boba: ')
numberOfBoba = int(numberOfBoba)
print(numberOfBoba)

# Second border containing *
print ("*" * 40)

# Make a space
print (" " * 41)

# Mid border containing *
print ("*" * 40)

# Display Title and "Receipt"
txt = "My Coffee and Muffin Shop Receipt"
title = txt.center(41)
print(title)

# Prices for each product
coffeePrice = 5.00

muffinPrice = 4.00

teaPrice = 3.00

bobaPrice = 7.00

salesTax = 1.06


# Quantity x Price
totalCoffeePrice = (numberOfCoffee * coffeePrice)
totalMuffinPrice = (numberOfMuffin * muffinPrice)
totalTeaPrice = (numberOfTea * teaPrice)
totalBobaPrice = (numberOfBoba * bobaPrice)


# Sales Tax
coffeeSalesTax = (numberOfCoffee * coffeePrice * 0.06)
muffinSalesTax = (numberOfMuffin * muffinPrice * 0.06)
teaSalesTax = (numberOfTea * teaPrice * 0.06)
bobaSalesTax = (numberOfBoba * bobaPrice * 0.06)

totalSalesTax = (coffeeSalesTax + muffinSalesTax + teaSalesTax + bobaSalesTax)

# Display value and text
print(numberOfCoffee , "Coffee at $5 each: $" , (format(totalCoffeePrice, '.2f')))
print(numberOfMuffin , "Muffin at $4 each: $" , (format(totalMuffinPrice, '.2f')))
print(numberOfTea , "Tea at $3 each: $" , (format(totalTeaPrice, '.2f')))
print(numberOfBoba , "Boba at $7 each: $" , (format(totalBobaPrice, '.2f')))

print("6% tax: $" , (format(totalSalesTax, '.2f')))


# Total Line Space
print("-"*10)

# Total and Tax
totalOrder = (totalCoffeePrice + totalMuffinPrice + totalTeaPrice + totalBobaPrice + totalSalesTax)

#Total
print("Total: $" , (format(totalOrder, '.2f')))

# End border containing *
print ("*" * 40)

# End greeting
txt = "Thank you for shopping with us!"
title = txt.center(41)
print(title)
