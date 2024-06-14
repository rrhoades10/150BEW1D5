# Python Exceptions
# try and except
# exception handling in python allows us to gracefully deal with errors
# and guide users to correctly use the program with nice little messages

# except portion of the try and accept is going to catch any exceptions that happen in our code
# exception is an error that python throws during execution of the code

# try: #this is going to attempt to run a block of code
#     # code that might cause an exception
#     # ValueError - we cant convert letter characters a string
#     # user_input = int(input("Please enter a number: "))
#     # print(user_input)
    
# except: # will catch potential errors without breaking the program
#     # any code that we use to handle the exception
#     print("Please enter a valid number and try again! ")


# stating the exception we're checking for
# try: #this is going to attempt to run a block of code
#     # code that might cause an exception
#     # ValueError - we cant convert letter characters a string
#     user_input = int(input("Please enter a number: "))
#     print(user_input)
# except ValueError: # will catch potential errors without breaking the program
#     # any code that we use to handle the exception
#     print("Please enter a valid number and try again! ")



# stating the exception we're checking for
# USING MORE THAN ON EXCEPTION
# try: #this is going to attempt to run a block of code
#     # code that might cause an exception
#     # ValueError - we cant convert letter characters a string
#     user_input = int(input("Please enter a number: "))
#     result = 100/user_input
#     print(result)
# except ValueError: # will catch potential errors without breaking the program
#     # any code that we use to handle the exception
#     print("Please enter a valid number and try again! ")
# except ZeroDivisionError:
#     # Code to handle exception of dividing by 0
#     print("Sorry, infinity is not something I can handle. Please enter a non-zero number.")

# multiple exceptions in one except block
# try: #this is going to attempt to run a block of code
#     # code that might cause an exception
#     # ValueError - we cant convert letter characters a string
#     user_input = int(input("Please enter a number: "))
#     result = 100/user_input
#     print(result)
# # except to hand both ValueError and ZeroDivisionError
# except (ValueError, ZeroDivisionError): # will catch potential errors without breaking the program
#     # any code that we use to handle the exception
#     print("Please enter a valid number that is also not 0. ")

# catching other potential errors
def complex_calculation(data):
    result = 0
    for item in data:
        result += int(item) ** 2
    average = result /len(data)
    return average
# function to handle a ValueError Exception
# removes strings that are not numbers
def remove_letters(data):
    for char in data:
        if isinstance(char, str) and not char.isdigit():
            data.remove(char)
    
# handleing exceptions with the above function
try:
    # creating a data variable that may have invalid data
    data = ["1", "2", 3, 4, "a"]
    result = complex_calculation(data)
    print(result)
except ValueError:
    print("Your list didn't had a letter character, trying to fix... ")
    remove_letters(data)
    print(complex_calculation(data))
    
except ZeroDivisionError:
    print("Make sure your list isn't empty")
# handling other general exceptions
# raises a general exception based on the error
# as -> renaming the exception as e so we dont need to keep typing out exeption in the handling portion
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# try, except, else - else will only run if the try is successful
# try:
#     number = int(input("Please enter a number: "))
# except ValueError:
#     print("Thats not a number!")
# # this will run if the try is succesful
# else:
#     print(f"You successfully enter a number, here it is: {number}")

def add_nums(num1, num2):
    return num1 + num2

# try:
#     num1 = int(input("Please enter a number: "))
#     num2 = int(input("Please enter another number: "))
# except:
#     print("Please enter a valid number")
# else:
#     # calling the funciton if we're successfully able to collectr numbers
#     print(add_nums(num1, num2))


# try, except, finally
# finally block will run regardless of an exception
# try:
#     number = int(input("Please enter a number: "))

# except: 
#     print("Please enter a valid number")
# # finally block will run regardless of an exception
# finally:
#     print("Whether or not you entered in a valid number, just know your feelings are valid! :)")


# using the raise keyword to raise exceptions
fuel_level = 10
# if fuel_level < 0:
#     raise ValueError("Fuel Level cannot be negative")
# else:
#     print("You should be good to go!")

try: 
    if fuel_level < 0:
        raise ValueError("Fuel Level cannot be negative")
    else:
        print("You're good to go for another few miles")
except ValueError:
    print("Something maybe wrong with your gas tank. Otherwise you cant have negative fuel")

# creating our own exceptions
# and raising those exceptions
class FuelTankOverflowError(Exception):
    """Exception raised when the fuel tank is overfilled"""
    pass


fuel_level = 50
tank_capacity = 40
if fuel_level > tank_capacity:
    raise FuelTankOverflowError("Fuel has exceeded the tank capacity")





