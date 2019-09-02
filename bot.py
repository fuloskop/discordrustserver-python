import discord
import asyncio
import requests

# Config:

token = ''   #Discord token
apiSite = 1
apiUrl = ''   #https://api.rust-servers.info/info/(id)


client = discord.Client()

# Print the starting text
print('---------------')
print('Discord Bot updates activity status every 2 min')
print('---------------')
print('Starting Bot...')


@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Game(name="Offline or Opening"))
    print("Logged in as " + client.user.name)
    print('---------------')
    await asyncio.sleep(10)

async def updateservers():
    await client.wait_until_ready()
    count = 0
    while (1):
        resp = requests.get(url=apiUrl)
        data = resp.json()
        online = data['online_state']
        if online == '0':
            await client.change_presence(activity=discord.Game(name="Offline or Opening"))
            print('Server offline this update')
        else:
            players = data['players_cur']
            maxplayers = data['players_max']
            ip = data['ip']
            port = data['port']
            if count == 0:
                await client.change_presence(activity=discord.Game(name=players + " / " + maxplayers))
                count = 1
                print('Server online this update with player')
                await asyncio.sleep(100)
            else:
                await client.change_presence(activity=discord.Game(name=ip + ":" + port))
                count = 0
                print('Server online this update with ip')
                await asyncio.sleep(10)
            print('---------------')
        await asyncio.sleep(10)


# Start bot
client.loop.create_task(updateservers())
client.run(token)
