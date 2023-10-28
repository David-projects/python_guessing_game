from art import logo
import random

print(logo)
print("Welcome to my guessing game")
new_game = 'y'


def set_level(level):
    """Sets the level in the game"""
    if level == "easy":
        return 10
    # end if
    return 5


def check_guess(answer, attempts, tries):
    """Checks if the guess is right"""
    guess = int(input(f"Guess a number between 1 and 100: {attempts} "))
    if tries >= attempts:
        print(f"You lost! The answer was {answer}")
        return False
    if guess == answer:
        print(f"You guessed it! You Win! The answer was {answer}")
        return True
    elif guess > answer:
        print(f"Too high. Your guess was {guess}")
        check_guess(answer, attempts, tries + 1)
    elif guess < answer:
        print(f"Too low. Your guess was {guess}")
        check_guess(answer, attempts, tries + 1)
    else:
        return
    #end if elif else

while new_game == 'y':
    level = input("Enter easy or hard.").lower()
    game_level = set_level(level)
    print(f"You have selected {level} you have {game_level} tries")

    # Generate a random number between 1 and 100
    number = random.randint(1, 101)
    check_guess(number, game_level, 1)
    new_game = input("Do you want to play again? (y/n)").lower()
    
