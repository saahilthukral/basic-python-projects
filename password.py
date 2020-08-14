#Secure password generator
import string
import random

true = True

while true: #While this statement is True, perform this code

    print("Secure password generator")
    print("-"*30)

    password_length = int(input("What do you want the length of your password to be ? "))

    if password_length >= 6:
        password_chars = string.ascii_letters + string.digits + string.punctuation
        password = []

        for i in range(password_length):
            password.append(random.choice(password_chars))

        print("".join(password))
    
    elif password_length<6:
        print("Choose a longer password")

    else:
        print("Enter a number")
        quit()

    try_again = input("Would you like to try again ? ")

    if try_again.lower() == "y" or try_again.lower() == "yes":
        continue #If you type yes or y then it'll automatically repeat the code
    else:
        break 