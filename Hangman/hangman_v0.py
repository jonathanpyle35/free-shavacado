#Jonathan Pyle
#October 19, 2016
#
#Hangman!

import os
import random

def show_start_screen():

    print("***************************************************** ")                                                                  
    print("                                                      ")
    print("             __ __                               __   ")
    print("            / // /__ ____  ___ ___ _  ___ ____  / /   ")
    print("           / _  / _ `/ _ \/ _ `/  ' \/ _ `/ _ \/_/    ")
    print("          /_//_/\_,_/_//_/\_, /_/_/_/\_,_/_//_(_)     ")  
    print("                         /___/                        ")
    print("                                                      ")
    print("                                                      ")
    print("***************************************************** ")                                                      


def show_start_screen():
    print("Let's play Hangman!")

def show_credits():
    print("by Jonathan Pyle on 10/20/16 ")

def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")

    for i, f in enumerate(files):
        full_path = path + "/" + f

        with open(full_path, 'r') as file:
            print(str(i+1) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)-1

    return path + "/" + files[choice]



def get_puzzle(file):
    #words = ["patriots", "harambe", "spicy", "pepe", "yeet","lemony goodness", "unecessary walrus", "eliot digiorno", " watermelon seeds", " communism is the superior form of government", " proxima centuri", " george washington", "paleolithic societies", "gotta blast"]


    with open(file, 'r') as f:
        words = f.read().splitlines()
        


    return random.choice(words[1:]).lower()

def check(word, solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Guess a single letter please.")

    
def display_board(solved, guesses, strikes):
    if strikes == 0:
        print("   ")
    elif strikes == 1:
        print("       _______           ")
        print("     |/      |           ")
        print("     |      (_)          ")
        print("     |                   ")
        print("     |                   ")
        print("     |                   ")
        print("     |                   ")
        print("     _|___               ")
    elif strikes == 2:
        print("                         ")
        print("       _______           ")
        print("     |/      |           ")
        print("     |      (_)          ")
        print("     |       |           ")
        print("     |                   ")
        print("     |                   ")
        print("     |                   ")
        print("     _|___               ")
    elif strikes == 3:
        print("                         ")
        print("        _______          ")
        print("      |/      |          ")
        print("      |      (_)         ")
        print("      |      \|          ")
        print("      |                  ")
        print("      |                  ")
        print("      |                  ")
        print("      _|___              ")
    elif strikes == 4:
        print("                         ")
        print("       _______           ")      
        print("     |/      |           ")
        print("     |      (_)          ")
        print("     |      \|/          ")
        print("     |                   ")
        print("     |                   ")
        print("     |                   ")
        print("     _|___               ")
    elif strikes == 5:
        print("                         ")
        print("       _______           ")
        print("     |/      |           ")
        print("     |      (_)          ")
        print("     |      \|/          ")
        print("     |       |           ")
        print("     |                   ")
        print("     |                   ")
        print("     _|___               ")
    elif strikes == 6:
        print("                         ")
        print("       _______           ")
        print("     |/      |           ")
        print("     |      (_)          ")
        print("     |      \|/          ")
        print("     |       |           ")
        print("     |      / \          ")
        print("     _|___               ")


    print(solved + "[" + guesses + "]")
    
def play_again():
    while True:
        answer = input("Would you like to play again? ")

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes' or answer == 'y':
            return True

        print("What! Just say yes or no bro. ")
    

def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    
    
    guesses = ""
    strikes = 0
    limit = 6

    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            
        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)
        
    if word == solved: 
        print("You win!")
    else:
        print("You lose")


def main():
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()

    show_credits()

# code execution begins here
if __name__ == "__main__":
    main()
