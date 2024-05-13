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
def get_value_area(sides):

    try:
        if shape == "square":
            n1 = float(input("length: "))


        elif shape == "retangle":
            n1 = float(input("length: "))
            n2 = float(input("width: "))

        elif shape == "triangle" or "parallelogram":
            n1 = float(input("base: "))
            n2 = float(input("height: "))
        
        elif shape == "trapezium":
            n1 = float(input("side 1: "))
            n2 = float(input("side 2: "))
            n3 = float(input("height: "))
        elif shape == "circle":
            n1 = float(input("radius: "))

    except ValueError:
        print("Invalid input. Please enter a number.")

