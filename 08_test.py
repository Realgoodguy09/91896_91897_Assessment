def peri_area(question):


    while True:
        operation = input(question).lower()

        if operation == "perimeter":
            return "perimeter"
        
        elif operation == "area":
            return "area"
        
        else:
            print("Please enter a valid response (perimeter / area).")

def shape_calc_area(question):
    # get the shape the user wants

    while True:
        shape = input(question).lower()
        try:
            if shape == "square":
                n1 = float(input("length: "))
                area = (n1*n1)
                return area

            elif shape == "retangle":
                n1 = float(input("length: "))
                n2 = float(input("width: "))
                area = (n1*n2)
                return area

            elif shape == "parallelogram":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
                area = ()

            elif shape == "triangle":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
            
            elif shape == "trapezium":
                n1 = float(input("side 1: "))
                n2 = float(input("side 2: "))
                n3 = float(input("height: "))

            elif shape == "circle":

                n1 = float(input("radius: "))

            else:
                print("Please enter a valid shape")

        except ValueError:
            print("Invalid input. Please enter a number.")
            
