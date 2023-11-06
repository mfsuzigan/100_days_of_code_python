class Workout:

    def __init__(self, exercise, duration=float, calories=float):
        self.date = ""
        self.time = ""
        self.exercise = exercise
        self.duration_min = duration
        self.calories = calories

    @staticmethod
    def from_json(json):
        return Workout(exercise=json["user_input"], duration=json["duration_min"],
                       calories=json["nf_calories"])
