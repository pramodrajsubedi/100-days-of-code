# blackjack program/ Game
import random
from art import logo

print("Welcome to the blackjack.")

def deal_card():
    cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose.\n Opponent has Blackjack."
    elif user_score == 0:
        return " You win with blackjack"
    elif user_score > 21:
        return " You went over . You lose."
    elif computer_score > 21:
        return "Computer went over . You won."
    elif user_score > computer_score :
        return " You Win."
    else:
        return " You lose."
    
def play_game():
    print(logo)

    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f" Your card: {user_card},\n current score = {user_score}")
        print(f" Computer's first card : {computer_card[0]}")


        if user_card == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: " )
            if user_choice == "y" :
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f" Your final hand : {user_card}, final score: {user_score} ")
    print(f" Computer's final hand : {computer_card}, final score : {computer_score}")
    print(compare(user_score, computer_score))


is_game_active = True
while is_game_active:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_input == "y":
        play_game()
    elif user_input == "n":
        print("Thanks for playing! Goodbye!")
        is_game_active = False
    else:
        print("Invalid input. Please type 'y' or 'n'.")


