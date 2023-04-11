from tkinter import Label


class PomoTimer(Label):

    def __init__(self, minutes: int, tick_event, end_event=None):
        super().__init__()
        self.minutes = minutes
        self.seconds = 0
        self.text = f"{self.minutes}:{self.seconds}"
        self.tick_event = tick_event
        self.end_event = end_event

    def tick(self):

        if self.seconds != 0:
            self.seconds -= 1

        elif self.minutes == 0 and self.end_event is not None:
            self.end_event()

        else:
            self.seconds = 59

            if self.minutes > 0:
                self.minutes -= 1

        self.text = f"{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"
        self.tick_event()
        self.after(ms=1000, func=self.tick)

    def start(self):
        self.after(ms=1000, func=self.tick)
