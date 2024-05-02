# used to print space between each run / restart
print()
print()
print()
print()

# functions go here

def peri_area(question):


    while True:
        response = input(question).lower()

        if response == "perimeter":
            return "perimeter"
        
        elif response == "area":
            return "area"
        
        else:
            print("Please enter a valid response (perimeter / area).")