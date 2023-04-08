import pandas

raw_squirrels_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrels_by_fur_color = raw_squirrels_data["Primary Fur Color"].value_counts(dropna=False)
print(squirrels_by_fur_color)
squirrels_by_fur_color.to_csv("squirrels_by_fur_color.csv")

print("Done.")
