import discord
import os

client = discord.Client()

emoji_id = "<:hjelp:705824146046844982>" 
triggers = {"bandy", "boll", "basket", "hockey", "mac", "macos", "linux", "ubuntu", "destiny", "elden ring", "kaffe", "stockholm", "njuta av livet", "paradox"}
white_boy_rpg = {"witcher", "fallout","deus ex", "vampire: the masquerade", "divinity", "dragon age", "star wars: knights"}
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
            await message.channel.send('{}. {}.'.format(response.capitalize(), emoji_id))

    for trigger in white_boy_rpg:
        if trigger in message.content.lower():
            await message.channel.send('{}. {}.'.format("White boy RPG", emoji_id))


client.run(os.environ['secret'])