import argparse
import logging

from day051.InternetSpeedTwitterBot import InternetSpeedTwitterBot

args: argparse.Namespace


def get_args():
    logging.info("Reading args")
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--username", "-u", required=True, help="Twitter account username")
    arg_parser.add_argument("--password", "-p", required=True, help="Twitter account password")

    return arg_parser.parse_args()


def main():
    logging.getLogger().setLevel(logging.INFO)

    global args
    args = get_args()

    # bot = InternetSpeedTwitterBot(InternetSpeedTwitterBot.PageLoadStrategy.EAGER)
    # bot.get_internet_speed()

    # bot.set_page_load_strategy(InternetSpeedTwitterBot.PageLoadStrategy.NORMAL)
    bot = InternetSpeedTwitterBot()
    bot.tweet_at_provider(args.username, args.password)


if __name__ == "__main__":
    main()
