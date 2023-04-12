from tkinter import *


def main():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    image_canvas = Canvas(width=200, height=200)
    background_image = PhotoImage(file="logo.png")
    image_canvas.create_image(100, 100, image=background_image)
    image_canvas.grid(row=0, column=0)

    window.mainloop()


if __name__ == "__main__":
    main()
