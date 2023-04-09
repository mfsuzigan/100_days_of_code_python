numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Joe"
lst = [l for l in name]
print(lst)

doubles = [2 * n for n in range(1, 5)]
print(doubles)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
all_caps = [n.upper() for n in names if len(n) >= 5]
print(all_caps)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squares = [n ** 2 for n in numbers]
print(squares)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

with open("file1.txt") as file1:
    with open("file2.txt") as file2:
        result = [int(n.strip()) for n in file1.readlines() if n in file2.readlines()]
print(result)
