import discord
from discord.ext import commands
from utils.confighelper import ConfigHelper

class Config(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description='View the current config options')
    async def config(self, ctx):
        config = ConfigHelper()
        mod_role = discord.utils.get(ctx.guild.roles, id=config.get_mod_role_id())
        mute_role = discord.utils.get(ctx.guild.roles, id=config.get_mute_role_id())
        admin_role = discord.utils.get(ctx.guild.roles, id=config.get_admin_role_id())
        modlog_channel = discord.utils.get(ctx.guild.channels, id=config.get_modlog_channel_id())
        # Get all the whitelisted roles 
        whitelisted_roles = []
        for role_id in config.get_whitelisted_roles():
            whitelisted_roles.append(discord.utils.get(ctx.guild.roles, id=role_id))
        

        embed = discord.Embed(title='Config', description='Current config options')
        embed.add_field(name='Modlog Channel', value=modlog_channel.mention if modlog_channel else 'None', inline=False)
        embed.add_field(name='Mod Role', value=mod_role.mention if mod_role else 'None', inline=False)
        embed.add_field(name='Mute Role', value=mute_role.mention if mute_role else 'None', inline=False)
        embed.add_field(name='Admin Role', value=admin_role.mention if admin_role else 'None', inline=False)
        embed.add_field(name='Whitelisted Roles', value=', '.join([role.mention for role in whitelisted_roles]) if whitelisted_roles else 'None', inline=False)
        await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(Config(client))
