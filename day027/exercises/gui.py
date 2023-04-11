from tkinter import *

label: Label = None
text_input: Entry = None


def main():
    window = Tk()
    window.title("Hello Tkinter GUI")
    window.minsize(width=800, height=600)

    global label
    label = Label(text="This is a label", font=("Arial", 24, "bold"))
    label.pack()

    button = Button(text="Click me", command=change_label)
    button.pack()

    global text_input
    text_input = Entry(width=10)
    text_input.pack()

    window.mainloop()


def change_label():
    label.config(text=text_input.get())


if __name__ == "__main__":
    main()
