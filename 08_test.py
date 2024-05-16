# Asks user if 
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
    

    while True:
        shape = input(question).lower()
        try:
            if shape == "1":
                n1 = float(input("length: "))
                area = (n1*n1)
                return area

            elif shape == "2":
                n1 = float(input("length: "))
                n2 = float(input("width: "))
                area = (n1*n2)
                return area
            elif shape == "3":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
            
            
            elif shape == "4":

                n1 = float(input("radius: "))


            elif shape == "5":
                n1 = float(input("base: "))
                n2 = float(input("height: "))
                area = (n1*n2)

            
            elif shape == "6":
                n1 = float(input("side 1: "))
                n2 = float(input("side 2: "))
                n3 = float(input("height: "))


            else:
                print("Please enter a valid choice. ")

        except ValueError:
            print("Invalid input. Please enter a number.")
            

print("Select Shape.")
print("1.Square")
print("2.Rectangle")
print("3.Triangle")
print("4.Circle")
print("5.Parallelogram")
print("6.Trapezium")
area = shape_calc_area("Enter choice(1/2/3/4/5/6): ")

print(area)