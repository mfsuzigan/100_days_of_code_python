import os

import requests


class Customer:
    first_name: str
    last_name: str
    email: str


def main():
    print("Welcome to Michel's Fight Club")
    print("We find the best flight deals and email you.")

    customer = Customer()
    customer.first_name = input("What is your first name? ")
    customer.last_name = input("What is your last name? ")
    customer.email = input("What is your e-mail? ")

    while input("Type your e-mail again: ") != customer.email:
        continue

    post_user_data(customer)
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
