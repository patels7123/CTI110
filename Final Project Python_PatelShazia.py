# Shazia Patel
# 7/22/2024
# Final Python Project Grocery shopping, check out receipt and the change of self-checkout

dict1 = {1:['apples', 3.69],
         2:['berries', 4.00],
         3:['chocolate', 2.89],
         4:['turkey', 6.99],
         5:['cheese', 4.00],
         6:['pepsi', 7.89],
         7:['eggs', 3.50],
         8:['bread', 3.00]}

# Print the names of the columns.
print()
print("{:<30} {:<30}".format('Grocery Item', 'Price'))
print("------------------------------------")
# print each data item.
for key, value in dict1.items():
    items, price = value
    print("{:<30} ${:.2f}".format(items, price))
print("------------------------------------\n")

# Get the grocery items in the cart
grocery_list = []

more_items = True

print("*Welcome to the Grocery Checkout*\n")

while more_items:
    grocery_item = input("Enter an item to add to the cart or type 'end' to stop adding items: ")
    grocery_list.append(grocery_item)

    if grocery_item == 'apples':
        more_items = True
    elif grocery_item == 'berries':
        more_items = True
    elif grocery_item == 'chocolate':
        more_items = True
    elif grocery_item == 'turkey':
        more_items = True
    elif grocery_item == 'cheese':
        more_items = True
    elif grocery_item == 'pepsi':
        more_items = True
    elif grocery_item == 'eggs':
        more_items = True
    elif grocery_item == 'bread':
        more_items = True
    elif grocery_item == "end":
        more_items = False
        # remove the "end" word from the cart list.
        grocery_list.remove("end")
        print('\nThe items currently in your cart are:')
        print('\n'.join(map(str, grocery_list)))

        # Make a list of cart items and add the price of the cart items
        receipt_list = []
        a = 'apples'
        b = 'berries'
        c = 'chocolate'
        d = 'turkey'
        e = 'cheese'
        f = 'pepsi'
        g = 'eggs'
        h = 'bread'
        # Print the Checkout Receipt
        print('\nGrocery Checkout Receipt')
        print('------------------------------')
        
        if a in grocery_list:
            print(f'{a:<25}${3.69}')
            item = 3.69
            receipt_list.append(item)
        if b in grocery_list:
            print(f'{b:<25}${4.00:.2f}')
            item = 4.00
            receipt_list.append(item)
        if c in grocery_list:
            print(f'{c:<25}${2.89}')
            item = 2.89
            receipt_list.append(item)
        if d in grocery_list:
            print(f'{d:<25}${6.99}')
            item = 6.99
            receipt_list.append(item)
        if e in grocery_list:
            print(f'{e:<25}${4.00:.2f}')
            item = 4.00
            receipt_list.append(item)
        if f in grocery_list:
            print(f'{f:<25}${7.89}')
            item = 7.89
            receipt_list.append(item)
        if g in grocery_list:
            print(f'{g:<25}${3.50:.2f}')
            item = 3.50
            receipt_list.append(item)
        if h in grocery_list:
            print(f'{h:<25}${3.00:.2f}')
            item = 3.00
            receipt_list.append(item)
        # Calculate the total amount of cart items
        sub_total = sum(receipt_list)
        print(f'\n{"SUBTOTAL:":<15}${sub_total:.2f}\n')
        # Print the tax amout
        print(f'{"TAX:":<15}${0.21:.2f}')
        # Print the total with the tax amout 
        total = (sub_total + 0.21)
        print(f'{"TOTAL:":<15}${total:.2f}')
        
    elif grocery_item == " ":
        grocery_list.remove(" ")
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != 'berries':
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != 'chocolate':
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != 'turkey':
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != 'cheese':
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != 'pepsi':
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != 'eggs':
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != 'bread':
        print("That item is not in stock.\n")
        more_items = True
    elif grocery_item != "apples":
        print("That item is not in stock.\n")
        more_items = True
   

def disperse_change(change):
        
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
            print(num_dollars,  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")
                
    if num_quarters > 0:
            print(num_quarters,  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")

    if num_dimes > 0:
            print(num_dimes,  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")

    if num_nickles > 0:
            print(num_nickles,  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")

    if num_pennies > 0:
            print(num_pennies,  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")


#Main Function
def main():
    # display the amount owed
    print()
    print(f"\nYou owe ${total:.2f} for the groceries\n")

    # prompt user to enter float amount as the cash they will into checkout machine
    amount_paid = float(input("How much cash will you put in the self-checkout machine? $"))

    # Calculate change owed
    change_owed = amount_paid - total

    # Display change owed
    print(f"\nThe change owed to you is ${change_owed:.2f}")
    print()

    # Convert the change owed to an integer
    change_owed = round(change_owed * 100)

    # call function and pass the change owed as a parameter
    print('Dispensing...\n')
    disperse_change(change_owed)
    

#Call the main function
main()



































