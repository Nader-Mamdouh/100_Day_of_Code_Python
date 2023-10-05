#Day3 
#BMI version2
weight = float(input("Enter ypur weight in kg : "))
height = float(input("Enter your height in m : "))
bmi = weight/(height**2)
bmi = round(bmi, 2)
if bmi < 18.5:
    print(f"Your BMI :{bmi} and you are Underweight")
elif bmi < 25:
    print(f"Your BMI : {bmi} and you are Normal weight")
elif bmi < 30:
    print(f"Your BMI : {bmi} and you are Over weight")
elif bmi < 35:
    print(f"Your BMI : {bmi} and you are Obese")
else:
    print(f"Your BMI : {bmi} and you are Clinically ")
