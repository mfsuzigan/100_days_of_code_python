from tkinter import Label

TICK_TIME_MILLIS = 10


class Pomodoro:

    def __init__(self, work_minutes, short_break_minutes, long_break_minutes):
        self.work_minutes = work_minutes
        self.short_break_minutes = short_break_minutes
        self.long_break_minutes = long_break_minutes

        self.segments = {
            0: {"label": "Work", "duration": self.work_minutes},
            1: {"label": "Short Break 1", "duration": self.short_break_minutes},

            2: {"label": "Work", "duration": self.work_minutes},
            3: {"label": "Short Break 2", "duration": self.short_break_minutes},

            4: {"label": "Work", "duration": self.work_minutes},
            5: {"label": "Short Break 3", "duration": self.short_break_minutes},

            6: {"label": "Work", "duration": self.work_minutes},
            7: {"label": "Short Break 4", "duration": self.short_break_minutes},

            8: {"label": "Longer Break", "duration": self.long_break_minutes}
        }

        self.current_segment = -1

    def get_next_segment(self):
        self.current_segment += 1

        if self.current_segment > len(self.segments):
            self.current_segment = 0

        return self.segments[self.current_segment]


class PomoTimer(Label):

    def __init__(self, minutes: int = 0, tick_event=None, end_event=None):
        super().__init__()
        self.minutes = minutes
        self.seconds = 0
        self.text = f"{self.minutes}:{self.seconds}"
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

            self.text = f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"
            self.tick_event()
            self.after(ms=TICK_TIME_MILLIS, func=self.tick)

    def start(self):
        self.is_running = True
        self.after(ms=TICK_TIME_MILLIS, func=self.tick)