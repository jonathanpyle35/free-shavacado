#Guess-A-Number AI
#
#Jonathan Pyle
#September 13, 2016

import random
import math


print("**********************************************************************")
print("                                                                      ")
print("   __        ___  __   __                              __   ___  __   ")
print("  / _` |  | |__  /__` /__` __  /\  __ |\ | |  |  |\/| |__) |__  |__)  ")
print("  \__> \__/ |___ .__/ .__/    /~~\    | \| \__/  |  | |__) |___ |  \  ")
print("                                                                      ")
print("                                                                      ")
print("**********************************************************************")
input("                     Press Enter to Start ") 

def play():
    
    low = 1
    high = 100
    limit = int(math.log(high - low, 2)) + 1
    tries = 1

    print("Welcome to Guess-A-Number AI. Please think of a number from " + str(low) + " to " + str(high) + " and I will try to guess it.")
    input("Please press Enter once you are ready.")

    num = random.randint(low, high)

    got_it = False

    while got_it == False and tries < limit:

        guess = int(high + low) // 2
        print("Is the number " + str(guess) + "?")
        print("Enter 'lower', 'higher', or 'yes'")

        response = input()
        
        if response.lower() == 'higher' or response.lower() == 'h':
            low = guess + 1
        elif response.lower() == 'lower' or response.lower() == 'l':
            high = guess - 1
        elif response.lower() == 'yes'or response.lower() == 'y':
            got_it = True
        else:
            print("I don't understand.")
            input("Enter 'lower', 'higher', or 'yes'")

        tries += 1

        if got_it == True:
            print("I got it!")




              
    print("This was created by Jonathan Pyle and finished on September 13, 2016")

def play_again():

    while True:
          answer = input("Would you like to play again?")

          if answer == 'no' or answer == 'n':
              return False
          elif answer == 'yes' or answer == 'y':
              return True

          print("Hey! Just say yes or no.")

# game_begins
          
again = True

while again == True:
          play()
          again = play_again()

print("Game over")





          

          
