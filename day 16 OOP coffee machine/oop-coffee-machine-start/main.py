from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def choice_is_good(typed):
    """Check if user wrote either 'off' or 'report' """
    there_is_an_error = True

    if typed == "off" or typed == "report":
        there_is_an_error = False

    return not there_is_an_error


def coffee_machine():
    is_on = True

    # menu object
    machine_menu = Menu()
    machine_maker = CoffeeMaker()
    money = MoneyMachine()

    while is_on:

        # user input and sanity check
        products_string = machine_menu.get_items()
        products_string = products_string.removesuffix("/")
        user_choice = input(f"What would you like? {products_string}: ")

        # special words
        if choice_is_good(user_choice):

            # off
            if user_choice == "off":
                is_on = False

                # report
            elif user_choice == "report":
                machine_maker.report()
                money.report()

        # order coffee
        else:
            user_drink = machine_menu.find_drink(user_choice)
            if not user_drink is None:

                # make coffee
                if machine_maker.is_resource_sufficient(user_drink):
                    if money.make_payment(user_drink.cost):
                        machine_maker.make_coffee(user_drink)


# todo: Report not working


coffee_machine()
