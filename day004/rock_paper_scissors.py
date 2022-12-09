from itertools import cycle
import random

rockDoodle = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paperDoodle = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissorsDoodle = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

doodlesByValue = {0: rockDoodle, 1: paperDoodle, 2: scissorsDoodle}
valuesHierarchy = cycle([0, 2, 1])

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(f"{doodlesByValue[input]}")

print("\nComputer chose:")
cpuInput = random.randint(0,2)
print(f"{doodlesByValue[cpuInput]}")

if input == cpuInput:
    print("It's a draw")

else:
    previousValue = None

    for value in valuesHierarchy:

        if value == input:

            if next(valuesHierarchy) == cpuInput:
                print("You win")
                break

            elif previousValue == cpuInput:
                print("You lose")
                break

        previousValue = value

    
