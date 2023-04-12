from tkinter import Label

TICK_TIME_MILLIS = 3
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"


class PomoEngine:

    def __init__(self, work_minutes, short_break_minutes, long_break_minutes):
        self.work_minutes = work_minutes
        self.short_break_minutes = short_break_minutes
        self.long_break_minutes = long_break_minutes

        self.phases = {
            0: {"label": "Work", "duration": self.work_minutes, "checkmarks": "", "title_color": GREEN},
            1: {"label": "Short Break 1", "duration": self.short_break_minutes, "checkmarks": "", "title_color": PINK},

            2: {"label": "Work", "duration": self.work_minutes, "checkmarks": "✓", "title_color": GREEN},
            3: {"label": "Short Break 2", "duration": self.short_break_minutes, "checkmarks": "✓", "title_color": PINK},

            4: {"label": "Work", "duration": self.work_minutes, "checkmarks": "✓✓", "title_color": GREEN},
            5: {"label": "Short Break 3", "duration": self.short_break_minutes, "checkmarks": "✓✓",
                "title_color": PINK},

            6: {"label": "Work", "duration": self.work_minutes, "checkmarks": "✓✓✓", "title_color": GREEN},
            7: {"label": "Short Break 4", "duration": self.short_break_minutes, "checkmarks": "✓✓✓",
                "title_color": PINK},

            8: {"label": "Longer Break", "duration": self.long_break_minutes, "checkmarks": "✓✓✓✓", "title_color": RED}
        }

        self.current_phase = -1

    def get_next_phase(self):
        self.current_phase += 1

        if self.current_phase > len(self.phases) - 1:
            self.current_phase = 0

        return self.phases[self.current_phase]

    def reset(self):
        self.current_phase = -1


class PomoTimer(Label):

    def __init__(self, minutes: int = 0, tick_event=None, end_event=None):
        super().__init__()
        self.is_on = False
        self.minutes = minutes
        self.seconds = 0
        self.tick_event = tick_event
        self.end_event = end_event
        self.value = ""
        self.set_value()

    def tick(self):

        if not self.is_on:
            return

        if self.minutes == 0 and self.seconds == 0:
            self.end_event()

        else:

            if self.seconds != 0:
                self.seconds -= 1

            else:
                self.seconds = 59

                if self.minutes > 0:
                    self.minutes -= 1

            self.set_value()
            self.tick_event()
            self.after(ms=TICK_TIME_MILLIS, func=self.tick)

    def reset(self):
        self.minutes = 0
        self.seconds = 0
        self.set_value()

    def set_value(self):
        self.value = f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

    def toggle_on(self):
        self.is_on = True

    def toggle_off(self):
        self.is_on = False
