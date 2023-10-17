#day 11
import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card(cards):
    card = random.choice(cards)
    return card


def calc_score(cardss):
    if sum(cardss) == 21 and len(cardss) == 2:
        return 0
    if 11 in cardss and sum(cardss) > 21:
        cardss.remove(11)
        cardss.append(1)

    return sum(cardss)


def compare(user_score, computer_score):
    if user_score > 21:
        return ("computer win ")
    elif computer_score > 21:
        return ("user win ")
    elif user_score > computer_score:
        return ("user win ")
    elif user_score < computer_score:
        return ("computer win ")
    elif computer_score == 0:
        return ("lose , opponet has blackjack ")
    elif user_score == 0:
        return ("you win by  blackjak ")
    else:
        return ("draw")


def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        computer_cards.append(deal_card(cards))
        user_cards.append(deal_card(cards))

    user_score = calc_score(user_cards)
    computer_score = calc_score(computer_cards)
    print(f" your cards is {user_cards} , and score is :{user_score}")
    print(f" computer cards is {computer_cards[0]} ")

    while not is_game_over:
        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            ans = input("do you want to draw a card ? y or n ? ")
            if ans == "y":
                user_cards.append(deal_card(cards))
                user_score = calc_score(user_cards)
                print(
                    f" your cards is {user_cards} , and score is :{user_score}")
                print(f" computer cards is {computer_cards[0]} ")
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calc_score(computer_cards)

    print(compare(user_score, computer_score))
    print(f" your cards is {user_cards} , and score is :{user_score}")
    print(
        f" computer cards is {computer_cards}and score is :{computer_score} ")



while input("Do you want to play the game ?? y or n ? ")== "y":
    clear_screen()
    play_game()

