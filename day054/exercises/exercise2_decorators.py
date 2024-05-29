def simple_function():
    print("Hi from a function")


def decorator(func):
    print("Decorating")
    return func


def decorator2(func):
    def inner():
        print("Inner before")
        func()
        print("Inner after")

    print("Decorator2")
    return inner


@decorator2
def simple_decorated_function():
    print("Hi from a decorated function")


def main():
    simple_function()
    simple_decorated_function()


if __name__ == "__main__":
    main()
