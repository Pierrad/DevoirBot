import discord
import os
from keep_alive import keep_alive
from APIHandler import APIHandler

client = discord.Client()

todo = APIHandler(os.environ['TODOIST_API'], "https://api.todoist.com/rest/v1")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print(todo.getAllTasks())
        await message.channel.send('Hello!')


keep_alive()
client.run(os.environ['TOKEN'])

