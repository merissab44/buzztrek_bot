import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is now ready')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print(f'{author}: {content}')
    await client.process_commands(message)

# @client.event
# async def on_message_delete(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     # .send function can be used for both commands and events
#     await channel.send(f'{author}: {content}')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def echo(ctx,*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)
client.run(TOKEN)