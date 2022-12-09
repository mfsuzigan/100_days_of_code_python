from itertools import cycle
import random

rock_doodle = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_doodle = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_doodle = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

doodles_by_value = [rock_doodle, paper_doodle, scissors_doodle]
values_hierarchy = cycle([0, 2, 1])

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if input < 0 or input > 2:
    print("Invalid number. You lose!")
    exit()

print(f"{doodles_by_value[input]}")

print("\nComputer chose:")
cpu_input = random.randint(0,2)
print(f"{doodles_by_value[cpu_input]}")

if input == cpu_input:
    print("It's a draw!")

else:
    previous_value = None

    for value in values_hierarchy:

        if value == input:

            if next(values_hierarchy) == cpu_input:
                print("You win!")
                break

            elif previous_value == cpu_input:
                print("You lose!")
                break

        previous_value = value

    
