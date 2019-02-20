import random

import sys

high_score = []

# Welcome message

hello = print("Well hello thar! Welcome to Josh's awesome guessing game.   ")

name = input("Firstly, what should I call you?   ")

print("What a weird name.")

print("Anyway {}, let's play.".format(name))

# Taking input          

def load():
    while True:
        try:
            load = int(input("Please guess a number between 1 and 20:   "))

        except ValueError:
            print("That doesn't work for me. Let's try this again.")

        else:
            if load < 1 or load > 20:
                print("Why not try a valid number this time?")
            else:
                return load

# The game function

def start_game():

    random_number = random.randint(1, 20)

    times_guessed = 1

    while True:

        times_guessed += 1

        guess = load()

        if guess > random_number:
            print("WRONG! It's lower :)")

        if guess < random_number:
            print("WRONG! It's higher :)")

        elif guess == random_number:
            print("Noice! You got it in {}!".format(times_guessed))
            high_score.append(times_guessed)
            nochmal()


# Sort the high score list and show lowest number

def highscore():

    print("The high score is {}.".format(min(high_score)))
    
# Let's do it again

def nochmal():

    highscore()

    again = input("Try again? (Y/N)    ")

    if again[0].lower() == "y":
        start_game()

    else:
        print("Well go away then.")
        sys.exit()

start_game()










    
