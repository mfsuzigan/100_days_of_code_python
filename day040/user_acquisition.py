import os

import requests


class User:
    first_name: str
    last_name: str
    email: str


def main():
    print("Welcome to Michel's Fight Club")
    print("We find the best flight deals and email you.")

    user = User()
    user.first_name = input("What is your first name? ")
    user.last_name = input("What is your last name? ")
    user.email = input("What is your e-mail? ")

    while input("Type your e-mail again: ") != user.email:
        continue

    post_user_data(user)
    print("Congratulations, you're in the club!")


def post_user_data(user):
    headers = {"Authorization": f"Bearer {os.environ['SHEETY_API_AUTH_TOKEN']}"}
    body = {
        "user": {
            "firstName": user.first_name,
            "lastName": user.last_name,
            "email": user.email,
        }
    }
    response = requests.post(f"{os.environ['SHEETY_SHEET_ENDPOINT']}",
                             json=body,
                             headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    main()
