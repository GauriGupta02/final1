import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is a test email from Python!")
msg['Subject'] = "Test Email"
msg['From'] = "gauriguptagwl@gmail.com"
msg['To'] = "24ad10ga24@mitsgwl.ac.in"

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login("gauriguptagwl@gmail.com", "ahyxdaufjnccgura")  # use the correct app password!
    server.send_message(msg)
    print("✅ Email sent successfully!")
