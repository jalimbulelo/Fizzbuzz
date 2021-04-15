

def start():

    bomb = False
    while bomb != True:
        bomb = user_input()


def user_input():

        number = 0
        while True:
            try:
                number = int(input("Please enter number: "))
                fizzbuzz(number)
                finished = finish()
                return finished
            except ValueError:
                print("Oops invalid input")
          

def finish():
    re_run = False 

    while re_run == False:
        out = input("Would you like to continue Y/N: ")
        output = out.upper()
    
        if output == "Y":
            return False
        elif output == "N":
            return True  
        else:
            pass

      
def fizzbuzz(number):

    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(str(number) + " is not Fizzbuzzable")

if __name__ == "__main__":

    start()
    