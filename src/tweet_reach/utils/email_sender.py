import smtplib
from datetime import datetime

def send_email(subject, message, sender, recipient, password):
    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, text)
    server.quit()
    print(f"Email sent at {datetime.now()}")
