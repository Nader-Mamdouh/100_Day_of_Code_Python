print("Welcome to tip claculator")
bill = float(input("What was total bill\n"))
people = int(input("How many people to split the bill $?\n"))
perc = int(input("What is the perc tip would you like to give ? 10% ,20% ?\n"))
totalbill = perc/100*bill+bill
sumforperson = (totalbill)/people
sumforperson = round(sumforperson, 2)
print("Each person should pay : ", sumforperson, "$")'''
