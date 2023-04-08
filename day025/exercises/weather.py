# print all lines standard way
# with open("weather_data.csv") as input_file:
#     data = [line.strip() for line in input_file.readlines()]

# getting all values from a single column standard way
# with open("weather_data.csv") as input_file:
#     data = csv.reader(input_file)
#     temperatures = [int(d[1]) for d in list(data)[1:]]

import pandas

data = pandas.read_csv("weather_data.csv")

# getting all values from a single column with pandas
# print(data["temp"])

# getting average value of single column with pandas
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(f"{average_temp :.2f}")

# getting biggest value with pandas
# print(data["temp"].max())

# getting temperatures of mondays and converting to Fahrenheit
print(data[data.day == "Monday"].temp * 9 / 5 + 32)
