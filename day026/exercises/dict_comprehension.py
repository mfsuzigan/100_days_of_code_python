import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
scores = {name: random.randint(0, 101) for name in names}
print(scores)

passed = {key: value for (key, value) in scores.items() if value >= 60}
print(passed)

sentence = "Try Googling to find out how to convert a sentence into a list of words"
letter_count = {word: len(word) for word in sentence.split()}
print(letter_count)

weather_c = {
    'Monday': 53.6,
    'Tuesday': 57.2,
    'Wednesday': 59.0,
    'Thursday': 57.2,
    'Friday': 69.8,
    'Saturday': 71.6,
    'Sunday': 75.2
}
weather_f = {day: round((temp_c * 9 / 5) + 32, 2) for (day, temp_c) in weather_c.items()}
print(weather_f)
