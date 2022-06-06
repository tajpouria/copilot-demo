# Receive email and send it to the specified email address


def send_email(email_address, email_subject, email_body):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    # Create the email message
    msg = MIMEMultipart()

    # Add the subject
    msg["Subject"] = email_subject

    # Add the body
    msg.attach(MIMEText(email_body, "plain"))

    # Add the attachment
    filename = "email_sender.py"

    # Open the file
    attachment = open(filename, "rb")

    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")

    # To change the payload into encoded form
    part.set_payload((attachment).read())
