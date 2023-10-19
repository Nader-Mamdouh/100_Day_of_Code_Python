import random
import os
logo = '''_     _ _____  ______ _     _ _______  ______    
|_____|   |   |  ____ |_____| |______ |_____/    
|     | __|__ |_____| |     | |______ |    \_    
                                                 
        _____  _  _  _ _______  ______           
|      |     | |  |  | |______ |_____/           
|_____ |_____| |__|__| |______ |    \_           '''
logo2 = '''_    _ _______
 \  /  |______
  \/   ______|'''


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


dir = {
    1: ["nymar", 90],
    2: ["messi", 110],
    3: ["crestiano", 150],
    4: ["johncina", 80],
    5: ["therock", 95]
}


print(logo)


def play_game():
    score = 0
    flag = True
    ans = 1
    while flag:

        num1 = ans
        num2 = random.randint(1, 5)

        if num1 == num2:
            continue
        print(f"compare between 1) : {dir[num1][0]}")
        print(logo2)
        print(f"Against 2) : {dir[num2][0]}")
        choice = int(input("What is your choice ?,who has more followers ? "))
        if choice == 1:
            if (dir[num1][1] > dir[num2][1]):
                score += 1
                ans = num2
                print(f"Yes you answered right,your score is {score}")
            else:
                clear_screen()
                print(logo)
                print(f"Game Over , your score is {score}")
                flag = False
        else:
            if (dir[num2][1] > dir[num1][1]):
                score += 1
                ans = num2
                print(f"Yes you answered right,your score is {score}")
            else:
                clear_screen()
                print(logo)
                print(f"Game Over , your score is {score}")
                flag = False


while input("Do you want to play ? y or n ?  ") == "y":
    clear_screen()
    print(logo)
    play_game()
