from coffe_f import choice_is_good, print_report, store_money, enough_ingredients, decrement_ingredients
from data_coffee import MENU


# TODO: loop everything
def coffee_machine():
    machine_is_on = True
    money = 0.0

    # TODO: ask and store answer from What would you like? (espresso/latte/cappuccino): make sure is type-proof
    while machine_is_on:

        user_choice = ""
        while not choice_is_good(user_choice):
            user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: off function
        if user_choice == "off":
            machine_is_on = False

        # TODO: report function
        elif user_choice == "report":
            print_report(money)

        # TODO: if money and ingredients are enough
        else:
            user_drink = MENU[user_choice]

            if enough_ingredients(user_drink["ingredients"]):

                # TODO: ask for money: please insert coins. How many quarters 0.25, dimes 0.10, nickels 0.5 and penny
                #  0.01
                print("Please insert coins.")
                user_money = store_money()

                if user_money < user_drink["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    money += user_drink["cost"]
                    decrement_ingredients(user_drink["ingredients"])

                    # TODO: than give change "Here is x in change", give coffee "Here is your x. Enjoy!", decrement
                    #  the ingredients

                    print(f"Here is ${user_money - user_drink['cost']} in change.")
                    print(f"Here is your {user_choice}")


coffee_machine()
