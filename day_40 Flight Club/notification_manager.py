import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

# Load env variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))


class NotificationManager:

    def __init__(self):
        # twilio
        self.client = Client(os.getenv('TWILIO_account_sid'), os.getenv("TWILIO_auth_token"))
        self._sender_phone_number = os.getenv("SENDER_PHONE_NUMBER")
        self._receiver_phone_number = os.getenv("RECEIVER_PHONE_NUMBER")

        # smtp
        self._email_sender_user = os.getenv("EMAIL_SENDER_USERNAME")
        self._email_sender_pass = os.getenv("EMAIL_SENDER_PASSWORD")
        self.connection = smtplib.SMTP("smtp.gmail.com")

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=self._sender_phone_number,
            body=message_body,
            to=self._receiver_phone_number
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        for email in email_list:
            # send email
            with self.connection:
                self.connection.starttls()
                self.connection.login(user=self._email_sender_user, password=self._email_sender_pass)
                self.connection.sendmail(
                    from_addr=self._email_sender_user,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
