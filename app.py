import discord, asyncio, os, smtplib
from datetime import date

client = discord.Client()

token = str(os.environ["DISCORD_TOKEN"])

def get_today():
    today = date.today().strftime("%Y-%m-%d") 
    return str(today)

def get_yesterday(): 
    yesterday = date.today() - timedelta(1)
    return str(yesterday.strftime('%Y-%m-%d'))

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