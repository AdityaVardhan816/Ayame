import random
import aiohttp
import discord
from discord.ext import commands
import praw

class Meme(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                reddit = praw.Reddit(client_id='Sgifl9fzxAKBAtNTScu8Jw',
                         client_secret='sLlqcsDuZzqvACS5j5UX6JrLEyT7Gg',
                         user_agent='python')
                embed = discord.Embed(title="Teh Meme", colour=0x0b0b0b, timestamp=ctx.message.created_at)
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.send(embed=embed)



async def setup(client):
    await client.add_cog(Meme(client))