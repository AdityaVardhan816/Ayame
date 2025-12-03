from ast import Invert
import asyncio
from multiprocessing.connection import wait
import time
import discord
import random
from discord.ext import commands
from discord import Spotify
from googlesearch import search
import urllib
from bs4 import BeautifulSoup

class Utils(commands.Cog):

    def __init__(self, client):
        self.client=client

#Ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

#User Info
    @commands.command(aliases=['ui', 'user'])
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles[1:25]]
        rls=[role.mention for role in roles]
        f'*Role list:\n* {", ".join((rls)[::-1])}, @everyone',

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.add_field(name="ID:", value=member.id, inline = False)
        custom_status = None
        for activity in member.activities:
            if isinstance(activity, discord.CustomActivity) and activity.name:
                custom_status = activity.name
                break
        if custom_status:
            embed.add_field(name="Custom Status", value=custom_status, inline=False)
        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = True)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = True)
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="Top Role:", value=member.top_role.mention, inline = False)
        user = await ctx.bot.fetch_user(member.id)
        if user.banner:
            embed.set_image(url=user.banner.url)
        await ctx.send(embed=embed)


#Say
    @commands.command()
    async def say(self, ctx, *, message = None):
        if message == None:
            await ctx.send("Do the full command you genius, it's ``,say (message)``")
            return

        await ctx.send(message)

#Latency
    @commands.command()
    async def latency(self, ctx):
        time_1 = time.perf_counter()
        time_2 = time.perf_counter()
        ping = round((time_2-time_1)*1000)

        await ctx.send(f"``Ping = {ping}``")

#Avatar
    @commands.command(name='avatar', aliases=['av'])
    async def avatar(self, ctx, member : discord.Member=None):
        if member == None:
            member = ctx.author

        memberAvatar = member.avatar.url
        avaEmbed = discord.Embed(title = f"{member.name}'s Avatar")
        avaEmbed.set_image(url = memberAvatar)

        await ctx.send(embed=avaEmbed)

#ServerInfo
    @commands.command(aliases=['si', 'server'])
    async def serverinfo(self, ctx):

        embed=discord.Embed(title=f"Server Information for {ctx.message.guild.name}", color=(0xffe0e0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.add_field(name="Owner", value=(ctx.message.guild.owner), inline=False)
        embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
        embed.add_field(name="Server Created at", value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = True)
        embed.add_field(name="You Joined at", value=ctx.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = True)
        embed.add_field(name="Roles", value=(f'{len(ctx.message.guild.roles)}'), inline=False)
        embed.add_field(name="Humans", value=len([m for m in ctx.guild.members if not m.bot]), inline=True)
        embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))), inline=True)
        embed.add_field(name="Total Members", value=len(ctx.guild.members), inline=True)
        embed.add_field(name="Verification Level", value=str(ctx.guild.verification_level), inline=False)
        embed.add_field(name="Text Channels", value=(f'{len(ctx.message.guild.text_channels)}'), inline=True)
        embed.add_field(name="Voice Channels", value=(f'{len(ctx.message.guild.voice_channels)}'), inline=True)
        embed.add_field(name="Categories", value=len(ctx.guild.categories), inline=True)
        if ctx.guild.banner:
            embed.set_image(url=ctx.guild.banner.url)

        await ctx.send(embed=embed)

#Spotify
    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
            pass
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, Spotify):
                    embed = discord.Embed(title = f"{user.name}'s Spotify", description = "Listening to **{}**".format(activity.title), color = user.color)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Artist", value=activity.artist)
                    embed.add_field(name="Album", value=activity.album)
                    embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
                    await ctx.send(embed=embed)
        else:
            await ctx.send("Bro isn't listening to spotify lul")


    
#Google
    @commands.command()
    async def google(self, ctx, *, search_msg = None):
        await ctx.send("Aight hol'up")
        if search_msg == None:
            await ctx.send("Gimme something to lookup and cope harder bozo \n ``,google (Message)`` is how you search")
        else:
            for URL in search(search_msg):
                await ctx.send(URL)
                break


#Calculator
    @commands.command()
    async def calculate(ctx, operation, *nums):
        if operation not in ['+', '-', '*', '/']:
            await ctx.send('Please type a valid operation type.')
        else:
            var = f' {operation} '.join(nums)
            await ctx.send(f'{var} = {eval(var)}')

            
            

async def setup(client):
    await client.add_cog(Utils(client))