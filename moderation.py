import asyncio
import datetime
import discord
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client=client

#KickCmd
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} was yeeted out of the server.. Rip bozo')
      

#PurgeCmd
    @commands.command(name='poof', aliases=['purge', 'woosh'])
    @commands.has_permissions(manage_messages=True)
    async def poof(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        message = await ctx.send(f'{amount} messages have been poofed!')
        await asyncio.sleep(2)
        if message.author.id == 915206129229914142:
            await message.delete()


#BanCmd
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} was bunned out of the server.. Imagine getting disowned')
       
#UnbanCmd
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}, imagine being banned, L bozo')        

#MuteCmd
    @commands.command(aliases=['stfu'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await ctx.send(f"{member.mention} has been silenced, let em' witness the abyss ")
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" Get muted bish, reason provided **{reason}**, just get good already, server you got muted in **{guild.name}**")
        
#UnmuteCmd
    @commands.command(aliases=['unstfu'])
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f" You have been unmuted from **{ctx.guild.name}** @-@")
        await ctx.send(f"{member.mention} has been released from the abyss")
        
#Lock
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
        await ctx.send(ctx.channel.mention + " is now in lockdown")

#Unlock
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + " has been unlocked")

async def setup(client):
    await client.add_cog(Mod(client))