# Jeanae Teal
# 11/01/2026
# P1HW2
#  Calculating Travel Expenses
# Calculates and displays travel expenses

print ()
print("This program calculate and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you spend on gas? "))
print()
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food = int(input ("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("--------------Travel Expenses------------------")
print("Location:", destination)
print ("Initial Budget:", budget)

print()
print("Fuel: ", gas)
print("Accomodation: ", accommodation)
print("Food: ", food)

print()

print("Remaining Balance:", remaining_balance)