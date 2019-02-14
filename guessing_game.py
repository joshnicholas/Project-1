import random
import sys


all_score = []

def start_game():
    answer = random.randint(1, 10)
    attempts = 0
    guess = 0
    print("""
    ------------------------------------
    Welcome to the Number Guessing Game!
    See if you can guess the correct
    number and beat the high score!
    ------------------------------------""")
    best = high_score()
    print("The high score is {}!".format(best))
    while True:
        try:
            guess = int(input("Pick a number between 1 & 10:  "))
        except ValueError:
            print("That's not a valid value. Try again")
        else:
            if guess < 1 or guess > 10:
                print("Please enter a value between 1 & 10")
            elif guess == answer:
                attempts += 1
                print("Correct! It took {} tries!".format(attempts))
                all_score.append(attempts)
                new_game = input("Would you like to try again? (y)es/(n)o  ")
                restart(new_game)            
            elif guess > answer:
                attempts += 1
                print("Too high!")
            elif guess < answer:
                attempts += 1
                print("Too low!")

def high_score():
    check = 99999999
    for score in all_score:
        num_score = int(score)
        if num_score < check:
            check = num_score
    return(check)

def restart(response):
    if response[0].lower() == 'y':
        start_game()
    elif response[0].lower() == 'n':
        sys.exit()
    else:
        print("Invalid answer")
        sys.exit()

start_game()