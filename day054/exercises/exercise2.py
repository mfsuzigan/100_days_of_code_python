def simple_function():
    print("Hi from a function")


def decorator(func):
    print("Decorating")
    return func


@decorator
def simple_decorated_function():
    print("Hi from a decorated function")


def main():
    simple_function()
    simple_decorated_function()


if __name__ == "__main__":
    main()
