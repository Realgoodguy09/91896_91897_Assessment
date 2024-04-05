# function goes here
def not_blank(question):


    while True:
        response = input(question)

        # If response is blank, outputs error
        if response == '':
            print("Sorry, this can't be blank. Please try again")
        else:
            return response
        


# main routine goes here
