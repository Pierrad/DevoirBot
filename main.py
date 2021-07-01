import discord
from discord.ext import tasks
import os
import backend.keep_alive
from backend.APIHandler import APIHandler
from backend.utils import extractFromMessage, writeTaskToLogFile, saveIdToFileNotifier,removeIdToFileNotifier, getNotifier, checkForNextTask, formatTasksOutput
from dotenv import load_dotenv


load_dotenv()

client = discord.Client()

todo = APIHandler(os.environ['TODOIST_API'], "https://api.todoist.com/rest/v1")

channelID = os.environ['channelID']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    getTasks.start()
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

    if message.content.startswith('!devoirBot getNotifier'):
        res = getNotifier()
        if (res):
            await message.channel.send(res)
        else:
            await message.channel.send("fail")

    if message.content.startswith('!devoirBot getTasks'):
        res = todo.getAllTasks()
        for task in res:
            print(task)
            print('\n--------------------------\n')

    if message.content.startswith('!devoirBot site'):
        await message.channel.send("https://devoir-bot.herokuapp.com/")
    

@tasks.loop(hours=24)
async def getTasks():
    res = checkForNextTask()
    res2 = todo.getTasksByIds(res)
    res3 = formatTasksOutput(res2)
    res4 = getNotifier()
    res5 = res4 + '\n' + res3
    if len(res3) != 0:
        await client.get_channel(int(channelID)).send(res5)


backend.keep_alive.keepAlive()
client.run(os.environ['TOKEN'])

