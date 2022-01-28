import smtplib

sender = ""
receiver = ""
password = ""
subject = "Python email test"
body = "Hello! I wrote an email hehe"

message = f"""" From: Lumine {sender}
To: Aether{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in :(")