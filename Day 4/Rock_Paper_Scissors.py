import random
num1 = input("choose 1 for paper , 2 for rock , 3 for scissors\n")
num2 = random.randint(1, 3)
if num1 == "paper":
    if num2 == 2:
        print("you win ")
    elif num2 == 3:
        print("computer choose scissors you lose")
    else:
        print("Draw")
elif num1 == "rock":
    if num2 == 3:
        print("you win ")
    elif num2 == 1:
        print("computer choose paper you lose")
    else:
        print("Draw")
else:
    if num2 == 1:
        print("you win ")
    elif num2 == 2:
        print("computer choose rock you lose")
    else:
        print("Draw")
