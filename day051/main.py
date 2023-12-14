import logging

from day051.InternetSpeedTwitterBot import InternetSpeedTwitterBot


def main():
    logging.getLogger().setLevel(logging.INFO)

    # bot = InternetSpeedTwitterBot(InternetSpeedTwitterBot.PageLoadStrategy.EAGER)
    # bot.get_internet_speed()

    # bot.set_page_load_strategy(InternetSpeedTwitterBot.PageLoadStrategy.NORMAL)
    bot = InternetSpeedTwitterBot()
    bot.tweet_at_provider()


if __name__ == "__main__":
    main()
