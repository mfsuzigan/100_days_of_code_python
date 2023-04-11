from tkinter import *


def main():
    window = Tk()
    window.title("Mile to km converter")
    window.minsize(width=250, height=100)
    window.config(padx=30, pady=30)

    text_input = Entry(width=15)
    text_input.grid(row=0, column=1)
    text_input.focus()

    miles_label = Label(text="Miles")
    miles_label.grid(row=0, column=2)
    miles_label.config(padx=5, pady=5)

    equals_label = Label(text="is equal to")
    equals_label.grid(row=1, column=0)

    result_label = Label(text="0")
    result_label.grid(row=1, column=1)
    result_label.config(padx=5, pady=5)

    km_label = Label(text="km")
    km_label.grid(row=1, column=2)

    calculate_button = Button(text="Calculate", command=lambda: convert(text_input.get(), result_label))
    calculate_button.grid(row=2, column=1)

    window.mainloop()


def convert(miles_input, result_label):
    result_label.config(text=f"{float(miles_input) * 1.609 :.3f}")


if __name__ == "__main__":
    main()
