import pandas as pd
import numpy as np

# Functions go here


def num_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer"

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or 'n' letters of a word from a valid list"""
    while True:
        response = input(question).lower()
        for item in valid_answers:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "ℹ️")
    print('''

For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the 
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket 
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free).

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        print("Sorry, this can't be blank.  Please try again.\n")


def int_check(question, low, high):
    """Checks users enter an integer"""
    error = f"Oops - please enter a number between {low} and {high}."
    while True:
        try:
            response = int(input(question))

            if response >= low or response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def show_menu(variable_name, list1, list2):
    """Shows a menu for users to see what they can order"""

    base_name = "_menu_dict"
    dynamic_key = variable_name + base_name
    dynamic_key = {
        'Pizza': list1,
        'Pizza Prices': list2
    }
    completed_menu_frame = pd.DataFrame(dynamic_key)

    # Rearranging index
    completed_menu_frame.index = np.arange(1, len(completed_menu_frame) + 1)
    print()
    make_statement("Menu", "📋")
    print(completed_menu_frame)


# Variables
MAX_PIZZAS = 5
order_type_ans = ('pickup', 'delivery')

# Variable lists

pizzas = ['Cheese', 'Italian', 'Meat Lovers', 'Pepperoni', 'Ham & Cheese', 'Vegetable',
          'Hawaiian', 'Chicken', 'Double Cheese', 'Spicey']
pizza_prices = [7, 8.5, 10, 6, 7, 7.5, 9.5, 12, 9, 13.5]

extras = ['Fries', 'Onion rings', 'Ice Cream']

extra_prices = [6, 7, 8.5]

# Main routine
make_statement("Pizza Program", "🍕")

print()
want_instructions = string_check("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()



print()
name = not_blank("What is the name for this order? ")

order_type = string_check("Is this order pickup or delivery? ", order_type_ans, 1)

if order_type == "pickup":
    phone_number = num_check("What is your phone number? ")
else:
    phone_number = int_check("What is your phone number? ")
    address = not_blank("Please enter your address: ")
    print("There is a $9 surcharge for delivery.")

show_menu("pizza", pizzas, pizza_prices)

user_selection = int_check("Select a pizza: ", 1, 10)

print(f"You selected {pizzas[user_selection - 1]} ${pizza_prices[user_selection - 1]}")
