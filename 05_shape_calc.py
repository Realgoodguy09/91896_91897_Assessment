# function goes here
def area(length):

    area = (length*length)
    area = float(area)
    return area 


# main routine goes here


area1 = area(int(input("Length: ")))

print("the area is {}".format(area))