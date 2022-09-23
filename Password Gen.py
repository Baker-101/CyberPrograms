from random import *
import string

def pasGen(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbol = string.punctuation

    combo = lower + upper + numbers + symbol
    password = "".join(choice(combo) for x in range(length))

    print("Your", length, "character password is:", password)

    return True

while True:
    option = int(input("Please choose 1 to start generating a password, 2 to exit password generator: "))

    if option == 1:
        char = int(input("Please choose how long the password will be: "))
        pasGen(char)
    elif option == 2:
        break
    else:
        print("Invalid input, please choose either 1 or 2")
