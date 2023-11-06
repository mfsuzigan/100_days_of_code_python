import os
import sys

import requests
from workout import Workout

sys.path.append(f"{os.path.dirname(__file__)}/..")
from pyutils.pyutils import get_configs

configs = {}


def main():
    global configs
    configs = get_configs(
        required_configs_set={"NUTRITIONIX_API_ENDPOINT", "NUTRITIONIX_APPLICATION_ID",
                              "NUTRITIONIX_APPLICATION_KEY",
                              "SHEETY_SHEET_ENDPOINT", "SHEETY_ENDPOINT_AUTH_TOKEN"},
        path=f"{os.path.dirname(__file__)}")

    query = input("Tell me the exercises you did: ")

    for exercise in get_exercise_information(query)["exercises"]:
        workout = Workout.from_json(exercise)
        print(f"Recording exercise: {workout.exercise} (duration {workout.duration_min})")
        save_to_sheet(workout)

    print("Done!")


def save_to_sheet(workout):
    body = {
        "workout": {
            "date": f"{workout.date}",
            "time": f"{workout.time}",
            "exercise": f"{workout.exercise}",
            "duration": workout.duration_min,
            "calories (kcal)": workout.calories
        }
    }

    headers = {
        "Authorization": f"Bearer {configs['SHEETY_ENDPOINT_AUTH_TOKEN']}"
    }

    response = requests.post(
        f"{configs['SHEETY_SHEET_ENDPOINT']}",
        json=body, headers=headers)

    response.raise_for_status()

    return response.json()


def get_exercise_information(query):
    body = {
        "query": f"{query}",
    }

    headers = {
        "x-app-id": f"{configs['NUTRITIONIX_APPLICATION_ID']}",
        "x-app-key": f"{configs['NUTRITIONIX_APPLICATION_KEY']}",
    }

    response = requests.post(f"{configs['NUTRITIONIX_API_ENDPOINT']}/natural/exercise", json=body, headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    main()
