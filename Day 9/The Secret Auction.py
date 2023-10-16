import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_hieght_bid(list_of_bid):
    max = 0
    winner = ""
    for key in list_of_bid:
        if list_of_bid[key] > max:
            max = list_of_bid[key]
            winner = key

    print(f"the winner is {winner} ,and his bid is {max}")


list_of_bid = {}
flag = True

while flag:
    name = input("what is your name ?\n")
    bid = int(input("what is your bid ?\n"))
    list_of_bid[name] = bid
    ex = input("do you want to bid ? y or n \n")
    if ex != "y":
        find_hieght_bid(list_of_bid)
        flag = False
    else:
        clear_screen()
