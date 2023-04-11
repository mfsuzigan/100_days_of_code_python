from tkinter import *

from pomotimer import PomoTimer

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def main():
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    timer_label.grid(row=0, column=1)

    canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
    image = PhotoImage(file='tomato.png')
    canvas.create_image(100, 112, image=image)
    canvas.grid(row=1, column=1)

    text_component = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

    timer = PomoTimer(minutes=2, tick_event=lambda: canvas.itemconfig(text_component, text=timer.text))
    timer.start()

    start_button = Button(text="Start")
    start_button.grid(row=2, column=0)

    reset_button = Button(text="Reset")
    reset_button.grid(row=2, column=2)

    checkmarks_label = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    checkmarks_label.grid(row=3, column=1)

    window.mainloop()


if __name__ == "__main__":
    main()
