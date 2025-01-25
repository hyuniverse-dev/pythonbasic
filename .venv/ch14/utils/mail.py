import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

'''
파일명: mail.py
위치: ch14/utils/
'''


def send_mail(receiver: str, subject: str, body: str):
    sender = "hyuniverse.dev@gmail.com"
    password = "ibab cgov oojt ymhy"

    message = MIMEMultipart()
    message['Form'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            print("이메일 발송되었습니다.")
    except Exception as e:
        print(f"이메일을 발송하는 중에 오류가 발생했습니다: {e}")
