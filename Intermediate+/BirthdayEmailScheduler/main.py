import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "jacquesmassi@gmail.com"
PASSWORD = ""

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthday = data.loc[(data.month == now.month) & (data.day == now.day)]

if birthday.empty:
    print("Empty")
else:
    letter_nr = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_nr}.txt") as letter:
        data = letter.read()
        data = data.replace("[NAME]", birthday.name.item())

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= birthday.email.item(),
                            msg= f"Subject: Birthday\n\n{data}")
