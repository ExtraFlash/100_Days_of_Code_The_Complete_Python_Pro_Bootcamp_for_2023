##################### Extra Hard Starting Project ######################
import smtplib
from datetime import datetime
import pandas as pd
import random

MY_EMAIL = "orshkuri632@gmail.com"
MY_PASS = "tqygafnseqvhjqwg"

birthdays_df = pd.read_csv("birthdays.csv")
now = datetime.now()
# go over all the birthdays
for index, row in birthdays_df.iterrows():
    # if birthday matches today
    if now.month == row.month and now.day == row.day:
        # pick random letter number
        letter_num = random.randint(1, 3)
        # read letter
        with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
            letter = letter_file.read().replace("[NAME]", row["name"])
        # send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row.email,
                msg=f"Subject: Happy Birthday!\n\n{letter}"
            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




