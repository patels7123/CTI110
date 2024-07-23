# Shazia Patel
# 7/11/2024
# P4LAB2
# This program will dislay a multiplication table

# Use while to control the program

keep_going = "yes"

while keep_going.lower() == "yes":
    # forloop goes here
    num = int(input("Enter an integer: "))
    print("\n")

    if num >= 0:
        for i in range(1, 12 + 1):
            print(f'{num} * {i} = {num * i}')
        print("\n")
    else:
        print("This program does not handle negative number")
        print("\n")
        
    keep_going = input("Would you like to run the program again? Enter yes or no: ")
    print("\n")
    
print("Exiting program...")
