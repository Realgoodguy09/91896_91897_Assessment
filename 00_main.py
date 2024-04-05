# functions go here
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



# main routine goes you

print("This is a program that calculates the perimeter or area of a shape. ")
response = yes_no("Would you like to see instructions? ")
while True:
    if response == 'yes':
        print("you will be asked to enter a shape.")
        print("valid shapes are... circle, square, rectangle, triangle, parallelogram, and trapezium.")
        print()
        print()
        print("you will then be asked for the needed values, such as the length, width, height and such.")
