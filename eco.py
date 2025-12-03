import discord
from discord.ext import commands
import asyncio
import sqlite3
import random
import datetime


# Define a dropdown menu for class selection
class ClassDropdown(discord.ui.Select):
    def __init__(self, user_id):
        self.user_id = user_id
        options = [
            discord.SelectOption(label="Demon Hunter", description="Agile and masters of ranged and close combat", emoji="<:demon_hunter:1255872124195704975> "),
            discord.SelectOption(label="Hunter", description="Skilled marksmen utilising guns, bows and beasts", emoji="<:hunter:1255872272988770346> "),
            discord.SelectOption(label="Mage", description="Masters of arcane, frost and fire magic ", emoji="<:wiz:1255872379918352384> "),
            discord.SelectOption(label="Monk", description="Spiritual close combat fighters harnessing inner focus", emoji="<:Death_Knight:1255873191373701241> "),
            discord.SelectOption(label="Paladin", description="Holy warriors that can heal and smite", emoji="<:Paladin:1255872513423048716> "),
            discord.SelectOption(label="Priest", description="Healers and the resurrectors of the light and dark", emoji="<:priest:1255872554631958729> "),
            discord.SelectOption(label="Rogue", description="Stealthy assassins and the master of trickery", emoji="<:Rogue:1255872600987664396> "),
            discord.SelectOption(label="Shaman", description="Elemental spellcasters while also using spirits", emoji="<:shaman:1255872632092495933> "),
            discord.SelectOption(label="Warlock", description="Dark spellcasters utilising demons and fel magic", emoji="<:warlock:1255872668675215380> "),
            discord.SelectOption(label="Warrior", description="Champions of valor, equipped with heavy armor", emoji="<:warrior:1255872722551050323> "),
        ]
        super().__init__(placeholder="Choose your Class..", min_values=1, max_values=1, options=options)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return
        selected_class = self.values[0]
        embed = discord.Embed(title=f"{selected_class} Class Selected", color=0x0a0a0a)
        
        if selected_class == "Demon Hunter":
            embed.description = "Demon Hunters are agile warriors who have sacrificed part of their humanity to obtain demonic powers. They excel in both melee and ranged combat, wielding dual blades with deadly precision. Their abilities revolve around agility, acrobatics, and harnessing the corrupting energies of the Burning Legion to combat demons and other supernatural foes."
            embed.set_image(url="https://e0.pxfuel.com/wallpapers/42/864/desktop-wallpaper-demon-hunter-world-of-warcraft-demon-hunter.jpg")
            embed.add_field(name="Skills <:demon_hunter:1255872124195704975>", value="**1. Fel Rush**: Charge forward, damaging enemies in your path\n **2. Chaos Strike**: Unleash a flurry of attacks, dealing massive damage in an area\n **3. Blur**: Evasion ability that reduces incoming damage")
        elif selected_class == "Hunter":
            embed.description = "Hunters are skilled marksmen and survivalists, adept at ranged combat and accompanied by loyal animal companions. They excel in tracking their prey across the wilderness, utilizing bows, guns, and traps to gain the upper hand in battle. Hunters are also known for their affinity with nature and their ability to tame and command various beasts to aid them in their adventures."
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/989/1022/519/hearthstone-podcast-rogue-hunter-wallpaper-preview.jpg")
            embed.add_field(name="Skills <:hunter:1255872272988770346>", value="**1. Steady Shot**: A precise shot with increased focus\n **2. Kill Command**: Deal damage to an enemy with increasing power if you control a beast\n **3. Multishot**: Fire several shots at enemies in an area")
        elif selected_class == "Mage":
            embed.description = "Mages are powerful wielders of arcane magic, mastering spells that manipulate reality and harnessing the energies of the elements. They are intellectuals and scholars who delve into ancient mysteries to expand their magical prowess. Mages excel in both offensive and defensive magic, making them formidable adversaries and valuable allies in any battle."
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/279/841/109/hearthstone-heroes-of-warcraft-video-games-fantasy-art-medivh-wallpaper-preview.jpg")
            embed.add_field(name="Skills <:wiz:1255872379918352384>", value="**1. Arcane Missiles**: Launch a barrage of arcane missiles at your opponents\n **2. Fireball**: Toss a ball of fire at your opponent doing massive damage\n **3. Frostbolt**: Fire a bolt of ice at your opponent and freeze them")
        elif selected_class == "Monk":
            embed.description = "Monks are disciplined martial artists who harness inner strength and agility to overcome their foes. They blend physical prowess with spiritual enlightenment, mastering various martial arts techniques and ancient traditions. Monks are versatile combatants, capable of swift movements and powerful strikes, making them formidable both in close-quarters combat and as supportive healers."
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/626/859/714/diablo-diablo-iii-monk-diablo-iii-wallpaper-preview.jpg")
            embed.add_field(name="Skills <:Death_Knight:1255873191373701241>", value="**1. Tiger Palm**: Strike with your palm, damage increases after each consecutive hit upto 3 times\n **2. Chi Wave**: Send a chi wave, healing allies and damaging enemies\n **3. Jab**: Quick attack which also restores energy")
        elif selected_class == "Paladin":
            embed.description = "Paladins are holy warriors dedicated to the protection of their allies and the pursuit of justice. Clad in heavy armor and wielding the power of the Light, they serve as beacons of hope on the battlefield. Paladins excel in both defensive and offensive capabilities, combining powerful melee attacks with potent healing magic to uphold righteousness and vanquish evil."
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/281/1000/932/jsyyy-drawing-league-of-legends-leona-league-of-legends-women-hd-wallpaper-preview.jpg")
            embed.add_field(name="Skills <:Paladin:1255872513423048716>", value="**1. Crusader Strike**: Strike with your your weapon enchanted in holy light\n **2. Divine Light**: Envelop urself in divine shield, healing you by half your hp\n **3. Avenging Wrath**: Enter a state of righteousness, increasing damage dealt")
        elif selected_class == "Priest":
            embed.description = "Priests are devout spiritual leaders who wield powerful divine magic to heal wounds, restore minds, and protect their allies. They are adept at channeling holy energies to bolster their allies' defenses and vanquish foes with potent spells. Priests are also known for their ability to inspire hope and provide guidance, making them invaluable in both battle and times of need."
            embed.set_image(url="https://staticg.sportskeeda.com/editor/2019/02/dac48-15511124847128-800.jpg")
            embed.add_field(name="Skills <:priest:1255872554631958729>", value="**1. Mind Blast**: Deal shadow damage to your opponent\n **2. Serenity**: Restore health based on your energy\n **3. Shadow Visions**: Deal shadow damage entrapping your opponent")
        elif selected_class == "Rogue":
            embed.description = "Rogues are stealthy and cunning operatives who excel in subterfuge, espionage, and deadly combat techniques. They are masters of deception and surprise, using their agility and quick reflexes to strike swiftly and vanish into the shadows before their enemies can react. Rogues are proficient in both melee and ranged combat, employing poisons, traps, and precise strikes to gain the upper hand in any encounter."
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/242/613/289/video-games-hearthstone-warcraft-digital-art-wallpaper-preview.jpg")
            embed.add_field(name="Skills <:Rogue:1255872600987664396>", value="**1. Vanish**: Enter stealth form, making you unable to be seen\n **2. Eviscerate**: Strike with a single weapon to deal damage, use double weapons for double damage\n **3. Shadowstep**: Teleport behind your opponent and stab them in the back")
        elif selected_class == "Shaman":
            embed.description = "Shamans are spiritual practitioners who commune with the elements to wield powerful magic and protect their allies. They have a deep connection to nature and the elemental forces, allowing them to call upon the spirits of earth, fire, water, and air to aid them in battle. Shamans are versatile spellcasters, capable of both healing and dealing damage, and they play a pivotal role in maintaining balance and harmony in the world."
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/454/654/529/warcraft-hearthstone-heroes-of-warcraft-wallpaper-thumb.jpg")
            embed.add_field(name="Skills <:shaman:1255872632092495933>", value="**1. Lightning Bolt**: Electrocute your foes with lightning\n **2. Flameburst**: Scorch enemies in an area\n **3. Earthen Totem**: Summon a totem that slows down opponents")
        elif selected_class == "Warlock":
            embed.description = "Warlocks are dark spellcasters who harness fel magic and summon demonic minions to do their bidding. They delve into forbidden arts to gain power, striking pacts with demonic entities for knowledge and strength. Warlocks are masters of curses, shadow magic, and destructive spells, wielding their dark powers to afflict enemies, drain life force, and manipulate the fabric of reality itself."
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/852/576/1013/artwork-guldan-hearthstone-heroes-of-warcraft-video-games-wallpaper-thumb.jpg")
            embed.add_field(name="Skills <:warlock:1255872668675215380>", value="**1. Hellfire**: Summon the flames of hell to deal damage in all directions\n **2. Shadow Bolt**: Deal shadow damage to an enemy\n **3. Curse of Agony**: Curse your opponent, they take exponentially more damage with each curse")
        elif selected_class == "Warrior":
            embed.description = "Warriors are stalwart and courageous fighters clad in heavy armor, wielding a variety of weapons to engage enemies in close combat. They are masters of battle tactics and relentless in their pursuit of victory. Warriors excel in both offense and defense, using their strength, skill, and resilience to protect their allies and cleave through their foes with devastating attacks."
            embed.set_image(url="https://images5.alphacoders.com/104/thumb-1920-1040146.jpg")
            embed.add_field(name="Skills <:warrior:1255872722551050323>", value="**1. Shield Slam**: Deal damage based on your armor\n **2. Heroic Strike**: Deal a mighty blow with your weapon\n **3. Whirlwind**: Deal damage in a huge area, striking multiple foes")


        view = ConfirmView(selected_class, user_id = interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)

# Define a confirm button to finalize class selection
class ConfirmView(discord.ui.View):
    def __init__(self, selected_class, user_id):
        super().__init__()
        self.selected_class = selected_class
        self.user_id=user_id
        self.add_item(ConfirmButton(selected_class, user_id))
        self.add_item(BackButton(user_id))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
            return interaction.user.id == self.user_id

class ConfirmButton(discord.ui.Button):
    def __init__(self, selected_class, user_id):
        super().__init__(label="Confirm", style=discord.ButtonStyle.green)
        self.selected_class = selected_class
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute("UPDATE eco SET class = ? WHERE user_id = ?", (self.selected_class, interaction.user.id))
        db.commit()
        cursor.close()
        db.close()
        await interaction.response.send_message(f"Congratulations champion.. You are now a {self.selected_class}", ephemeral=False)

class BackButton(discord.ui.Button):
    def __init__(self, user_id):
        super().__init__(label="Back to Classes", style=discord.ButtonStyle.blurple)
        self.user_id=user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return
        view = discord.ui.View()
        view.add_item(ClassDropdown(self.user_id))
        await interaction.response.edit_message(view=view)

# Define the main cog for economy commands
class main(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.daily_cooldown = {}

    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS eco (
            user_id INTEGER, wallet INTEGER, qcr INTEGER, zan TEXT, class TEXT, arm TEXT, guild TEXT
        )''')
        print("Economy loaded")
        db.commit()
        cursor.close()
        db.close()

    @commands.command()
    async def start(self, ctx):
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT user_id FROM eco WHERE user_id = ?", (ctx.author.id,))
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO eco(user_id, wallet, qcr, zan, class, arm, guild) VALUES(?, ?, ?, ?, ?, ?, ?)")
            val = (ctx.author.id, 100, 0, "Unidentified Weapon", None, "Unidentified Weapon", "Wandering Traveler")
            cursor.execute(sql, val)
            
            embed = discord.Embed(title="The Path that Lies ahead..", color=0x0a0a0a)
            embed.set_image(url="https://w.wallha.com/ws/14/CrDhFzSu.jpg")
            embed.add_field(name="Welcome to Ayame", value=("Inspired from the world of warcraft lore, re-imagine the games within the discord bot. We are very grateful for you to become part of our community"), inline=False)
            embed.add_field(name="Getting Started", value=("The decision is yours, the path you choose is solely in your hands. Start by choosing your class."), inline=False)
            embed.add_field(name="Death", value=("A warrior's sacrifice shall never go in vain. Check out `,info` to have a brief summary of the commands"), inline=False)
            embed.add_field(name="Class", value=("Choose a class from the below list, all have unique skills and equipment, no class is the best in comparison, so pick your liking. **ONCE YOU PICK A CLASS, IT CANNOT BE CHANGED AGAIN**."), inline=False)
            view = discord.ui.View()
            view.add_item(ClassDropdown(ctx.author.id))
            await ctx.send(embed=embed, view=view)
        else:
            await ctx.send("You have already started your journey, champion.")
        
        db.commit()
        cursor.close()
        db.close()

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT wallet, qcr, zan, class, arm, guild FROM eco WHERE user_id = ?", (member.id,))
        bal = cursor.fetchone()
        try:
            wallet = bal[0]
            formatted_wallet = "{:,}".format(wallet)
            qcr = bal[1]
            zan = bal[2]
            class_name = bal[3]
            arm = bal[4]
            guild_name = bal[5]
        except:
            wallet = 0
            formatted_wallet = 0
            qcr = 0
            zan = "None"
            class_name = "None"
            arm = "None"
            guild_name = "None"

        embed = discord.Embed(title=f"{member}'s Stash", color=0x0a0a0a, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Gold", value=f"{formatted_wallet}", inline=True)
        embed.add_field(name="Monstrous Essence", value=f"{qcr}", inline=True)
        embed.add_field(name="Rank", value="Coming Soon!", inline=False)
        embed.add_field(name="Guild", value=f"{guild_name}", inline=False)
        embed.add_field(name="Class", value=f"{class_name}", inline=False)
        embed.add_field(name="Weapon", value=f"{zan}", inline=True)
        embed.add_field(name="Off Hand", value=f"{arm}", inline=True)
        await ctx.send(embed=embed)
        
        db.commit()
        cursor.close()
        db.close()

    @commands.command()
    async def earn(self,ctx):
        member = ctx.author
        earnings = random.randint(1,5)
        
        db = sqlite3.connect("eco.sqlite")
        cursor=db.cursor()
        cursor.execute(f"SELECT wallet FROM eco WHERE user_id = {member.id}")
        wallet = cursor.fetchone()
        try:
            wallet = wallet[0]
        except:
            wallet = 0
        sql = ("UPDATE eco SET wallet = ? where user_id = ?")
        val = (wallet + int(earnings), member.id)
        cursor.execute(sql,val)
        await ctx.send("Ok")


        db.commit()
        cursor.close()
        db.close()



    @commands.command()
    async def blbuy(self, ctx, item_id):
        user_id = str(ctx.author.id)
        dbs = sqlite3.connect("shop.sqlite", timeout=50)
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        dbi = sqlite3.connect("inv.sqlite", timeout=50)
        shop_cursor = dbs.cursor()
        eco_cursor = dbe.cursor()
        inv_cursor = dbi.cursor()

        shop_cursor.execute("SELECT * FROM shop WHERE item_id = ?", (item_id,))
        item = shop_cursor.fetchone()
        if not item:
            await ctx.send("I can't seem to find the item u listed")
            return
        item_id, item_name, item_price, item_attack = item

        eco_cursor.execute('SELECT wallet FROM eco WHERE user_id=?', (user_id,))
        user_balance = eco_cursor.fetchone()[0]
        if user_balance < item_price:
            await ctx.send('You dont have enough gold to buy this item')
            return
        
        inv_cursor.execute("SELECT qty FROM inv WHERE user_id = ? AND item_name = ?", (user_id, item_name))
        existing_quantity = inv_cursor.fetchone()

        if existing_quantity:
            # If the item already exists, update the quantity
            new_quantity = existing_quantity[0] + 1
            inv_cursor.execute("UPDATE inv SET qty = ? WHERE user_id = ? AND item_name = ?", (new_quantity, user_id, item_name))
        else:
            # If the item is not in the inventory, insert a new record
            inv_cursor.execute("INSERT INTO inv (user_id, item_name, qty) VALUES (?, ?, 1)", (user_id, item_name))

        

    # Update user balance and log the purchase
        eco_cursor.execute('UPDATE eco SET wallet=wallet-? WHERE user_id=?', (item_price, user_id))
        dbe.commit()
        dbi.commit()
        dbi.close()
        dbe.close()
        dbs.close()

        await ctx.send(f'{ctx.author.display_name} bought {item_name} for {item_price} gold')




    @commands.command()
    async def dfbuy(self, ctx, item_id):
        user_id = str(ctx.author.id)
        dbs = sqlite3.connect("shop.sqlite", timeout=50)
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        dbi = sqlite3.connect("inv.sqlite", timeout=50)
        shop_cursor = dbs.cursor()
        eco_cursor = dbe.cursor()
        inv_cursor = dbi.cursor()

        shop_cursor.execute("SELECT * FROM df WHERE item_id = ?", (item_id,))
        item = shop_cursor.fetchone()
        if not item:
            await ctx.send("I can't seem to find the item u listed")
            return
        item_id, item_name, item_price, item_attack, item_defense = item

        eco_cursor.execute('SELECT wallet FROM eco WHERE user_id=?', (user_id,))
        user_balance = eco_cursor.fetchone()[0]
        if user_balance < item_price:
            await ctx.send('You dont have enough gold to buy this item')
            return
        
        inv_cursor.execute("SELECT qty FROM armor WHERE user_id = ? AND item_name = ?", (user_id, item_name))
        existing_quantity = inv_cursor.fetchone()

        if existing_quantity:
            # If the item already exists, update the quantity
            new_quantity = existing_quantity[0] + 1
            inv_cursor.execute("UPDATE armor SET qty = ? WHERE user_id = ? AND item_name = ?", (new_quantity, user_id, item_name))
        else:
            # If the item is not in the inventory, insert a new record
            inv_cursor.execute("INSERT INTO armor (user_id, item_name, qty) VALUES (?, ?, 1)", (user_id, item_name))

        

    # Update user balance and log the purchase
        eco_cursor.execute('UPDATE eco SET wallet=wallet-? WHERE user_id=?', (item_price, user_id))
        dbe.commit()
        dbi.commit()
        dbi.close()
        dbe.close()
        dbs.close()

        await ctx.send(f'{ctx.author.display_name} bought {item_name} for {item_price} gold')


    @commands.command()
    async def daily(self, ctx):
        user_id = ctx.author.id
        
        # Check if user has claimed their daily reward already today
        if user_id in self.daily_cooldown:
            last_claimed = self.daily_cooldown[user_id]
            delta = datetime.datetime.utcnow() - last_claimed
            remaining_time = datetime.timedelta(seconds=86400) - delta
            
            if delta < datetime.timedelta(seconds=86400):
                hours, remainder = divmod(remaining_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                await ctx.send(f"Tsk Tsk Tsk, You've already claimed your daily reward.. Try again in **{hours}** hours, **{minutes}** minutes, and **{seconds}** seconds.")
                return
        
        # Retrieve user's current wallet from the database
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()
        cursor.execute("SELECT wallet FROM eco WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        
        if result:
            current_wallet = result[0]
        else:
            current_wallet = 0
        
        # Define daily reward (example)
        daily_reward = random.randint(50, 200)
        
        # Calculate new wallet amount
        new_wallet = current_wallet + daily_reward
        
        # Update the database with new wallet amount
        cursor.execute("UPDATE eco SET wallet = ? WHERE user_id = ?", (new_wallet, user_id))
        db.commit()
        
        # Inform user about the reward
        await ctx.send(f"Here's your daily reward: **{daily_reward}** gold.\nTotal gold now: **{new_wallet}**")
        
        # Update last claimed time for the user
        self.daily_cooldown[user_id] = datetime.datetime.utcnow()
        
        cursor.close()
        db.close()



async def setup(client):
    await client.add_cog(main(client))