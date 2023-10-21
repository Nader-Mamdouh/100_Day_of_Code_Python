from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to order ? ({options})").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #print(drink)
        if my_coffee_maker.is_resource_sufficient(drink)and my_money_machine.make_payment(drink.cost):
               my_coffee_maker.make_coffee(drink)

