from tkinter import *
from tkinter import messagebox
import json

import pyperclip

import pypassword_generator

LETTERS_AMOUNT_FOR_GENERATED_PASSWORD = 5
DIGITS_AMOUNT_FOR_GENERATED_PASSWORD = 5
SYMBOLS_AMOUNT_FOR_GENERATED_PASSWORD = 3


def main():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=40)
    window.resizable(False, False)

    image_canvas = Canvas(width=200, height=200)
    background_image = PhotoImage(file="logo.png")
    image_canvas.create_image(135, 80, image=background_image)
    image_canvas.create_text(135, 180, text="")
    image_canvas.grid(row=0, column=1)

    Label(text="Website:").grid(row=2, column=0)
    Label(text="Email/Username:").grid(row=3, column=0)
    Label(text="Password:").grid(row=4, column=0)

    website_entry = Entry(width=45, name="website")
    website_entry.grid(row=2, column=1, columnspan=2)
    website_entry.focus()

    email_entry = Entry(width=45, name="username")
    email_entry.grid(row=3, column=1, columnspan=2)

    password_entry = Entry(width=25, name="password")
    password_entry.grid(row=4, column=1)

    generate_password_button = Button(text="Generate Password",
                                      command=lambda: generate_password(password_entry, generate_password_button))
    generate_password_button.grid(row=4, column=2)

    add_button = Button(text="Save password",
                        command=lambda: save_data([website_entry, email_entry, password_entry]))
    add_button.grid(row=5, column=1, columnspan=2)
    add_button.config(width=42)

    window.mainloop()


def string_is_valid(string):
    return bool(string is not None and string.strip())


def get_validated_entries(entries):
    return {entry.winfo_name(): string_is_valid(entry.get()) for entry in entries}


def save_data(entries):
    validated_entries_map = get_validated_entries(entries)
    invalid_entries = [f"❌ {entry_name}" for (entry_name, entry_is_valid) in validated_entries_map.items() if
                       not entry_is_valid]

    if len(invalid_entries) > 0:
        invalid_entries = "\n".join(invalid_entries)
        messagebox.showinfo(title="Invalid values",
                            message=f"Please check for invalid values in these fields:\n\n{invalid_entries}")

    else:
        data = {}

        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("Data file not found, creating new one")

        data.update(format_password_data(entries))

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        for entry in entries:
            clear_entry(entry)


def format_password_data(entries):
    raw_data = {entry.winfo_name(): entry.get() for entry in entries}
    return {
        raw_data["website"]:
            {key: value for (key, value) in raw_data.items() if key != "website"}
    }


def clear_entry(entry):
    entry.delete(0, END)


def generate_password(password_entry, password_button):
    generated_password = pypassword_generator.generate_password(LETTERS_AMOUNT_FOR_GENERATED_PASSWORD,
                                                                DIGITS_AMOUNT_FOR_GENERATED_PASSWORD,
                                                                SYMBOLS_AMOUNT_FOR_GENERATED_PASSWORD)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)

    try:
        # check requirements for Linux: https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error
        pyperclip.copy(generated_password)
        password_button.config(text="Copied to clipboard!")
        password_button.after(ms=1000, func=lambda: password_button.config(text="Generate Password"))

    except pyperclip.PyperclipException:
        pass


if __name__ == "__main__":
    main()
