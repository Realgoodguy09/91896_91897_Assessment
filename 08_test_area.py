def askshape():
    print("Select Shape.")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")
    print("5.Parallelogram")
    print("6.Trapezium")

# function that contains code to find the area of each shape
def shape_calc_area(question):
    

    while True:
        try:
            
            print()
            print()
            print()
            shape = input(question).lower()
        
            # code to find square area
            if shape == "1":
                n1 = float(input("length: "))
                print("Area = ", n1*n1)
                
                
            # Code to find area of rectangle
            elif shape == "2":
                n1 = float(input("length: "))
                n2 = float(input("width: "))
                print("Area = ", n1*n2)
                
            # Calculate area of a triangle
            elif shape == "3":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
                print("Area = ", (n1*n2)/2)
            
            # Calculate area of a circle
            elif shape == "4":

                pi = 3.14159265359
                # Asks user what value they have between radius and diameter
                data = input("Please enter the data you have(radius/diameter): ").lower()

                while True:
                    if data == "radius":
                        n1 = float(input("radius: "))
                        break


                    elif data == "diameter":
                        n0 = float(input("diameter: "))
                        n1 = n0/2
                        break

                                    
                    else:
                        print("invalid response.")

                print("Area = ", n1*pi)

            # Calculates area of a parallelogram
            elif shape == "5":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
                print("Area = " , n1*n2)

            # Calculates area of a trapezium
            elif shape == "6":
                n1 = float(input("side 1: "))
                n2 = float(input("side 2: "))
                n3 = float(input("height: "))
                print("Area = ", (n1+n2)/2*n3)


            else:
                print("Please enter a valid choice. ")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        break
        


calc_question = "Enter choice(1/2/3/4/5/6): "


print()
print()
print()
print()

askshape()
area = shape_calc_area(calc_question)

