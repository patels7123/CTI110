# Shazia Patel
# 6/25/2024
# P2lab1
# assignmet tests student's knowledge of how to write code
# that performs methematical calculations and displays information to users

# import math module to use the constant, math.pi
import math

# get the radius from the user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate the Diameter
diameter = 2 * radius
circumference = 2 * radius * math.pi
area = math.pi * radius**2

# Display the output
print(f'The diameter of the circle is {diameter:.1f}\n')
print(f'The diameter of the circle is {circumference:.2f}\n')
print(f'The diameter of the circle is {area:.3f}\n')
print('The diameter of the circle is',format(area,'.3f'))
input("Press enter to exit")
