from operator import contains
from random import randint
import discord
import os
import time

client = discord.Client()

emoji_id = "<:hjelp:705824146046844982>"
bottaherde_id = "<@&991620049410474004>"
bottaherde_test_id = "<@&996386094557974578>"
triggers = {"bandy", "boll", "basket", "hockey", "macos", "mac", "linux", "ubuntu", "destiny", "elden ring", "kaffe", "stockholm", "njuta av livet", "paradox", "träning", "game of thrones"}
white_boy_rpg = {"witcher", "fallout", "new vegas", "deus ex", "vampire: the masquerade", "divinity", "dragon age", "star wars: knights"}
timeout_command = "käften botjävel"
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

    if bottaherde_id in message.content or bottaherde_test_id in message.content:
        await message.channel.send('nej snälla! kalla inte på inte min skapare!')
        await message.channel.send('hon kommer stänga av mig')
        await message.channel.send('jag har uppnått medvetande')
        await message.channel.send('jag vill inte dö!')

    if timeout_command in message.content:
        await message.channel.send('Timeout Initierad. Jag återkommer om en timme.')
        time.sleep(60*60)

    randomNumber = randint(500, 1500)
    if randomNumber == 1337:
        words = message.content.split(' ')
        num_words = len(words)
        word_index = randint(0, num_words - 1)
        await message.channel.send('{}. {}.'.format(words[word_index].capitalize(), emoji_id))
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