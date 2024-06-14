# exception handling within a while loop
inventory = []

def add_item(inventory):
    item = input("What would you like to add to your inventory? ")  
    
    inventory.append(item)
    print(inventory)
    "* Wash Dishes - the dishes are dirty - 6/15/2014"
def remove_item(inventory):
    # take an item via user input and try to remove it from the list
    try:
        item = input("What item would you like to remove? ")
        inventory.remove(item)
    # removing an item from a list that doesnt exist throws an error
    # handle trying to remove something that we havent added to our inventory yet
    except: # raise a ValueError for something that doesn't exist inside the list.
        print(f"{item} does not exist. You can't remove things that don't exist!")

    # you can also use a conditional to check if the item exists before trying to remove it
    item = input("What would you like to remove? ")
    if item in inventory:
        inventory.remove(item)
        print(inventory)
    else:
        print("You dont have that item. ")
    

def main(inventory):
   
    while True:
        response = input("What would you like to do? 1. add 2. remove 3. quit")
        if response == "1":

            
            add_item(inventory)

        elif response == "2":
            remove_item(inventory)
        elif response == "3":
            print("Have a nice adventure!")
            for item in inventory:
                print(item)
        else:
            print("Please enter 1, 2, or 3")

# main(inventory)




# **Problem Statement**:
# An online bookstore is processing orders for a popular novel. 
# They need a simple system to ensure that customers enter a valid quantity when placing their orders.

# **Instructions**:

# 1. Prompt the user to enter the quantity of books they wish to order.
# 2. Validate the input to ensure it is a positive integer.
# 3. If the input is valid, confirm the order by printing a message.
# 4. If the input is invalid (not an integer or a negative number), display an error message and prompt the user again.
# 5. Use a try/except block to catch non-numeric inputs.

# **Hints**:

# - Use a while loop to keep asking for input until a valid quantity is entered.
# - Utilize the `int()` function to convert the input to an integer and catch `ValueError` for non-numeric inputs.

# while True:
#     try:
#         user_input = int(input("Enter the amount of books you would like to order: "))
#         if user_input > 0:
#             print(f"You ordered {user_input} books.")
#             break
#         else:
#             raise ValueError("Please enter a positive number")
        
#     except ValueError:
#         print("Please enter a valid number")
#   defines the function
def validate_order_2():
    # how many times does this thing need be delcared 
    orders = [] #declare the orders list variable ONE TIME outside of the while
    while True:        
        response = input("enter item to add to your orders or say quit to quit")
        if response == "quit":
            break
        else:
            orders.append(response)
            print(orders)
# calls the function which runs the code
# validate_order_2()


def validate_order():
    while True:
        try:
            quantity = int(input("Enter the quantity of books you want to order."))
            if quantity > 0:
                print(f"You ordered {quantity} books!")
                break
            else:
                print("Invalid quantity, please enter a positive number")
        except ValueError:
            print("Invalid input, please enter a number!")

# call the function
validate_order()


