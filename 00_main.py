# functions go here

# Function to print all possible shapes
def askshape():
    print("Select Shape.")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")
    print("5.Parallelogram")
    print("6.Trapezium")

# Area calculator
def shape_calc_area(question):
    

    while True:
        try:
            

            print()
            shape = input(question).lower()
        
            # code to find square area
            if shape == "1":
                n1 = float(input("length: "))
                print("Area = ", n1*n1)
                break
                
                
            # Code to find area of rectangle
            elif shape == "2":
                n1 = float(input("length: "))
                n2 = float(input("width: "))
                print("Area = ", n1*n2)
                break
                
            # Calculate area of a triangle
            elif shape == "3":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
                print("Area = ", (n1*n2)/2)
                break
            
            # Calculate area of a circle
            elif shape == "4":

                # the value of pi used for calculations
                pi = 3.14159265359
                # Asks user what value they have between radius and diameter
                
                while True:
                    data = input("Please enter your data type. radius(r)/diameter(d): ").lower()

                    if data == "radius" or data == "r":
                        n1 = float(input("radius: "))
                        break


                    elif data == "diameter" or data == "d":
                        n0 = float(input("diameter: "))
                        n1 = n0/2
                        break

                                    
                    else:
                        print("invalid response.")

                print("Area = ", (n1*n1)*pi)
                break

            # Calculates area of a parallelogram
            elif shape == "5":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
                print("Area = " , n1*n2)
                break


            # Calculates area of a trapezium
            elif shape == "6":
                n1 = float(input("side 1: "))
                n2 = float(input("side 2: "))
                n3 = float(input("height: "))
                print("Area = ", (n1+n2)/2*n3)
                break

            else:
                print("Please enter a valid choice. ")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue



# Area calculator
def shape_calc_peri(question):
    
    while True:
        try:
            

            print()
            shape = input(question).lower()
        
            # code to find square area
            if shape == "1":
                n1 = float(input("length: "))
                print("Perimeter = ", n1*4)
                break
                
                
            # Code to find area of rectangle
            elif shape == "2":
                n1 = float(input("length: "))
                n2 = float(input("width: "))
                print("Perimeter = ", (n1*2)+(n2*2))
                break
                
            # Calculate area of a triangle
            elif shape == "3":
                n1 = float(input("side 1: "))
                n2 = float(input("side 2: "))
                n3 = float(input("side 3: "))
                print("Perimeter = ", n1+n2+n3)
                break
            
            # Calculate area of a circle
            elif shape == "4":

                # the value of pi used for calculations
                pi = 3.14159265359

                while True:
                    data = input("Please enter your data type. radius(r)/diameter(d): ").lower()

                    if data == "radius" or data == "r":
                        n1 = float(input("radius: "))
                        break


                    elif data == "diameter" or data == "d":
                        n0 = float(input("diameter: "))
                        n1 = n0/2
                        break

                                    
                    else:
                        print("invalid response.")

                print("Perimeter = ", 2*pi*n1)
                break


            # Calculates area of a parallelogram
            elif shape == "5":
                n1 = float(input("base: "))
                n2 = float(input("side: "))
                print("Perimeter = " , 2*(n1+n2))
                break

            # Calculates area of a trapezium
            elif shape == "6":
                n1 = float(input("base 1: "))
                n2 = float(input("base 2: "))
                n3 = float(input("side 1: "))
                n4 = float(input("side 1: "))
                print("Perimeter = ", n1+n2+n3+n4)
                break
            # Loops if response is invalid
            else:
                print("Please enter a valid choice. ")

        # if user enters wrong data code loops and doesn't break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue



# Function that asks the user if they want to calculate area or peri
def peri_area(question):


    while True:
        operation = input(question).lower()

        # Returns Perimeter if chosen
        if operation == "perimeter" or operation == "p":
            return "perimeter"
        
        # Returns Area if chosen
        elif operation == "area" or operation == "a":
            return "area"
        
        # Incase of invalid response, loops
        else:
            print("Please enter a valid response (perimeter(p) / area(a)).")

# function to end code
def end(question):

    while True:
        end = input(question).lower()

        if end == "no" or end == "n":
            return "no"
        
        elif end == "yes" or end == "y":
            return "yes"
        
        else:
            print("Invalid response.")


# Variables
calc_question = "Enter choice(1/2/3/4/5/6): "

# Main Routine

while True:

    print()
    operation = peri_area("Please select operation.(perimeter(p) / area(a)): ")
    print()

    if operation == "area":
        askshape()
        area = shape_calc_area(calc_question)
        end("Continue to next calculation? (yes / no) ")
        if end == "no":
            quit()

    elif operation == "perimeter":
        
        askshape()
        perimeter = shape_calc_peri(calc_question)
        end("Continue to next calculation? (yes / no) ")
        if end == "no":
            quit()

    