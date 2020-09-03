import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from GUI import window, values

def run_code():
    while True:
        event, value = window.read()
        if event == 'SEND':
            print('Sending...')
            verify_email()
        elif event == 'EXIT':
            break
        elif event == 'WIN_CLOSED':
            break

def verify_email():
    email = values[0]
    password = values[1]
    send_to_email = values[2]
    subject = values[3]
    message = values[4]

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print('Email Sent')

run_code()