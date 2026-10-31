# Standard Python SMTP library  
import smtplib

# Import the email class needed
from email.message import EmailMessage

# Build Message and body
msg = EmailMessage()
msg.set_content('This is a test')

# Email Headers
msg['Subject'] = 'test Parasend'
msg['From'] = 'parasire.010@gmail.com'
msg['To'] = 'parasire.010@gmail.com'


