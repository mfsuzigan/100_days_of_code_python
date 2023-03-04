def encode(input):
    return

def decode(input):
    return

def get_input():
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    return [shift, text]
    

def main():
    print("Select an option: ")
    print("1 - encode")
    print("2 - decode")
    print("3 - exit")
    option_chosen = input()

    match option_chosen:
        
        case "1":
            input = get_input()
            encode(input)

        case "2":
            input = get_input()
            decode(input)

        case "3":
            exit()


if __name__ == "__main__":
    main()
