print("welcome to python pizza delivery ")
print("OUR MENU")
print("SMALL PIZZA FOR 9$")
print("MEDUIM PIZZA FOR 13$")
print("LARGE PIZZA FOR 15$")
print("EXTRA")
print("pepproni for SMALL 2$")
print("pepproni for MEDUIM 3$")
print("pepproni for LARGE 5$")
print("CHEESE FOR ANY SIZE 2$")
price = 0
size = input("What is the size do you want ? L or M or S ?\n ")
if size == "L":
    price += 15
    extra_pep = input("Do you want extra pepproni ? Y or N? \n")
    if extra_pep == "Y":
        price += 5
    extra_cheese = input("Do you want extra cheese ? Y or N?\n")
    if extra_cheese == "Y":
        price += 2
elif size == "M":
    price += 13
    extra_pep = input("Do you want extra pepproni ? Y or N?\n")
    if extra_pep == "Y":
        price += 3
    extra_cheese = input("Do you want extra cheese ? Y or N?\n")
    if extra_cheese == "Y":
        price += 2
else:
    price += 9
    extra_pep = input("Do you want extra pepproni ? Y or N?\n")
    if extra_pep == "Y":
        price += 2
    extra_cheese = input("Do you want extra cheese ? Y or N?\n")
    if extra_cheese == "Y":
        price += 2

print(f"your final order if {size} pizza and the totla price is {price}")
print("Enjoy with your pizza :) ")
