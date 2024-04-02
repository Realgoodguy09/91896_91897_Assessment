# funtion goes here
def shape_chooser(question):
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
print("Please pick a shape")

shape = shape_chooser("Shape: ")

print("you have chosen a {}".format(shape))