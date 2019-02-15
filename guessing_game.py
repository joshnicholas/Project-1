import random
import sys


all_score = []

def start_game():
    answer = random.randint(1, 10)
    attempts = 0
    print("""
    ------------------------------------
    Welcome to the Number Guessing Game!
    See if you can guess the correct
    number and beat the high score!
    ------------------------------------""")
    if len(all_score) >= 1:
        best = high_score(all_score)
        print("The high score is {}!".format(best))
    else:
        print("No high score yet")
    while True:
        user_num = user_input()
        if user_num < 1 or user_num > 10:
            print("Please enter a value between 1 & 10")
        elif user_num == answer:
            attempts += 1
            if attempts == 1:
                print("Correct! It took {} try!".format(attempts))
            else:
                print("Correct! It took {} tries!".format(attempts))
            all_score.append(attempts)
            new_game = input("Would you like to try again? (y)es/(n)o  ")
            restart(new_game)            
        elif user_num > answer:
            attempts += 1
            print("Too high!")
        elif user_num < answer:
            attempts += 1
            print("Too low!")

def user_input():
    try:
        foo =  int(input("Pick a number between 1 & 10:  "))
        print("DEBUG!!!!! This the the value of foo ---> {}".format(foo))
    except ValueError:
        print("That's not a valid value. Try again")
    
                
def high_score(score):
    return min(score)

def restart(response):
    if response[0].lower() == 'y':
        start_game()
    elif response[0].lower() == 'n':
        print("Thanks for playing!")
        sys.exit()
    else:
        print("Invalid answer")
        sys.exit()

start_game()