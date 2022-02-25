import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Conor Schreiner'
email['to'] = 'conradschrei@gmail.com'
email['subject'] = 'Shhh Im coding lol'

email.set_content(html.substitute({'name' : 'Conrad'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('conorschrei@gmail.com', '!Novigrad_9547!')
    smtp.send_message(email)
    print('all good sir!')