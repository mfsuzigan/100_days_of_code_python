from tkinter import *


def main():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    image_canvas = Canvas(width=200, height=200)
    background_image = PhotoImage(file="logo.png")
    image_canvas.create_image(100, 100, image=background_image)
    image_canvas.grid(row=0, column=1)

    Label(text="Website:").grid(row=1, column=0)
    Label(text="Email/Username:").grid(row=2, column=0)
    Label(text="Password:").grid(row=3, column=0)

    website_entry = Entry(width=45)
    website_entry.grid(row=1, column=1, columnspan=2)

    email_entry = Entry(width=45)
    email_entry.grid(row=2, column=1, columnspan=2)

    password_entry = Entry(width=25)
    password_entry.grid(row=3, column=1)

    generate_pwd_button = Button(text="Generate Password")
    generate_pwd_button.grid(row=3, column=2)

    add_button = Button(text="Add")
    add_button.grid(row=4, column=1, columnspan=2)
    add_button.config(width=42)

    window.mainloop()


if __name__ == "__main__":
    main()
