# used to print spaces each restart / run
print()
print()
print()
print()

# function will go here


def yes_no(question):

    # checks user enters a valid response
    while True:
        response = input(question).lower()

        # if answer is yes, returns yes
        if response == 'yes' or response == 'y':
            return 'yes'

        # if answer is no, returns no
        elif response == 'no' or response == 'n':
            return 'no'

        # loops and asks for a valid response
        else:
            print("Please enter yes / no")

# main routine goes here


cheese = yes_no("Do you like cheese? ")

if cheese == "yes":
    print("Noice")

else:
    print("Shame on you.")

print("cheese")
