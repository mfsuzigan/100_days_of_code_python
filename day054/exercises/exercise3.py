import time


def speed_calc_decorator(func):
    def decorator():
        start = time.time()
        func()
        print(f"{func.__name__} run duration: {time.time() - start}")

    return decorator


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


def main():
    fast_function()
    slow_function()


if __name__ == "__main__":
    main()
