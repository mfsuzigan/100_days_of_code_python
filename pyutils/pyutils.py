import logging

from getch import getch


def escape_was_pressed():
    return ord(getch()) == 27


def get_pressed_key():
    return getch()


def get_configs(required_configs_set: set, path: str = None):
    try:
        with open(f"{path + '/' if path else ''}configurations.ini") as configurations_file:
            configs = {key: value for (key, value) in
                       [line.strip().split("=") for line in configurations_file.readlines()]}

    except FileNotFoundError:
        logging.exception("Configuration file configurations.ini not found")

    if not required_configs_set.issubset(configs):
        raise Exception(
            f"Required keys not found in configurations.ini: {required_configs_set.difference(configs.keys())}")

    return configs
