def make_bold(func):
    def decorator():
        return f"<b>{func()}</b>"

    return decorator


def make_italic(func):
    def decorator():
        return f"<em>{func()}</em>"

    return decorator


def make_underlined(func):
    def decorator():
        return f"<u>{func()}</u>"

    return decorator
