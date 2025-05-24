import smtplib
from dotenv import load_dotenv
load_dotenv()
email = input("SENDER EMAIL: ")
rec_email = input("RECEIVER EMAIL: ")
subject = input("SUBJECT: ")
message = input("MESSAGE: ")
text = f"Subject: {subject}\n\n{message}"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, "fiiyqxvwrfqlmzsu")
server.sendmail(email, rec_email, text)
print("Email has been sent to: " + rec_email)