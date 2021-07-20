import datetime as dt
import pandas
import os
import random
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = ""
MY_PASSWORD = ""

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    letter = random.choice(os.listdir("letter_templates"))
    name = birthdays_dict[today_tuple]['name']
    recipient = birthdays_dict[today_tuple]['email']
    with open(f"letter_templates/{letter}") as file:
        letter_contents = file.read()
        letter_contents = letter_contents.replace(PLACEHOLDER, name)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipient,
            msg=f"Subject:Happy Birthday!\n\n{letter_contents}"
        )


# ------------------ Extra Hard Starting Project --------------- #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

