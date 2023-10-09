#challenge 1
import random
word_list = ["nader", "mamdouh", "ahmed"]
word = random.choice(word_list)
guess = input("Guess a character in the word: ").lower()

for letter in word:
    if letter != guess:
        print("That is a wrong character")
    else:
        print("That is a true character")
