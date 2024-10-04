from data_coffee import MENU, resources, coins


def choice_is_good(typed):
    """Check if user wrote either: 'cappuccino','latte', 'espresso', 'off' or 'report' """
    there_is_an_error = True
    for drink in MENU:
        if typed == drink:
            there_is_an_error = False
    if typed == "off" or typed == "report":
        there_is_an_error = False

    return not there_is_an_error


def print_report(money):
    """get water, milk, coffee and money report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def store_money():
    """returns the sum of coins insert by customer"""
    amount = 0
    quarters = int(input("How many quarters?: "))
    amount += quarters * coins["quarters"]

    dimes = int(input("How many dimes?: "))
    amount += dimes * coins["dimes"]

    nickles = int(input("How many nickles?: "))
    amount += nickles * coins["nickles"]

    pennies = int(input("How many pennies?: "))
    amount += pennies * coins["pennies"]

    return amount


def enough_ingredients(drink_ingredients):
    """returns True if there are enough ingredients and False if not"""
    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def decrement_ingredients(ingredients_to_decrease):
    """decrements from the resources the amount of ingredients used"""
    for ingredient in ingredients_to_decrease:
        resources[ingredient] -= ingredients_to_decrease[ingredient]
