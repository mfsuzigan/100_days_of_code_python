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

window = None
engine = None
timer = None
phase_label = None
image_canvas = None
timer_text = None
checkmarks_label = None


def main():
    global window
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=50, pady=25, bg=YELLOW)
    window.resizable(False, False)

    global phase_label
    phase_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    phase_label.grid(row=0, column=1)

    global image_canvas
    image_canvas = Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
    image_canvas.grid(row=1, column=1)
    background_image = PhotoImage(file='tomato.png')
    image_canvas.create_image(175, 112, image=background_image)

    global timer_text
    timer_text = image_canvas.create_text(175, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))

    global checkmarks_label
    checkmarks_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    checkmarks_label.grid(row=3, column=1)

    global engine
    engine = PomoEngine(work_minutes=WORK_MIN, short_break_minutes=SHORT_BREAK_MIN, long_break_minutes=LONG_BREAK_MIN)

    global timer
    timer = PomoTimer(tick_event=lambda: image_canvas.itemconfig(timer_text, text=timer.value))
    timer.end_event = run_pomodoro_phase

    start_button = Button(text="Start", command=run_pomodoro_phase)
    start_button.grid(row=2, column=0)

    reset_button = Button(text="Reset", command=reset_pomodoro)
    reset_button.grid(row=2, column=2)

    window.mainloop()


# noinspection PyUnresolvedReferences
def run_pomodoro_phase():
    next_phase = engine.get_next_phase()
    phase_label.config(text=next_phase["label"], fg=next_phase["title_color"])
    checkmarks_label.config(text=next_phase["checkmarks"])
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    timer.minutes = next_phase["duration"]

    timer.toggle_on()
    timer.tick()


# noinspection PyUnresolvedReferences
def reset_pomodoro():
    timer.toggle_off()
    engine.reset()
    timer.reset()

    image_canvas.itemconfig(timer_text, text="25:00")
    phase_label.config(text="")
    checkmarks_label.config(text="")


if __name__ == "__main__":
    main()
