# function goes here
def square_area(length):

    area = (length*length)
    return area


# main routine goes here


area = square_area(int(input("Length: ")))

print("the area is {}".format(area))