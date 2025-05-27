import smtplib
import os
import ssl
from email.message import EmailMessage
from datetime import date

def send_email_report(attachments, sender_email, recipient_email, password):
    current_date = date.today()
    subject = f"{current_date} – High Risk Customer Report"
    body = (
        "Attached is a list of districts at high risk of termination. "
    )
  
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.set_content(body)

    for path in attachments:
        with open(path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(path)
            subtype = 'html' if file_name.endswith('.html') else 'octet-stream'
            msg.add_attachment(file_data, maintype='application', subtype=subtype, filename=file_name)
          
    context = ssl.create_default_context()
  
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
