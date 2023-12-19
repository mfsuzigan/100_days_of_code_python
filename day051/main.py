import argparse
import logging

from InternetProvider import InternetProvider
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

args: argparse.Namespace


def get_args():
    logging.info("Reading args")
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--account", "-a", required=True, help="Twitter account's username")
    arg_parser.add_argument("--password", "-p", required=True, help="Twitter account's password")
    arg_parser.add_argument("--min-upload", "-u", required=True, help="Minimum expected upload speed")
    arg_parser.add_argument("--min-download", "-d", required=True, help="Minimum expected download speed")
    arg_parser.add_argument("--service-provider", "-s", required=True, help="Internet provider's Twitter account")
    arg_parser.add_argument("--invisible", "-i", action="store_true", help="Run invisibly (headless Chrome driver)")

    return arg_parser.parse_args()


def main():
    logging.getLogger().setLevel(logging.INFO)

    global args
    args = get_args()

    internet_provider = InternetProvider(args.service_provider, float(args.min_download), float(args.min_upload))
    bot = InternetSpeedTwitterBot(internet_provider, args.invisible, InternetSpeedTwitterBot.PageLoadStrategy.EAGER)
    bot.get_internet_speed()

    bot.set_page_load_strategy(InternetSpeedTwitterBot.PageLoadStrategy.NORMAL)
    # bot = InternetSpeedTwitterBot(internet_provider)
    bot.tweet_at_provider(args.account, args.password)

    logging.info("Done")


if __name__ == "__main__":
    main()
