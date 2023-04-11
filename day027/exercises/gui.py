from tkinter import *

label: Label = None
text_input: Entry = None


def main():
    window = Tk()
    window.title("Hello Tkinter GUI")
    window.minsize(width=800, height=600)

    global label
    label = Label(text="This is a label", font=("Arial", 24, "bold"))
    label.grid(row=0, column=0)

    button = Button(text="Click me", command=change_label)
    button.grid(row=1, column=1)

    global text_input
    text_input = Entry(width=10)
    text_input.grid(row=3, column=3)

    button2 = Button(text="2nd button", command=change_label)
    button2.grid(row=0, column=2)

    window.mainloop()


def change_label():
    label.config(text=text_input.get())


if __name__ == "__main__":
    main()
