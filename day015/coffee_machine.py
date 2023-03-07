def format_indicator(name, amount):
    match name:
        case "water" | "milk":
            return f"{amount} ml"
        case "coffee":
            return f"{amount} g"
        case "money":
            return f"${amount / 100:.2f}"


MACHINE_INDICATORS = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}



def print_report():
    for i in MACHINE_INDICATORS:
        print(f"{i.title()}: {format_indicator(i, MACHINE_INDICATORS[i])}")


user_input = input("What would you like? (espresso/latte/capuccino) ")

match user_input:
    case "report":
        print_report()
    case "off":
        exit()
