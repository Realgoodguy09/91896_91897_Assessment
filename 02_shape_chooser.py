# blanks for space between each test
print()
print()
print()
print()
print()

# yes_no function for testing purposes
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

# main funtion for development goes here
def ask_shape(question):
    # get the shape the user wants

    while True:
        shape = input(question).lower()
        if shape == "circle":
            return "circle"
        
        elif shape == "square":
            return "square"
        
        elif shape == "rectangle":
            return "rectangle"
        
        elif shape == "triangle":
            return "triangle"
        
        elif shape == "parallelogram":
            return  "parallelogram"
        
        elif shape == "trapezium":
            return "trapezium"
        
        else:
            print("Please enter a valid shape")



# main routine goes here

while True:
    shape = ask_shape("Please pick a shape. ")

    confirm_shape = yes_no("Do you wish to select {}? ".format(shape))
    
    
    if confirm_shape == "yes":
        break

    else:
        print("Returning to slection...")

print("continuing...")