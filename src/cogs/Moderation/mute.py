import discord
from discord import Option
from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.slash_command(description="Mute a member")
    async def mute(self, ctx, member: Option(discord.Member, 'The member to mute', required=True), reason: Option(str, 'The reason for the mute', required=False)):
        await ctx.defer()
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.add_reactions = False
        overwrite.create_private_threads = False
        overwrite.create_public_threads = False
        overwrite.send_messages_in_threads = False
        # Check if there is a muted role and if not, create one
        if not discord.utils.get(ctx.guild.roles, name="Muted") and not discord.utils.get(ctx.guild.roles, name="muted"):
            muted_role = await ctx.guild.create_role(name="Muted", reason="Muted role not found")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, overwrite=overwrite)
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        else:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
            if mutedRole:
                for channel in ctx.guild.channels:  
                    await channel.set_permissions(mutedRole, overwrite=overwrite)
            else:
                mutedRole = discord.utils.get(ctx.guild.roles, name="muted")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(mutedRole, overwrite=overwrite)

        # Check if the member has the muted role
        if mutedRole in member.roles:
            await ctx.respond(f"{member.mention} is already muted!")
        else:
            # Check if there is a reason
            if reason == None:
                await member.add_roles(mutedRole, reason="No reason provided")
                await ctx.respond(f"{member.mention} has been muted!", ephemeral=True)
            else:
                await member.add_roles(mutedRole, reason=reason)
                await ctx.respond(f"{member.mention} has been muted for {reason}!", ephemeral=True)

def setup(client):
    client.add_cog(Mute(client))