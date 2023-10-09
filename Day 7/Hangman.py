import random
word_list = ["nader", "mamdouh", "ahmed"]
word = random.choice(word_list)
display = []
level=["0","#","##","###","####","#####"]
for letter in word:
    display.append("_")
lives=5
check=False
while not check:
    print("you have :" ,level[lives])
    guess = input("Guess a character in the word: ").lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter
            print(display)                  
    if "_" not in display:
        print("you win")
        check=True
    if guess not in word:
        lives-=1
        print("Wrong guess")
        if lives==0:
            check=True
            print("you lose")
     
