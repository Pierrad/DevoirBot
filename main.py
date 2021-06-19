import discord
from discord.ext import tasks
import os
import keep_alive
from APIHandler import APIHandler
from utils import extractFromMessage, writeTaskToLogFile, saveIdToFileNotifier,removeIdToFileNotifier

client = discord.Client()

todo = APIHandler(os.environ['TODOIST_API'], "https://api.todoist.com/rest/v1")

channelID = os.environ['channelID']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    send_message.start("Toutes les minutes")
    await client.get_channel(int(channelID)).send("Hola, je suis prêt !")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if not message.content.startswith('!devoirBot'):
        return

    if message.content.startswith('!devoirBot help'):
        help = "Commande actuellement disponible :\n- addTask \"ProjectName\" \"TaskContent\" \"Date\" "
        await message.channel.send(help)

    if message.content.startswith('!devoirBot addTask'):
        (projectID, taskContent, dueDate) = extractFromMessage(message, todo)
        result = todo.createTask(taskContent, projectID, dueDate)

        writeTaskToLogFile(result)

        await message.channel.send("Okay")
    
    if message.content.startswith('!devoirBot addNotifier'):
        id = message.author.id
        res = saveIdToFileNotifier(id)
        if (res):
            await message.channel.send(f"<@{id}> save")
        else:
             await message.channel.send(f"<@{id}> fail")
    
    if message.content.startswith('!devoirBot removeNotifier'):
        id = message.author.id
        res = removeIdToFileNotifier(id)
        if (res):
            await message.channel.send(f"<@{id}> remove")
        else:
             await message.channel.send(f"<@{id}> fail")
    


@tasks.loop(minutes=1)
async def send_message(message):
    await client.get_channel(int(channelID)).send(message)


keep_alive.keepAlive()
client.run(os.environ['TOKEN'])

