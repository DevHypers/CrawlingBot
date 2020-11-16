import os, smtplib
from datetime import date
from email.mime.text import MIMEText

def get_today():
    today = date.today().strftime("%Y-%m-%d") 
    return str(today)

def get_yesterday(): 
    yesterday = date.today() - timedelta(1)
    return str(yesterday.strftime('%Y-%m-%d'))

# 세션생성, 로그인
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(str(os.environ["EMAIL"]), str(os.environ["PASS"]))

# 제목, 본문 작성
msg = MIMEMultipart()
msg['Subject'] = get_yesterday() + " Report"

# 파일첨부 (파일 미첨부시 생략가능)
attachment = open(get_yesterday() + ".txt", 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(part)

# 메일 전송
s.sendmail(str(os.environ["EMAIL"]), str(os.environ["REPORT_EMAIL"]), msg.as_string())
s.quit()
