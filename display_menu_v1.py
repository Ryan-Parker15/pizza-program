import pandas as pd

# lists to store menu details
pizzas = ['Cheese', 'Vege', 'Meat Lovers', 'Pepperoni']
pizza_prices = [7, 8.5, 10, 6]

# Create a dictionary where keys are column names and values are lists of data
pizza_menu_dict = {
    'Pizza': pizzas,
    'Pizza Prices': pizza_prices
}

# Create a Pandas DataFrame from the dictionary
pizza_menu_frame = pd.DataFrame(pizza_menu_dict)

# Print the DataFrame to observe the result
print()
print(pizza_menu_frame)
