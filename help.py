import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(description = "Below is the list of all my commands. If you want more info on a specific command, do ``,help (command)``", color=(0xfdbb64))
        embed.set_author(name="Commands List!", icon_url=ctx.author.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.set_thumbnail(url=ctx.guild.icon.url)

        embed.add_field(name="<:rightarrow:1256528979871924265>  Fun", value="``rate``, ``8ball``, ``imagine``, ``coinflip``, ``ship``, ``intellect``, ``hack``, ``roll``, ``meme``, ``mindread``", inline=False)
        embed.add_field(name="<:rightarrow:1256528979871924265>  Utility", value="``ping``, ``say``, ``latency``, ``avatar``, ``userinfo``, ``serverinfo``, ``spotify``", inline = True)
        embed.add_field(name="<:rightarrow:1256528979871924265>  Actions", value="``hug``, ``boop``, ``kill``, ``cuddle``, ``pat``, ``kiss``, ``bonk``, ``nom`` ,``cry``, ``slap``, ``wave``", inline = False)
        embed.add_field(name="<:rightarrow:1256528979871924265>  Economy", value="``start``, ``daily``, ``profile``, ``view``, ``info``, ``inventory``, ``equip``, ``unequip`` ,``armup``, ``unarm``", inline = False)
        embed.add_field(name="<:rightarrow:1256528979871924265>  Guilds", value="``createguild``, ``joinguild``, ``guildinfo``, ``leaveguild``, ``guildpromote``, ``guilddemote``, ``guildkick``", inline = False)
        embed.add_field(name="<:rightarrow:1256528979871924265>  Battles", value="``duelnpc``, ``duelboss``, ``duelpractice``, ``dueluser``", inline = False)
        embed.add_field(name="<:rightarrow:1256528979871924265>  Extras", value="``lore``, ``study``, ``learn``, ``discard``, ``shop``, ``blacksmith``, ``dwarvenfield``, ``armory``", inline = False)
        embed.add_field(name="<:rightarrow:1256528979871924265>  Information", value="``wiki``, ``google``")

        await ctx.send (embed=embed)

    @commands.group(invoke_without_command=True, alias=["help staff, Help staff"])
    @commands.has_permissions(manage_messages=True)
    async def help_staff(self, ctx):
        embed = discord.Embed(description = "Staff commands, don't abooz or I will bean you <a:a_love:1085944146017136721> ", color=(0xffdede))
        embed.set_author(name="Commands List!")
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.set_thumbnail(url=ctx.guild.icon.url)

        embed.add_field(name="<:rightarrow:1256528979871924265> Moderation", value="``kick``, ``poof``, ``ban``, ``unban``, ``mute``, ``unmute``, ``lock``, ``unlock``", inline = True)
        embed.add_field(name="<:rightarrow:1256528979871924265> Advanced Utility", value="``createrole``, ``delrole``, ``gibrole``, ``removerole``, ``miniemb``, ``setnick``, ``nuke``, ``roleall``", inline = False)

        await ctx.send(embed=embed)

#Mod Cmds

    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(title="Kick", description = "Basically a kick command, kicks the loser out of the server", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/BUZOVzZoN-gAAAAC/get-up-out-of-my-bed-anime.gif')
        embed.add_field(name="Usage", value=",kick [member] [reason]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have kick members permission")
        await ctx.send(embed=embed)

    @help.command()
    async def poof(self, ctx):
        embed = discord.Embed(title="Poof", description = "Well, just like the name suggests, magically makes the text disappear! (Kinda like a purge)", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/xyuyxkZQtuoAAAAC/disappear-naruto.gif')
        embed.add_field(name="Usage", value=",poof [value]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have manage messages permission")
        await ctx.send(embed=embed)

    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(title="Ban", description = "Ban someone and let them suffer >:)", color = 0xffe8e8)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/q96_L6Ajcu4AAAAC/ban-banned.gif')
        embed.add_field(name="Usage", value=",ban [member] [reason]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have ban members permission")
        await ctx.send(embed=embed)


    @help.command()
    async def unban(self, ctx):
        embed = discord.Embed(title="Unban", description = "Unban someone and let them live peacefully", color = 0x8bfdd5)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/NTIvkl9plf4AAAAC/release-the-spyce-anime.gif')
        embed.add_field(name="Usage", value=",unban [member#tag]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have administrator permission")
        await ctx.send(embed=embed)

    @help.command()
    async def mute(self, ctx):
        embed = discord.Embed(title="Mute", description = "Make someone go to the corner and keep there mouth shut (It's a mute command btw)", color = 0xc1e8fa)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/H_ryBQOeVdQAAAAC/hawks-keigo-takami.gif')
        embed.add_field(name="Usage", value=",mute [member]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have manage messages permission")
        await ctx.send(embed=embed)

    @help.command()
    async def unmute(self, ctx):
        embed = discord.Embed(title="Unmute", description = "Release a person you shutted but don't hesitate to send them back to the corner again (It's an unmute command if you haven't realized yet dummy)", color = 0xd8cdc2)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/W9kzAnY4pQoAAAAd/ram-anime.gif')
        embed.add_field(name="Usage", value=",unmute [member]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have manage messages permission")
        await ctx.send(embed=embed)

    @help.command()
    async def lock(self, ctx):
        embed = discord.Embed(title="Lock", description = "Lock a channel down", color = 0xffffe4)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://media.tenor.com/-PLvb2A9dn8AAAAC/love-live-nico.gif')
        embed.add_field(name="Usage", value=",lock [channel]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have manage channel permission")
        await ctx.send(embed=embed)

    @help.command()
    async def unlock(self, ctx):
        embed = discord.Embed(title="Unlock", description = "Unlocks a channel", color = 0x8b0000)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://media.tenor.com/_QPAGlZr3Z4AAAAC/spirited-away-anime.gif')
        embed.add_field(name="Usage", value=",unlock [channel]", inline=False)
        embed.add_field(name="Permissions Required", value="Must have manage channel permission")
        await ctx.send(embed=embed)
        


#Fun Cmds

    @help.command()
    async def rate(self, ctx):
        embed = discord.Embed(title="Rate", description = "Rate someone out of 10 and try not to die if a low roll happens", color = 0xfacd7f)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/2M60gk22-B4AAAAC/anime-noob.gif')
        embed.add_field(name="Usage", value=",rate [member]", inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        embed = discord.Embed(title="8Ball", description = "Let the bot decide what is the best for you (Totally real 100%)", color = 0xfd8fba)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://c.tenor.com/t80Qwz2QouMAAAAC/yuru-yuri-ayano-sugiura.gif')
        embed.add_field(name="Usage", value=",8ball [question]", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def imagine(self, ctx):
        embed = discord.Embed(title="Imagine", description = "Imagine imagining imagination", color = 0xfacd7f)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://c.tenor.com/uwDvjZmPbSAAAAAd/snafu-iroha.gif")
        embed.add_field(name="Usage", value=",imagine [message]", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def coinflip(self, ctx):
        embed = discord.Embed(title="Coinflip", description = "So.. Heads you're mine, tails I'm yours.. 🤝", color = 0xa20000)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://c.tenor.com/VbOlfmK_Nu8AAAAC/nogamenolife-sora.gif")
        embed.add_field(name="Usage", value=",coinflip", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def wanted(self, ctx):
        embed = discord.Embed(title="Wanted", description = "I see a bounty on your head", color = 0xffffff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://c.tenor.com/CSrI-DV3CXUAAAAd/cowboy-bebop-andy.gif")
        embed.add_field(name="Usage", value=",wanted [user]", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def ship(self, ctx):
        embed = discord.Embed(title="Ship", description = "Ahem, lets see how well you go along with someone", color = 0xfff8d1)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://media.tenor.com/PGXshKPAUh4AAAAC/my-dress-up-darling-anime-love.gif")
        embed.add_field(name="Usage", value=",ship [user1] [user2]", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def intellect(self, ctx):
        embed = discord.Embed(title="Intellect", description = "Randomly changes your sentence or word to upper case or lower case, im more brainy than u btw", color = 0xaaf0ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://media.tenor.com/X8sbMkeZK8EAAAAC/book-reading.gif")
        embed.add_field(name="Usage", value=",intellect [message]", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def hack(self, ctx):
        embed = discord.Embed(title="Hack", description = "Hacks a user, totally real and very dangerous btw", color = 0x49d7ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://media.tenor.com/JPX5iWzkrfQAAAAd/akudama-drive-anime.gif")
        embed.add_field(name="Usage", value=",hack [user]", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def roll(self, ctx):
        embed = discord.Embed(title="Roll", description = "Roll a dice and witness your sad luck, its between 1-6 if you dont know, ya hobo", color = 0xffd4a2)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://media.tenor.com/FqkVMdLs7cEAAAAC/after-school-dice-club-aya-taka-yashiki.gif")
        embed.add_field(name="Usage", value=",roll", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def meme(self, ctx):
        embed = discord.Embed(title="Meme", description = "Generates a random meme to make you ~~sad~~ laugh, trust <3", color = 0xc7ffbf)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = "https://media.tenor.com/gzM_6h_nC_sAAAAC/nichijou-hahaha.gif")
        embed.add_field(name="Usage", value=",meme", inline=False)
        embed.add_field(name="Precautions", value="To avoid repition of memes, try not to spam the command, the command might not work sometimes, if it doesnt, just repeat it again", inline=False)
        await ctx.send(embed=embed)


#hug, boop, kill, cuddle, pat, kiss, bonk, nom ,cry, slap, wave
    @help.command()
    async def hug(self, ctx):
        await ctx.send("Won't lie, you stink") 

    @help.command()
    async def boop(self, ctx):
        await ctx.send("This generation is ruined bru")

    @help.command()
    async def kill(self, ctx):
        await ctx.send("I feel the monke era was much more intellectual")

    @help.command()
    async def cuddle(self,ctx):
        await ctx.send("Honestly no one wants to cuddle you, why do you still insist on knowing the command?")

    @help.command()
    async def pat(self, ctx):
        await ctx.send("Really a donke moment")

    @help.command()
    async def kiss(self, ctx):
        await ctx.send("Kinda self explanatory innit mate")

    @help.command()
    async def bonk(self, ctx):
        await ctx.send("Truly a bozo moment")

    @help.command()
    async def nom(self, ctx):
        await ctx.send("Personally, i cant even rate you on the scale of dumbness")

    @help.command()
    async def cry(self, ctx):
        await ctx.send("Man I don't get paid enough for this, this gen is hopeless smh")

    @help.command()
    async def slap(self, ctx):
        await ctx.send("I need a raise god damnit")

    @help.command()
    async def wave(self, ctx):
        await ctx.send("No one likes you to be fair")


    


async def setup(client):
    await client.add_cog(Help(client))