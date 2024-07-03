# Shazia Patel
# 6/30/2024
# P2HW2
# Assignment assess understanding of Lists
#
# *************** Pseudocode **************
# Ask user "Enter your grade for Module 1:"
# Input grade for Module 1
# Ask user "Enter your grade for Module 2:"
# Input grade for Module 2
# Ask user "Enter your grade for Module 3:"
# Input grade for Module 3
# Ask user "Enter your grade for Module 4:"
# Input grade for Module 4
# Ask user "Enter your grade for Module 5:"
# Input grade for Module 5
# Ask user "Enter your grade for Module 6:"
# Input grade for Module 6
# Display "-------------Results------------------"
# Calculate Lowest grade
# Display "Lowest Grade:", lowest
# Calculate Highest Grade
# Display "Highest Grade:", highest 
# Calculate Sum of Grades
# Display "Sum of Grades:", total
# Calculate length= len(num_list)
# Calculate Avg = (total / length)
# Display "Average:", Avg
# Display "--------------------------------------"

num_list = []

num1=float(input("Enter grade for Module 1: "))
num_list.append(num1)
num1=float(input("Enter grade for Module 2: "))
num_list.append(num1)
num1=float(input("Enter grade for Module 3: "))
num_list.append(num1)
num1=float(input("Enter grade for Module 4: "))
num_list.append(num1)
num1=float(input("Enter grade for Module 5: "))
num_list.append(num1)
num1=float(input("Enter grade for Module 6: "))
num_list.append(num1)

print()

print(12 * "-"+"Results"+12*"-")

lowest = min(num_list)
print(f'{"Lowest Grade:":<20}{lowest:.1f}')
highest = max(num_list)
print(f'{"Highest Grade:":<20}{highest:.1f}')
total = sum(num_list)
print(f'{"Sum of Grades:":<20}{total:.1f}')
length = len(num_list)
Avg = total /length
print(f'{"Average:":<20}{Avg:.2f}')

print(31 * "-")

