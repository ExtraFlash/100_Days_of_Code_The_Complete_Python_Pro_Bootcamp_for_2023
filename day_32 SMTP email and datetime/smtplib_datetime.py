import smtplib

# walla
# username: orshkuri123789
# pass: ororor159

# yahoo
# username: orshkuri123
# pass: tyuiTYUI1459

# gmail
# username: orshkuri632
# pass: ororor159
# pass for Python: tqygafnseqvhjqwg

# my_email = "orshkuri632@gmail.com"
# password = "tqygafnseqvhjqwg"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  # secure connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="orshkuri123789@walla.co.il",
#         msg="Subject: Hello\n\nThis is the body of my email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)