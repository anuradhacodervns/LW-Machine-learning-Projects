import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_bulk_emails(sender_email, sender_password, subject, message, recipient_list):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"  # Replace with your email provider's SMTP server
    smtp_port = 587  # Port for TLS
    
    # Establish the connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted TLS connection
    server.login(sender_email, sender_password)

    for recipient in recipient_list:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        
        # Add the message body to the email
        msg.attach(MIMEText(message, 'plain'))
        
        # Send the email
        server.sendmail(sender_email, recipient, msg.as_string())

    # Terminate the SMTP session and close the connection
    server.quit()

    print("Emails sent successfully.")

# Example usage
sender_email = "your-email@gmail.com"
sender_password = "your-email-password"
subject = "Your Subject"
message = "This is a bulk email sent using Python."
recipient_list = [
    "recipient1@example.com",
    "recipient2@example.com",
    "recipient3@example.com"
]

send_bulk_emails(sender_email, sender_password, subject, message, recipient_list)
