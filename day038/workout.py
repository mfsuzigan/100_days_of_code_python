import datetime


class Workout:

    def __init__(self, exercise, duration=float, calories=float):
        now = datetime.datetime.now()

        self.date = now.strftime("%Y-%m-%d")
        self.time = now.strftime("%H:%M:%S")
        self.exercise = exercise
        self.duration_min = str(datetime.timedelta(minutes=int(duration)))
        self.calories = calories

    @staticmethod
    def from_json(json):
        return Workout(exercise=json["name"], duration=json["duration_min"],
                       calories=json["nf_calories"])
