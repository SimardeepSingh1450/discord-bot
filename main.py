import os
import discord
from better_profanity import profanity
from dotenv import load_dotenv
#load_dotenv from dotenv
load_dotenv()

#profanity curse words from file
profanity.load_censor_words_from_file("./profanity.txt")

DISCORD_BOT_TOKEN=os.getenv('DISCORD_BOT_TOKEN')

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
    #profanity message check and removing the message
    if profanity.contains_profanity(message.content):
        await message.delete()
        await message.channel.send(f'You cannot use that word here @{message.author}')


client.run(DISCORD_BOT_TOKEN)