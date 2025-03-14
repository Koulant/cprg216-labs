# Assignment: Programming Strategies
# Author: Anton Koulikov

# Use module 1 and 2 content only
# Part 1

# Variables
profit = 0
category = 0
profit1 = 120.45
profit2 = 99.50
profit3 = 75.69
profit4 = 65.73
profit5 = 51.49

# Revised part 1 code
print("Welcome to Circle Phones’ Profit calculator.")
category = 0
while category < 6:
    category = int(input("Enter product number 1-5, or enter 0 to stop: "))
    if category == 1:
        quantity = int(input("Enter quantity sold: "))
        profit += profit1 * quantity
        continue
    if category == 2:
        quantity = int(input("Enter quantity sold: "))
        profit += profit2 * quantity
        continue
    if category == 3:
        quantity = int(input("Enter quantity sold: "))
        profit += profit3 * quantity
        continue
    if category == 4:
        quantity = int(input("Enter quantity sold: "))
        profit += profit4 * quantity
        continue
    if category == 5:
        quantity = int(input("Enter quantity sold: "))
        profit += profit5 * quantity
        continue
    elif category == 0:
        break
    else:
        print("Error: Invalid input.")
print("Your total profit for today is: $", profit)


