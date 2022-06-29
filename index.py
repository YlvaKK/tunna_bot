from random import randint
import discord
import os

client = discord.Client()

emoji_id = "<:hjelp:705824146046844982>" 
triggers = {"bandy", "boll", "basket", "hockey", "macos", "mac", "linux", "ubuntu", "destiny", "elden ring", "kaffe", "stockholm", "njuta av livet", "paradox", "träning", "game of thrones"}
white_boy_rpg = {"witcher", "fallout", "new vegas", "deus ex", "vampire: the masquerade", "divinity", "dragon age", "star wars: knights"}
response = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 545178588996173826:
        return

    if message.content

    randomNumber = randint(500, 1500)
    if randomNumber == 1337:
        words = message.content.split(' ')
        num_words = len(words)
        word_index = randint(0, num_words - 1)
        await message.channel.send('{}. {}.'.format(words[word_index], emoji_id))
    else:
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
                break

client.run(os.environ['secret'])