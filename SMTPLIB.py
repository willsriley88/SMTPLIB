import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, sender_email, sender_password, recipient_email,
                 smtp_server='smtp.example.com', smtp_port=465):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, subject, message):
        # Set up the SMTP server
        smtp_server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)

        # Login to the SMTP server
        smtp_server.login(self.sender_email, self.sender_password)

        # Create a MIMEText object to represent the email
        email_message = MIMEMultipart()
        email_message['From'] = self.sender_email
        email_message['To'] = self.recipient_email
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp_server.send_message(email_message)

        # Close the connection to the SMTP server
        smtp_server.quit()

# Example usage
sender_email = 'your_email@example.com'
sender_password = 'your_email_password'
recipient_email = 'recipient@example.com'
subject = 'Notification'
message = 'This is a notification email sent from a Python script.'
