from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while True:
        user_input = str.lower(input(f"\nWhat would you like? {menu.get_items()} "))

        match user_input:
            case "report":
                coffee_maker.report()
                money_machine.report()

            case "off":
                exit()

            case n if n in menu.get_items().split("/"):
                drink = menu.find_drink(user_input)

                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

            case _:
                print("\n*** ❌ Sorry, invalid input ***")


if __name__ == "__main__":
    main()
