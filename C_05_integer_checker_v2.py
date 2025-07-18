# Functions go here
def int_check(question, low, high):
    """Checks users enter an integer between to values"""

    error = f"Oops - please enter an integer between {low} and {high}"

    while True:
        response = input(question).lower()

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(response))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes
while True:
    print()

    # ask user for an integer
    my_num = int_check("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")
