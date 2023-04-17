import datetime
import os
import random
import smtplib

import pandas
from exercises.mail_utils import get_args


def main():
    birthdays = pandas.read_csv("birthdays.csv")
    today = datetime.datetime.today()
    birthdays_today = birthdays[(birthdays.day == today.day) & (birthdays.month == today.month)]

    letter_templates = os.listdir("letter_templates")
    args = get_args()

    with smtplib.SMTP(args.smtp, 587) as smtp_connection:
        smtp_connection.starttls()
        smtp_connection.login(user=args.from_mail, password=args.password)

        for birthday in birthdays_today.itertuples():
            print(f"Birthday detected: {birthday.name} ({birthday.year}-{birthday.month}-{birthday.day})")

            with open(f"letter_templates/{random.choice(letter_templates)}") as letter_file:
                letter = letter_file.read().replace("[NAME]", birthday.name)
                letter = f"Subject:Happy Birthday {birthday.name}!\n" + letter
                smtp_connection.sendmail(from_addr=args.from_mail, to_addrs=birthday.email, msg=letter)
                print("E-mail sent\n")


if __name__ == "__main__":
    main()
