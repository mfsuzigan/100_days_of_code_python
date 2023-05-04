import datetime
import json


class Workout:
    def __init__(self, weightlifting: int = 0, cycling: int = 0, walking: int = 0, date: str = None):
        self.weightlifting = weightlifting
        self.cycling = cycling
        self.walking = walking
        self.date = date if date else datetime.datetime.now().strftime("%Y%m%d")

    def to_request(self):
        return {
            "date": self.date,
            "quantity": f"{(self.weightlifting + self.cycling + self.walking)}",
            "optional_data": json.dumps({
                "weightlifting": self.weightlifting,
                "cycling": self.cycling,
                "walking": self.walking
            })
        }
