# unlimited positional arguments
def add(*args):
    return sum(args)


def operation(n, **kwargs):
    print(n)
    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
print(add(1))

print(operation(2, add=3, multiply=5))
