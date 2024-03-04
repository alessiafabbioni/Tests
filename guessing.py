def clear():  # Prints 50 blank lines
    print("\n" * 50)

import random

#Function to define a random number
#Function to define the level and the number of attempts
#Function to define whether the guess is too high or too low


def deal_number():
    return random.randint(1,100)


def play_game(level_attempts):
    random_number = deal_number()
    attempts_left = level_attempts
    
    while level_attempts > 0:
        guess = int(input(f"Guess the number (1-100). Attempts left: {attempts_left}"))
        
        if guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        
        elif guess < random_number:
            print("Too low, try again")
        
        else:
            print("Too high, try again")
            
        attempts_left -= 1
    
    if attempts_left == 0:
        print(f"Sorry you have run out of attempts, the correct number was {random_number} ")


def main():
    print("Welcome to the Guessing Number Game")
    print("I'm thinking of a number between 1 and 100")
    
    level = input("Choose a level between easy and hard")
    
    if level == 'easy':
        play_game(10)
        
    else:
        play_game(5)
    

if __name__ == "__main__":
    main()