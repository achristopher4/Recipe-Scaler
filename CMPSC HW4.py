"""
Alex Christopher
abc5885@psu.edu
HW4
"""
import math

##Introduction/Instructions 
print("This is a recipe scaler for serving large crowds!")
print("Enter one ingredient per line, with a numeric value first.")
print("Indicate the end of input with an empty line.")

##dictionary and saved values
savedValues = {}
count = 0

##Record user input
while True:
    save = input(" ")
    if save == "":
        break
    amount, unit, item = save.split(' ', 2)
    savedValues[count] = amount, unit, item
    count += 1

##Repeat recipe list
print("Here is the recipe that has been recorded: ")
repeatCount = 0

while repeatCount < count:
    amount = savedValues[repeatCount][0]
    unit = savedValues[repeatCount][1]
    item = savedValues[repeatCount][2]
    print("%-10s%-10s%-10s"%(amount, unit, item))
    repeatCount += 1

##Serving Size Input
servingSize = int(input("How many does this recipe serve? "))
mustServe = int(input("How many people must be served? "))

##Serving Size Algorthim
if mustServe <= servingSize:
    print(f'The recipe will serve all the guests')
elif (mustServe / servingSize) % 2 == 0:
    newServingSize = mustServe // servingSize
    print(f'Multiplying the recipe by {newServingSize}')
else:
    findNewServing = mustServe // servingSize
    newServingSize = findNewServing + 1
    print(f'Multiplying the recipe by {newServingSize}')    

##Creating new recipe to support the amount of guest
repeatCount = 0
remainder = ''

while repeatCount < count:
    amount = savedValues[repeatCount][0]
    unit = savedValues[repeatCount][1]
    item = savedValues[repeatCount][2]
    if '/' in amount:
        number, slash, denom = amount.partition('/')
        number = int(number)
        setNumber = int(number)
        denom = int(denom)
        number *= newServingSize
        ##Extra Credit
        if number % denom != 0:
            gcd = math.gcd(number, denom)
            number = number // gcd
            denom = denom // gcd
            if number / denom > 1:
                remainder = number // denom
                number = number - (remainder * denom)
                remainder = str(remainder) + ' '
        amount = remainder + str(number) + '/' + str(denom)
    else:
        amount = int(amount)
        amount *= newServingSize
    
    print("%-10s%-10s%-10s"%(amount, unit, item))
    repeatCount += 1

##New Serving Size
totalServings = servingSize * newServingSize
print(f'Serves {totalServings}')
