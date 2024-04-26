import smtplib
import datetime as dt
import random

today = 3
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == today:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()  # includes \n
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="orshkuri632@gmail.com", password="tqygafnseqvhjqwg")
        connection.sendmail(
            from_addr="orshkuri632@gmail.com",
            to_addrs="orshkuri123789@walla.co.il",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )
