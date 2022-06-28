import discord
import os

client = discord.Client()

emoji_id = "<:hjelp:705824146046844982>" 
triggers = {"bandy", "boll", "basket", "hockey", "mac", "macos", "linux", "ubuntu", "destiny", "elden ring", "kaffe", "stockholm", "njuta av livet"}
response = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for trigger in triggers:
        if trigger in message.content.lower():
            if trigger == "boll":
                response = "bollsport"
            else:
                response = trigger
            await message.channel.send('{}. {}.'.format(response, emoji_id))



client.run(os.environ['secret'])