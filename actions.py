import random
import discord
from discord.ext import commands

class Actions(commands.Cog):

    def __init__(self, client):
        self.client=client

#Hug, Boop, Kill, Wave, Cuddle, Pat, Bonk, Cry, Slap, Nom,
#Kiss, Tickle, Punch, Blush, Happy, Sad, Lick, Triggered

#Hug Command
#*18 Hug gifs*

    @commands.command()
    async def hug (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Hug who bruv")
            return
        hug_names = ['Hugs you!', 'Adorable!', 'Sends a hug! uwu']
        hug_gifs = ['https://c.tenor.com/PuuhAT9tMBYAAAAC/anime-cuddles.gif', 'https://i.gifer.com/6li2.gif', 'https://c.tenor.com/5UwhB5xQSTEAAAAC/anime-hug.gif'
        ,'https://c.tenor.com/pYzpQgkAQJkAAAAC/violet-evergarden-hug.gif', 'https://c.tenor.com/uVzTcP8RLZgAAAAC/loli-lolita.gif'
        ,'https://c.tenor.com/znURt9fG-KcAAAAC/anime-hug-anime-nekopara.gif','https://i.gifer.com/2QEa.gif','https://data.whicdn.com/images/334153915/original.gif'
        ,'https://cdn.myanimelist.net/s/common/uploaded_files/1460988091-6e86cd666a30fcc1128c585c82a20cdd.gif'
        ,'https://i.pinimg.com/originals/bb/84/1f/bb841fad2c0e549c38d8ae15f4ef1209.gif','https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif','https://acegif.com/wp-content/gif/anime-hug-45.gif'
        ,'https://c.tenor.com/EGHawmNW-L4AAAAC/anime-hug.gif','https://i.imgur.com/7DPuocI.gif','https://media3.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif'
        ,'https://c.tenor.com/rQ2QQQ9Wu_MAAAAC/anime-cute.gif','https://c.tenor.com/WMjnqKcGYTQAAAAd/ao-haru-ride-hug.gif'
        ,'https://i.gifer.com/Yp9v.gif']
        embed = discord.Embed(
            colour=(0xd2fdff), 
            description=f"{ctx.author.mention} {(random.choice(hug_names))}" 
            
            ) 
        embed.set_image(url=(random.choice(hug_gifs)))

        await ctx.send(embed=embed)


#Boop Command
#*15 boop gifs*

    @commands.command()
    async def boop (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Boop who? The air?")
            return
        boop_gifs = ['https://c.tenor.com/_vVL5fuzj4cAAAAC/nagi-no.gif','https://c.tenor.com/APqauOtznp4AAAAC/boop-poke.gif', 'https://c.tenor.com/XwOxT1ZCucwAAAAC/yuri-nose-to-nose.gif'
        ,'https://c.tenor.com/fxIMcE41WpgAAAAd/anime-boop.gif', 'https://i.pinimg.com/originals/43/1e/34/431e3414cf0432f0c2c6027ab800c048.gif'
        ,'https://c.tenor.com/4OHxyGd4qp0AAAAC/boop-nose.gif','https://giffiles.alphacoders.com/187/187490.gif', 'https://c.tenor.com/3dOqO4vVlr8AAAAC/poke-anime.gif'
        ,'https://c.tenor.com/NjIdfk7i3bsAAAAC/poke-poke-poke.gif','https://i.gifer.com/FK0b.gif','https://i.gifer.com/QJHs.gif','https://i.imgur.com/hWXeCMO.gif'
        ,'https://c.tenor.com/7iV_gBGrRAUAAAAC/boop-poke.gif','https://c.tenor.com/KyPxfr4AVFcAAAAC/poke.gif']
        boop_names = ['Get poked!', 'Oop boop boop!', 'Poke poke!', 'Wakey wakey! >.<']
        embed = discord.Embed(
            colour=(0xfdc6e3),
            description=f"{ctx.author.mention} {(random.choice(boop_names))}"

        )
        embed.set_image(url=(random.choice(boop_gifs)))

        await ctx.send(embed=embed)


#Kill Command
#*15 Kill gifs*

    @commands.command()
    async def kill (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Yes I get it, u wanna kill someone, but who")
            return
        kill_gifs = ['https://pa1.narvii.com/6152/c952848b013a6ba98022a8ce1dcfa0545abc9b4b_hq.gif','https://c.tenor.com/WRMZ2Kvm33wAAAAC/anime-smash.gif'
        ,'http://24.media.tumblr.com/tumblr_melc0lbzdJ1rw1exqo2_500.gif','https://i.pinimg.com/originals/71/07/f7/7107f75958a64cb9cc0e7472a859b64b.gif'
        ,'https://thumbs.gfycat.com/DisguisedHeartyAmericanbulldog-max-1mb.gif','https://c.tenor.com/_Zl4NmO5aJkAAAAC/anime-pillow.gif','https://c.tenor.com/bpgPEPfFlnIAAAAd/yeet-anime.gif'
        ,'https://c.tenor.com/rjR2Z67erfkAAAAd/death-saitama.gif','https://c.tenor.com/1dtHuFICZF4AAAAC/kill-smack.gif','https://c.tenor.com/HltbzNICQeAAAAAC/satsuki-kiryuin-kill-la-kill.gif'
        ,'https://c.tenor.com/j38Y2WWBJiUAAAAd/one-punch-man.gif', 'https://c.tenor.com/dR93uTOAy6wAAAAC/anime-run.gif', 'https://c.tenor.com/m5JE6qMbO6cAAAAC/anime-hit.gif'
        , 'https://c.tenor.com/SOaiOy7Jx9IAAAAC/horimiya-anime.gif', 'https://c.tenor.com/0X-69vStx4QAAAAd/truck-hit.gif']
        kill_names = ['May thy soul attain peace x.x', 'Ouch!', 'Rest in Peace.. ;-;', "Must've hurt, no? >.>"]
        embed = discord.Embed(
            color=(0xffdede),
            description=f"{ctx.author.mention} {(random.choice(kill_names))}"

        )
        embed.set_image(url=(random.choice(kill_gifs)))

        await ctx.send(embed=embed)


#Wave Command
#*15 Wave gifs*

    @commands.command()
    async def wave (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Wave who?")
            return
        wave_gifs = ['https://c.tenor.com/dessgik7ovcAAAAC/anime-wave.gif','https://c.tenor.com/fraRGD3luZ4AAAAC/precure-precure-wave.gif'
        ,'https://c.tenor.com/S6Kxbixp1yUAAAAC/gakkou-gurashi-hello.gif','https://c.tenor.com/AuBOgaPV41cAAAAC/shinya-shinyahiragi.gif'
        ,'https://c.tenor.com/2yC5Fpjrh88AAAAC/hello-waving.gif', 'https://c.tenor.com/FMpLzF4UJhwAAAAC/kisumi-wave.gif', 'https://c.tenor.com/-TKyQcZRmwkAAAAC/hi-hey.gif'
        ,'https://c.tenor.com/6gR0abE6x8MAAAAC/anime-baby.gif', 'https://c.tenor.com/MTapkX_690gAAAAC/sailor-moon-anime.gif', 'https://c.tenor.com/_Exw4V_izbkAAAAC/cute-anime.gif'
        ,'https://c.tenor.com/DDnp-TLMTWQAAAAC/hello-anime.gif', 'https://c.tenor.com/ZzKI5LHlIE8AAAAC/anime-girl.gif'
        ,'https://c.tenor.com/NuUrjErxTGkAAAAC/the-promised-neverland-yakusoku-no-neverland.gif','https://c.tenor.com/UPa7j2Dz3rgAAAAC/wave.gif'
        ,'https://c.tenor.com/B8PvHQ3BhuoAAAAd/kakashi-kakashi-hatake.gif' ]
        wave_names= ['Well hello there!', 'Heya!', '*Waving intesifies*']
        embed = discord.Embed(
            color=(0xe4ffe1),
            description=f"{ctx.author.mention} {(random.choice(wave_names))}"

        )
        embed.set_image(url=(random.choice(wave_gifs)))

        await ctx.send(embed=embed)


#Cuddle Command
#*15 cuddle gifs*

    @commands.command()
    async def cuddle (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Cuddle who tho")
            return
        cuddle_gifs = ['https://c.tenor.com/H7i6GIP-YBwAAAAd/a-whisker-away-hug.gif', 'https://c.tenor.com/dbIbtIyByEwAAAAC/cuddle-anime.gif', 'https://c.tenor.com/sK9icjg3xm4AAAAC/strugglesnuggle-annoyed.gif'
        ,'https://c.tenor.com/hsnYxyxQbRoAAAAC/hug-anime.gif','https://c.tenor.com/okeP090NK1cAAAAC/anime-couples.gif','https://c.tenor.com/WWgamF4xjZcAAAAC/anime-cuddle.gif'
        ,'https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif','https://c.tenor.com/fklZNDaU9NMAAAAC/hideri-hideri-kanzaki.gif'
        ,'https://c.tenor.com/GuHHnDT6quYAAAAd/anime-couples.gif','https://c.tenor.com/A5ZuMAZ44l8AAAAC/anime-cuddle.gif','https://c.tenor.com/NaJIRcVnWloAAAAd/sao-sword-art-online.gif'
        ,'https://c.tenor.com/zvlN9ZJEaj4AAAAC/anime-hug.gif','https://c.tenor.com/DVOTqLcB2jUAAAAC/anime-hug-love.gif','https://c.tenor.com/-QIbjtrBd64AAAAC/cuddle-anime.gif'
        ,'https://c.tenor.com/ch1kq7TOxlkAAAAC/anime-cuddle.gif']
        cuddle_names = ['I- u- uwu', 'This is so cute!', 'Adorable!']
        embed = discord.Embed(
            color=(0xfff7bf),
            description=f"{ctx.author.mention} {(random.choice(cuddle_names))}"

        )
        embed.set_image(url=(random.choice(cuddle_gifs)))

        await ctx.send(embed=embed)


#Pat Command
#*15 pat gifs*

    @commands.command()
    async def pat (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Pat who bruh")
            return
        pat_gifs = ['https://c.tenor.com/Hgt-mT0KXN0AAAAd/chtholly-tiat.gif','https://c.tenor.com/9R7fzXGeRe8AAAAC/fantasista-doll-anime.gif'
        ,'https://c.tenor.com/jBuHEbqxarcAAAAC/k-on-anime.gif','https://c.tenor.com/wLqFGYigJuIAAAAC/mai-sakurajima.gif','https://c.tenor.com/8DaE6qzF0DwAAAAC/neet-anime.gif'
        ,'https://c.tenor.com/iIZ5BwSuaCQAAAAd/anime-senko-san.gif', 'https://c.tenor.com/rZRQ6gSf128AAAAC/anime-good-girl.gif'
        ,'https://c.tenor.com/N41zKEDABuUAAAAC/anime-head-pat-anime-pat.gif','https://c.tenor.com/dmYhPDHbbI4AAAAC/misha-misha-necron-anos-voldigoad-the-misfit-of-demon-king-academy-headpat-pat.gif'
        ,'https://c.tenor.com/E6fMkQRZBdIAAAAC/kanna-kamui-pat.gif','https://c.tenor.com/DCMl9bvSDSwAAAAd/pat-head-gakuen-babysitters.gif','https://c.tenor.com/jEfC8cztigIAAAAC/anime-pat.gif'
        ,'https://c.tenor.com/o0re0DQzkd8AAAAC/anime-head-rub.gif','https://c.tenor.com/EYhRCNjiyIYAAAAC/momokuri-anime-pat.gif','https://c.tenor.com/lnoDyTqMk24AAAAC/anime-anime-headrub.gif']
        pat_names = ['Pat pat', 'There there', 'Aww..']
        embed = discord.Embed(
            color=(0xadf8bd),
            description=f"{ctx.author.mention} {(random.choice(pat_names))}"

        )
        embed.set_image(url=(random.choice(pat_gifs)))

        await ctx.send(embed=embed)


#Bonk Command
#*15 bonk gifs*

    @commands.command()
    async def bonk (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Who needs a bonk")
            return
        bonk_gifs = ['https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif', 'https://c.tenor.com/EiFGi9dZXSAAAAAC/toradora-taiga.gif'
        ,'https://c.tenor.com/1T5bgBYtMgUAAAAC/head-hit-anime.gif','https://c.tenor.com/CrmEU2LKix8AAAAC/anime-bonk.gif','https://c.tenor.com/3AHXkQLyVScAAAAd/anime-konosuba.gif'
        ,'https://c.tenor.com/fz-V6dZ1PiQAAAAC/how-to-raise-a-boring-girlfriend-saenai.gif','https://c.tenor.com/TCxz2fAU75IAAAAC/love-lab-head-smack-anime-smack.gif'
        ,'https://c.tenor.com/mXwNLMSQRN8AAAAC/yuru-yuri-chinatsu-yoshikawa.gif','https://c.tenor.com/31WOy2yRK3QAAAAC/chuunibyou-hit.gif','https://c.tenor.com/D_-8tx--KDAAAAAC/chuunibyou-anime.gif'
        ,'https://c.tenor.com/vmBaynQNcLoAAAAC/anime.gif','https://c.tenor.com/OwlLGMnwu8sAAAAM/bongo-cat-hat-bongo-cat.gif','https://c.tenor.com/N3ZdP-hTVHYAAAAC/anime-anime-bonk.gif'
        ,'https://c.tenor.com/utXUqcxLf_IAAAAd/anime-bonk.gif','https://c.tenor.com/1NgForvfNAAAAAAC/no-more-brain-rikka-takanashi.gif']
        bonk_names = ['Ouch', 'Bop Bop', '*Random Hitting noises*']
        embed = discord.Embed(
            color=(0xc5fdff),
            description=f"{ctx.author.mention} {(random.choice(bonk_names))}"

        )
        embed.set_image(url=(random.choice(bonk_gifs)))

        await ctx.send(embed=embed)

#Cry Command
#*15 cry gifs*

    @commands.command()
    async def cry (self, ctx):
        cry_gifs = ['https://c.tenor.com/SVvaVhZlVB8AAAAC/anime-crying.gif', 'https://c.tenor.com/q0nNfTktQ7wAAAAC/crying-anime.gif', 'https://c.tenor.com/gDk49oAcW9QAAAAd/anime-cry-cry.gif'
        ,'https://c.tenor.com/Q0HUwg81A_0AAAAd/anime-cry.gif', 'https://c.tenor.com/thw0X00MurYAAAAC/anime-crying.gif', 'https://c.tenor.com/fBNK66X1CWwAAAAC/cry-anime.gif'
        ,'https://c.tenor.com/zPGH1GeElyAAAAAd/anime-anime-panic.gif', 'https://c.tenor.com/v2or0RQAK1UAAAAC/taiga-crying.gif', 'https://c.tenor.com/hge_M0aodP4AAAAC/free-iwatobi.gif'
        ,'https://c.tenor.com/v_FOnNyYuGcAAAAC/cry-k-on.gif', 'https://c.tenor.com/lJJ4GfvoJKwAAAAC/anime-crying.gif', 'https://c.tenor.com/AawIsMGnR88AAAAC/llorar1-cry.gif'
        ,'https://c.tenor.com/K1uo_rC838wAAAAC/princess-anime.gif', 'https://c.tenor.com/tgVGh4R71MEAAAAC/anime-cry.gif', 'https://c.tenor.com/SgjbrdojHZwAAAAC/anohana-tears.gif']
        cry_names = [f'Aww they need some hugs', 'I- ;-;', "I- I'm here for you- ;-;"]
        embed = discord.Embed(
            color=(0xc5fdff),
            description=f"{ctx.author.mention} {(random.choice(cry_names))}"

        )
        embed.set_image(url=(random.choice(cry_gifs)))

        await ctx.send(embed=embed)

#Slap Command
#*15 slap gifs*

    @commands.command()
    async def slap (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Who needs a taste of this hand?")
            return
        slap_gifs = ['https://c.tenor.com/pgq_YsVX7sEAAAAC/meliodas-seven-deadly-sins.gif', 'https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif', 'https://c.tenor.com/PeJyQRCSHHkAAAAC/saki-saki-mukai-naoya.gif'
        ,'https://c.tenor.com/E3OW-MYYum0AAAAC/no-angry.gif', 'https://c.tenor.com/UDo0WPttiRsAAAAd/bunny-girl-slap.gif', 'https://c.tenor.com/BYu41fLSstAAAAAC/when-you-cant-accept-reality-slap.gif'
        ,'https://c.tenor.com/8SoReGELlnAAAAAC/anime-girl-slap.gif', 'https://c.tenor.com/bW9sL6u6V7AAAAAC/fly-away-slap.gif', 'https://c.tenor.com/noSQI-GitQMAAAAC/mm-emu-emu.gif'
        ,'https://c.tenor.com/2R9-4O6jqEsAAAAC/slap-slapping.gif', 'https://c.tenor.com/fKzRzEiQlPQAAAAC/anime-slap.gif', 'https://c.tenor.com/uTT2gXruNtkAAAAC/oreimo-anime.gif'
        ,'https://c.tenor.com/aP7Du3RWX6YAAAAC/slap-anime.gif', 'https://c.tenor.com/F11VMCuXthAAAAAC/anime-slap.gif', 'https://c.tenor.com/eStYuttoV7QAAAAd/osamake-anime.gif']
        slap_names = [f"Don't worry, you deserve it", 'Ow!!', "Must've hurt.. oof"]
        embed = discord.Embed(
            color=(0xc5fdff),
            description=f"{member.mention} {(random.choice(slap_names))}"

        )
        embed.set_image(url=(random.choice(slap_gifs)))

        await ctx.send(embed=embed)
    
#Nom Command
#*12 nom gifs*

    @commands.command()
    async def nom (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Who's ready to get bitten, _nom nom nom >:)_")
            return
        nom_gifs = ['https://c.tenor.com/nkNsOraAx4AAAAAC/anime-bite.gif', 'https://c.tenor.com/DrLl1pH034gAAAAC/gamerchick42092-anime.gif', 'https://c.tenor.com/1LtA9dSoAIQAAAAC/zero-no-tsukaima-bite.gif'
        ,'https://c.tenor.com/aKzAQ_cFsFEAAAAC/arms-bite.gif', 'https://c.tenor.com/8UjO54apiUIAAAAC/gjbu-bite.gif', 'https://c.tenor.com/hwCVSWyji0QAAAAC/anime-bite.gif'
        ,'https://c.tenor.com/Xpv7HTk-DIYAAAAC/mad-angry.gif', 'https://c.tenor.com/5FOgNEcoaYMAAAAC/neck-kisses.gif', 'https://c.tenor.com/6HhJw-4zmQUAAAAC/anime-bite.gif'
        ,'https://c.tenor.com/YaLlfgzRahYAAAAC/anime-neko.gif', 'https://c.tenor.com/JKUW0YQtyTAAAAAC/cheek-kiss.gif', 'https://c.tenor.com/n0DPyBDtZHgAAAAC/anime-bite.gif']
        nom_names = [f"Reeeeeeeeee", 'Ow!!', "_Tasty_"]
        embed = discord.Embed(
            color=(0xc5fdff),
            description=f"{ctx.author.mention} {(random.choice(nom_names))}"

        )
        embed.set_image(url=(random.choice(nom_gifs)))

        await ctx.send(embed=embed)
    
#Kiss Command
#*15 kiss gifs*

    @commands.command()
    async def kiss (self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Imagine kissing someone without mentioning them")
            return
        kiss_gifs = ['https://c.tenor.com/etSTc3aWspcAAAAC/yuri-kiss.gif', 'https://c.tenor.com/F02Ep3b2jJgAAAAC/cute-kawai.gif', 'https://c.tenor.com/7T1cuiOtJvQAAAAC/anime-kiss.gif'
        ,'https://c.tenor.com/4ofp_xCUBxcAAAAC/eden-of-the-east-akira-takizawa.gif', 'https://c.tenor.com/AtcFtesvEcEAAAAd/kissing-anime.gif', 'https://c.tenor.com/wDYWzpOTKgQAAAAC/anime-kiss.gif'
        ,'https://c.tenor.com/TnjL6WcdkkwAAAAd/anime-kiss.gif', 'https://c.tenor.com/cp9FdcuAWbcAAAAC/katanagatari-kiss.gif', 'https://c.tenor.com/0mdCwkmGD1oAAAAC/kiss-love.gif'
        ,'https://c.tenor.com/YbIFALM1-MIAAAAC/anime-kiss.gif', 'https://c.tenor.com/HgV0doOr_YoAAAAC/golden-time-anime.gif', 'https://c.tenor.com/qfY-5liiihUAAAAC/blowkiss-anime.gif'
        ,'https://c.tenor.com/0E_odieuKmwAAAAC/anime-zero.gif', 'https://c.tenor.com/Ct9yIxN5nE0AAAAC/kiss-anime.gif', 'https://c.tenor.com/h9A4bnxJys8AAAAC/cheek-kiss.gif']
        kiss_names = [f"_Smooches_", 'Woah', "👀"]
        embed = discord.Embed(
            color=(0xc5fdff),
            description=f"{ctx.author.mention} {(random.choice(kiss_names))}"

        )
        embed.set_image(url=(random.choice(kiss_gifs)))

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Actions(client))