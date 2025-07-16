import pandas


# lists to store menu details
pizzas = ['Cheese', 'Vege', 'Meat Lovers', 'Pepperoni']
pizza_prices = [7, 8.5, 10, 6]
# 1. Create a dictionary where keys are column names and values are lists of data
pizza_menu_dict = {
    'Pizza': [pizzas],
    'Pizza Prices': [pizza_prices]
}

# 2. Create a Pandas DataFrame from the dictionary
pizza_menu = pandas.DataFrame(pizza_menu_dict)

# 3. Print the DataFrame to observe the result
print()
print(pizza_menu)
