# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating Pickling and Error Handling.
#              Create a program that demonstrates the functionality
#              of pickling and error handling.
# ChangeLog (Who,When,What):
# Daniel White,11.29.2021,Created started script
# Daniel White,11.30.2021,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #
import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = 'GroceryList.dat'
grocery_list = []

# Processing  --------------------------------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file = open(file_name, "wb")
    pickle.dump(list_of_data, file)
    file.close()

def read_data_from_file(file_name):
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

# Presentation (Input/Output)  -------------------------------------------- #
#Get user input for grocery items and their price to begin the grocery list
while True:
    item = input("Enter Your Grocery Store Item: ")
    price = input("Enter the Items Price: $")
    grocery_list = {"Item": item, "Price": price}

    try:
        item = str(item)
        if item.isnumeric():
            raise Exception("Items are not Numbers! Try Again!")

    except Exception as e:
        print(e)
        continue

    try:
        price = float(price)
        break

    except:
        print("Price Must be a Number! Try Again!")
        continue

# TODO: store the list object into a binary file
save_data_to_file(strFileName, grocery_list)

# TODO: Read the data from the file into a new list object and display the contents
print(read_data_from_file(strFileName))
