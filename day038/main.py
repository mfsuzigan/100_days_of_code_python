import requests

from day038.workout import Workout

APPLICATION_ID = "***"
APPLICATION_KEY = "**"

NUTRITIONIX_API_ENDPOINT = "https://trackapi.nutritionix.com/v2"
SHEETY_API_ENDPOINT = "https://api.sheety.co"


def main():
    query = input("Tell me the exercises you did: ")

    for exercise in get_exercise_information(query)["exercises"]:
        print(exercise)
        workout = Workout.from_json(exercise)
        print(workout.duration_min)
        save_to_sheet(workout)


def save_to_sheet(workout):
    body = {
        "workout": {
            "date": f"{workout.date}",
            "time": f"{workout.time}",
            "exercise": f"{workout.exercise}",
            "duration": workout.duration_min,
            "calories": workout.calories
        }
    }

    headers = {
        "Authorization": "Bearer **"
    }

    response = requests.post(
        f"{SHEETY_API_ENDPOINT}/ebcc8b45da148c254bf923a03f6a98b8/100DaysofcodePythonMyWorkouts/workouts",
        json=body, headers=headers)

    response.raise_for_status()

    return response.json()


def get_exercise_information(query):
    body = {
        "query": f"{query}",
        "gender": "male",
        "weight_kg": 72,
        "height_cm": 167,
        "age": 35
    }

    headers = {
        "x-app-id": f"{APPLICATION_ID}",
        "x-app-key": f"{APPLICATION_KEY}",
    }

    response = requests.post(f"{NUTRITIONIX_API_ENDPOINT}/natural/exercise", json=body, headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    main()
