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

COIN_VALUES = {
    "quarter": 25,
    "dime": 10,
    "nickel": 5,
    "penny": 1
}

DRINK_COSTS = {
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
    drink_costs = DRINK_COSTS[drink]
    resources_are_enough = True

    for indicator in machine_indicators:

        if machine_indicators[indicator] < drink_costs[indicator]:
            resources_are_enough = False
            print(f"\n*** Sorry, there is not enough {indicator} ***")

    return resources_are_enough


def money_was_processed(drink):
    print("\n*** Please insert coins. ***\n")
    total_inserted_money = 0

    for coin_type in COIN_VALUES:
        coin_amount = int(input(f"How many {coin_type}s? "))
        total_inserted_money += COIN_VALUES[coin_type] * coin_amount

    money_was_processed = False
    global revenue

    if DRINK_COSTS[drink]["money"] > total_inserted_money:
        print(
            f"\n*** Sorry, {format_indicator('money', total_inserted_money)} "
            f"is not enough to buy a {drink} ({format_indicator('money', DRINK_COSTS[drink]['money'])}). ***")
        print("\n ***Money refunded. ***")

    else:
        if total_inserted_money > DRINK_COSTS[drink]["money"]:
            change = total_inserted_money - DRINK_COSTS[drink]["money"]
            print(f"\nHere is {format_indicator('money', change)} in change.")

        revenue += total_inserted_money
        money_was_processed = True

    return money_was_processed


def print_report():
    print("\n")

    for i in machine_indicators:
        print(f"{i.title()}: {format_indicator(i, machine_indicators[i])}")

    print(f"Revenue: {format_indicator('money', revenue)}\n")


def make_drink(drink):
    print("making drink")


def main():

    while True:
        user_input = input("\nWhat would you like? (espresso/latte/capuccino) ")

        match user_input:
            case "report":
                print_report()

            case "off":
                exit()

            case "espresso" | "latte" | "cappuccino":
                if resources_are_enough(user_input) and money_was_processed(user_input):
                    make_drink(user_input)

            case _:
                print("\n*** Invalid input ***")


if __name__ == "__main__":
    main()
