def make_bold(func):
    def decorator():
        return make_styled("b", func)

    return decorator


def make_italic(func):
    def decorator():
        return make_styled("em", func)

    return decorator


def make_underlined(func):
    def decorator():
        return make_styled("u", func)

    return decorator


def make_styled(html_tag, func):
    return f"<{html_tag}>{func()}</{html_tag}>"
