# Shazia Patel
# 6/25/2024
# P2lab1
# assignmet tests student's knowledge of how to write code
# that performs methematical calculations and displays information to users
# lists
num_list = []
# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter a number: "))
# num3 = float(input("Enter a number: "))
# num4 = float(input("Enter a number: "))
# num5 = float(input("Enter a number: "))
# num_list = [num1,num2,num3,num4,num5]
# print(num_list)

num1=float(input("Enter a number: "))
num_list.append(num1)
num1=float(input("Enter a number: "))
num_list.append(num1)
num1=float(input("Enter a number: "))
num_list.append(num1)
num1=float(input("Enter a number: "))
num_list.append(num1)
num1=float(input("Enter a number: "))
num_list.append(num1)


lowest = min(num_list)
print(lowest)
highest = max(num_list)
print(highest)
total = sum(num_list)
print(total)
length = len(num_list)
Avg = total /length
print(Avg)
num_list.remove(lowest)
print(num_list)
