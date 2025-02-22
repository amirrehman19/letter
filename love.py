import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail credentials
EMAIL_ADDRESS = "amirrehman16022022@gmail.com"  # Replace with your Gmail
EMAIL_PASSWORD = "tvim qvva qbys fbxy"  # Replace with your App Password

# Email details
TO_EMAIL = "soniaazhar02@gmail.com"  # Replace with recipient's email
SUBJECT = "letter "
BODY = ("Te quiero / Te amo\n"
        " Je t’aime\n"
        "Ti amo\n")


# Function to send email
def send_email():
    try:
        # Set up the email server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Create email
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = TO_EMAIL
        msg["Subject"] = SUBJECT
        msg.attach(MIMEText(BODY, "plain"))

        # Send email
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
        server.quit()
        print(f"Email sent to {TO_EMAIL}")

    except Exception as e:
        print(f"Error: {e}")


# Send email every minute
while True:
    send_email()
    time.sleep(1800)  # Wait 60 seconds before sending the next email
