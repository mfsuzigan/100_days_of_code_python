import requests

url = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url, params=parameters)
response.raise_for_status()
response = response.json()

question_data = response["results"]
