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

'''
For each event in the database of events, 
create a voice channel with the name of the event
'''
@client.command()
async def create(ctx):
    #This takes in a list of events
    events = ['Test Event']
    #Get our server id
    guild = client.get_guild(832358521378308158)
    #For each event create a category and then setup a voice channel
    category = await guild.create_category(f"Hive Spots", overwrites=None, reason=None)
    for event in events:
        # try:
            await create_voice_channel(ctx,guild, event, category)
async def create_voice_channel(ctx,guild, event, category):
    overwrites = {
    guild.default_role: discord.PermissionOverwrite(connect=False),
    guild.get_role(guild.roles[1].id): discord.PermissionOverwrite(connect = True),
#     guild.owner: discord.PermissionOverwrite(connect=True)
}
    print(guild.roles)

    # channel = await guild.create_text_channel('secret', overwrites=overwrites)

    await ctx.send(f"Setting up {event}!")
    channel = await guild.create_voice_channel(f"{event}", overwrites=overwrites, category=category, reason=None)
    await ctx.send("Setup finished!")

'''
1. Check if role name already exists
1.b. if not create it
2. Add user to role.
'''

'''
In the event on join, 
validate that the user has rsvp'd to that 
event by checking their user id to the user id in teh database.
'''

# @client.command()
# async def ping(ctx):
#     await ctx.send('Pong!')

# @client.command()
# async def echo(ctx,*args):
#     output = ''
#     for word in args:
#         output += word
#         output += ' '
#     await ctx.send(output)
client.run(TOKEN)