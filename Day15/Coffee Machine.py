import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = '''            __  __                                  _     _            
  ___ ___  / _|/ _| ___  ___   _ __ ___   __ _  ___| |__ (_)_ __   ___ 
 / __/ _ \| |_| |_ / _ \/ _ \ | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ \
| (_| (_) |  _|  _|  __/  __/ | | | | | | (_| | (__| | | | | | | |  __/
 \___\___/|_| |_|  \___|\___| |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___| '''


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
quarters_value = 0.25
dimes_value = 0.10
nickles_value = 0.05
pennies_value = 0.01



def calc():
    print("please enter the coin ")
    quarters = int(input("How many quarters do you have ? "))
    dimes = int(input("How many dimes do you have ? "))
    nickles = int(input("How many nickles do you have ? "))
    pennies = int(input("How many pennies do you have ? "))
    total_money = (dimes * dimes_value) + (quarters * quarters_value) + (nickles_value * nickles) + (
                pennies_value * pennies)
    return total_money


def again(resource, menu):
    water = False
    milk = False
    coffee = False
    cost = False
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso":
        water_required_for_espresso = MENU["espresso"]["ingredients"]["water"]
        coffee_required_for_espresso = MENU["espresso"]["ingredients"]["coffee"]
        if resources["water"] >= water_required_for_espresso:
            water = True
            resources["water"] -= water_required_for_espresso
        else:
            print("Sorry , There is no water enough ")
        if resources["coffee"] >= coffee_required_for_espresso:
            coffee = True
            resources["coffee"] -= coffee_required_for_espresso
        else:
            print("Sorry , There is no coffee enough ")
        if water and coffee:
            total_money = calc()
            if total_money >= MENU["espresso"]["cost"]:
                cost = True
                resources["money"] += MENU["espresso"]["cost"]
                remain_money = total_money-MENU["espresso"]["cost"]
                remain_money = round(remain_money, 2)
                print(f"Here you are the {remain_money} in charge ")
                print("Enjoy your drink :) ")
            else:
                print("Sorry , your money is not enough ")

    elif choice == "latte":
        water_required_for_latte = MENU["latte"]["ingredients"]["water"]
        milk_required_for_latte = MENU["latte"]["ingredients"]["milk"]
        coffee_required_for_latte = MENU["latte"]["ingredients"]["coffee"]
        if resources["water"] >= water_required_for_latte:
            water = True
            resources["water"] -= water_required_for_latte
        else:
            print("Sorry , There is no water enough ")
        if resources["milk"] >= milk_required_for_latte:
            milk = True
            resources["milk"] -= milk_required_for_latte
        else:
            print("Sorry , There is no milk enough ")
        if resources["coffee"] >= coffee_required_for_latte:
            coffee = True
            resources["coffee"] -= coffee_required_for_latte
        else:
            print("Sorry , There is no coffee enough ")
        if water and milk and coffee:
            total_money = calc()
            if total_money >= MENU["latte"]["cost"]:
                cost = True
                resources["money"] += MENU["latte"]["cost"]
                remain_money = total_money - MENU["espresso"]["cost"]
                remain_money = round(remain_money, 2)
                print(f"Here you are the {remain_money} in charge ")
                print("Enjoy your drink :) ")
            else:
                print("Sorry , your money is not enough ")
    elif choice == "cappuccino":
        water_required_for_cappuccino = MENU["cappuccino"]["ingredients"]["water"]
        milk_required_for_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]
        coffee_required_for_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]
        if resources["water"] >= water_required_for_cappuccino:
            water = True
            resources["water"] -= water_required_for_cappuccino
        else:
            print("Sorry , There is no water enough ")
        if resources["milk"] >= milk_required_for_cappuccino:
            milk = True
            resources["milk"] -= milk_required_for_cappuccino
        else:
            print("Sorry , There is no milk enough ")
        if resources["coffee"] >= coffee_required_for_cappuccino:
            coffee = True
            resources["coffee"] -= coffee_required_for_cappuccino
        else:
            print("Sorry , There is no coffee enough ")
        if water and milk and coffee:
            total_money = calc()
            if total_money >= MENU["cappuccino"]["cost"]:
                cost = True
                resources["money"] += MENU["cappuccino"]["cost"]
                remain_money = total_money - MENU["espresso"]["cost"]
                remain_money = round(remain_money, 2)
                print(f"Here you are the {remain_money} in charge ")
                print("Enjoy your drink :) ")
            else:
                print("Sorry , your money is not enough ")
    else:
        print(resources)


print(logo)

while input("Do you want to order? y or n? ") == "y":
    clear_screen()
    again(resources, MENU)
