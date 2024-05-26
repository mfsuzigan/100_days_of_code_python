@decorator
def simple_decorated_function():
    print("Hi from a decorated function")


def simple_function():
    print("Hi from a function")


def decorator(func):
    return func
