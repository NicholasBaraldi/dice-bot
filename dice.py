import discord
import random
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        m = message.content[1]
        if m == 'D':
            dice = int(message.content.split('D')[-1])
            author = message.author.mention
            if dice > 100:
                await message.channel.send(str(author) + " escolha um numero entre 1 e 100")
            else:
                msg = "{} tirou {}".format(author, random.randint(1, dice))
                await message.channel.send(msg)
        elif m.isnumeric():
            m = int(message.content[1])
            i = 0
            dice = int(message.content.split('D')[-1])
            author = message.author.mention
            if dice > 100:
                await message.channel.send(str(author) + " escolha um numero entre 1 e 100")
            else:
                msg = "{} tirou {}".format(author, random.randint(1, dice))
                while i in range(m-1):
                    msg += ", {}".format(random.randint(1, dice))
                    i += 1
                await message.channel.send(msg)

with open(r"token.json", "r") as json_file:
    secret = json.load(json_file)
client.run(secret["token"])
