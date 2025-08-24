import pandas as pd
import numpy as np

# Functions go here

def num_check(question):
    """Checks users enter an integer"""
    error = "Oops - please enter an integer"
    while True:
        try:
            # return the response if its an integer
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
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_answers}")


def instructions():
    """Displays instructions if user says yes"""
    make_statement("Instructions", "ℹ️")
    print('''

🍕 Pizza Program Instructions

Welcome to the Pizza Program! This program will guide you through placing your pizza order step by step.

In this program, you will:

- Enter your name and choose if your order is pickup or delivery.
- Select how many pizzas you want (up to 5).
- Choose pizzas from the menu.
- Decide if you would like to add extras (like fries or ice cream).
- See an itemised summary of your order, including all pizzas, extras, and the total cost.

Enjoy!!!
    ''')


def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        print("Sorry, this can't be blank. Please try again.\n")


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


def show_menu(list1, list2):
    """Shows a menu for users to see what they can order"""
    dynamic_key = {
        'Pizza': list1,
        'Pizza Prices': list2
    }
    completed_menu_frame = pd.DataFrame(dynamic_key)
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

    #Rearranging index
    completed_extras_frame.index = np.arange(1, len(completed_extras_frame) + 1)
    print()
    make_statement("Extras Menu", "🍟")
    print(completed_extras_frame)


def show_total_costs(user_pizza_list, user_pizza_list_cost, user_extras_list, user_extras_list_cost):
    """Shows the total order """
    total_dict = {
        'Pizza': user_pizza_list,
        'Pizza Prices': user_pizza_list_cost,
        'Extras': user_extras_list,
        'Extra Prices': user_extras_list_cost
    }
    total_costs_frame = pd.DataFrame(total_dict)

    # Rearranging index
    total_costs_frame.index = np.arange(1, len(total_costs_frame) + 1)
    print()
    make_statement("Total Costs", "🧾")
    print(total_costs_frame)


def get_extras_selection(extras, extra_prices):
    """Allows user to select extras and returns the chosen one and its cost"""
    show_extras_menu(extras, extra_prices)
    user_choice = int_check("Select an extra: ", 1, len(extras))
    chosen_extra = extras[user_choice - 1]
    chosen_cost = extra_prices[user_choice - 1]
    print(f"Added {chosen_extra} for ${chosen_cost}")
    return chosen_extra, chosen_cost

# Main Ordering function code

def process_order():
    # Variables
    pizzas = ['Cheese', 'Italian', 'Meat Lovers', 'Pepperoni', 'Ham & Cheese', 'Vegetable',
              'Hawaiian', 'Chicken', 'Double Cheese', 'Spicey']
    pizza_prices = [7, 8.5, 10, 6, 7, 7.5, 9.5, 12, 9, 13.5]
    extras = ['Fries', 'Onion rings', 'Ice Cream']
    extra_prices = [6, 7, 8.5]

    user_pizza_list = []
    user_pizza_list_cost = []
    user_extras_list = []
    user_extras_list_cost = []

    delivery_surcharge = 0
    credit_surcharge = 0

    print()
    want_instructions = string_check("Do you want to see the instructions? ")
    if want_instructions == "yes":
        instructions()

    print()
    name = not_blank("What is the name for this order? ")

    order_type = string_check("Is this order pickup or delivery? ", ('pickup', 'delivery'), 1)

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
        user_selection = int_check("Select a pizza: ", 1, len(pizzas))

        user_pizza_list.append(pizzas[user_selection - 1])
        user_pizza_list_cost.append(pizza_prices[user_selection - 1])

        print(f"You selected {pizzas[user_selection - 1]} ${pizza_prices[user_selection - 1]}")

        want_extras = string_check("Do you want extras? ")
        if want_extras == "yes":
            chosen_extras, extra_costs = get_extras_selection(extras, extra_prices)
        else:
            chosen_extras, extra_costs = "NA", 0

        user_extras_list.append(chosen_extras)
        user_extras_list_cost.append(extra_costs)

    # Display Itemised costs
    show_total_costs(user_pizza_list, user_pizza_list_cost, user_extras_list, user_extras_list_cost)

    if order_type == "delivery":
        print(f"\nThere is a delivery surcharge of: ${delivery_surcharge:.2f}")

    # Subtotal
    subtotal = sum(user_pizza_list_cost) + sum(user_extras_list_cost) + delivery_surcharge
    print(f"\nSubtotal: ${subtotal:.2f}")

    # Payment method
    payment_type = string_check("Are you paying with cash or credit? ", ('cash', 'credit'), 1)

    if payment_type == "cash":
        print("You picked cash")
    else:
        print("You picked credit")
        card_number = num_check("What is your card number? ")
        credit_surcharge = 3
        print(f"There is a ${credit_surcharge} surcharge for credit.")

    # Final total code
    total_cost = subtotal + credit_surcharge
    print(f"\nYour total order cost is: ${total_cost:.2f}")

    # Confirmation code
    confirm = string_check("Do you want to confirm this order? (yes/no) ")
    if confirm == "no":
        print("\nOrder cancelled.")
    else:
        print("\n✅ Order confirmed! Your food will be ready soon.")

# Program Loop code

make_statement("Pizza Program", "🍕")

while True:
    process_order()
    another = string_check("\nDo you want to make another order? (yes/no) ")
    if another == "no":
        print("\nThank you for using the Pizza Program. Goodbye! 🍕")
        break
    else:
        print("\nStarting a new order...\n")
