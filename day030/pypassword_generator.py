import random

# ASCII:

# 33-47 - special chars interval 1
# 58-64 - special chars interval 2
# 48-57 - digits
# 97-122 - letters interval 1, lowercase
# 65-90 - letters interval 2, uppercase

ascii_limits_by_char_type = {
    "letters": [[65, 90], [97, 122]],
    "symbols": [[33, 47], [58, 64]],
    "numbers": [48, 57]
}


def get_char_list(char_type, list_size):
    char_type_ascii_limits = ascii_limits_by_char_type[char_type]
    multiple_char_intervals_exist_for_type = type(char_type_ascii_limits[0]) == type([])
    output_list = []

    for i in range(0, list_size):
        if multiple_char_intervals_exist_for_type:
            ascii_limits = char_type_ascii_limits[random.randint(0, (len(char_type_ascii_limits) - 1))]

        else:
            ascii_limits = char_type_ascii_limits

        output_list.append(chr(random.randint(ascii_limits[0], ascii_limits[1])))

    return output_list


def generate_password(number_of_letters, number_of_digits, number_of_symbols):
    password_config = {"letters": number_of_letters, "numbers": number_of_digits, "symbols": number_of_symbols}

    char_list = []

    for (char_type, char_type_amount) in password_config.items():
        char_list.extend(get_char_list(char_type, char_type_amount))

    random.shuffle(char_list)
    return ''.join(char_list)

# print("Welcome to the PyPassword Generator!")
# char_list = []
#
# for char_type in ascii_limits_by_char_type:
#     char_amount = int(input(f"How many {char_type} would like in your password? "))
#     char_list.extend(get_char_list(char_type, char_amount))
#
# random.shuffle(char_list)
# print(f"Here's your password: {''.join(char_list)}")
