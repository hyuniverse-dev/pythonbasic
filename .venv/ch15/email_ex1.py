'''
파일명: email_ex1.py
위치: .venv/ch15/
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

### 이메일 발송하기

###     이메일 발신 정보
sender = "ggolre90@gmail.com"
password = "hqat licc bufq uzjo"
receiver = "hyuniverse.dev@gmail.com"

###     이메일 내용 구성
subject = "[파이썬] 이메일 발송 테스트"
body = "파이썬 이메일 발송 연습 중입니다 :)"

###     이메일 구성
message = MIMEMultipart()
message['Form'] = sender
message['To'] = receiver
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

###     이메일 발송
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    print("이메일 발송되었습니다.")



