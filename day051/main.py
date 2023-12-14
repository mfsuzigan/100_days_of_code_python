import logging

from day051.InternetSpeedTwitterBot import InternetSpeedTwitterBot


def main():
    logging.getLogger().setLevel(logging.INFO)
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()


if __name__ == "__main__":
    main()
