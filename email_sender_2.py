import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  #os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = #name here''
email['to'] = #mail here''
email['subject'] = #subjet here''

#put your name under 'name' value 
email.set_content(html.substitute({'name':'name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your mail@gmail.com', 'your password')
    smtp.send_message(email)
    print('all good!')