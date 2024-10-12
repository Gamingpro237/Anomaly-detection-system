import smtplib
from email.mime.text import MIMEText
from config import ALERT_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Real-Time Anomaly Alert'
    msg['From'] = SMTP_USERNAME
    msg['To'] = ALERT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, ALERT_EMAIL, msg.as_string())
            print(f"Alert sent to {ALERT_EMAIL}")
    except Exception as e:
        print(f"Failed to send alert email: {e}")
