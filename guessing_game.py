import random
import sys


all_score = []


def welcome():
    print("""
    ------------------------------------
    Welcome to the Number Guessing Game!
    See if you can guess the correct
    number and beat the high score!
    ------------------------------------""")

def show_score():
    if len(all_score) >= 1:
        best = high_score(all_score)
        print("The high score is {}!".format(best))
    else:
        print("No high score yet")
    
def main():
    answer = random.randint(1, 10)
    attempts = 0
    welcome()
    show_score()
    
    
    while True:
        user_num = validate_input()
        attempts += 1
        if user_num == answer:
            if attempts == 1:
                print("Correct! It took {} try!".format(attempts))
            else:
                print("Correct! It took {} tries!".format(attempts))
            all_score.append(attempts)
            break
        elif user_num > answer:
            print("Too high!")
        elif user_num < answer:
            print("Too low!")
    restart()  

def validate_input():
    while True:
        try:
            guess = int(input("Pick a number between 1 & 10:  "))
        except ValueError:
            print("That's not a valid value. Try again")
        else:
            if guess < 1 or guess > 10:
                print("Please enter a value between 1 & 10")
            else:
                return guess
    
def high_score(score):
    return min(score)

def restart():
    new_game = input("Would you like to try again? (y)es/(n)o  ")
    if new_game[0].lower() == 'y':
        main()
    elif new_game[0].lower() == 'n':
        print("Thanks for playing!")
        sys.exit()
    else:
        print("Invalid answer")
        sys.exit()

if __name__ == '__main__':
    main()