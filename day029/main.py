from tkinter import *
from tkinter import messagebox


def main():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    image_canvas = Canvas(width=200, height=200)
    background_image = PhotoImage(file="logo.png")
    image_canvas.create_image(135, 100, image=background_image)
    image_canvas.grid(row=0, column=1)

    Label(text="Website:").grid(row=1, column=0)
    Label(text="Email/Username:").grid(row=2, column=0)
    Label(text="Password:").grid(row=3, column=0)

    website_entry = Entry(width=45, name="website")
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()

    email_entry = Entry(width=45, name="e-mail/username")
    email_entry.grid(row=2, column=1, columnspan=2)

    password_entry = Entry(width=25, name="password")
    password_entry.grid(row=3, column=1)

    generate_pwd_button = Button(text="Generate Password")
    generate_pwd_button.grid(row=3, column=2)

    add_button = Button(text="Add",
                        command=lambda: save_data([website_entry, email_entry, password_entry]))
    add_button.grid(row=4, column=1, columnspan=2)
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
        details_entered = "\n".join([f"∙ {entry.winfo_name()}: {entry.get()}" for entry in entries])
        save_is_confirmed = messagebox.askokcancel(title="Confirm save",
                                                   message=f"These are the details entered:\n\n{details_entered} \n\nIs it ok to save?")

        if save_is_confirmed:

            with open("data.txt", "a") as file:
                data_to_file = "|".join([f"{entry.winfo_name()}={entry.get()}" for entry in entries]) + "\n"
                file.write(data_to_file)

                for entry in entries:
                    clear_entry(entry)


def clear_entry(entry):
    entry.delete(0, END)


if __name__ == "__main__":
    main()
