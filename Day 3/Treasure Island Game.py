print("Welcome to Treasure island")
print("Your mission to find the treasure")
choise1 = input("Now choose your dirction Left or Right?\n").lower()
if choise1 == "left":
    print("Nice you passed first trap")
    choise2 = input(
        "Now there is a lake and there is an island in the midlle of the lake will you swim or wait boat ?\n").lower()
    if choise2 == "wait":
        print("Nice you passed second trap")
        choise3 = input(
            "Now there is a 3 doors Red ,BLue and Yellow ?\n").lower()
        if choise3 == "yellow":
            print("Congratulations! you win")
        else:
            print("You choosed the wrong door ")
            print("Game over! :(")
    else:
        print("No the lake has alot of crocodiles ")
        print("Game over! :(")
else:
    print("You entered the maze ")
    print("Game over! :(")
