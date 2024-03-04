
def clear():  # Prints 50 blank lines
    print("\n" * 50)

import random

## Functions to define game's rules

#Deal cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Calculate score
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

#Compare score
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Show result
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    
    elif computer_score == 0:
        return "the computer wins"
    
    elif user_score == 0:
        return "You win"
    
    elif computer_score > 21:
        return "You win"
    
    elif user_score > 21:
        return "Computer wins"
    
    elif user_score>computer_score:
        return "You win"
    else: 
        return "You lose"
    
    

def play_game():   
#Deal initial cards
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    calculate_score(user_cards)
    calculate_score(computer_cards)


    #initialise is_game_over loop

    while not is_game_over:
        
        #Calculate scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        #Display current scores
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        #Check for game over conditions
        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            user_deal = input("Type y to draw another card, type n to pass")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Set the computer's hand
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    
#Restart the game
while input("Do you want to play again a game of BlackJack? Type y or n") == "y":
    clear()
    play_game()
