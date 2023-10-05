print("Welcome in RollerCoaster")
height = int(input("What is your height ? :"))
price = 0
if height >= 120:
    print("Your height is ok")
    age = int(input("What is your Age ? :"))
    if age < 12:
        price += 5
        print(f"your age is suitable and you need to pay {price}$ ")
    elif age <= 18:
        price += 8
        print(f"your age is suitable and you need to pay {price}$")
    else:
        price += 12
        print(f"your age is suitable and you need to pay {price}$")
    photo = input("Do you want photos ? and add 3$ ")
    if photo == "yes":
        price += 3
        print(f"The totla price {price}$ ")
    else:
        print(f"The total price is {price}$")
else:
    print("You can not book a ticket")
