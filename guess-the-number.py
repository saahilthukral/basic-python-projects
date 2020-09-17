import random


while True: #This will repeat the code until you break the loop

    print("Welcome to Guess the number")
    print('-'* 40)

    class Number:
        def __init__(self,maximum,minimum):
            self.maximum = int(maximum) 
            self.minimum = int(minimum)

        def Random_no(self):
            random_no = random.randint(self.maximum,self.minimum)

            user_input = int(input("Enter a number that you believe is correct "))

            if user_input == random_no:
                print("Congrats you got it right")

            elif user_input > random_no:
                if user_input > maximum:
                    print("The number is beyond the maximum")

                else:
                    print("Your no is too high, the generated number is {}".format(random_no))

            elif user_input < random_no:
                
                if user_input < minimum:
                    print("Your number is lesser than the minimum, try again ")
                    
                else:    
                    print("Your no is too low, the generated no is {}".format(random_no))
            
            else:
                raise ValueError #This will raise a Value Error when you enter anything other than a number.

    minimum = int(input("Enter the minimum value: "))
    maximum = int(input("Enter the maximum value: "))
    
    if maximum < minimum:
    	raise ValueError("Please enter a proper value")
    	

    random_no = Number(minimum,maximum)
    random_no.Random_no()

    try_again = input("Do you want to try again ?: ")


    if try_again.lower() == "yes" or try_again.lower() == "y":
        print("-"*40)
        continue
    
    elif try_again.lower() == "no" or try_again.lower() == "n":
    
    	print("All right, have a good day!!!")
    	break
    
    else:
    	
    	raise TypeError("input must be a string")
    

    
