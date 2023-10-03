# BMI Calculator
#Day 2.1
weight = float(input("Enter ypur weight in kg : "))
height = float(input("Enter your height in m : "))
bmi = weight/(height**2)
bmi = round(bmi, 2)
print("Your BMI : ", bmi)
