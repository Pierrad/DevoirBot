import discord
import os
from keep_alive import keep_alive
from APIHandler import APIHandler
from utils import extractFromMessage, writeTaskToLogFile

client = discord.Client()

todo = APIHandler(os.environ['TODOIST_API'], "https://api.todoist.com/rest/v1")
            
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.get_channel(851848071544569859).send("Hola, je suis prêt !")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if not message.content.startswith('!todoBot'):
        return

    if message.content.startswith('!todoBot help'):
        help = "Commande actuellement disponible :\n- addTask \"ProjectName\" \"TaskContent\" \"Date\" "
        await message.channel.send(help)

    if message.content.startswith('!todoBot addTask'):
        (projectID, taskContent, dueDate) = extractFromMessage(message, todo)
        result = todo.createTask(taskContent, projectID, dueDate)

        writeTaskToLogFile(result)

        await message.channel.send("Okay")


keep_alive()
client.run(os.environ['TOKEN'])

