import discord

client=discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as '+str(client.user))

@client.event
async def on_message(message):
     # username=str(message.author).split('#')[0]
    # channel=str(message.channel.name)
    # user_message=str(message.content)
    # print(f'{username}:{user_message} ({channel})')
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello i am python bot')


client.run('put-token-from-env')