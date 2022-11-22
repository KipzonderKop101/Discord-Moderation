import discord
from discord import Option
from discord.ext import commands
from utils.warningstore import WarningStore
from utils.modlog import ModLog

class RemoveWarning(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Remove a warning from a member")
    async def removewarning(self, ctx, member: Option(discord.Member, 'The member to remove the warning from', required=True), warning_name: Option(str, 'The warning to remove (by name)', required=False), warning_index: Option(str, 'The warning to remove (by index)', required=False), reason: Option(str, 'Reason for removing this warning', required=False)):
        if reason is None: reason = "No reason provided"

        # Create instance of WarningStore and ModLog
        warning_store = WarningStore()
        log = ModLog()
        
        # Check if there is an entry, and if not, create one
        warning_store.create_entry(member.id)
        
        # Get the warnings for this member
        warnings = warning_store.get_warnings(member.id)
        
        # Check if the member has any warnings, if so, remove the warning
        if len(warnings) > 0:
            if warning_name == None and warning_index == None:
                await ctx.respond('You must specify a warning to remove', ephemeral=True)
            elif warning_name != None and warning_index == None:
                warning_store.remove_warning(member.id, warning_name)
                await ctx.respond(f'Removed warnings "{warning_name}" from {member.mention}')
                await log.log(ctx, 'Removed warning', reason)
            elif warning_index != None and warning_name == None:
                warning_store.remove_warning_by_index(member.id, int(warning_index)) 
                await ctx.respond(f'Removed warning at index {warning_index} from {member.mention}')
                await log.log(ctx, 'Removed warning', reason)
            elif warning_name != None and warning_index != None:
                warning_by_index = warning_store.get_warning_by_index(member.id, int(warning_index))
                if warning_by_index == warning_name:
                    warning_store.remove_warning_by_index(member.id, int(warning_index))
                    await log.log(ctx, 'Removed warning', reason)
                else:
                    await ctx.respond('The warning name and index do not match', ephemeral=True)
        else:
            await ctx.respond('This member has no warnings', ephemeral=True)


def setup(client):
    client.add_cog(RemoveWarning(client))