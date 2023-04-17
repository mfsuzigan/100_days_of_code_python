import datetime
import random
import smtplib
from mail_utils import get_args

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


if __name__ == "__main__":
    main()
