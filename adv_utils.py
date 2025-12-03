import asyncio
import discord
from discord.ext import commands


class adv_utils(commands.Cog):

    def __init__(self, client):
        self.client=client



#RoleMaker
    @commands.command(aliases=['cr'])
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, *, name = None):

        if name == None:
            await ctx.send("Atleast give me a role name smh..-")
            return
        guild=ctx.guild
        await guild.create_role(name=name, colour=discord.Colour(0xffffff))
        await ctx.send(f"Done! I've made a new invention named {name}!")

#RoleDestroyer
    @commands.command(aliases=["dr"], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def delrole(self, ctx, *, role_name = None):

        if role_name == None:
            await ctx.send("Yes but- which role do I need to obliterate..-")
            return
        role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
        await role_object.delete()
        await ctx.send(f'Successfully annihilated {role_name}!')

#RoleAdder
    @commands.command(aliases=['gr'], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def gibrole(self, ctx, user: discord.Member = None, *, role: discord.Role = None):

        if user == None:
            await ctx.send("Woah, atleast tell me a person's name to gib a role to")
            return
        if role == None:
            await ctx.send("Tell me a role name to gib-")
            return
        await user.add_roles(role)
        await ctx.send(f"Given the role {role.name} to {user.name} :eyes:")
        

#RoleRemover
    @commands.command(aliases=['rr'], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, user: discord.Member = None, role: discord.Role = None):

        if user == None:
            await ctx.send("Whom do you want me to snatch a role from?")
            return
        if role == None:
            await ctx.send(f"Ok.. you want me to take a role away from {user.name} but like.. which role tho..")
            return
        await user.remove_roles(role)
        await ctx.send(f"Bullied {user.name} and took there {role.name} role away")

#Change Nick
    @commands.command(aliases=['sn'], pass_context=True)
    @commands.has_permissions(manage_nicknames=True)
    async def setnick(self, ctx, member: discord.Member, *, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention}')

#Nuke Channel
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            await ctx.send("You did not mention a channel!")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            await new_channel.send("Successfully Hiroshima Nagasaki'd this channel! ")
            await new_channel.send("https://c.tenor.com/Rqe9gYz_WPcAAAAC/explosion-boom.gif")
            await ctx.send("Bombed the Channel sucessfully! ")

        else:
            await ctx.send(f"No channel named {channel.name} was found!")

#RoleEveryone
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def roleall(self, ctx, role: discord.Role = None):
        if role == None:
            await ctx.send("Tell me a role name to gib-")
            return
        await ctx.send("This might take an eternity.. Please hang on")
        for m in ctx.guild.members:
            await m.add_roles(role)
            await asyncio.sleep(2)
        await ctx.send("Finished adding the role :D")
        

    
    
async def setup(client):
    await client.add_cog(adv_utils(client))