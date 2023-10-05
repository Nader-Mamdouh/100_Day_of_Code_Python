print("Welcome to Love Calculator ")
name1 = input("Waht is your name : \n")
name2 = input("Waht is her name : \n")
name1 = name1.lower()
name2 = name2.lower()
first = name1.count("t")+name2.count("t")+name1.count("r")+name2.count("r") + \
    name1.count("u")+name2.count("u")+name1.count("e")+name2.count("e")
second = name1.count("l")+name2.count("l")+name1.count("o")+name2.count("o") + \
    name1.count("v")+name2.count("v")+name1.count("e")+name2.count("e")
first = str(first)
second = str(second)
score = int(first+second)
if score < 10 or score > 90:
    print(f"The score is {score} , you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"The score is {score} , you are alright together ")
else:
    print(f"Your score is {score}")
