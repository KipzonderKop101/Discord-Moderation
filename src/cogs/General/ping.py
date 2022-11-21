import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Pong!")
    async def ping(self, ctx):
        # Respond with bot's latency
        await ctx.respond(f'Pong! `{round(self.bot.latency * 1000)}ms`')

def setup(bot):
    bot.add_cog(Ping(bot))