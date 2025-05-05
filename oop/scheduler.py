from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import smtplib
from email.mime.text import MIMEText


def send_email(to_email, subject, message):
    sender_email = "gauriguptagwl@gmail.com"
    sender_password = "ahyxdaufjnccgura"  

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"📨 Email sent to {to_email}")
    except Exception as e:
        print("❌ Email failed:", e)


def check_reminders(reminder_manager):
    now = datetime.now().strftime("%H:%M")
    print("🔍 Checking reminders at", now)

    reminders = reminder_manager.get_all_reminders()
    for name, time, email in reminders:
        if time.strip()[:5] == now:
            print(f"⏰ Time matched! Sending email for {name}")
            send_email(
                email, "💊 Medicine Reminder", f"Time to take your medicine: {name}"
            )


def start_scheduler(reminder_manager):
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: check_reminders(reminder_manager), "interval", seconds=30)
    scheduler.start()
    print("✅ Scheduler started.")
