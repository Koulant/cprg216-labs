#
# Assignment: Programming Strategies
# Author: Anton Koulikov

# Use module 1 and 2 content only
# Part 2

# Variables
profit = 0
category = 0
profit1 = 120.45
profit2 = 99.50
profit3 = 75.69
profit4 = 65.73
profit5 = 51.49
time_period = 0
period_of_time = "some period of time"

# Start
print("Welcome to Circle Phones Profit calculator")
print("You can calculate the profit of the company according to a specific day or"
      " by a week or divide the week into weekdays and weekend")

time_period = int(input("Enter 1 - For specific day, 2 - For the Week, "
                        "3 - For Week Business Days, 4 - For Weekend days, 0 - Exit: "))

# For a specific day
if time_period == 1:
    print("Enter sales data for a specific day.")
    period_of_time = str(input("Enter a specific day (Monday, Tuesday, Wednesday, Thursday, Friday): "))
    print(f"For {period_of_time}")
    while period_of_time == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday" or "Saturday" or "Sunday":
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
# For the week
elif time_period == 2:
    print("Enter sales data for the week.")
    period_of_time = "the week"
    for n in range(7):
        if n == 0:
            print("For Monday")
        elif n == 1:
            print("For Tuesday")
        elif n == 2:
            print("For Wednesday")
        elif n == 3:
            print("For Thursday")
        elif n == 4:
            print("For Friday")
        elif n == 5:
            print("For Saturday")
        elif n == 6:
            print("For Sunday")
        else:
            print("Error: Invalid input.")
        while category <6:
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
# For week business days
elif time_period == 3:
    period_of_time = "week business days"
    print("Enter sales data for week business days.")
    for n in range(5):
        if n == 0:
            print("For Monday")
        elif n == 1:
            print("For Tuesday")
        elif n == 2:
            print("For Wednesday")
        elif n == 3:
            print("For Thursday")
        elif n == 4:
            print("For Friday")
        else:
            print("Error: Invalid input.")
        while category <6:
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
# For weekend days
elif time_period == 4:
    period_of_time = "weekend days"
    print("Enter sales data for weekend days.")
    for n in range(5, 7):
        if n == 5:
            print("For Saturday")
        elif n == 6:
            print("For Sunday")
        else:
            print("Error: Invalid input.")
        while category <6:
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
elif time_period == 0:
    print("Exiting.")
else:
    print("Error: Invalid input.")
#End
if profit >= 10000:
    print(f"Total Profit for {period_of_time} is: $", round(profit, 2))
    print("You did well this period! Keep up the great work!")
if profit < 10000:
    print(f"Total Profit for {period_of_time} is: $", round(profit, 2))
    print("We didn’t reach our goal for this period. More work is needed.")
