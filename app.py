import discord, asyncio, os, smtplib
from datetime import date
from email.mime.text import MIMEText

client = discord.Client()

token = str(os.environ["DISCORD_TOKEN"])

def get_today():
    today = date.today().strftime("%Y-%m-%d") 
    return str(today)

def get_yesterday(): 
    yesterday = date.today() - timedelta(1)
    return str(yesterday.strftime('%Y-%m-%d'))

def send_report():
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
    s.sendmail(str(os.environ["EMAIL"]), str("REPORT_EMAIL"), msg.as_string())
    s.quit()


async def bt(games):
    await client.wait_until_ready()
    while not client.is_closed():
        for g in games:
            await client.change_presence(status=discord.Status.online, activity=discord.Game(g))

            await asyncio.sleep(5)


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

    ch = 0
    for g in client.guilds:
        ch += 1
    await client.change_presence(status=discord.Status.online, activity=await bt(['AI에게 데이터를 기부 ', f'{ch}개의 서버장님들에게 감사', ]))

@client.event
async def on_message(message):
    with open("./data/" + get_today() + ".txt", "at", encoding="UTF-8") as f:
        f.writelines(message.content + "\n")
        print(message.content)

client.run(token)