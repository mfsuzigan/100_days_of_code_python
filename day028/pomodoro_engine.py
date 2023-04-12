from tkinter import Label

TICK_TIME_MILLIS = 3


class PomoEngine:

    def __init__(self, work_minutes, short_break_minutes, long_break_minutes):
        self.work_minutes = work_minutes
        self.short_break_minutes = short_break_minutes
        self.long_break_minutes = long_break_minutes

        self.phases = {
            0: {"label": "Work", "duration": self.work_minutes, "checkmarks": ""},
            1: {"label": "Short Break 1", "duration": self.short_break_minutes, "checkmarks": ""},

            2: {"label": "Work", "duration": self.work_minutes, "checkmarks": "✓"},
            3: {"label": "Short Break 2", "duration": self.short_break_minutes, "checkmarks": "✓"},

            4: {"label": "Work", "duration": self.work_minutes, "checkmarks": "✓✓"},
            5: {"label": "Short Break 3", "duration": self.short_break_minutes, "checkmarks": "✓✓"},

            6: {"label": "Work", "duration": self.work_minutes, "checkmarks": "✓✓✓"},
            7: {"label": "Short Break 4", "duration": self.short_break_minutes, "checkmarks": "✓✓✓"},

            8: {"label": "Longer Break", "duration": self.long_break_minutes, "checkmarks": "✓✓✓✓"}
        }

        self.current_phase = -1

    def get_next_phase(self):
        self.current_phase += 1

        if self.current_phase > len(self.phases) - 1:
            self.current_phase = 0

        return self.phases[self.current_phase]


class PomoTimer(Label):

    def __init__(self, minutes: int = 0, tick_event=None, end_event=None):
        super().__init__()
        self.minutes = minutes
        self.seconds = 0
        self.value = f"{self.minutes}:{self.seconds}"
        self.tick_event = tick_event
        self.end_event = end_event
        self.is_running = False

    def tick(self):

        if not self.is_running:
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

            self.value = f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"
            self.tick_event()
            self.after(ms=TICK_TIME_MILLIS, func=self.tick)

    def start(self):
        self.is_running = True
        self.after(ms=TICK_TIME_MILLIS, func=self.tick)
