# Shazia Patel
# 7/6/2024
# P3HW2
# This program takes an employee salary detail, and calculate its over time pay, register salary and gross salary
#
# *************** Pseudocode **************
# Ask user "Enter employee's name:"
# Input employee's name
# Ask user "Enter number hours worked:"
# Input number hours worked
# Ask user "Enter employee's pay rate:"
# Input employee's pay rate
# Display "--------------------------------------"
# Use if statement to check weather employee have worked extra hours
# Calculate extra working hours more than 40 hrs
# calculate extra hours pay with "one & half pay rate"
# Calculate reg hours pay
# Calculate total gross pay
# Use elseif statement to calculate for emplyee worked hours less or equal to 40 hours
# Set OverTime = 0
# Set OverTime_pay = 0
# Calculate reg hours pay for the 40 or less hours
# Calculate total gross pay for the 40 or less hours
# Display employee's name: with little space
# Leave a line space
# Display with one tab space, titles (Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, Gross Pay) with one tab space
# Display "---------------------------------------------------------------------------------------------------"
# Display with two tab space, input(Hours Worked, Pay Rate) and calculated result of(OverTime, OverTime Pay, RegHour Pay, Gross Pay)
# Enter employee name, hours worked and salary detail
print()
emp_name = input("Enter employee's name: ")
hrs_worked = float(input('Enter number hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))


if hrs_worked > 40:
    # Calculate the over time.
    OverTime = hrs_worked - 40
    # Calculate extra hours pay
    OverTime_pay = OverTime * (pay_rate * 1.5)
    # Calculate reg hours pay
    RegHour_Pay = pay_rate * (hrs_worked - OverTime)
    # Calculate total gross pay
    Gross_Pay = OverTime_pay + RegHour_Pay
elif hrs_worked <= 40:
    OverTime = 0
    OverTime_pay = 0
    # Calculate reg hours pay
    RegHour_Pay = pay_rate * hrs_worked
    # Calculate total gross pay
    Gross_Pay = OverTime_pay + RegHour_Pay
    
print(35 * "-")
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
print(95 * "-")
print(f'{hrs_worked:<15.1f}{pay_rate:<12.1f}{OverTime:<12.1f}{OverTime_pay:<20.2f}{"$"}{RegHour_Pay:<20.2f}{"$"}{Gross_Pay:.2f}')


##print(35 * "-")
##print(f'{"Employee name:":<17}{emp_name:}\n')
##print('Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay')
##print(95 * "-")
##print(f'{hrs_worked:.1f}'+f'\t\t{pay_rate:.1f}'+f'\t\t{OverTime:.1f}'+f'\t\t{OverTime_pay:.2f}'+f'\t\t${RegHour_Pay:.2f}'+f'\t\t${Gross_Pay:.2f}')
