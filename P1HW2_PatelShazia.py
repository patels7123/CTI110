# Shazia Patel
# 6/20/2024
# P1HW2
# Calculating Expense and Budget.
#
# *************** Pseudocode **************
# Ask user "Please enter your Budget"
# Display "---------------------------------------------------------"
# Input Budget
# Ask user "Please enter your travel destination"
# Display "---------------------------------------------------------"
# Input destination
# Ask user "Please enter amount you will spend on gas"
# Display "---------------------------------------------------------"
# Input gas expense
# Ask user "Please enter amount you will spend on accomodation"
# Display "---------------------------------------------------------"
# Input accommodation expense
# Ask user "Please enter amount you will spend on food"
# Display "---------------------------------------------------------"
# Input food expense
# set remaining_Balance = budget - (gas + accomodation + food)
# Display "Destination entered", destination
# Display "Budget entered", budget
# Display "Gas entered", gas
# Display "Accomodation entered", accomodation
# Display "Food entered", food
# Display "---------------------------------------------------------"
# Display "The Remaining Balance is:", remaining_Balance

print()
print("This ptogram calculates and displays travel expenses")
print()
integer1 = int(input("Enter Budget: "))
print()
integer2 = input("Enter your travel destination: ")
print()
integer3 = int(input("How much do you think you will spend on gas? "))
print()
integer4 = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
integer5 = int(input("Last, how much do you need for food? "))
print()
print("-----Travel Expenses----")
print()

print("Location: ",integer2)
print("Initial Budget: ",integer1)
print()
print("Fuel: ",integer3)
print("Accomodation: ",integer4)
print("Food: ",integer5)
print()
print("Remaining Balance: ",integer1-(integer3+integer4+integer5))
