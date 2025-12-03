import discord
from discord.ext import commands
import wikipediaapi
import asyncio
import random

class info(commands.Cog):

    def __init__(self, client):
        self.client=client

#Wikipedia
    @commands.command()
    async def wiki(self, ctx, *, query):
        wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent="Ayame/1.0"
        )
        page = wiki_wiki.page(query)
    
        if not page.exists():
            await ctx.send("Sorry, I couldn't find any information on that topic.")
            return
    
        summary = page.summary[:2000]
        await ctx.send(f'**{page.title}**: {summary}')



#Weapon Info
    @commands.group(invoke_without_command=True)
    async def info(self, ctx):
        embed = discord.Embed(description = "Below are the basics of the bot and how to play it! To view the details and attributes of weapons, equipment, do ``,info (item)``", color=(0xffd48d))
        embed.set_author(name="Getting Started!", icon_url=ctx.author.avatar.url)
        embed.set_image(url="https://cdn.suwalls.com/wallpapers/games/diablo-iii-24689-1920x1080.jpg")

        embed.add_field(name="<a:a_right:1085932661140369490> Gearing up", value="Start off by picking a class of your choice, each class offers a different set of equipment, rely on different attributes, have unique moves and much more!", inline=False)
        embed.add_field(name="<a:a_right:1085932661140369490> Profile", value="To view your profile, do ``,profile``, all your necessary information shows up on there, make sure to outclass everyone", inline = False)
        embed.add_field(name="<a:a_right:1085932661140369490> Lore Repository", value="The lore repository consists of the history and stories of heros and villains from all your classes, do ``,lr`` for more info on it", inline = True)
        embed.add_field(name="<a:a_right:1085932661140369490> Marketplace", value="Ayame offers a lot of different shops to visit, for instance, the blacksmith offers you your primary weapons, the dwarvenfield offers you your off hand slot equipment, check out ``,shop`` for more info", inline = False)
        embed.add_field(name="<a:a_right:1085932661140369490> Inventory", value="Your inventory is your place where u store your items, make sure to collect the rarest of the rarest items! Your main inventory can be accessed through ``,inv`` or ``,bag``, your secondary inventory which is for off-hands can be accessed through ``,ars`` or ``,arsenal``")

        await ctx.send (embed=embed)

    @info.command(aliases=['1', 'Holy_Sword'])
    async def holy_sword(self,ctx):
        embed = discord.Embed(title="Holy Sword", description = "A sword of righteousness, forged in holy light, its blade it sharper than your mind", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/saofanon/images/c/ca/Sword-4.jpg/revision/latest?cb=20140629042139')
        embed.add_field(name="Favoured Classes", value="Paladin, Warrior, Monk", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['2','Abyssal_Axe'])
    async def abyssal_axe(self,ctx):
        embed = discord.Embed(title="Abyssal Axe", description = "A menacing weapon forged from dark materials, infused with malevolent energies. It is favored by warriors who draw power from the abyss", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://i.pinimg.com/736x/70/4b/41/704b4106e5c32bed498beae818d84e86.jpg')
        embed.add_field(name="Favoured Classes", value="Shaman, Warrior, Hunter, Paladin", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['3', "Hunters_Bow"])
    async def hunters_bow(self,ctx):
        embed = discord.Embed(title="Hunters Bow", description = "A finely crafted ranged weapon designed for precision and agility. It is favored by hunters and archers for its lightweight construction and deadly accuracy.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/e/e7/Mok%27Nathal_Bow_full.jpg/revision/latest?cb=20210127204150')
        embed.add_field(name="Favoured Classes", value="Hunter, Demon Hunter, Rogue", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['4', 'Spectral_Mace'])
    async def spectral_mace(self,ctx):
        embed = discord.Embed(title="Spectral Mace", description = "A mystical weapon infused with ethereal energies, often wielded by priests, paladins, or spiritual warriors. Its head emits a faint, ghostly glow, hinting at its otherworldly origins. ", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static1.squarespace.com/static/5be5fdd4cc8fed54b96bdc64/5bf3043603ce64ef0e4aac78/5cd5a4fa7817f796f4ade335/1557516416004/500px-Powermace_%28Devout_Aurastone_Hammer%29.png?format=1500w')
        embed.add_field(name="Favoured Classes", value="Priest, Paladin, Warlock, Mage, Monk", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['5', 'Long_Greatsword'])
    async def long_greatsword(self,ctx):
        embed = discord.Embed(title="Long Greatsword", description = "A formidable melee weapon known for its size and reach. It features a long, straight blade with a sturdy hilt designed for two-handed use.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://cdnb.artstation.com/p/assets/images/images/060/008/125/large/khaynan-ferreira-ilustracao-sem-titulo-22.jpg?1682364108')
        embed.add_field(name="Favoured Classes", value="Warrior, Paladin", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)
        
    @info.command(aliases=['6', 'Royal_Staff'])
    async def royal_staff(self,ctx):
        embed = discord.Embed(title="Royal Staff", description = "A prestigious magical weapon often adorned with ornate designs and precious gems, symbolizing authority and power.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/4/4e/Staff_of_Origination_full.jpg/revision/latest?cb=20160802005421')
        embed.add_field(name="Favoured Classes", value="Priest, Warlock, Shaman, Mage", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['7', 'Corrupted_Daggers'])
    async def corrupted_daggers(self,ctx):
        embed = discord.Embed(title="Corrupted Daggers", description = "Sinister weapons tainted by dark magic or malevolent forces. These daggers are often used by assassins and rogues who embrace the shadows.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://hearthstone.wiki.gg/images/thumb/5/53/Aldrachi_Warblades_full.jpg/375px-Aldrachi_Warblades_full.jpg')
        embed.add_field(name="Favoured Classes", value="Demon Hunter, Rogue", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['8', 'Burning_Warblade'])
    async def burning_warblade(self,ctx):
        embed = discord.Embed(title="Burning Warblade", description = "A fierce weapon imbued with elemental fire, often wielded by warriors and champions with a mastery of flame.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/2/20/Splitting_Axe_full.jpg/revision/latest?cb=20190829130434')
        embed.add_field(name="Favoured Classes", value="Demon Hunter, Warrior, Shaman", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['9', 'Shadowy_Ruins'])
    async def shadowy_ruins(self,ctx):
        embed = discord.Embed(title="Shadowy Ruins", description = "A ancient tome filled with dark secrets and forbidden knowledge about lost civilizations and cursed lands.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://hearthstone.wiki.gg/images/thumb/e/ea/Primordial_Studies_full.jpg/462px-Primordial_Studies_full.jpg')
        embed.add_field(name="Favoured Classes", value="Warlock, Mage, Priest", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['10', 'Spirit_Claws'])
    async def spirit_claws(self,ctx):
        embed = discord.Embed(title="Spirit Claws", description = "Ethereal weapons favored by spiritual guardians. These claws are imbued with the essence of ancestral spirits, allowing the wielder to strike with both physical and spectral force.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://i.pinimg.com/474x/87/37/30/8737303e6dac562dded7cb133889e13d.jpg')
        embed.add_field(name="Favoured Classes", value="Rogue, Monk, Hunter, Shaman", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['11', 'Death_Mantle'])
    async def death_mantle(self,ctx):
        embed = discord.Embed(title="Death Mantle", description = "Despite its humble status, the Death Mantle is a reliable and efficient tool for any aspiring adventurer. Forged from sturdy fibres and tempered with basic enchantments, this weapon is often the first choice for those just starting their journey.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/d/df/Jan%27alai%27s_Mantle_full.jpg/revision/latest?cb=20181211120243')
        embed.add_field(name="Favoured Classes", value="Mage, Rogue, Priest", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)
    
    @info.command(aliases=['12', 'Kings_Sabre'])
    async def kings_sabre(self,ctx):
        embed = discord.Embed(title="Kings Sabre", description = "The King's Sabre, though considered common, bears the mark of craftsmanship and legacy. Its blade, forged from tempered steel, shines with a brilliant polish that reflects its regal origins. The hilt is intricately adorned with ornate designs, depicting scenes of battles won and kingdoms united.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://i.redd.it/8rihq63imhi81.jpg')
        embed.add_field(name="Favoured Classes", value="Paladin, Warrior, Priest", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['13', 'Sharp_Katar'])
    async def sharp_katar(self,ctx):
        embed = discord.Embed(title="Sharp Katar", description = "The Sharp Katar is a sleek and deadly weapon, favored by rogues and assassins for its swift and precise strikes. Crafted from hardened steel, its double-edged blade tapers to a razor-sharp point, ideal for piercing through armor and delivering fatal blows with precision.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://i.pinimg.com/474x/97/6d/5d/976d5d1f99a8e0354e63d7306487b367.jpg')
        embed.add_field(name="Favoured Classes", value="Rogue, Demon Hunter, Hunter, Monk", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['14', 'Bloody_Sword'])
    async def bloody_sword(self,ctx):
        embed = discord.Embed(title="Bloody Sword", description = "The Bloody Sword is a grim reminder of battles fought and lives lost. Its blade, stained with the blood of foes vanquished and comrades fallen, tells tales of valor and sacrifice on the battlefield. Crafted from hardened steel and tempered with the heat of conflict, its edge retains a keen sharpness despite its grim history.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/7/7a/Blood_Razor_full.jpg/revision/latest/scale-to-width-down/450?cb=20170810152820')
        embed.add_field(name="Favoured Classes", value="Paladin, Warrior, Monk, Warlock", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['15', 'Quick_Pick'])
    async def quick_pick(self,ctx):
        embed = discord.Embed(title="Quick Pick", description = "The Quick Pick is a sleek and nimble dagger, favored by rogues and swift-handed warriors for its agility and precision. Crafted from lightweight steel, its blade is honed to a razor-sharp edge, capable of swift strikes and deft maneuvers in close-quarters combat.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/b/b8/Greedy_Pickaxe_full.jpg/revision/latest/scale-to-width-down/250?cb=20171212063638')
        embed.add_field(name="Favoured Classes", value="Rogue, Warrior, Monk", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)

    @info.command(aliases=['16', 'Mithril_Rod'])
    async def mithril_rod(self,ctx):
        embed = discord.Embed(title="Mithril Rod", description = "The Mithril Rod is a marvel of craftsmanship and arcane mastery, forged from the rare and resilient metal known as mithril. Standing tall and elegant, it serves as both a symbol of authority and a potent conduit for magical energies.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/2/2e/Runed_Mithril_Rod_full.jpg/revision/latest/scale-to-width-down/250?cb=20230323095559')
        embed.add_field(name="Favoured Classes", value="Rogue, Warrior, Monk", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus\n40+ **Intelligence** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['17', 'Thundering_Hammer'])
    async def thundering_hammer(self,ctx):
        embed = discord.Embed(title="Thunderin Hammer", description = "The Thundering Hammer is a formidable weapon forged in the heart of mighty thunderstorms by skilled dwarven blacksmiths. Crafted from the finest ores and infused with the essence of thunder itself, this imposing two-handed hammer resonates with raw power.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ed13c911-551e-4abc-8ec3-bf52aae1ec95/dhb4vw8-b80c5043-ee6f-44aa-8115-8bd883a58ba2.jpg/v1/fill/w_1024,h_1024,q_75,strp/hearthstone___tempest_hammer_by_avarond_dhb4vw8-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcL2VkMTNjOTExLTU1MWUtNGFiYy04ZWMzLWJmNTJhYWUxZWM5NVwvZGhiNHZ3OC1iODBjNTA0My1lZTZmLTQ0YWEtODExNS04YmQ4ODNhNThiYTIuanBnIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.2WwBKS3IOKXGpoFZ7avXDGI2AjvqcM8v28VZ0JVmAR8')
        embed.add_field(name="Favoured Classes", value="Shaman, Monk", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="50+ **Attack** Bonus\n20+ **Strength** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['18', 'Starsung_Bow'])
    async def starsung_bow(self,ctx):
        embed = discord.Embed(title="Starsung Bow", description = "The Starsung Bow is a masterpiece crafted by elven archers under the light of a thousand stars. Fashioned from the rarest materials found deep within enchanted forests, this bow is renowned for its exquisite craftsmanship and magical properties.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/6/6d/Starstrung_Bow_full.jpg/revision/latest/scale-to-width-down/250?cb=20230804154926')
        embed.add_field(name="Favoured Classes", value="Hunter, Demon Hunter", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Attack", value="40+ **Attack** Bonus\n30+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['19', 'Incanters_Flow'])
    async def incanters_flow(self,ctx):
        embed = discord.Embed(title="Incanters Flow", description = "The Incanters Flow is a rare and mystical tome sought after by wizards and scholars alike for its profound knowledge and arcane secrets. Bound in supple, enchanted leather that seems to shimmer with its own inner light, this ancient book holds untold wisdom and power within its pages. ", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIgxwgIt2Rbn1wUeQ_U2oATEG4hRPrBkPn8w&s')
        embed.add_field(name="Favoured Classes", value="Mage, Priest, Warlock", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Attack", value="40+ **Attack** Bonus\n30+ **Intelligence** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['20', 'Goblins_Gold'])
    async def goblins_gold(self,ctx):
        embed = discord.Embed(title="Goblins Gold", description = "Goblin's Gold is a rare and coveted item, forged deep within the labyrinthine caves of the Goblin Kingdom. Crafted from a mysterious alloy that glints with an otherworldly sheen, this weapon is prized not only for its lustre but also for the supernatural properties imbued by goblin shamans during its creation.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://admin.esports.gg/wp-content/uploads/2022/08/Hearthstone-Runestones-1568x845.jpg')
        embed.add_field(name="Favoured Classes", value="Shaman, Hunter, Rogue", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Attack", value="30+ **Attack** Bonus\n30+ **Strength** Bonus\n10+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)
        
    @info.command(aliases=['21', 'Necrium_Blade'])
    async def necrium_blade(self,ctx):
        embed = discord.Embed(title="Necrium Blade", description = "The Necrium Blade is a rare and sinister dagger, forged in the depths of ancient crypts by necromancers who sought to harness the power of death itself. The blade exudes a dark aura, whispering secrets of the afterlife to those who dare to wield it.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://hearthstone.wiki.gg/images/thumb/4/46/Necrium_Blade_full.jpg/375px-Necrium_Blade_full.jpg')
        embed.add_field(name="Favoured Classes", value="Mage, Warlock, Rogue", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n10+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['22', 'Tainted_Fork'])
    async def tainted_fork(self,ctx):
        embed = discord.Embed(title="Tainted Fork", description = "The Tainted Fork is a rare and enigmatic weapon, often found in the hands of assassins and shadowy figures who lurk in the dark alleys of bustling cities. Its sinister reputation is well-deserved, as the weapon's design and purpose are steeped in treachery and malevolence.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/6/6e/Fork_full.jpg/revision/latest?cb=20160815132056')
        embed.add_field(name="Favoured Classes", value="Hunter, Monk, Priest, Warrior", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="40+ **Attack** Bonus\n20+ **Strength** Bonus\n10+ **Intelligence** Bonus", inline=False)
        await ctx.send(embed=embed)
    
    @info.command(aliases=['23', 'Dragon_Spear'])
    async def dragon_spear(self,ctx):
        embed = discord.Embed(title="Dragon Spear", description = "The Dragon Spear is a rare and majestic weapon, revered by warriors who seek to channel the power and might of dragons in their battles. This spear is not just a tool of war but a symbol of honor, strength, and mythical prowess.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/d/d8/Rare_Spear_full.jpg/revision/latest/scale-to-width-down/443?cb=20160502091420')
        embed.add_field(name="Favoured Classes", value="Hunter, Monk, Demon Hunter", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="50+ **Attack** Bonus\n20+ **HP** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['24', 'Arcanite_Ripper'])
    async def arcanite_ripper(self,ctx):
        embed = discord.Embed(title="Arcanite Ripper", description = "The Arcanite Ripper is a rare and formidable weapon, favored by those who seek to blend brute strength with arcane power. This two-handed axe is not only a tool of destruction but also a conduit for powerful magical energies, making it a prized possession for any warrior or spellcaster.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/f/fc/Arcanite_Ripper_full.jpg/revision/latest/scale-to-width-down/250?cb=20230407091115')
        embed.add_field(name="Favoured Classes", value="Warrior, Demon Hunter, Hunter", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="50+ **Attack** Bonus\n20+ **Strength** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['25', 'Spectral_Cutlass'])
    async def spectral_cutlass(self,ctx):
        embed = discord.Embed(title="Spectral Cutlass", description = "The Spectral Cutlass is a rare weapon, famed for its ethereal beauty and otherworldly power. This elegant dagger is favored by agile warriors and daring adventurers who seek to strike with both precision and supernatural force. Its sleek design and spectral attributes make it a unique and valuable addition to any armory.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/8/8a/Spectral_Cutlass_full.jpg/revision/latest/scale-to-width-down/250?cb=20180412172337')
        embed.add_field(name="Favoured Classes", value="Warrior, Demon Hunter, Hunter", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="30+ **Attack** Bonus\n10+ **Strength** Bonus\n20+ **Intelligence** Bonus\n10+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['26', 'Runed_Shortsword'])
    async def runed_shortsword(self,ctx):
        embed = discord.Embed(title="Runed Shortsword", description = "The Runed Shortsword is a rare weapon, prized for its compact size, elegant design, and the intricate runes that adorn its blade. This weapon is favored by warriors and adventurers who value agility, precision, and the added mystical properties that the runes bestow.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/c/c9/Runic_Shortsword_full.jpg/revision/latest/scale-to-width-down/250?cb=20230801225840')
        embed.add_field(name="Favoured Classes", value="Paladin, Priest, Warlock", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="30+ **Attack** Bonus\n40+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['27', 'Calamity_Grasp'])
    async def calamity_grasp(self,ctx):
        embed = discord.Embed(title="Calamity Grasp", description = "The Calamity Grasp is a rare weapon renowned for its brutal efficiency and intimidating design. This claw weapon is favored by those who prefer close-quarters combat and the ability to unleash swift, devastating attacks.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://hearthstone.wiki.gg/images/thumb/9/9c/Calamity%27s_Grasp_full.jpg/375px-Calamity%27s_Grasp_full.jpg')
        embed.add_field(name="Favoured Classes", value="Demon Hunter, Monk, Rogue, Warrior", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="30+ **Attack** Bonus\n40+ **HP** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['28', 'Boundless_Glaive'])
    async def boundless_glaive(self,ctx):
        embed = discord.Embed(title="Boundless Glaive", description = "The Boundless Glaive is a rare and formidable weapon known for its exceptional reach and unparalleled versatility. This weapon is favored by warriors who value agility, precision, and the ability to control the battlefield from a distance.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/8/85/Warden%27s_Glaive_full.jpg/revision/latest/scale-to-width-down/400?cb=20210801095635')
        embed.add_field(name="Favoured Classes", value="Demon Hunter, Monk, Hunter", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n10+ **Strength** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['29', 'Runic_Axe'])
    async def runic_axe(self,ctx):
        embed = discord.Embed(title="Runic Axe", description = "The Runic Axe is a rare and powerful weapon, revered by those who appreciate the blend of raw physical strength and ancient mystical power. Forged by master blacksmiths, this axe is not just a tool of destruction but also a conduit for arcane energies.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/d/d6/Runic_Axe_full.jpg/revision/latest/scale-to-width-down/250?cb=20230801225936')
        embed.add_field(name="Favoured Classes", value="Warrior, Hunter, Paladin", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="50+ **Attack** Bonus\n20+ **Strength** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['30', 'Tolins_Goblet'])
    async def tolins_goblet(self,ctx):
        embed = discord.Embed(title="Tolins Goblet", description = "Tolin's Goblet is an enigmatic and mystical weapon, shrouded in ancient lore and arcane power. Once belonging to the legendary sorcerer Tolin, this goblet is more than a simple drinking vessel—it is a conduit for dark magic and forbidden rituals.", color = 0x44b3ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/1/18/Tolin%27s_Goblet_full.jpg/revision/latest/scale-to-width-down/400?cb=20171107002115')
        embed.add_field(name="Favoured Classes", value="Mage, Priest, Rogue", inline=False)
        embed.add_field(name="Rarity", value="Rare", inline=False)
        embed.add_field(name="Stats", value="40+ **Attack** Bonus\n20+ **Intelligence** Bonus\n10+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['31', 'Swinetusk_Shank'])
    async def swinetusk_shank(self,ctx):
        embed = discord.Embed(title="Swinetusk Shank", description = "The Swinetusk Shank rests in its scabbard at his side, a weapon of legend among pirates and adventurers alike. Its blade, forged from a rare metal known for its resilience and shimmering with an otherworldly sheen, is etched with intricate symbols that tell tales of ancient seas and forgotten treasures.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/e/ea/Swinetusk_Shank_full.jpg/revision/latest/scale-to-width-down/250?cb=20210330200550')
        embed.add_field(name="Favoured Classes", value="Rogue", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a rogue class, speed is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n20+ **Intelligence** Bonus\n40+ **HP** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['32', 'Super_Collider'])
    async def super_collider(self,ctx):
        embed = discord.Embed(title="Super Collider", description = "The Super Collider is a large-scale particle accelerator used in high-energy physics to accelerate and collide particles at nearly the speed of light. It's designed to study the fundamental properties of matter and the forces that govern them by smashing particles together under controlled conditions. ", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/1/18/Supercollider_full.jpg/revision/latest/scale-to-width-down/250?cb=20180807185646')
        embed.add_field(name="Favoured Classes", value="Warrior", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a warrior class, strength is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="80+ **Attack** Bonus\n40+ **Strength** Bonus", inline=False)
        await ctx.send(embed=embed)


    @info.command(aliases=['33', 'Trueaim_Crescent'])
    async def trueaim_crescent(self,ctx):
        embed = discord.Embed(title="Trueaim Crescent", description = "Each arrow drawn from its quiver feels weightless yet potent, as if guided by unseen forces toward its target. The bowstring hums with a harmonic resonance, resonating with the user's intent to strike true. Legends speak of its ability to pierce through the thickest armor and strike at the heart of even the most elusive prey.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/4/45/Trueaim_Crescent_full.jpg/revision/latest?cb=20200815044030')
        embed.add_field(name="Favoured Classes", value=" Demon Hunter", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a  Demon Hunter class, attack is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="70+ **Attack** Bonus\n50+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['34', 'Cog_Hammer', 'cog_hammer'])
    async def cg_hammer(self,ctx):
        embed = discord.Embed(title="Cog Hammer", description = "Each swing of the Cog Hammer resonates with the force of a thousand gears turning, delivering bone-crushing blows capable of sundering armor and rending through defenses. Its handle is wrapped in supple leather, providing a firm grip that allows its wielder to channel their might with precise control.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/9/9b/Coghammer_full.jpg/revision/latest/scale-to-width-down/250?cb=20150917205646')
        embed.add_field(name="Favoured Classes", value="Hunter", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a Hunter class, speed is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="80+ **Attack** Bonus\n20+ **Strength** Bonus\n20+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['35', 'Primal_Staff'])
    async def primal_staff(self,ctx):
        embed = discord.Embed(title="Primal Staff", description = "Carved from the heartwood of the oldest trees in the mystical forests, the Primal Staff is a majestic artifact that radiates with the essence of nature itself. Its length is adorned with intricate runes that shimmer faintly with verdant energy, marking it as a conduit between the mortal realm and the primal forces that shape it.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/4/4e/Staff_of_the_Primus_full.jpg/revision/latest/scale-to-width-down/250?cb=20230803153655')
        embed.add_field(name="Favoured Classes", value="Mage", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a Mage class, intelligence is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n60+ **Intelligence** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['36', 'Felstring_Harp'])
    async def felstring_harp(self,ctx):
        embed = discord.Embed(title="Felstring Harp", description = "Crafted from the blackened wood of ancient trees found deep within cursed forests, the Felstring Harp is a harrowing instrument that resonates with a melancholic melody. Its strings, made from the sinew of demonic creatures, emit an eerie hum that echoes through the shadows, captivating listeners with its haunting allure.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/e/e2/Felstring_Harp_full.jpg/revision/latest/scale-to-width-down/250?cb=20230407091336')
        embed.add_field(name="Favoured Classes", value="Warlock", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a Warlock class, HP is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n60+ **HP** Bonus", inline=False)
        await ctx.send(embed=embed)
    
    @info.command(aliases=['37', 'Argent_Lance'])
    async def argent_lance(self,ctx):
        embed = discord.Embed(title="Argent Lance", description = "Forged from gleaming silver mined from the depths of sacred mountains, the Argent Lance is a symbol of valor and purity. Its shaft, polished to a brilliant shine, bears intricate engravings depicting tales of heroic deeds and noble lineage. At its tip, a sharp blade gleams with a silvery light, honed to pierce through the thickest armor with precision.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/0/08/Flame_Lance_full.jpg/revision/latest/scale-to-width-down/449?cb=20230323095147')
        embed.add_field(name="Favoured Classes", value="Paladin", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a Paladin class, strength is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n30+ **Strength** Bonus\n30+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['38', 'Azsharan_Trident'])
    async def azsharan_trident(self,ctx):
        embed = discord.Embed(title="Azsharan Trident", description = "Crafted from coral-encrusted steel and shimmering with an iridescent glow, the Azsharan Trident is a formidable weapon that resonates with the magic of the ocean depths. Its three-pronged head, adorned with runes of water and currents, channels the elemental forces of the sea.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/f/f9/Azsharan_Trident_full.jpg/revision/latest/scale-to-width-down/250?cb=20220408133537')
        embed.add_field(name="Favoured Classes", value="Shaman", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a Shaman class, intelligence is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n20+ **Strength** Bonus\n40+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['39', 'Ceremonial_Maul'])
    async def ceremonial_maul(self,ctx):
        embed = discord.Embed(title="Ceremonial Maul", description = "Forged from the finest metals and blessed by spiritual leaders, the ceremonial maul is a symbol of authority and reverence. Its massive head, adorned with intricate carvings and symbols of ancient significance, reflects the craftsmanship of skilled artisans who imbued it with spiritual power.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/7/79/Ceremonial_Maul_full.jpg/revision/latest/scale-to-width-down/250?cb=20200815061616')
        embed.add_field(name="Favoured Classes", value="Monk", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a Monk class, attack is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n20+ **Strength** Bonus\n40+ **HP** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['40', 'Obsidian_Shard'])
    async def obsidian_shard(self,ctx):
        embed = discord.Embed(title="Obsidian Shard", description = "An obsidian shard is a sharp and ancient piece of volcanic glass with many uses. Formed from rapidly cooling lava, obsidian is known for its sharpness, making it effective for tools, weapons, and ritual objects.", color = 0x8d00ff)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/1/12/Obsidian_Shard_full.jpg/revision/latest?cb=20170404194543')
        embed.add_field(name="Favoured Classes", value="Priest", inline=False)
        embed.add_field(name="Passive", value="If this weapon is equipped on a Priest class, HP is increased by 20%", inline=False)
        embed.add_field(name="Rarity", value="Epic", inline=False)
        embed.add_field(name="Stats", value="60+ **Attack** Bonus\n40+ **Intelligence** Bonus\n20+ **Speed** Bonus", inline=False)
        await ctx.send(embed=embed)


#Dwarven

    @info.command(aliases=['51', 'Blazing_Shield'])
    async def blazing_shield(self,ctx):
        embed = discord.Embed(title="Blazing Shield", description = "A formidable defensive tool forged in the heart of a raging volcano. It emanates a constant, searing heat that scorches any who dare to come too close. Its surface glows with an intense, fiery hue, and intricate runes etched into its core pulse with a rhythmic light, suggesting a deep, untapped power within.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://pbs.twimg.com/media/EFAYY1CW4AEA8_s.jpg')
        embed.add_field(name="Favoured Classes", value="Warrior, Demon Hunter, Hunter, Shaman", inline=False)
        embed.add_field(name="Rarity", value="COmmon", inline=False)
        embed.add_field(name="Stats", value="40+ **Defense** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['52', 'Spiked_Shield'])
    async def spiked_shield(self,ctx):
        embed = discord.Embed(title="Spiked Shield", description = "A brutal and imposing defensive armament designed for both protection and offense. Crafted from the toughest iron and reinforced with layers of hardened steel, its surface is studded with razor-sharp spikes that jut out menacingly.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://i.pinimg.com/474x/c0/e1/63/c0e163c03663e17b7ebf5b1dd9bef885.jpg')
        embed.add_field(name="Favoured Classes", value="Warrior, Warlock, Hunter, Paladin", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="10+ **Attack** Bonus\n20+ **Defense** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['53', 'Crackling_Shield'])
    async def crackling_shield(self,ctx):
        embed = discord.Embed(title="Crackling Shield", description = "An extraordinary defensive tool, shimmering with arcane energy. Crafted from rare, enchanted metals and inscribed with runes of protection, the shield crackles with vibrant electrical currents. When held, the shield emits a faint hum and occasional sparks, signaling its readiness to absorb and deflect attacks", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://i.pinimg.com/originals/17/38/7f/17387f1ee0c2c8ec6c66051f7ca83e57.png')
        embed.add_field(name="Favoured Classes", value="Paladin, Mage, Monk, Priest", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="40+ **Defense** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['54', 'Wooden_Wheel'])
    async def wooden_wheel(self,ctx):
        embed = discord.Embed(title="Wooden Wheel", description = "A rugged and unconventional weapon, crafted from sturdy oak and fitted with sharp, protruding spikes. Its circular form and balanced weight make it easy to wield, either by rolling it towards adversaries or using it as a melee weapon.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/9/92/Spiked_Wheel_full.jpg/revision/latest?cb=20210127150031')
        embed.add_field(name="Favoured Classes", value="Rogue, Warrior, Monk, Shaman", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="10+ **Attack** Bonus\n20+ **Defense** Bonus", inline=False)
        await ctx.send(embed=embed)

    @info.command(aliases=['55', 'Amethyst_Dagger'])
    async def amethyst_dagger(self,ctx):
        embed = discord.Embed(title="Amethyst Dagger", description = "An exquisite weapon of stealth and precision, forged from rare amethyst gemstones and fine steel. Its blade, crafted with meticulous care, shimmers with a deep purple hue, reflecting the mesmerizing beauty of its namesake gem.", color = 0xd3d4f3)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_image(url = 'https://static.wikia.nocookie.net/hearthstone_gamepedia/images/0/04/Mindspike_full.jpg/revision/latest?cb=20210414193224')
        embed.add_field(name="Favoured Classes", value="Rogue, Demon Hunter", inline=False)
        embed.add_field(name="Rarity", value="Common", inline=False)
        embed.add_field(name="Stats", value="20+ **Attack** Bonus")
        await ctx.send(embed=embed)
    

async def setup(client):
    await client.add_cog(info(client))