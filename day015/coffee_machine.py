def format_indicator(name, amount):
    match name:
        case "water" | "milk":
            return f"{amount} ml"
        case "coffee":
            return f"{amount} g"
        case "money":
            return f"${amount / 100:.2f}"

revenue = 0

machine_indicators = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COSTS = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "money": 150
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "money": 250
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "money": 300
    }
}


def resources_are_enough(drink):
    drink_costs = COSTS[drink]
    resources_are_enough = True

    for indicator in machine_indicators:

        if machine_indicators[indicator] < drink_costs[indicator]:
            resources_are_enough = False
            print(f"Sorry, there is not enough {indicator}")

    return resources_are_enough


def print_report():
    for i in machine_indicators:
        print(f"{i.title()}: {format_indicator(i, machine_indicators[i])}")


def make_drink(drink):
    print("making drink")


def main():
    user_input = input("What would you like? (espresso/latte/capuccino) ")

    match user_input:
        case "report":
            print_report()
        case "off":
            exit()
        case "espresso" | "latte" | "cappuccino":
            if resources_are_enough(user_input):
                make_drink(user_input)
        case _:
            print("Invalid input")


if __name__ == "__main__":
    main()
