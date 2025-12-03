import asyncio
from io import BytesIO
import random
import discord
from discord.ext import commands
from discord import app_commands
from io import BytesIO


class Fun(commands.Cog):

    def __init__(self, client):
        self.client=client

#Rate
    @commands.command()
    async def rate(self, ctx, member : discord.Member=None):
        if member == None:
            member=ctx.author
        responses = ["I'll give em' a **0/10** <:a_ohno:1085927192992686101>",
                    "How about a **1/10** <:a_thonk:1085947462402973737>",
                    "Ummm **2/10** <:a_SadKitty:1085927855617212446>",
                    "Uh maybe **3/10** <:a_wait:1085927223086829619>",
                    "I'd give a **4/10** <:a_SadKitty:1085927855617212446>",
                    "I'd give a **5/10** <:a_ohno:1085927192992686101>",
                    "How about a **6/10** <:a_wait:1085927223086829619>",
                    "I'll give em' a **7/10**<:a_catohmogawd:1085928203576676443>",
                    "Probably a **8/10** <:a_thonk:1085947462402973737>",
                    "Imagine getting a **9/10** <:a_imagine:1085927591577395323>",
                    "Umm **10/10** <:a_KekShook:1085927482038947931>"]

        await ctx.send(random.choice(responses))
                
#8Ball
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain <a:a_hmmyes:1086179205873664041>",
                     "It is decidedly so <a:a_hmmyes:1086179205873664041>",
                     "Without a doubt <a:a_hmmyes:1086179205873664041>",
                     "Yes, definitely <a:a_hmmyes:1086179205873664041>",
                     "You may rely on it <a:a_hmmyes:1086179205873664041>",
                     "Ah i see it, yes <a:a_hmmyes:1086179205873664041>",
                     "Most likely yes <a:a_hmmyes:1086179205873664041>",
                     "Yes <a:a_hmmyes:1086179205873664041>",
                     "Try again <:a_shrug:1086179782535938081>",
                     "Ask again later <:a_shrug:1086179782535938081>",
                     "Better not tell you now <:a_shrug:1086179782535938081>",
                     "Concentrate and ask again <:a_shrug:1086179782535938081>",
                     "Don't count on it <a:a_nonononononononoon:1086179963838926919>",
                     "My sources say no <a:a_nonononononononoon:1086179963838926919>",
                     "Unreliable much <a:a_nonononononononoon:1086179963838926919>",
                     "Very doubtful indeed <a:a_nonononononononoon:1086179963838926919>",
                     "Outlooks aren't looking so good <a:a_nonononononononoon:1086179963838926919>"]

        await ctx.send(f'**Question**: {question}\n**Answer**: {random.choice(responses)}')

#Imagine
    @commands.command()
    async def imagine(self, ctx, *, message=None):
        if message == None:
            await ctx.send('Give me something to imagine when <:a_bruhdoge:1085927295782486066>')
            return
        message = discord.Embed(color=(0xe8ffe7), description=f'imagine {message}')
        message.set_footer(text=f'Woah.. imagine imagining imagination', icon_url=ctx.author.avatar.url)

        await ctx.send(embed=message)
        

#Flip
    @commands.command()
    async def coinflip(self, ctx):
        options=["Heads", "Tails"]
        await ctx.send(random.choice(options))


#Ship
    @commands.command()
    async def ship(self,ctx, user_1 : discord.Member = None , user_2 : discord.Member = None):
        num1 = 0
        num2 = 100
        value = random.randint(num1,num2)
        if value > 0:
            emoji = "<:a_catohmogawd:1085928203576676443>"
        if value > 10:
            emoji = "<:a_catohmygod:1085928183813128242>"
        if value > 20:
            emoji = "<:a_SadKitty:1085927855617212446>"
        if value > 30:
            emoji = "<:a_angycri:1085974891527934112>"
        if value > 40:
            emoji = "<:a_imagine:1085927591577395323>"
        if value > 50:
            emoji = "<:a_crii:1085975201768030238>"
        if value > 60:
            emoji = "<:a_wait:1085927223086829619>"
        if value > 70:
            emoji = "<:a_clown:1085949380076519455>"
        if value > 80:
            emoji = "<:a_KekShook:1085927482038947931>"
        if value > 90:
            emoji = "<:a_roolob:1085974367860703352>"
        
        
        await ctx.send(f"{user_1.name} and {user_2.name} are like {value}% compatible {emoji}")
        await asyncio.sleep(2)
        fla = "||Imagine having a partner, im single btw >:)||" , "", "", "", "", "", "", "", "", "", "Now kiss"
        await ctx.send(random.choice(fla))

#Intellect
    @commands.command()
    async def intellect(self, ctx, *, msg:str):
        intellectify = ""
        for char in msg:
            intellectify += random.choice([char.upper(), char.lower()])
        await ctx.send(intellectify)

#Hack
    @commands.command()
    async def hack(self, ctx, *, user: discord.Member = None):
        if user == None:
            await ctx.send("Hol' up, whom we hacking <:a_imagine:1085927591577395323>")
            return
        Bypass=['_Bypassed 2FA.._', f"_{user.name} didn't set up a 2FA.._ <:a_Lmfao:1085927457116389436>"]
        Idpass=[f'**Email**: {user.name}xxx@yahoo.com_ | **Password**: _password_'
        ,f'**Email**: _{user.name}1234@outlook.com_| **Password**: _incorrect_'
        ,f'**Email**: _Shawty{user.name}@hotmail.com_ | **Password**: _12345678_'
        ,f'**Email**: _CoolPerson{user.name}69@gmail.com_ | **Password**: _sadlife123_'
        ,f'**Email**: _Dead{user.name}420@epic.com_ | **Password**: _fineasf69420_'
        ,f'**Email**: _YourDailyKpopStan786@yahoo.com_ | **Password**: _kpopuwuwu_'
        ,f'**Email**: _{user.name}gotFriends@outlook.com_ | **Password**: _Ihabfriendsyoudont_']
        DMs=[f"What's life", "Dinosaurs are cool", "Will you give me nitro..?", "man i love my mommy", "Mario Ftw", "I had a dream ngl", "I think it's smaller than most"]
        Mcw=[f"UwU", "reeeee", "ehe", "a", "lmao", "boop", "kinky", "smol"]
        Emotes=[f"<:a_PogTF:1085949102501679154>", '<:a_imagine:1085927591577395323>', '<:a_clown:1085949380076519455>'
        , '<:a_blekclown:1085949395163414530>', '<:a_eheboi:1085949907950637168>', '<a:a_twerk:1085950128638144534>', '<a:a_sadDays:1085950437368283227>'
        , '<:a_dorime:1085948582185668658>', '<:a_sauce:1085948849866154014>', '<:a_wth:1085950892773220352>']
        Ip=["127.0.0.1:147", "127.0.0.1:325", "127.0.0.1:654", "127.0.0.1:874", "127.0.0.1:1245", "127.0.0.1:1534", "127.0.0.1:9401"]
        

        await ctx.typing()
        message = await ctx.send(f"Proceeding to hack {user.name} now.. <a:a_hecks:1085951177562279966>")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send("_Finding discord login_..")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send("_Bypassing 2FA_..")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f" {(random.choice(Bypass))}")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f" {(random.choice(Idpass))}")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send("_Finding DM's with closest friends.. if there are any friends at all.._")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f' **Last Message**: _"{(random.choice(DMs))}"_')
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f' **Most Common Word**: _"{(random.choice(Mcw))}"_')
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Continuing to inject Trojan virus in user ID {user.id}.._")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Successfully injected Trojan virus, stolen emotes_ {(random.choice(Emotes))}")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Hacking Mihoyo Account.._ <:a_xiaoayo:1085951515820294236>")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Stolen all primogems and banned genshin account.._ <:a_Okden:1085927253277409341>")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Stealing IP address.._")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"**IP**: _{(random.choice(Ip))}_")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Selling data to the government.._")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Waiting for government approval.._")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        message = await ctx.send(f"_Approval Obtained.._ <:a_KekOk:1085927518189666384>")
        async with ctx.typing():
            await asyncio.sleep(1)
            if message.author.id == 915206129229914142:
                await message.delete()
        await ctx.send(f"Finished hacking {user.name}..")
        await asyncio.sleep(1)
        await ctx.send(f"{user.name} after they realise they were hacked <a:a_fuckyou:1085950763290869850>")


    @commands.command()
    async def roll(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        else:
            return
        a=random.randint(1,6)
        await ctx.send(f"{user.name} rolled a **{a}**!")


    @commands.command()
    async def mindread(self, ctx, message=None):
        if message==None:
            await ctx.send("Yeah but u need to provide me a number that u are thinking of you know :)")
        else:
            await ctx.send("Brainstorming Mathematics")
            await asyncio.sleep(1)
            await ctx.send("Rearranging Thoughts")
            await asyncio.sleep(1)
            await ctx.send("Reading Pulse")
            await asyncio.sleep(1)
            await ctx.send("Concluding Conclusion")
            await asyncio.sleep(1)
            await ctx.send("I think you thought of..")
            await asyncio.sleep(1)
            async with ctx.typing():
                await asyncio.sleep(1)
                await ctx.send(f"**{message}**!")



    

async def setup(client):
    await client.add_cog(Fun(client))