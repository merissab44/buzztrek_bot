from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = commands.Bot(command_prefix='.')

class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = client

    @commands.Cog.listener()
    @commands.has_permissions(connect=True)
    async def on_member_join(self, member):
        '''
        When a user joins, validate their user id against the one in the database
        '''
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member}!')
client.add_cog(Greeting(client))

client.run(TOKEN)