# Shazia Patel
# 6/27/2024
# P2LAB2
# Program that creates a dictionary where the key and value pairs

# Create dictionary
cars = {"Camaro" : 18.21, "Prius" : 52.36, "Model S" : 110, "Silverado" : 26}
# Displays keys
keys = cars.keys()
print(keys)
print()
# get input from user
car_input = input("Enter a vehicle to see is mpg: ")
print()
# Get the mpg associated with the vehicle
mpg_output = cars[car_input]
print(f'The {car_input} gets {mpg_output} mpg.\n')
# get the distance
distance = float(input(f'How many miles will you drive the {car_input}? '))
print()
# calculate gallons of gas need
gallons = distance/mpg_output
# print gallons needed to drive the car
print(f'{gallons:.2f} gallon(s) of gas are needed to', end=' ')
print(f'drive the {car_input} {distance} miles. ')
