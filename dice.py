import discord
import random
import json
import re

client = discord.Client()

dice_regex = re.compile(r'!(\d+)?D(\d+)')
dice_num_regex = re.compile(r'!(\d+)D')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    author = message.author.mention

    if dice_regex.search(message.content):
        match = dice_num_regex.search(message.content)
        if match == None:
            m = 1
        else:
            m_start = match.start()
            m_end = match.end()
            m = int(message.content[m_start+1: m_end-1])

        dice = int(message.content.split('D')[-1])

        if m > 100 or m == 0:
            await message.channel.send(str(author) + " escolha um numero de dados entre 1 e 100")
        elif dice > 100:
            await message.channel.send(str(author) + " escolha um numero de faces entre 1 e 100")
        else:
            msg = "{} tirou {}".format(author, random.randint(1, dice))
            for i in range(1, m):
                msg += ", {}".format(random.randint(1, dice))
            await message.channel.send(msg)

with open(r"token.json", "r") as json_file:
    secret = json.load(json_file)
client.run(secret["token"])
