import argparse


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--from-mail", "-f", required=True, help="Sender's email")
    arg_parser.add_argument("--password", "-p", required=True, help="Password for sender's email")
    arg_parser.add_argument("--smtp", "-s", required=True, help="Sender's SMTP server")
    arg_parser.add_argument("--to-mail", "-t", required=True, help="Recipient's email")

    return arg_parser.parse_args()
