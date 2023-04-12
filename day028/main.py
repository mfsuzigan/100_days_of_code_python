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

    phase_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    phase_label.grid(row=0, column=1)

    image_canvas = Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
    image_canvas.grid(row=1, column=1)
    background_image = PhotoImage(file='tomato.png')
    image_canvas.create_image(175, 112, image=background_image)

    timer_text = image_canvas.create_text(175, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
    timer = PomoTimer(tick_event=lambda: image_canvas.itemconfig(timer_text, text=timer.value))

    start_button = Button(text="Start", command=timer.start)
    start_button.grid(row=2, column=0)

    reset_button = Button(text="Reset")
    reset_button.grid(row=2, column=2)

    checkmarks_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    checkmarks_label.grid(row=3, column=1)

    engine = PomoEngine(work_minutes=WORK_MIN, short_break_minutes=SHORT_BREAK_MIN, long_break_minutes=LONG_BREAK_MIN)

    run_pomodoro(engine, timer, phase_label, checkmarks_label)

    window.mainloop()


def run_pomodoro(engine, timer: PomoTimer, phase_label, checkmarks_label):
    next_phase = engine.get_next_phase()
    phase_label.config(text=next_phase["label"])
    checkmarks_label.config(text=next_phase["checkmarks"])

    timer.minutes = next_phase["duration"]
    timer.end_event = lambda: run_pomodoro(engine, timer, phase_label, checkmarks_label)
    timer.tick()


if __name__ == "__main__":
    main()
