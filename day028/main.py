from tkinter import *

from pomodoro_engine import *

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
    window.config(padx=50, pady=25, bg=YELLOW)

    segment_description_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    segment_description_label.grid(row=0, column=1)

    canvas = Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
    canvas.grid(row=1, column=1)
    background_image = PhotoImage(file='tomato.png')
    canvas.create_image(175, 112, image=background_image)
    timer_text = canvas.create_text(175, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))

    pomotimer = PomoTimer(tick_event=lambda: canvas.itemconfig(timer_text, text=pomotimer.text))

    start_button = Button(text="Start", command=pomotimer.start)
    start_button.grid(row=2, column=0)

    reset_button = Button(text="Reset")
    reset_button.grid(row=2, column=2)

    checkmarks_label = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    checkmarks_label.grid(row=3, column=1)

    pomodoro = Pomodoro(work_minutes=WORK_MIN, short_break_minutes=SHORT_BREAK_MIN, long_break_minutes=LONG_BREAK_MIN)
    xxx(pomodoro, pomotimer, segment_description_label)

    window.mainloop()


def xxx(pomodoro, pomotimer: PomoTimer, segment_description_label):
    next_segment = pomodoro.get_next_segment()
    segment_description_label.config(text=next_segment["label"])

    pomotimer.minutes = next_segment["duration"]
    pomotimer.end_event = lambda: xxx(pomodoro, pomotimer, segment_description_label)
    pomotimer.tick()


if __name__ == "__main__":
    main()
