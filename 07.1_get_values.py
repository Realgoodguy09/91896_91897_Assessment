# function added to experiment for main code
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



# gets the values needed for each shape
def get_value(sides):


    if shape == "square":
        v1 = float(input("length: "))

    elif shape == "retangle":
        v1 = float(input("length: "))
        v2 = float(input("width: "))

    elif shape == "triangle":
        v1 = float(input())
