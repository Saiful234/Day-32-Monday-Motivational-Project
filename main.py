import datetime
import random
import smtplib


my_email = "bandotech46@gmail.com"
my_password = "ildoygqbxpeggivi"

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 6:
with open("quotes.txt") as quote_file:
    all_quote = quote_file.readlines()
    quote = random.choice(all_quote)
    print(quote)

with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday Motivationn\n\n{quote}")

