print("Welcome to the Tip Calculator")

total_bill = float(input("What was the total bill? $"))
number_of_people = int(input("How many people will split the bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

individual_pay = total_bill/number_of_people * (1 + tip_percentage/100)

print(f"Each person should pay: ${round(individual_pay, 2): .2f}" )