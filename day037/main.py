import argparse

import pandas
import requests
import logging
from workout import Workout
from requests.adapters import HTTPAdapter, Retry

PIXELA_ENDPOINT = "https://pixe.la"
USERNAME = "mfsuzigan"
token = None


def create_user():
    request_body = {
        "token": token,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(f"{PIXELA_ENDPOINT}/v1/users", json=request_body)
    response.raise_for_status()
    print(response.json())


def create_graph():
    request_body = {
        "id": "workouts",
        "name": "Workouts",
        "unit": "workout",
        "type": "int",
        "color": "sora",
        "timezone": "America/Sao_Paulo"
    }

    headers = {
        "X-USER-TOKEN": token
    }

    response = requests.post(f"{PIXELA_ENDPOINT}/v1/users/{USERNAME}/graphs", json=request_body, headers=headers)
    print(response.json())
    response.raise_for_status()


def update_graph():
    request_body = {
        "id": "workouts",
        "name": "Workouts",
        "unit": "workouts",
        "type": "int",
        "color": "ajisai",
        "timezone": "America/Sao_Paulo"
    }

    headers = {
        "X-USER-TOKEN": token
    }

    response = requests.put(f"{PIXELA_ENDPOINT}/v1/users/{USERNAME}/graphs/workouts", json=request_body,
                            headers=headers)
    response.raise_for_status()


def post_workout(workout: Workout):
    headers = {
        "X-USER-TOKEN": token
    }

    session = requests.session()
    retries = Retry(total=1000, backoff_factor=1, status_forcelist=[503])
    session.mount("http://", HTTPAdapter(max_retries=retries))
    response = session.post(f"{PIXELA_ENDPOINT}/v1/users/{USERNAME}/graphs/workouts", json=workout.to_request(),
                            headers=headers)

    # Not resilient
    # response = requests.post(f"{PIXELA_ENDPOINT}/v1/users/{USERNAME}/graphs/workouts", json=workout.to_request(),
    #                          headers=headers)

    print(f"{workout.date}: {response.json()}")
    # response.raise_for_status()


def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument("--token", "-t", required=True, help="Pixela API Token")
    global token
    token = parser.parse_args()

    workouts_csv = pandas.read_csv("workouts.csv")

    # converting float columns in CSV to int
    for column in workouts_csv.select_dtypes(include=["float64"]):
        workouts_csv[column] = workouts_csv[column].fillna(0).astype("int64")

    for workout in workouts_csv.itertuples():
        post_workout(Workout(date=f"{workout.date.replace('-', '')}", weightlifting=workout.wl, cycling=workout.c,
                             walking=workout.wk))


if __name__ == "__main__":
    main()
