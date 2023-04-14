from tkinter import *
import json
import pyperclip
import pypassword_generator

MESSAGE_FLASHING_DURATION_SECONDS = 1500

PASSWORD_MAP_KEY = "password"
USERNAME_MAP_KEY = "username"
WEBSITE_MAP_KEY = "website"

LETTERS_AMOUNT_FOR_GENERATED_PASSWORD = 5
DIGITS_AMOUNT_FOR_GENERATED_PASSWORD = 5
SYMBOLS_AMOUNT_FOR_GENERATED_PASSWORD = 3

window = Tk()
canvas = Canvas(width=242, height=200)
canvas_message = canvas.create_text(148, 180, text="")
username_entry = Entry(name="username")
password_entry = Entry(name="password")
website_entry = Entry(name="website")


def main():
    window.title("Password Manager")
    window.config(padx=20, pady=20)
    window.resizable(False, False)

    background_image = PhotoImage(file="logo.png")
    canvas.create_image(148, 80, image=background_image)
    canvas.grid(row=0, column=1)

    Label(text="Website:").grid(row=2, column=0)
    Label(text="Email/Username:").grid(row=3, column=0)
    Label(text="Password:").grid(row=4, column=0)

    website_entry.grid(row=2, column=1, sticky="WE")
    website_entry.focus()

    username_entry.grid(row=3, column=1, columnspan=3, sticky="WE")

    password_entry.grid(row=4, column=1, sticky="WE")

    Button(text="Search", command=lambda: search_data(website_entry.get())).grid(row=2, column=2, columnspan=2,
                                                                                 sticky="WE")
    Button(text="Generate", command=generate_password).grid(row=4, column=2, sticky="WE")
    Button(text="Copy", command=copy_password_to_clipboard).grid(row=4, column=3)

    save_button = Button(text="Save password", command=save_data)
    save_button.grid(row=5, column=1, columnspan=3)
    save_button.config(width=47)

    window.mainloop()


def string_is_valid(string):
    return bool(string is not None and string.strip())


def get_validated_entries(entries):
    return {entry.winfo_name(): string_is_valid(entry.get()) for entry in entries}


def save_data():
    entries = [website_entry, username_entry, password_entry]
    validated_entries_map = get_validated_entries(entries)
    invalid_entries = [f"❌ {entry_name}" for (entry_name, entry_is_valid) in validated_entries_map.items() if
                       not entry_is_valid]

    if len(invalid_entries) > 0:
        show_message("All fields required")

    else:
        data = read_data_file()
        data.update(format_password_data(entries))

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        show_message("Password saved!")

        for entry in entries:
            clear_entry(entry)


def read_data_file():
    data = {}
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        pass

    return data


def format_password_data(entries):
    raw_data = {entry.winfo_name(): entry.get() for entry in entries}
    return {
        raw_data["website"]:
            {key: value for (key, value) in raw_data.items() if key != "website"}
    }


def search_data(website_name):
    if website_name != "":
        data = read_data_file()

        try:
            password_data = data[website_name]

            username_entry.delete(0, END)
            username_entry.insert(END, password_data[USERNAME_MAP_KEY])

            password_entry.delete(0, END)
            password_entry.insert(END, password_data[PASSWORD_MAP_KEY])

            show_message(f"Found entry for '{website_name}'")

        except KeyError:
            show_message("Entry not found")


def clear_entry(entry):
    entry.delete(0, END)


def show_message(message, flashing=True):
    message_before = canvas.itemcget(canvas_message, "text")
    canvas.itemconfig(canvas_message, text=message)

    if flashing:
        canvas.after(MESSAGE_FLASHING_DURATION_SECONDS, func=lambda: show_message(message_before, flashing=False))


def generate_password():
    generated_password = pypassword_generator.generate_password(LETTERS_AMOUNT_FOR_GENERATED_PASSWORD,
                                                                DIGITS_AMOUNT_FOR_GENERATED_PASSWORD,
                                                                SYMBOLS_AMOUNT_FOR_GENERATED_PASSWORD)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    copy_password_to_clipboard()


def copy_password_to_clipboard():
    password = password_entry.get()

    if password != "":

        try:
            # check requirements for Linux: https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error
            pyperclip.copy(password)
            show_message("Password copied to clipboard")

        except pyperclip.PyperclipException:
            pass


if __name__ == "__main__":
    main()
