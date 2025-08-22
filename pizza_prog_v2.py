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

Welcome to my Pizza Program!

In this program 


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

            if low <= response <= high:
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


def show_extras_menu(extras, extra_prices):
    """Shows a menu for users to see what extras they can order"""
    extras_dict = {
        'Extras': extras,
        'Extra Prices': extra_prices
    }
    completed_extras_frame = pd.DataFrame(extras_dict)

    # Rearranging index
    completed_extras_frame.index = np.arange(1, len(completed_extras_frame) + 1)
    print()
    make_statement("Extras Menu", "🍟")
    print(completed_extras_frame)


def show_total_costs(pizzas, pizza_prices,extras, extra_prices):
    """Shows the total order """
    total_dict = {
        'Pizza': pizzas,
        'Pizza Prices': pizza_prices,
        'Extras': extras,
        'Extra Prices': extra_prices
    }
    total_costs_frame = pd.DataFrame(total_dict)

    # Rearranging index
    total_costs_frame.index = np.arange(1, len(total_costs_frame) + 1)
    print()
    make_statement("Total Costs", "🧾")
    print(total_costs_frame)


def get_extras_selection(extras, extra_prices):
    """Allows user to select extras and returns the total cost of selected extras"""
    total_extras_cost = 0
    selected_extras = []

    show_extras_menu(extras, extra_prices)
    user_choice = int_check("Select an extra (0 to finish): ", 0, len(extras))

    selected_extras.append(extras[user_choice - 1])
    total_extras_cost += extra_prices[user_choice - 1]
    print(f"Added {extras[user_choice - 1]} for ${extra_prices[user_choice - 1]}")

    return selected_extras, total_extras_cost


# Variables
MAX_PIZZAS = 5
order_type_ans = ('pickup', 'delivery')
total_pizza_made = 0
MAX_PER_ORDER = 5

user_pizza_list = []
user_pizza_list_cost = []

user_extras_list = []
user_extras_list_cost = []
# buy max 3 pizzas but if less total remaining buy less

max_remaining = MAX_PIZZAS - total_pizza_made

max_allowed = min(MAX_PER_ORDER, max_remaining)

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
    phone_number = num_check("What is your phone number? ")
    address = not_blank("Please enter your address: ")
    delivery_surcharge = 9
    print(f"There is a ${delivery_surcharge} surcharge for delivery.")

num_of_pizzas = int_check("How many pizzas? ", 1, 5)

for i in range(num_of_pizzas):

    show_menu("pizza", pizzas, pizza_prices)

    user_selection = int_check("Select a pizza: ", 1, 10)

    pizza = user_pizza_list.append(pizzas[user_selection - 1])
    pizza_cost = user_pizza_list_cost.append(pizza_prices[user_selection - 1])

    print(f"You selected {pizzas[user_selection - 1]} ${pizza_prices[user_selection - 1]}")

    # Get product details

    want_extras = string_check("Do you want extras? ")

    if want_extras == "yes":
        # Get extras
        selected_extras, total_extras_cost = get_extras_selection(extras, extra_prices)
        chosen_extras = extras[user_selection - 1]
        extra_costs = extra_prices[user_selection - 1]
    else:
        chosen_extras = "NA"
        extra_costs = 0

    user_extras_list.append(chosen_extras)
    user_extras_list_cost.append(extra_costs)

# Display Itemised costs

show_total_costs(user_pizza_list, user_pizza_list_cost, user_extras_list, user_extras_list_cost)
if order_type == "delivery":
    print(f"\nThere is a delivery surcharge of: ${delivery_surcharge:.2f}")
total_cost = sum(user_pizza_list_cost )+ sum(user_extras_list_cost)
print(f"\nYour total order cost is: ${total_cost:.2f}")
# print(f"Extras selected: {', '.join(selected_extras) if selected_extras else 'None'}")
