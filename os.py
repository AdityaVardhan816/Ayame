import discord
from discord.ext import commands
import asyncio

class os(commands.Cog):

    def __init__(self, client):
        self.client=client

    #Acc_Emb
    @commands.command(pass_context=True)
    async def access_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Bar Instructions",color=0xacd6ff)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="", value="◃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯▹", inline=False)
        embed.add_field(name="", value="**1.** Use the desired bots in their specific channels, u aren't supposed to use dank commands in owo channels", inline=False)
        embed.add_field(name="", value="**2.** Do not flood the channels by spamming the commands, it will result in a verbal and then a warn if continued", inline=False)
        embed.add_field(name="", value="**3.** Use Ayame commands only in the commands 1 and 2 channels", inline=False)
        embed.add_field(name="", value="**4.** And lastly, the general server rules apply here as well, u dummy", inline=False)
        embed.add_field(name="", value="◃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯▹", inline=False)
        embed.add_field(name="", value="To gain access to the bot channels, react below fr", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value='_Oh and btw, excuses like "omg i didnt know rules existed" wont be excused, you filthy human_ ', inline=False)
        embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/989/823/578/lantern-winter-hatsune-miku-anime-girls-wallpaper-preview.jpg")
        await ctx.send(embed=embed)

    #Rules_Emb
    @commands.command(pass_context=True)
    async def rules_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "__**Court Rules**__",color=0x801a36)
        embed.add_field(name="", value="(Anyone found violating server rules will be punished accordingly. Not knowing the rules is not a valid reason.)\n**Terms Of Service!**\n • Must strictly follow https://discord.com/terms")
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="««⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯•**.**༻✦༺**.**•⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯»»", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="__**Language**__", value="• We are an English server, refrain from speaking in other languages." , inline=False)
        embed.add_field(name="__**Behaviour**__", value="• Racism, slurs or disrespectful remarks of any kind will not be tolerated.\n• Keep the server SFW, NSFW emotes and media are forbidden within the server.\n• No form of harassing or bullying will be tolerated. Doing so will result in a ban.\n• No disrespect to any owner or admin will be tolerated and will result in a ban or temporary mute.", inline=False)
        embed.add_field(name="__**Begging**__", value="• Begging for nitro/items is strictly not allowed in the server or in DMs.", inline=False)
        embed.add_field(name="__**Spamming**__", value="• Spamming in any way or form is forbidden.\n• Mass pinging anyone will result in an automatic mute.\n• Pinging co-owners/owners for invalid reasons can lead to a mute/ban.", inline=False)
        embed.add_field(name="__**Trading**__", value="• Only ping relevant to your trade and not random people.\n• Scammers will immediately be given a chance to return the scammed items or money,\n• If not returned the scammer will be blacklisted and banned upon leaving the server.", inline=False)
        embed.add_field(name="__**Advertisement**__", value="• No DM advertising, this will result in a warn, if done twice then a ban.\n• Any form of ads or server links are not allowed, if you would like to partner please contact a partnership manager." , inline=False)
        embed.add_field(name="__**Impersonation**__", value="• We are an English server, refrain from speaking in other languages." , inline=False)
        embed.add_field(name="__**Support**__", value="• Do not ping co-owners/owners for situations a mod or admin can handle.\n• Respect our staff/moderation team and their decisions, arguing will lead to mute/ban.\n• Refrain from pinging or DMing staff right away when an issue arises use help-office, if there is no response then you may message staff." , inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="««⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯•**.**༻✦༺**.**•⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯»»", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="These are the only restrictions you need to follow in the server, if you are caught breaking these, you will be warned. Rules could change so keep an eye out")
        embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2022/10/Gotei_13_Captains.jpg")
        await ctx.send(embed=embed)

    #WarnP_Emb
    @commands.command(pass_context=True)
    async def warnp_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Court Punishments",color=0xcb95e0)
        embed.add_field(name="", value="**Below are the punishments given to the people who break rules, the severity of the punishment increases with every warn", inline=False)
        embed.add_field(name="", value="««⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯•**.**༻✦༺**.**•⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯»»", inline=False)
        embed.add_field(name="", value="**1st Warn \n** 1 hour mute", inline=False)
        embed.add_field(name="", value="**2nd Warn \n** 12 hour mute", inline=False)
        embed.add_field(name="", value="**3rd Warn \n** 24 hour mute", inline=False)
        embed.add_field(name="", value="**4th Warn \n** Temporary ban, 7 days", inline=False)
        embed.add_field(name="", value="**5th Warn \n** Temporary ban, 30 days", inline=False)
        embed.add_field(name="", value="**6th Warn \n** Permanent ban", inline=False)
        embed.add_field(name="", value="««⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯•**.**༻✦༺**.**•⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯»»", inline=False)
        embed.set_image(url="https://static.wikia.nocookie.net/bleach/images/5/54/137Kido_Corps_prepares.png/revision/latest?cb=20200414060358&path-prefix=en")
        await ctx.send(embed=embed)

    #Info_Emb
    @commands.command(pass_context=True)
    async def info_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Court Ranks",color=0xacd6ff)
        embed.add_field(name="", value="Rank **75** - <@&1087989004189847642> \n Generalissimo of the server, top most rank and the most respected ones \n **_Access to shogunates area_**", inline=False)
        embed.add_field(name="", value="Rank **70** - <@&1087989014528794634> \n Lords related to the Shoguns", inline=False)
        embed.add_field(name="", value="Rank **65** - <@&1088002626458767390> \n Provincial Lords \n **_Early access to upcoming updates_**", inline=False)
        embed.add_field(name="", value="Rank **60** - <@&1087989047013675060> \n Lords with kunimochi-nami", inline=False)
        embed.add_field(name="", value="Rank **55** - <@&1087989042928435220> \n Lords of a castle", inline=False)
        embed.add_field(name="", value="Rank **50** - <@&1087989040269230110> \n Lords without a castle \n **_Nickname Perms_**", inline=False)
        embed.add_field(name="", value="Rank **45** - <@&1087989049236664370> \n Elder councilor", inline=False)
        embed.add_field(name="", value="Rank **40** - <@&1087989045482770543> \n Banner Knights", inline=False)
        embed.add_field(name="", value="Rank **35** - <@&1087989020635693178> \n First Rank Retainers, has the right to wield double blades and ride horses into wars & peace", inline=False)
        embed.add_field(name="", value="Rank **30** - <@&1087989012083507320> \n Second Rank Retainers, has the right to wield double blades and ride horses into wars \n", inline=False)
        embed.add_field(name="", value="Rank **25** - <@&1087989017129267210> \n Third Rank Retainers, has the right to wield double blades \n **_Image Perms Granted_**", inline=False)
        embed.add_field(name="", value="Rank **20** - <@&1087989023689166928> \n Senior Attendants", inline=False)
        embed.add_field(name="", value="Rank **15** - <@&1087991027270426711> \n Junior Attendants \n **_External stickers usage Granted_**", inline=False)
        embed.add_field(name="", value="Rank **10** - <@&1087989051522555955> \n Personal Attendants", inline=False)
        embed.add_field(name="", value="Rank **5** - <@&1087988926213537842> \n Nakakoshos are the stablemen", inline=False)
        embed.add_field(name="", value="Rank **1** - <@&1087988362771705886> \n Koyakunins are the gate guards of the city", inline=False)
        embed.set_image(url="https://w0.peakpx.com/wallpaper/721/453/HD-wallpaper-samurai-girl-anime-katana-manga-white-callarin-blue.jpg")
        await ctx.send(embed=embed)

    #Aya_Emb
    @commands.command(pass_context=True)
    async def ayame_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(color=0x6a0000)
        embed.add_field(name="", value="««⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯•**.**༻✦༺**.**•⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯»»", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="Ayame is a very fun bot with utility and moderation as well, it's one of the most hilarious bots out there fr, prefix will be ``,``", inline=False)
        embed.add_field(name="", value="The bot is currently non inviteable as it doesn't support slash commands just yet, and its not public as well, you will be notified if the bot goes public!")
        embed.set_image(url="https://images.hdqwalls.com/download/elesis-elsword-anime-character-4k-7i-1920x1200.jpg")
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="««⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯•**.**༻✦༺**.**•⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯»»", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="Ayame offers a wide variety of commands to select from, more commands will be added in the future!", inline=False)
        embed.add_field(name="", value="▸ Fun commands to play with! \n ▸ Utility commands included \n ▸ Action commands to give a more real feel when hugging and all \n ▸ Moderation and Advanced Utility only available to the higher ups (Imagine not being a staff member)")
        await ctx.send(embed=embed)

    #Gender_Emb
    @commands.command(pass_context=True)
    async def roles_gen_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Gender Roles", description = "Take your gender roles from the given options",color=0xd5a7ff)
        embed.add_field(name="", value="<a:male:1090205275094528030> ~ If you're a guy", inline=False)
        embed.add_field(name="", value="<a:female:1090205329117155338> ~ If you're a girl", inline=False)
        embed.add_field(name="", value="<:genderless:1090205300323258391> ~ If you're a classified person", inline=False)
        embed.set_image(url="https://static.wikia.nocookie.net/bleach/images/8/8a/BBSSAFWYKenpachi_Azashiro_and_Urozakuro.png/revision/latest?cb=20230116075742&path-prefix=en")
        await ctx.send(embed=embed)
        
    #Nation_Emb
    @commands.command(pass_context=True)
    async def roles_nat_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Nationality Roles", description = "Pick your nationality from the given choices",color=0xffecbb)
        embed.add_field(name="", value="<:hanginaround:987645974254067772> ~ If you're north american", inline=False)
        embed.add_field(name="", value="<:Wait:1089032423016247346> ~ If you're south american", inline=False)
        embed.add_field(name="", value="<:okDen:1089032471611441263> ~ If you're asian", inline=False)
        embed.add_field(name="", value="<:fuckyousaytome:1089032485402325112> ~ If you're antarctican", inline=False)
        embed.add_field(name="", value="<:sauce:1089032318733254717> ~ If you're european", inline=False)
        embed.add_field(name="", value="<:handsomehampter:1306293650480693250> ~ If you're from africa", inline=False)
        embed.add_field(name="", value="<:Wheezee:1089038594498367538> ~ If you're from oceania", inline=False)
        embed.set_image(url="https://images.saymedia-content.com/.image/t_share/MTc1MTExNDMxNzkwOTI4OTkx/best-captains-bleach.png")
        await ctx.send(embed=embed)

    #Age_Emb
    @commands.command(pass_context=True)
    async def roles_age_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Age Roles", description = "Tell us your age, dont lie about it, we all know you're short",color=0xffebb5)
        embed.add_field(name="", value="<:pookie:1306299510208860160> ~ If you're between 13-17", inline=False)
        embed.add_field(name="", value="<:Hampter:1128598748201766993> ~ If you're between 18-21", inline=False)
        embed.add_field(name="", value="<:handsomehampter:1306293650480693250> ~ If you're 22 or above", inline=False)
        embed.set_image(url="https://animevania.com/wp-content/uploads/2023/11/Jushiro-Ukitake-1024x576.jpg")
        await ctx.send(embed=embed)


    #Ping_Emb
    @commands.command(pass_context=True)
    async def roles_ping_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Ping Roles", description = "Tell us your what all you want to be included in, except being the owner, thats out of your league",color=0xc7f4ff)
        embed.add_field(name="", value="<:lurk:1089035161951272972> ~ Get pinged for announcements", inline=False)
        embed.add_field(name="", value="<:PepeThumbsUp:1089038392693624963> ~ Get pinged for giveaways", inline=False)
        embed.add_field(name="", value="<:hmmmmmmmmmm:1134418031062286356> ~ Get pinged for minigames", inline=False)
        embed.set_image(url="https://cdn.oneesports.gg/cdn-data/2023/03/Anime_Bleach_Urahara_BBS-1-1024x576.jpg")
        await ctx.send(embed=embed)

    #Ticket_Emb
    @commands.command(pass_context=True)
    async def ticket_emb(self, ctx):
        if ctx.author.id != 744831273406824449:
            return
        embed=discord.Embed(title= "Ticketing", description = "Open a ticket for assistance",color=0xc5093b)
        embed.add_field(name="__**Ticket Rules**__", value="Do not open a ticket without proper reasoning, it is impossible to accidentally open a ticket. Please do not @ any staff members when opening a ticket, we will get back to you ASAP.", inline=False)
        embed.add_field(name="__**Proper Reasons to Open a Ticket**__", value="", inline=False)
        embed.add_field(name="", value="__**1.**__ Claiming giveaway, drop, event or other winnings.", inline=False)
        embed.add_field(name="", value="__**2.**__ General Support (Questions that need to be answered by staff.).", inline=False)
        embed.add_field(name="", value="__**3.**__ Reporting another user in this server.''Please follow all these rules and know if you break any of them, there will be consequences.", inline=False)
        embed.set_image(url="https://i.pinimg.com/originals/1b/56/49/1b5649caa9bd963c8470f7a05efc0c5d.png")
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(os(client))