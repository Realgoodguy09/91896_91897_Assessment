# used to print space between each run / restart
print()
print()
print()
print()

# functions go here

def peri_area(question):


    while True:
        operation = input(question).lower()

        if operation == "perimeter":
            return "perimeter"
        
        elif operation == "area":
            return "area"
        
        else:
            print("Please enter a valid response (perimeter / area).")