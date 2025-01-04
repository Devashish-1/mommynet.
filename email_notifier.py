import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_alert_email(anomaly_description):
    sender_email = "zinder0001@gmail.com"
    sender_password = "devaw3w3"
    receiver_email = "devss94645@gmail.com"

    subject = "Anomaly Detection Alert"
    body = f"An anomaly has been detected:\n\n{anomaly_description}"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send alert email: {e}")
