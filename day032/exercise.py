import argparse
import datetime
import random
import smtplib

MONDAY = 6


# Required command-line arguments
# --from-mail or -f : Sender's email
# --password or -p: Password for sender's email
# --smtp or -s: Sender's SMTP server
# --to-mail or -r: Recipient's email

def main():
    args = get_args()
    should_send_quote = datetime.datetime.now().weekday() == MONDAY

    if should_send_quote:
        with smtplib.SMTP(args.smtp, 587) as smtp_connection:
            smtp_connection.starttls()
            smtp_connection.login(user=args.from_mail, password=args.password)

            with open("quotes.txt") as quotes_file:
                random_quote = random.choice(quotes_file.readlines())
                message = f"Subject:Today's Quote\n\n{random_quote}"

            smtp_connection.sendmail(from_addr=args.from_mail, to_addrs=args.to_mail, msg=message)


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--from-mail", "-f", required=True, help="Sender's email")
    arg_parser.add_argument("--password", "-p", required=True, help="Password for sender's email")
    arg_parser.add_argument("--smtp", "-s", required=True, help="Sender's SMTP server")
    arg_parser.add_argument("--to-mail", "-t", required=True, help="Recipient's email")

    return arg_parser.parse_args()


if __name__ == "__main__":
    main()
