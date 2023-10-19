import random
import os
logo = ''' __        __                       __                   __   __         
|    |  | |   |<< |<<   >>|<< |  | |     | | |  | |\ /| |  | |   |<<     
| >> |  | |<< --  --      |   |><| |<<   |\| |  | | < | |<>' |<< |>>|    
'__| '<<' |__ >>| >>|     |   |  | |__   | | '<<' |   | |__' |__ |  \    '''


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():
    randomnum = random.randint(1, 100)

    def guess(randomnum):
        guesss = int(input("Make a guess : "))
        if guesss > randomnum:
            print("too hiegh ")
        elif guesss < randomnum:
            print("too low ")
        else:
            return 1

    def Game(randomnum, diffeculty):
        flag = False
        if diffeculty == "easy":
            attempts = 10
        else:
            attempts = 5
        while flag == False and attempts >= 1:
            print(f"You have {attempts} remaining to gues the number")
            result = guess(randomnum)
            if result == 1:
                print("Yes you got it :)")
                flag = True
            else:
                attempts -= 1
        if attempts == 0:
            print(f"Sorry , you lose the right guess is {randomnum}")

    #print(randomnum)
    print("Welcome to Guessing number Game!!")
    print("Iam thinking in number from 1 -> 100")
    level = input("Choose diffecult, type 'easy' or 'hard' : ").lower()
    if (level == "easy"):
        Game(randomnum, level)
    else:
        Game(randomnum, level)


while input("Do you want to play ? y or n ?  ") == "y":
    clear_screen()
    print(logo)
    play_game()
