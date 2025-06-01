import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def notify_mail(text):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    password = os.getenv('EMAIL_PASSWORD')
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    if not password or not sender_email or not receiver_email:
        print("Environment variables for email are not set properly.")
        return

    subject = "YOU GOT A MAIL THROUGH YOUR WEBSITE!!"
    body = text

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] =receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

        print("Email sent successfully")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()