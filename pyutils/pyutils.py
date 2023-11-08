import logging

import vonage
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from getch import getch

VONAGE_SMS_ERROR_STATUS = "-1"


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


def send_twilio_sms(message, configs):
    required_configs = {"TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "TWILIO_SENDER_PHONE", "TWILIO_RECIPIENT_PHONE"}

    if required_configs.issubset(configs):
        client = Client(configs["TWILIO_ACCOUNT_SID"], configs["TWILIO_AUTH_TOKEN"])

        try:
            message = client.messages.create(
                body=message,
                from_=configs["TWILIO_SENDER_PHONE"],
                to=configs["TWILIO_RECIPIENT_PHONE"]
            )

            return message.sid

        except TwilioRestException:
            logging.exception("Error sending SMS")

    else:
        logging.warning(f"Unable to send SMS. One or more configs not present: {required_configs}")


def send_vonage_sms(message_text, message_from, configs):
    required_configs = {"VONAGE_API_KEY", "VONAGE_API_SECRET", "VONAGE_RECIPIENT_PHONE"}

    if required_configs.issubset(configs):
        client = vonage.Client(key=configs["VONAGE_API_KEY"], secret=configs["VONAGE_API_SECRET"])
        sms = vonage.Sms(client)

        response = sms.send_message(
            {
                "from": message_from,
                "to": configs["VONAGE_RECIPIENT_PHONE"],
                "text": message_text,
            }
        )

        if response["messages"][0]["status"] == "0":
            return response["messages"][0]["message-id"]
        else:
            logging.exception(f"Unable to send SMS. Message failed with error: {response['messages'][0]['error-text']}")
            return VONAGE_SMS_ERROR_STATUS

    else:
        logging.warning(f"Unable to send SMS. One or more configs not present: {required_configs}")
