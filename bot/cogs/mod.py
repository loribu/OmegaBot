""" MODERATION COMMANDS """
import discord
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Omega has connected to Discord!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(client):
    client.add_cog(Mod(client))
