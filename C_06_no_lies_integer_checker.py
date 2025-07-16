# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer"

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again.\n")


# Main Routine goes here

# loop for testing purposes
while True:
    print()

    # ask user for their name
    name = not_blank("Name: ")  # replace with call to 'not blank' function!
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue

    else:
        print(f"{name} bought a ticket")
print("The program has ended")