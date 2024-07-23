# Shazia Patel
# 7/11/2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules
print()
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
print()
print(12 * "-"+"Results"+12*"-")
lowest = min(grades)
print(f'{"Lowest Grade:":<20}{lowest:.1f}')
highest = max(grades)
print(f'{"Highest Grade:":<20}{highest:.1f}')
total = sum(grades)
print(f'{"Sum of Grades:":<20}{total:.1f}')
length = len(grades)
Avg = total /length
print(f'{"Average:":<20}{Avg:.2f}')
print(31 * "-")

# determine letter grade for average
if Avg >= 90:
    print('Your grade is: A')

elif Avg >= 80:
    print('Your grade is: B')

elif Avg >= 70:
    print('Your grade is: C')

elif Avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F')

