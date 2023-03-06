from getch import getch

def escape_was_pressed():
    return ord(getch()) == 27

def get_pressed_key():
    return getch()