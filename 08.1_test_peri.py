def askshape():
    print("Select Shape.")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")
    print("5.Parallelogram")
    print("6.Trapezium")



def shape_calc_peri(question):

    while True:
        try:

            print()
            print()
            print()
            shape = input(question).lower()

            # code to find square area
            if shape == "1":
                n1 = float(input("length: "))
                print("Perimeter = ", n1*4)


            # Code to find area of rectangle
            elif shape == "2":
                n1 = float(input("length: "))
                n2 = float(input("width: "))
                print("Perimeter = ", (n1*2)+(n2*2))

            # Calculate area of a triangle
            elif shape == "3":
                n1 = float(input("side 1: "))
                n2 = float(input("side 2: "))
                n3 = float(input("side 2: "))
                print("Perimeter = ", n1+n2+n3)

            # Calculate area of a circle
            elif shape == "4":

                # the value of pi used for calculations
                pi = 3.14159265359

                while True:
                    data = input("do you have radius(r) / diameter(d): ").lower()

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


            # Calculates area of a parallelogram
            elif shape == "5":
                n1 = float(input("base: "))
                n2 = float(input("side: "))
                print("Perimeter = " , 2*(n1+n2))

            # Calculates area of a trapezium
            elif shape == "6":
                n1 = float(input("base 1: "))
                n2 = float(input("base 2: "))
                n3 = float(input("side 1: "))
                n4 = float(input("side 1: "))
                print("Perimeter = ", n1+n2+n3+n4)

            # Loops if response is invalid
            else:
                print("Please enter a valid choice. ")

        # if user enters wrong data code loops and doesn't break
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
perimeter = shape_calc_peri(calc_question)