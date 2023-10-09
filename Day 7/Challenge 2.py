#check if the player win 
import random
word_list = ["nader", "mamdouh", "ahmed"]
word = random.choice(word_list)
display = []

for letter in word:
    display.append("_")

i = 0
counter=0
print(word)

while i>=0:
    i += 1
    guess = input("Guess a character in the word: ").lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            counter+=1
            display[position] = letter
            print(display)
    if counter==len(word):
        print("you win")
        break

