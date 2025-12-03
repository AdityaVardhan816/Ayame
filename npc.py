import discord
from discord.ext import commands
import sqlite3
import random
from discord.ui import Button, View
import asyncio

class NPCClassDropdown(discord.ui.Select):
    def __init__(self, user_id):
        self.user_id = user_id
        options = [
            discord.SelectOption(label="Illidari", description="Class: Demon Hunter", emoji="<:demon_hunter:1255872124195704975>"),
            discord.SelectOption(label="Elf", description="Class: Hunter", emoji="<:hunter:1255872272988770346>"),
            discord.SelectOption(label="Warden", description="Class: Mage", emoji="<:wiz:1255872379918352384>"),
            discord.SelectOption(label="Disciple", description="Class: Monk", emoji="<:Death_Knight:1255873191373701241>"),
            discord.SelectOption(label="Recruit", description="Class: Paladin", emoji="<:Paladin:1255872513423048716>"),
            discord.SelectOption(label="Cleric", description="Class: Priest", emoji="<:priest:1255872554631958729>"),
            discord.SelectOption(label="Thief", description="Class: Rogue", emoji="<:Rogue:1255872600987664396>"),
            discord.SelectOption(label="Goblin", description="Class: Shaman", emoji="<:shaman:1255872632092495933>"),
            discord.SelectOption(label="Imp", description="Class: Warlock", emoji="<:warlock:1255872668675215380>"),
            discord.SelectOption(label="Orc", description="Class: Warrior", emoji="<:warrior:1255872722551050323>"),
        ]
        super().__init__(placeholder="Choose the NPC Class..", min_values=1, max_values=1, options=options)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return
        selected_class = self.values[0]
        embed = discord.Embed(title=f"{selected_class} Selected", color=0x0a0a0a)

        if selected_class == "Illidari":
            embed.description = "Foolish mortal, you dare challenge the power of a Demon Hunter? I have sacrificed everything... what have you given?"
            embed.set_image(url="https://i.imgur.com/lAJXV1M.jpg")
            embed.add_field(name="Class", value="Demon Hunter", inline=False)
            embed.add_field(name="HP", value=100, inline=True)
            embed.add_field(name="Attack", value=40, inline=True)
            embed.add_field(name="Energy", value=60, inline=False)
            embed.add_field(name="Intelligence", value=20, inline=True)
            embed.add_field(name="Strength", value=30, inline=False)
            embed.add_field(name="Speed", value=60, inline=True)
            embed.add_field(name="Armor", value=10, inline=False)
            embed.add_field(name="Equipped Weapon", value="Fel Blades", inline=False)
            embed.add_field(name="Skills <:demon_hunter:1255872124195704975>", value="**1. Fel Rush** Charge forward, damaging enemies in your path\n **2. Chaos Strike** Unleash a flurry of attacks, dealing massive damage in an area\n **3. Blur** Evasion ability that reduces incoming damage")
        if selected_class == "Elf":
            embed.description = "I stand watch over the ancient forests, guardians of nature's balance. Our bowstrings hum with the whispers of the wind, our eyes keen as the hawk's gaze. We are hunters, attuned to the heartbeat of the wild, protectors of life's delicate harmony."
            embed.set_image(url="https://s1.1zoom.me/big3/539/422615-Kycb.jpg")
            embed.add_field(name="Class", value="Hunter", inline=False)
            embed.add_field(name="HP", value=120, inline=True)
            embed.add_field(name="Attack", value=50, inline=True)
            embed.add_field(name="Energy", value=70, inline=False)
            embed.add_field(name="Intelligence", value=30, inline=True)
            embed.add_field(name="Strength", value=40, inline=False)
            embed.add_field(name="Speed", value=70, inline=True)
            embed.add_field(name="Armor", value=20, inline=False)
            embed.add_field(name="Equipped Weapon", value="Hunting Bow", inline=False)
            embed.add_field(name="Skills <:hunter:1255872272988770346>", value="**1. Steady Shot** A precise shot with increased focus\n **2. Kill Command** Deal damage to an enemy with increasing power if you control a beast\n **3. Multishot** Fire several shots at enemies in an area")
        if selected_class == "Warden":
            embed.description = "We are the vigilant sentinels of justice, bound by oath to uphold order and safeguard the realms. Through the shadows we move, silent as the night, our blades keen and hearts steadfast. "
            embed.set_image(url="https://e1.pxfuel.com/desktop-wallpaper/488/520/desktop-wallpaper-fire-magic-dragon-elf-map-art-staff-wow-world-of-warcraft-guy-hearthstone-blackrock-mountain-the-dragon-s-breath-dragon-s-breath-section-%D0%B8%D0%B3%D1%80%D1%8B-fire-mage.jpg")
            embed.add_field(name="Class", value="Mage", inline=False)
            embed.add_field(name="HP", value=130, inline=True)
            embed.add_field(name="Attack", value=60, inline=True)
            embed.add_field(name="Energy", value=80, inline=False)
            embed.add_field(name="Intelligence", value=40, inline=True)
            embed.add_field(name="Strength", value=50, inline=False)
            embed.add_field(name="Speed", value=80, inline=True)
            embed.add_field(name="Armor", value=30, inline=False)
            embed.add_field(name="Equipped Weapon", value="Magic Wand", inline=False)
            embed.add_field(name="Skills <:wiz:1255872379918352384>", value="**1. Arcane Missiles** Launch a barrage of arcane missiles at your opponents\n **2. Fireball** Toss a ball of fire at your opponent doing massive damage\n **3. Frostbolt** Fire a bolt of ice at your opponent and freeze them")    
        if selected_class == "Disciple":
            embed.description = "Balance is found not in the strength of our fists, but in the serenity of our minds. Through discipline and harmony, we channel our energy to heal, to protect, and to strike with precision. Each step is a lesson, each breath a meditation on the path of enlightenment. "
            embed.set_image(url="https://wallpaper.forfun.com/fetch/72/7233056ef2832014d4b0aac27687fe64.jpeg")
            embed.add_field(name="Class", value="Monk", inline=False)
            embed.add_field(name="HP", value=140, inline=True)
            embed.add_field(name="Attack", value=70, inline=True)
            embed.add_field(name="Energy", value=90, inline=False)
            embed.add_field(name="Intelligence", value=50, inline=True)
            embed.add_field(name="Strength", value=60, inline=False)
            embed.add_field(name="Speed", value=90, inline=True)
            embed.add_field(name="Armor", value=40, inline=False)
            embed.add_field(name="Equipped Weapon", value="Death Spear", inline=False)
            embed.add_field(name="Skills <:Death_Knight:1255873191373701241>", value="**1. Tiger Palm** Strike with your palm, damage increases after each consecutive hit upto 3 times\n **2. Chi Wave** Send a chi wave, healing allies and damaging enemies\n **3. Jab** Quick attack which also restores energy")
        if selected_class == "Recruit":
            embed.description = "As a Silver Hand Recruit, I pledge my sword and shield to defend the innocent, uphold justice, and stand against the darkness that threatens our lands. With unwavering faith and valor, I march forward, ready to face any challenge that tests our resolve. "
            embed.set_image(url="https://cdna.artstation.com/p/assets/images/images/003/112/454/4k/andrew-theophilopoulos-andrewtheophilopoulos-hearthstone.jpg?1469813929")
            embed.add_field(name="Class", value="Paladin", inline=False)
            embed.add_field(name="HP", value=150, inline=True)
            embed.add_field(name="Attack", value=80, inline=True)
            embed.add_field(name="Energy", value=100, inline=False)
            embed.add_field(name="Intelligence", value=60, inline=True)
            embed.add_field(name="Strength", value=70, inline=False)
            embed.add_field(name="Speed", value=100, inline=True)
            embed.add_field(name="Armor", value=50, inline=False)
            embed.add_field(name="Equipped Weapon", value="Holy Hammer", inline=False)
            embed.add_field(name="Skills <:Paladin:1255872513423048716>", value="**1. Crusader Strike** Strike with your your weapon enchanted in holy light\n **2. Divine Light** Envelop urself in divine shield, healing you by half your hp\n **3. Avenging Wrath** Enter a state of righteousness, increasing damage dealt")
        if selected_class == "Cleric":
            embed.description = "As a Cleric devoted to the divine, I channel the light to heal the wounded, uplift the spirits of the weary, and dispel the shadows of doubt and fear. With prayers as my shield and faith as my strength, I stand ready to confront darkness wherever it may lurk."
            embed.set_image(url="https://admin.esports.gg/wp-content/uploads/2023/03/Hearthstone-new-Overheal-Keyword-Priest-Festival-of-Legends.jpg")
            embed.add_field(name="Class", value="Priest", inline=False)
            embed.add_field(name="HP", value=160, inline=True)
            embed.add_field(name="Attack", value=90, inline=True)
            embed.add_field(name="Energy", value=110, inline=False)
            embed.add_field(name="Intelligence", value=70, inline=True)
            embed.add_field(name="Strength", value=80, inline=False)
            embed.add_field(name="Speed", value=110, inline=True)
            embed.add_field(name="Armor", value=60, inline=False)
            embed.add_field(name="Equipped Weapon", value="Holy Ruins", inline=False)
            embed.add_field(name="Skills <:priest:1255872554631958729>", value="**1. Mind Blast**:Deal shadow damage to your opponent\n **2. Serenity**:Restore health based on your energy\n **3. Shadow Visions** Deal Shadow damage to your opponent, entrapping them")
        if selected_class == "Thief":
            embed.description = "In the shadows, I thrive. Swift and unseen, I am the whisper in the night, the master of deception. For every lock, there is a key; for every guard, a distraction. Wealth and secrets are my domain, and in the art of subterfuge, I am unparalleled."
            embed.set_image(url="https://cdnb.artstation.com/p/assets/images/images/016/931/345/large/jim-nelson-vendetta-candle.jpg?1554033990")
            embed.add_field(name="Class", value="Rogue", inline=False)
            embed.add_field(name="HP", value=170, inline=True)
            embed.add_field(name="Attack", value=100, inline=True)
            embed.add_field(name="Energy", value=120, inline=False)
            embed.add_field(name="Intelligence", value=80, inline=True)
            embed.add_field(name="Strength", value=90, inline=False)
            embed.add_field(name="Speed", value=120, inline=True)
            embed.add_field(name="Armor", value=60, inline=False)
            embed.add_field(name="Equipped Weapon", value="Tainted Daggers", inline=False)
            embed.add_field(name="Skills <:Rogue:1255872600987664396>", value="**1. Vanish** Enter stealth form, making you unable to be seen\n **2. Eviscerate** Strike with a single weapon to deal damage, use double weapons for double damage\n **3. Shadowstep** Teleport behind your opponent and stab them in the back")
        if selected_class == "Goblin":
            embed.description = "Ah, gold and gears, the heartbeat of innovation! In the crucible of commerce, I forge my destiny. From tinkering in the depths of Mechagon to wheeling and dealing in the bustling markets of Booty Bay, profit is my passion and invention my creed."
            embed.set_image(url="https://sm.ign.com/t/ign_in/articlepage/h/hearthstones-spectator-mode-will-launch-with-gobli/hearthstones-spectator-mode-will-launch-with-gobli_kkey.1280.jpg")
            embed.add_field(name="Class", value="Shaman", inline=False)
            embed.add_field(name="HP", value=180, inline=True)
            embed.add_field(name="Attack", value=110, inline=True)
            embed.add_field(name="Energy", value=130, inline=False)
            embed.add_field(name="Intelligence", value=90, inline=True)
            embed.add_field(name="Strength", value=100, inline=False)
            embed.add_field(name="Speed", value=130, inline=True)
            embed.add_field(name="Armor", value=60, inline=False)
            embed.add_field(name="Equipped Weapon", value="Thundering Orb", inline=False)
            embed.add_field(name="Skills <:shaman:1255872632092495933>", value="**1. Lightning Bolt** Electrocute your foes with lightning\n **2. Flameburst** Scorch enemies in an area\n **3. Earthen Totem** Summon a totem that slows down opponents")
        if selected_class == "Imp":
            embed.description = "Petty mortals, quiver before the fiery wrath of an Imp! I dance on the edge of chaos, reveling in the flames of my infernal might. With mischief as my cloak and fire as my sword, I weave curses and conjure chaos, leaving a trail of laughter and destruction in my wake."
            embed.set_image(url="https://i.pinimg.com/736x/a0/22/8a/a0228ae52dd5ad8ce81880202d9ed24f.jpg")
            embed.add_field(name="Class", value="Warlock", inline=False)
            embed.add_field(name="HP", value=190, inline=True)
            embed.add_field(name="Attack", value=120, inline=True)
            embed.add_field(name="Energy", value=140, inline=False)
            embed.add_field(name="Intelligence", value=100, inline=True)
            embed.add_field(name="Strength", value=110, inline=False)
            embed.add_field(name="Speed", value=140, inline=True)
            embed.add_field(name="Armor", value=60, inline=False)
            embed.add_field(name="Equipped Weapon", value="Infernal Claws", inline=False)
            embed.add_field(name="Skills <:warlock:1255872668675215380>", value="**1. Hellfire** Summon the flames of hell to deal damage in all directions\n **2. Shadow Bolt** Deal shadow damage to an enemy\n **3. Curse of Agony** Curse your opponent, they take exponentially more damage with each curse")
        if selected_class == "Orc":
            embed.description = "Honored by the spirits, forged in the fires of battle, I am an Orc, born of strength and honor. My veins surge with the blood of warriors, and my heart beats to the rhythm of war drums. With every swing of my axe, I carve a path through adversity."
            embed.set_image(url="https://imageio.forbes.com/blogs-images/insertcoin/files/2015/10/warsong1.jpg?format=jpg&height=600&width=1200&fit=bounds")
            embed.add_field(name="Class", value="Warrior", inline=False)
            embed.add_field(name="HP", value=200, inline=True)
            embed.add_field(name="Attack", value=130, inline=True)
            embed.add_field(name="Energy", value=150, inline=False)
            embed.add_field(name="Intelligence", value=110, inline=True)
            embed.add_field(name="Strength", value=120, inline=False)
            embed.add_field(name="Speed", value=150, inline=True)
            embed.add_field(name="Armor", value=60, inline=False)
            embed.add_field(name="Equipped Weapon", value="Fury Basher", inline=False)
            embed.add_field(name="Skills <:warrior:1255872722551050323>", value="**1. Shield Slam** Deal damage based on your armor\n **2. Heroic Strike** Deal a mighty blow with your weapon\n **3. Whirlwind** Deal damage in a huge area, striking multiple foes")

        view = NPCConfirmView(selected_class, user_id=interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=view)


class NPCConfirmView(discord.ui.View):
    def __init__(self, selected_class, user_id):
        super().__init__()
        self.selected_class = selected_class
        self.user_id = user_id
        self.add_item(NPCConfirmButton(selected_class, user_id))
        self.add_item(NPCBackButton(user_id))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

class NPCConfirmButton(discord.ui.Button):
    def __init__(self, selected_class, user_id):
        super().__init__(label="Confirm", style=discord.ButtonStyle.green)
        self.selected_class = selected_class
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return

        # Retrieve user's stats from the database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp, base_attack, energy, intelligence, speed, strength, armor FROM stats WHERE user_id=?", (self.user_id,))
        user_stats = c.fetchone()
        conn.close()
        

        if not user_stats:
            await interaction.response.send_message("User stats not found!", ephemeral=True)
            return

        user_hp, user_attack, user_energy, user_intelligence, user_speed, user_strength, user_armor = user_stats

        if self.selected_class == "Illidari":
            npc_hp = 100
            npc_attack = 40
            npc_energy = 60
            npc_intelligence = 20
            npc_strength = 30
            npc_speed = 60
            npc_armor = 10
        elif self.selected_class == "Elf":
            npc_hp = 120
            npc_attack = 50
            npc_energy = 70
            npc_intelligence = 30
            npc_strength = 40
            npc_speed = 70
            npc_armor = 20
        elif self.selected_class == "Warden":
            npc_hp = 130
            npc_attack = 60
            npc_energy = 80
            npc_intelligence = 40
            npc_strength = 50
            npc_speed = 80
            npc_armor = 30
        elif self.selected_class == "Disciple":
            npc_hp = 140
            npc_attack = 70
            npc_energy = 90
            npc_intelligence = 50
            npc_strength = 60
            npc_speed = 90
            npc_armor = 40
        elif self.selected_class == "Recruit":
            npc_hp = 150
            npc_attack = 80
            npc_energy = 100
            npc_intelligence = 60
            npc_strength = 70
            npc_speed = 100
            npc_armor = 50
        elif self.selected_class == "Cleric":
            npc_hp = 160
            npc_attack = 90
            npc_energy = 110
            npc_intelligence = 70
            npc_strength = 80
            npc_speed = 110
            npc_armor = 60
        elif self.selected_class == "Thief":
            npc_hp = 170
            npc_attack = 100
            npc_energy = 120
            npc_intelligence = 80
            npc_strength = 90
            npc_speed = 120
            npc_armor = 60
        elif self.selected_class == "Goblin":
            npc_hp = 180
            npc_attack = 110
            npc_energy = 130
            npc_intelligence = 90
            npc_strength = 100
            npc_speed = 130
            npc_armor = 60
        elif self.selected_class == "Imp":
            npc_hp = 190
            npc_attack = 120
            npc_energy = 140
            npc_intelligence = 100
            npc_strength = 110
            npc_speed = 140
            npc_armor = 60
        elif self.selected_class == "Orc":
            npc_hp = 200
            npc_attack = 130
            npc_energy = 150
            npc_intelligence = 110
            npc_strength = 120
            npc_speed = 150
            npc_armor = 70

        embed = discord.Embed(title="Duel Started!", color=0xffffff)
        embed.add_field(name=f"{interaction.user.display_name}", value=f"**HP**: {user_hp}\n\n**Attack**: {user_attack}\n\n**Energy**: {user_energy}\n\n**Intelligence**: {user_intelligence}\n\n**Speed**: {user_speed}\n\n**Strength**: {user_strength}\n\n**Armor**%: {user_armor}\n\n", inline=True)
        embed.add_field(name=f"{self.selected_class} NPC", value=f"**HP**: {npc_hp}\n\n**Attack**: {npc_attack}\n\n**Energy**: {npc_energy}\n\n**Intelligence**: {npc_intelligence}\n\n**Speed**: {npc_speed}\n\n**Strength**: {npc_strength}\n\n**Armor**%: {npc_armor}\n\n", inline=True)
        embed.set_image(url="https://images4.alphacoders.com/777/thumb-1920-777910.jpg")
        embed.set_footer(text="The match has begun, spectators! Sit back and relax and enjoy the view! Try not to get hit by any spells! ")
        view = DuelActionsView(user_id=interaction.user.id, npc_class=self.selected_class, user_hp=user_hp, npc_hp=npc_hp, user_energy=user_energy, npc_energy=npc_energy, original_message=None)
        message = await interaction.response.send_message(embed=embed, view=view)
        view.children[0].original_message = message
        await asyncio.sleep(1)
        await interaction.message.delete()
        

class NPCBackButton(discord.ui.Button):
    def __init__(self, user_id):
        super().__init__(label="Back to NPC Classes", style=discord.ButtonStyle.blurple)
        self.user_id = user_id


    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return
        view = discord.ui.View()
        view.add_item(NPCClassDropdown(self.user_id))
        await interaction.response.edit_message(view=view)

class DuelActionsView(discord.ui.View):
    def __init__(self, user_id, npc_class, user_hp, npc_hp, user_energy, npc_energy, original_message):
        super().__init__()
        self.user_id = user_id
        self.npc_class = npc_class
        self.user_hp = user_hp
        self.npc_hp = npc_hp
        self.user_energy = user_energy
        self.npc_energy = npc_energy

        self.add_item(DuelNormalAttackButton(user_id=user_id, npc_class=npc_class))
        self.add_item(DuelSkillsButton(user_id=user_id, npc_class=npc_class, original_message=original_message))
        self.add_item(DuelForfeitButton(user_id=user_id, npc_class=npc_class))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

class DuelNormalAttackButton(discord.ui.Button):
    def __init__(self, user_id, npc_class):
        super().__init__(label="Attack", style=discord.ButtonStyle.red)
        self.user_id = user_id
        self.npc_class = npc_class

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return

        # Retrieve user's attack value from the database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM tempstats WHERE user_id=?", (self.user_id,))
        self.user_hp = c.fetchone()[0]
        conn.close()

        # Retrieve user's attack value from the database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM npc WHERE npcname=?", (self.npc_class,))
        self.npc_hp = c.fetchone()[0]
        conn.close()

        # Retrieve user's attack value from the database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT base_attack FROM stats WHERE user_id=?", (self.user_id,))
        user_attack = c.fetchone()[0]
        conn.close()

        # Retrieve user's armor value from the database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT armor FROM stats WHERE user_id=?", (self.user_id,))
        user_armor = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT strength FROM stats WHERE user_id=?", (self.user_id,))
        user_strength = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT speed FROM stats WHERE user_id=?", (self.user_id,))
        user_speed = c.fetchone()[0]
        conn.close()

        if self.npc_class == "Illidari":
            npc_attack = 40
            npc_energy = 60
            npc_intelligence = 20
            npc_strength = 30
            npc_speed = 60
            npc_armor = 10
            diff = "Easiest"
        elif self.npc_class == "Elf":
            npc_attack = 50
            npc_energy = 70
            npc_intelligence = 30
            npc_strength = 40
            npc_speed = 70
            npc_armor = 20
            diff = "Easy"
        elif self.npc_class == "Warden":
            npc_attack = 60
            npc_energy = 80
            npc_intelligence = 40
            npc_strength = 50
            npc_speed = 80
            npc_armor = 30
            diff = "Easy"
        elif self.npc_class == "Disciple":
            npc_attack = 70
            npc_energy = 90
            npc_intelligence = 50
            npc_strength = 60
            npc_speed = 90
            npc_armor = 40
            diff = "Easy"
        elif self.npc_class == "Recruit":
            npc_attack = 80
            npc_energy = 100
            npc_intelligence = 60
            npc_strength = 70
            npc_speed = 100
            npc_armor = 50
            diff = "Medium"
        elif self.npc_class == "Cleric":
            npc_attack = 90
            npc_energy = 110
            npc_intelligence = 70
            npc_strength = 80
            npc_speed = 110
            npc_armor = 60
            diff = "Medium"
        elif self.npc_class == "Thief":
            npc_attack = 100
            npc_energy = 120
            npc_intelligence = 80
            npc_strength = 90
            npc_speed = 120
            npc_armor = 60
            diff = "Medium"
        elif self.npc_class == "Goblin":
            npc_attack = 110
            npc_energy = 130
            npc_intelligence = 90
            npc_strength = 100
            npc_speed = 130
            npc_armor = 60
            diff = "Hard"
        elif self.npc_class == "Imp":
            npc_attack = 120
            npc_energy = 140
            npc_intelligence = 100
            npc_strength = 110
            npc_speed = 140
            npc_armor = 60
            diff = "Hard"
        elif self.npc_class == "Orc":
            npc_attack = 130
            npc_energy = 150
            npc_intelligence = 110
            npc_strength = 120
            npc_speed = 150
            npc_armor = 70
            diff = "Hard"

        user_damage_min = ((user_attack - 30) - (npc_armor)) + (user_strength)*2 - 30
        user_damage_max = ((user_attack + 30) - (npc_armor)) + (user_strength)*2 - 30
        if user_damage_min < 0:
            user_damage_min = 0
        if user_damage_max < 0:
            user_damage_max = 10

        npc_damage_min = ((npc_attack - 20) - (user_armor)) + (npc_strength)*2 - 30
        npc_damage_max = ((npc_attack + 20) - (user_armor)) + (npc_strength)*2 - 30
        if npc_damage_min < 0:
            npc_damage_min = 0
        if npc_damage_max < 0:
            npc_damage_max = 10
        

        # Randomly pick damage values within the calculated ranges
        user_damage_dealt = random.randint(user_damage_min, user_damage_max)
        npc_damage_dealt = random.randint(npc_damage_min, npc_damage_max)

        # Update HP values after damage calculation
        self.user_hp -= npc_damage_dealt
        self.npc_hp -= user_damage_dealt

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.user_hp, self.user_id,))
        conn.commit()
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("UPDATE npc SET hp = ? WHERE npcname=?", (self.npc_hp, self.npc_class,))
        conn.commit()
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM stats WHERE user_id = ?", (self.user_id,))
        normal = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT npcname FROM npc WHERE npcname = ?", (self.npc_class,))
        npc_temp_class = c.fetchone()[0]
        conn.close()

        npc_def_stats = {
            "Illidari": (100,),
            "Elf": (120,),
            "Warden": (130,),
            "Disciple": (140,),
            "Recruit": (150,),
            "Cleric": (160,),
            "Thief": (170,),
            "Goblin": (180,),
            "Imp": (190,),
            "Orc": (200,)
        }

        npcnormal = npc_def_stats[npc_temp_class][0]

        img = ["https://wallpapers.com/images/hd/hearthstone-rastakhan-s-rumble-2560-x-1440-psz606u2cedv34ln.jpg","https://s1.1zoom.me/b5050/636/Hearthstone_Heroes_of_Warcraft_Battles_Dragons_529821_1366x768.jpg",
               "https://d1lss44hh2trtw.cloudfront.net/assets/article/2018/12/04/rastakhan-s-rumble-cinematic-still-7-png-jpgcopy_feature.jpg", "https://dotesports.com/wp-content/uploads/2018/11/24030406/Screenshot-140.png",
                "https://cdn.mos.cms.futurecdn.net/JgySFGeQcRRH3zf6QecaJM-1200-80.jpg", "https://dotesports.com/wp-content/uploads/2018/11/26075329/Screenshot-163.png" ]

        if npc_speed > user_speed:
            speed = f"{self.npc_class} is faster! They get to move first.."
        elif user_speed > npc_speed:
            speed = f"{interaction.user.display_name} is faster! They get to move first.."
        else:
            speed = f"Ladies and Gentlemen, its a speed tie!"

        clrs = [0x0a0a0a, 0x9fd2ff, 0xff5151, 0xffffff, 0xffdbaf]
        # Create embed with damage dealt and updated stats
        embed_damage = discord.Embed(title="Normal Attack - Damage Dealt", color=random.choice(clrs))
        embed_damage.add_field(name="", value=speed, inline=False)
        embed_damage.add_field(name=f"{interaction.user.display_name}'s Damage Dealt", value=f"{user_damage_dealt} HP", inline=True)
        embed_damage.add_field(name=f"{self.npc_class}'s Damage Dealt", value=f"{npc_damage_dealt} HP", inline=True)
        embed_damage.add_field(name="", value="", inline=False)
        embed_damage.add_field(name=f"{interaction.user.display_name}'s Remaining HP", value=f"{self.user_hp} HP", inline=True)
        embed_damage.add_field(name=f"{self.npc_class}'s Remaining HP", value=f"{self.npc_hp} HP", inline=True)
        embed_damage.set_image(url= random.choice(img))

        if self.user_hp <= 0 or self.npc_hp <= 0:
            embed_damage.add_field(name="Duel Ended", value="The duel has ended!", inline=False)
            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (normal, self.user_id,))
            conn.commit()
            conn.close()
            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("UPDATE npc SET hp = ? WHERE npcname=?", (npcnormal, self.npc_class,))
            conn.commit()
            conn.close()
            for item in self.view.children:
                    item.disabled = True

        if self.user_hp >= 0 and self.npc_hp < 0:
                eco_db = sqlite3.connect("eco.sqlite")
                eco = eco_db.cursor()
                eco.execute("SELECT wallet FROM eco WHERE user_id = ?", (self.user_id,))
                rew = eco.fetchone()[0]
                if diff == "Easiest":
                    bonus = random.randint(5,50)
                elif diff == "Easy":
                    bonus = random.randint(50,100)
                elif diff == "Medium":
                    bonus = random.randint(100,150)
                elif diff == "Hard":
                    bonus = random.randint(150,200)
                rew += bonus
                eco.execute("UPDATE eco SET wallet = ? where user_id = ?", (rew, self.user_id,))
                eco_db.commit()
                eco_db.close()
                embed_damage.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                embed_damage.add_field(name="Winner!", value=f"{interaction.user.display_name} has won the battle and has won **{bonus}** gold!", inline=False)
                for item in self.view.children:
                    item.disabled = True
        elif self.user_hp < 0 and self.npc_hp > 0:
                embed_damage.add_field(name="Loser..", value=f"{interaction.user.display_name} lost.. and fleed..", inline=False)
                embed_damage.set_image(url="https://preview.redd.it/more-3440-x-1440-wallpapers-i-made-with-photoshop-ai-part-2-v0-i7yil1lompdb1.png?width=640&crop=smart&auto=webp&s=2cf455311c487848ff30027f1debf55f8883dace")
                for item in self.view.children:
                    item.disabled = True
        elif self.user_hp <= 0 and self.npc_hp <= 0:
                if npc_speed > user_speed:
                    embed_damage.add_field(name="Loser..", value=f"{self.npc_class} was faster than {interaction.user.display_name} and strook first..", inline=False)
                    for item in self.view.children:
                        item.disabled = True
                elif user_speed > npc_speed:
                    embed_damage.add_field(name="Winner!", value=f"{interaction.user.display_name} was faster than {self.npc_class} and strook first..", inline=False)
                    eco_db = sqlite3.connect("eco.sqlite")
                    eco = eco_db.cursor()
                    eco.execute("SELECT wallet FROM eco WHERE user_id = ?", (self.user_id,))
                    rew = eco.fetchone()[0]
                    bonus = random.randint(100,200)
                    rew += bonus
                    eco.execute("UPDATE eco SET wallet = ? where user_id = ?", (rew, self.user_id,))
                    eco_db.commit()
                    eco_db.close()
                    embed_damage.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                    embed_damage.add_field(name="Winner!", value=f"{interaction.user.display_name} was faster than {self.npc_class} and strook first.. Oh and {interaction.user.display_name} also won {bonus}", inline=False)
                    for item in self.view.children:
                        item.disabled = True
                elif user_speed == npc_speed:
                    embed_damage.add_field(name="Tie..?", value=f"{interaction.user.display_name} tied.. how unamusing, both struck at the same time..", inline=False)
                    for item in self.view.children:
                        item.disabled = True
                    
        await interaction.response.edit_message(embed=embed_damage, view=self.view)

        await interaction.response.edit_message(embed=embed_damage)

        if self.user_hp > 0 and self.npc_hp > 0:
            pass


class DuelSkillsButton(discord.ui.Button):
    def __init__(self, user_id, npc_class, original_message):
        super().__init__(label="Skills", style=discord.ButtonStyle.blurple)
        self.user_id = user_id
        self.npc_class = npc_class
        self.original_message = original_message

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return

        # Retrieve user's current HP from tempstats database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM tempstats WHERE user_id=?", (self.user_id,))
        self.user_hp = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM npc WHERE npcname=?", (self.npc_class,))
        self.npc_hp = c.fetchone()[0]
        conn.close()

        # Retrieve user's learned skills from the skills database
        conn = sqlite3.connect('skills.sqlite')
        c = conn.cursor()
        c.execute("SELECT skill_id, skill_name FROM user_skills WHERE user_id=?", (self.user_id,))
        learned_skills = c.fetchall()
        conn.close()

        skill_buttons = []
        for skill_id, skill_name in learned_skills:
            skill_buttons.append(SkillButton(skill_id, skill_name, self.user_id, self.npc_class, self.user_hp, self.npc_hp, self.original_message))
        view = discord.ui.View()
        view.add_item(DuelNormalAttackButton(user_id=self.user_id, npc_class=self.npc_class))
        for button in skill_buttons:
            view.add_item(button)
        view.add_item(DuelForfeitButton(user_id=self.user_id, npc_class=self.npc_class))
        embed = interaction.message.embeds[0]
        embed.add_field(name="Incantation!", value=f"{interaction.user.display_name} is casting a skill!", inline=False)
        await interaction.response.edit_message(view=view, embed=embed)

class SkillButton(discord.ui.Button):
    def __init__(self, skill_id, skill_name, user_id, npc_class, user_hp, npc_hp, original_message):
        super().__init__(label=skill_name, style=discord.ButtonStyle.green)
        self.skill_id = skill_id
        self.user_id = user_id
        self.npc_class = npc_class
        self.user_hp = user_hp
        self.npc_hp = npc_hp
        self.original_message = original_message

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return

        # Retrieve user's current HP from tempstats database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM tempstats WHERE user_id=?", (self.user_id,))
        self.user_hp = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM npc WHERE npcname=?", (self.npc_class,))
        self.npc_hp = c.fetchone()[0]
        conn.close()

        # Retrieve skill effects from the skills database
        conn = sqlite3.connect('skills.sqlite')
        c = conn.cursor()
        c.execute("SELECT damage FROM skills WHERE skill_id=?", (self.skill_id,))
        skill_damage = c.fetchone()[0]
        conn.close()

        # Retrieve NPC stats
        if self.npc_class == "Illidari":
            npc_attack = 40
            npc_energy = 60
            npc_intelligence = 20
            npc_strength = 30
            npc_speed = 60
            npc_armor = 10
            diff = "Easiest"
        elif self.npc_class == "Elf":
            npc_attack = 50
            npc_energy = 70
            npc_intelligence = 30
            npc_strength = 40
            npc_speed = 70
            npc_armor = 20
            diff = "Easy"
        elif self.npc_class == "Warden":
            npc_attack = 60
            npc_energy = 80
            npc_intelligence = 40
            npc_strength = 50
            npc_speed = 80
            npc_armor = 30
            diff = "Easy"
        elif self.npc_class == "Disciple":
            npc_attack = 70
            npc_energy = 90
            npc_intelligence = 50
            npc_strength = 60
            npc_speed = 90
            npc_armor = 40
            diff = "Easy"
        elif self.npc_class == "Recruit":
            npc_attack = 80
            npc_energy = 100
            npc_intelligence = 60
            npc_strength = 70
            npc_speed = 100
            npc_armor = 50
            diff = "Medium"
        elif self.npc_class == "Cleric":
            npc_attack = 90
            npc_energy = 110
            npc_intelligence = 70
            npc_strength = 80
            npc_speed = 110
            npc_armor = 60
            diff = "Medium"
        elif self.npc_class == "Thief":
            npc_attack = 100
            npc_energy = 120
            npc_intelligence = 80
            npc_strength = 90
            npc_speed = 120
            npc_armor = 60
            diff = "Medium"
        elif self.npc_class == "Goblin":
            npc_attack = 110
            npc_energy = 130
            npc_intelligence = 90
            npc_strength = 100
            npc_speed = 130
            npc_armor = 60
            diff = "Hard"
        elif self.npc_class == "Imp":
            npc_attack = 120
            npc_energy = 140
            npc_intelligence = 100
            npc_strength = 110
            npc_speed = 140
            npc_armor = 60
            diff = "Hard"
        elif self.npc_class == "Orc":
            npc_attack = 130
            npc_energy = 150
            npc_intelligence = 110
            npc_strength = 120
            npc_speed = 150
            npc_armor = 70
            diff = "Hard"

        # Calculate damage based on skill power and user's stats
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT energy FROM stats WHERE user_id=?", (self.user_id,))
        user_energy = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT intelligence FROM stats WHERE user_id=?", (self.user_id,))
        user_intelligence = c.fetchone()[0]
        conn.close()
        
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT armor FROM stats WHERE user_id=?", (self.user_id,))
        user_armor = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT speed FROM stats WHERE user_id=?", (self.user_id,))
        user_speed = c.fetchone()[0]
        conn.close()

        user_damage_min = skill_damage + ((user_energy - 30) - (npc_armor)) + (user_intelligence/2)
        user_damage_max = skill_damage + ((user_energy + 30) - (npc_armor)) + (user_intelligence/2)
        if user_damage_min < 0:
            user_damage_min = 0
        if user_damage_max < 0:
            user_damage_max = 10

        npc_damage_min = ((npc_energy - 20) - (user_armor)) + (npc_intelligence/2)
        npc_damage_max = ((npc_energy + 20) - (user_armor)) + (npc_intelligence/2)
        if npc_damage_min < 0:
            npc_damage_min = 0
        if npc_damage_max < 0:
            npc_damage_max = 10
        

        # Randomly pick damage values within the calculated ranges
        user_damage_dealt = random.randint(user_damage_min, user_damage_max)
        npc_damage_dealt = random.randint(npc_damage_min, npc_damage_max)


        conn = sqlite3.connect('skills.sqlite')
        c = conn.cursor()
        c.execute("SELECT skill_id FROM user_skills WHERE skill_id = ?", (self.skill_id,))
        effect = c.fetchone()[0]
        conn.close()

        evi = sqlite3.connect("eco.sqlite")
        evi_cur = evi.cursor()
        evi_cur.execute("SELECT zan FROM eco WHERE user_id = ?", (self.user_id,))
        wep = evi_cur.fetchone()[0]
        evi.close()

        evi = sqlite3.connect("eco.sqlite")
        evi_cur = evi.cursor()
        evi_cur.execute("SELECT arm FROM eco WHERE user_id = ?", (self.user_id,))
        off = evi_cur.fetchone()[0]
        evi.close()

        sideeff = ""


        if effect == 1:
            user_speed = user_speed*1.4
            skilldis = f"**{interaction.user.display_name}** used **Fel Rush**, they have increased speed this turn"
        
        elif effect == 2:
            a = ("They also hit **twice!**", "They also hit **twice!**", f"They hit {self.npc_class} once", f"They hit {self.npc_class} once", f"They hit {self.npc_class} once", f"They hit {self.npc_class} once", f"They hit {self.npc_class} once", f"They hit {self.npc_class} once", f"They hit {self.npc_class} once", f"They hit {self.npc_class} once")
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Chaos Strike**, {b}"
            if b == "They also hit **twice!**":
                user_damage_dealt *= 2

        elif effect == 3:
            skilldis = f"**{interaction.user.display_name}** used **Blur**, Damage reduced greatly!"
            npc_damage_dealt = npc_damage_dealt * 0.5

        elif effect == 4:
            skilldis = f"**{interaction.user.display_name}** used **Steady Shot**, Accuracy is increased!"

        elif effect == 5:
            skilldis = f"**{interaction.user.display_name}** used **Kill Command**, They deal increased damage!"
            user_damage_dealt *= 2 

        elif effect == 6:
            skilldis = f"**{interaction.user.display_name}** used **Multishot**, It hit 3 times!"
            user_damage_dealt = (user_damage_dealt * 3) - 50
                
        elif effect == 7:
            a = (f"It also burnt {self.npc_class}!", f"It also burnt {self.npc_class}!", f"It also burnt {self.npc_class}!", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", )
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Fireball**, {b}"
            if b == f"It also burnt {self.npc_class}!":
                sideeff = f"**{self.npc_class}** is **BURNING!** They take an additional **30** damage this turn"
                user_damage_dealt += 30

        elif effect == 8:
            a = (f"It also froze {self.npc_class}!", f"It also froze {self.npc_class}!", f"It also froze {self.npc_class}!", f"{self.npc_class} hasn't caught a Frostbite yet", f"{self.npc_class} hasn't caught a Frostbite yet", f"{self.npc_class} hasn't caught a Frostbite yet", f"{self.npc_class} hasn't caught a Frostbite yet", f"{self.npc_class} hasn't caught a Frostbite yet", f"{self.npc_class} hasn't caught a Frostbite yet", f"{self.npc_class} hasn't caught a Frostbite yet")
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Frostbolt**, {b}"
            if b == f"It also froze {self.npc_class}!":
                sideeff = f"**{self.npc_class}** is **FROZEN**, They can't move this turn"
                npc_damage_dealt = 0

        elif effect == 9:
            a = (2,3,4,5)
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Arcane Missiles**, It hit {b} times!"
            if b == 2:
                user_damage_dealt = (user_damage_dealt * 2) - 100
            elif b == 3:
                user_damage_dealt = (user_damage_dealt * 3) - 150
            elif b == 4:
                user_damage_dealt = (user_damage_dealt * 4) - 200
            elif b == 5:
                user_damage_dealt = (user_damage_dealt * 5) - 250

        elif effect == 10:
            a = (f"{self.npc_class} is stunned! They can't move!", f"{self.npc_class} is stunned! They can't move!", f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!", )
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Tiger Palm**, {b}"
            if b == f"{self.npc_class} is stunned! They can't move!":
                npc_damage_dealt = 0

        elif effect == 11:
            skilldis = f"**{interaction.user.display_name}** used **Chi Wave**, They are radiating immense energy!"
            a = random.randint(50, 75)
            sideeff = f"**{interaction.user.display_name}** has healed {a} HP!"
            self.user_hp += a

        elif effect == 12:
            skilldis = f"**{interaction.user.display_name}** used **Jab**, {self.npc_class} is feeling lightheaded!"

        elif effect == 13:
            skilldis = f"**{interaction.user.display_name}** used **Crusader Strike**, {self.npc_class} has been crushed!"

        elif effect == 14:
            health = sqlite3.connect("stats.sqlite")
            h_cur = health.cursor()
            h_cur.execute("SELECT hp FROM stats WHERE user_id = ?", (self.user_id,))
            hp = h_cur.fetchone()[0]
            health.close()
            user_damage_dealt = 0
            self.user_hp += self.user_hp/2
            if self.user_hp > hp:
                self.user_hp = hp
            skilldis = f"**{interaction.user.display_name}** used **Divine Light**, and have restored **{self.user_hp/2}** health!"
            
        elif effect == 15:
            skilldis = f"**{interaction.user.display_name}** used **Avenging Wrath**, They have now entered righteousness stance and will deal more damage!"
            user_damage_dealt *= 1.5

        elif effect == 16:
            skilldis = f"**{interaction.user.display_name}** used **Mind Blast**, {self.npc_class} is having a concussion!"
        
        elif effect == 17:
            health = sqlite3.connect("stats.sqlite")
            h_cur = health.cursor()
            h_cur.execute("SELECT hp FROM stats WHERE user_id = ?", (self.user_id,))
            hp = h_cur.fetchone()[0]
            health.close()
            user_damage_dealt = 0
            self.user_hp += hp/2
            if self.user_hp > hp:
                self.user_hp = hp
            skilldis = f"**{interaction.user.display_name}** used **Serenity**, and have restored **{self.user_hp/2}** health!"
        
        elif effect == 18:
            if not hasattr(self, 'shadow_vision_count'):
                self.shadow_vision_count = 1
            else:
                self.shadow_vision_count += 1
            skilldis = f"**{interaction.user.display_name}** used **Shadow Visions**, {self.npc_class} is now entrapped and will take increasing damage for every Shadow Visions casted!"
            a = 15
            a *= self.shadow_vision_count
            sideeff = f"**{self.npc_class}** is **ENTRAPPED**, they took an additional {a} this turn!"
            user_damage_dealt += a

        elif effect == 19:
            npc_damage_dealt = 0
            user_damage_dealt = 0
            skilldis = f"**{interaction.user.display_name}** used **Vanish**, they are nowhere to be seen!"

        elif effect == 20:
            if not wep or wep == "Unidentified Weapon":
                skilldis = f"**{interaction.user.display_name}** used **Eviscerate**, sadly they aren't holding a weapon.."
                user_damage_dealt = 0
            elif wep and (not off or off == "Unidentified Weapon"):
                skilldis = f"**{interaction.user.display_name}** used **Eviscerate**, they are holding a single weapon.."
            elif wep and off:
                skilldis = f"**{interaction.user.display_name}** used **Eviscerate**, they are holding dual weapons! Damage is **doubled!**"
                user_damage_dealt = user_damage_dealt*2 - 50
        
        elif effect == 21:
            a = (f"{self.npc_class} started to bleed!", f"{self.npc_class} started to bleed!", f"{self.npc_class} started to bleed!", f"{self.npc_class} wound isn't too deep yet", f"{self.npc_class} wound isn't too deep yet", f"{self.npc_class} wound isn't too deep yet", f"{self.npc_class} wound isn't too deep yet", f"{self.npc_class} wound isn't too deep yet", f"{self.npc_class} wound isn't too deep yet", f"{self.npc_class} wound isn't too deep yet")
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Shadowstep**, they teleported behind their opponent and stabbed them!"
            if b == f"{self.npc_class} started to bleed!":
                sideeff = f"**{self.npc_class}** is **BLEEDING**, they take an additional **30** damage this turn"
                user_damage_dealt += 30

        elif effect == 22:
            a = (f"{self.npc_class} is paralysed!", f"{self.npc_class} is paralysed!", f"{self.npc_class} is paralysed!", f"{self.npc_class} didn't get a good shock yet..", f"{self.npc_class} didn't get a good shock yet..", f"{self.npc_class} didn't get a good shock yet..", f"{self.npc_class} didn't get a good shock yet..", f"{self.npc_class} didn't get a good shock yet..", f"{self.npc_class} didn't get a good shock yet..", f"{self.npc_class} didn't get a good shock yet..")
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Thunderbolt**, {b}"
            if b == f"{self.npc_class} is paralysed!":
                sideeff = f"**{self.npc_class}** is **PARALYSED**, they can't move this turn!"
                npc_damage_dealt = 0

        elif effect == 23:
            a = (f"It also burnt {self.npc_class}!", f"It also burnt {self.npc_class}!", f"It also burnt {self.npc_class}!", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", )
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Flame Burst**, {b}"
            if b == f"It also burnt {self.npc_class}!":
                sideeff = f"**{self.npc_class}** is **BURNING!** They take an additional **30** damage this turn"
                user_damage_dealt += 30

        elif effect == 24:
            skilldis = f"**{interaction.user.display_name}** used **Earthen Totem**, {self.npc_class}'s speed is greatly reduced!"
            npc_speed = npc_speed - npc_speed

        elif effect == 25:
            a = (f"It also burnt {self.npc_class}!", f"It also burnt {self.npc_class}!", f"It also burnt {self.npc_class}!", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", f"{self.npc_class} didn't burn however..", )
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Hellfire**, {b}"
            if b == f"It also burnt {self.npc_class}!":
                sideeff = f"**{self.npc_class}** is **BURNING!** They take an additional **30** damage this turn"
                user_damage_dealt += 30

        elif effect == 26:
            skilldis = f"**{interaction.user.display_name}** used **Shadow Bolt**, {self.npc_class} is being consumed by the shadows!"

        elif effect == 27:
            if not hasattr(self, 'curse_of_agony_count'):
                self.curse_of_agony_count = 1
            else:
                self.curse_of_agony_count += 1
            skilldis = f"**{interaction.user.display_name}** used **Curse of Agony**, {self.npc_class} is now cursed and will take more damage! Current Curse: {self.curse_of_agony_count}"
            skill_damage = skill_damage * self.curse_of_agony_count
            
        elif effect == 28:
            skilldis = f"**{interaction.user.display_name}** used **Shield Slam**, {self.npc_class} has been pelted by {interaction.user.display_name}'s armor!"
            user_damage_dealt = random.randint(user_damage_min, user_damage_max) + user_armor

        elif effect == 29:
            a = (f"{self.npc_class} is stunned! They can't move!", f"{self.npc_class} is stunned! They can't move!", f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!",f"{self.npc_class} is still in their senses!", )
            b = random.choice(a)
            skilldis = f"**{interaction.user.display_name}** used **Heroic Strike**, {b}"
            if b == f"{self.npc_class} is stunned! They can't move!":
                npc_damage_dealt = 0

        elif effect == 30:
            skilldis = f"**{interaction.user.display_name}** used **Whirlwind**, {self.npc_class} is being thrown all around!"

        # Update HP values after damage calculation
        self.user_hp -= npc_damage_dealt
        self.npc_hp -= user_damage_dealt

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.user_hp, self.user_id,))
        conn.commit()
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("UPDATE npc SET hp = ? WHERE npcname=?", (self.npc_hp, self.npc_class,))
        conn.commit()
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT hp FROM stats WHERE user_id = ?", (self.user_id,))
        normal = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT npcname FROM npc WHERE npcname = ?", (self.npc_class,))
        npc_temp_class = c.fetchone()[0]
        conn.close()

        npc_def_stats = {
            "Illidari": (100,),
            "Elf": (120,),
            "Warden": (130,),
            "Disciple": (140,),
            "Recruit": (150,),
            "Cleric": (160,),
            "Thief": (170,),
            "Goblin": (180,),
            "Imp": (190,),
            "Orc": (200,)
        }

        npcnormal = npc_def_stats[npc_temp_class][0]

        img = ["https://wallpapers.com/images/hd/hearthstone-rastakhan-s-rumble-2560-x-1440-psz606u2cedv34ln.jpg","https://s1.1zoom.me/b5050/636/Hearthstone_Heroes_of_Warcraft_Battles_Dragons_529821_1366x768.jpg",
               "https://d1lss44hh2trtw.cloudfront.net/assets/article/2018/12/04/rastakhan-s-rumble-cinematic-still-7-png-jpgcopy_feature.jpg", "https://dotesports.com/wp-content/uploads/2018/11/24030406/Screenshot-140.png",
                "https://cdn.mos.cms.futurecdn.net/JgySFGeQcRRH3zf6QecaJM-1200-80.jpg", "https://dotesports.com/wp-content/uploads/2018/11/26075329/Screenshot-163.png" ]

        if npc_speed > user_speed:
            speed = f"{self.npc_class} is faster! They get to move first.."
        elif user_speed > npc_speed:
            speed = f"{interaction.user.display_name} is faster! They get to move first.."
        else:
            speed = f"Ladies and Gentlemen, its a speed tie!"


        clrs = [0x0a0a0a, 0x9fd2ff, 0xff5151, 0xffffff, 0xffdbaf]
        # Create embed with damage dealt and updated stats
        embed_damage = discord.Embed(title="Skills - Damage Dealt", color=random.choice(clrs))
        embed_damage.add_field(name="", value=speed, inline=False)
        embed_damage.add_field(name="", value=skilldis, inline=False)
        embed_damage.add_field(name="", value=sideeff, inline=False)
        embed_damage.add_field(name=f"{interaction.user.display_name}'s Damage Dealt", value=f"{user_damage_dealt} HP", inline=True)
        embed_damage.add_field(name=f"{self.npc_class}'s Damage Dealt", value=f"{npc_damage_dealt} HP", inline=True)
        embed_damage.add_field(name="", value="", inline=False)
        embed_damage.add_field(name=f"{interaction.user.display_name}'s Remaining HP", value=f"{self.user_hp} HP", inline=True)
        embed_damage.add_field(name=f"{self.npc_class}'s Remaining HP", value=f"{self.npc_hp} HP", inline=True)
        embed_damage.set_image(url= random.choice(img))

        if self.user_hp <= 0 or self.npc_hp <= 0:
            embed_damage.add_field(name="Duel Ended", value="The duel has ended!", inline=False)
            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (normal, self.user_id,))
            conn.commit()
            conn.close()
            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("UPDATE npc SET hp = ? WHERE npcname=?", (npcnormal, self.npc_class,))
            conn.commit()
            conn.close()
            for item in self.view.children:
                    item.disabled = True

        if self.user_hp >= 0 and self.npc_hp < 0:
                eco_db = sqlite3.connect("eco.sqlite")
                eco = eco_db.cursor()
                eco.execute("SELECT wallet FROM eco WHERE user_id = ?", (self.user_id,))
                rew = eco.fetchone()[0]
                if diff == "Easiest":
                    bonus = random.randint(5,50)
                elif diff == "Easy":
                    bonus = random.randint(50,100)
                elif diff == "Medium":
                    bonus = random.randint(100,150)
                elif diff == "Hard":
                    bonus = random.randint(150,200)
                rew += bonus
                eco.execute("UPDATE eco SET wallet = ? where user_id = ?", (rew, self.user_id,))
                eco_db.commit()
                eco_db.close()
                embed_damage.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                embed_damage.add_field(name="Winner!", value=f"{interaction.user.display_name} has won the battle and has won **{bonus}** gold!", inline=False)
                for item in self.view.children:
                    item.disabled = True
        elif self.user_hp < 0 and self.npc_hp > 0:
                embed_damage.add_field(name="Loser..", value=f"{interaction.user.display_name} lost.. and fleed..", inline=False)
                embed_damage.set_image(url="https://preview.redd.it/more-3440-x-1440-wallpapers-i-made-with-photoshop-ai-part-2-v0-i7yil1lompdb1.png?width=640&crop=smart&auto=webp&s=2cf455311c487848ff30027f1debf55f8883dace")
                for item in self.view.children:
                    item.disabled = True
        elif self.user_hp <= 0 and self.npc_hp <= 0:
                if npc_speed > user_speed:
                    embed_damage.add_field(name="Loser..", value=f"{self.npc_class} was faster than {interaction.user.display_name} and strook first..", inline=False)
                    for item in self.view.children:
                        item.disabled = True
                elif user_speed > npc_speed:
                    embed_damage.add_field(name="Winner!", value=f"{interaction.user.display_name} was faster than {self.npc_class} and strook first..", inline=False)
                    eco_db = sqlite3.connect("eco.sqlite")
                    eco = eco_db.cursor()
                    eco.execute("SELECT wallet FROM eco WHERE user_id = ?", (self.user_id,))
                    rew = eco.fetchone()[0]
                    bonus = random.randint(100,200)
                    rew += bonus
                    eco.execute("UPDATE eco SET wallet = ? where user_id = ?", (rew, self.user_id,))
                    eco_db.commit()
                    eco_db.close()
                    embed_damage.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                    embed_damage.add_field(name="Winner!", value=f"{interaction.user.display_name} was faster than {self.npc_class} and strook first.. Oh and {interaction.user.display_name} also won {bonus}", inline=False)
                    for item in self.view.children:
                        item.disabled = True
                elif user_speed == npc_speed:
                    embed_damage.add_field(name="Tie..?", value=f"{interaction.user.display_name} tied.. how unamusing, both struck at the same time..", inline=False)
                    for item in self.view.children:
                        item.disabled = True
                    
        await interaction.response.edit_message(embed=embed_damage, view=self.view)

        await interaction.response.edit_message(embed=embed_damage)

        if self.user_hp > 0 and self.npc_hp > 0:
            pass
        
class DuelForfeitButton(discord.ui.Button):
    def __init__(self, user_id, npc_class):
        super().__init__(label="Forfeit", style=discord.ButtonStyle.danger)
        self.user_id = user_id
        self.npc_class = npc_class

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return

        # Disable all buttons
        for item in self.view.children:
            item.disabled = True

        # Update the user's HP to full in the tempstats database
        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT class FROM tempstats WHERE user_id = ?", (self.user_id,))
        user_class = c.fetchone()[0]
        conn.close()

        default_stats = {
            "Demon Hunter": (150, 20, 100, 50, 80, 70, 30),
            "Hunter": (130, 25, 80, 40, 70, 60, 40),
            "Mage": (100, 15, 120, 90, 40, 50, 20),
            "Monk": (120, 20, 90, 60, 60, 60, 30),
            "Paladin": (140, 25, 80, 50, 80, 80, 50),
            "Priest": (110, 15, 100, 80, 30, 40, 20),
            "Rogue": (120, 30, 100, 40, 50, 50, 30),
            "Shaman": (130, 25, 90, 70, 60, 60, 40),
            "Warlock": (110, 20, 110, 90, 40, 40, 20),
            "Warrior": (150, 30, 70, 40, 90, 90, 60)
        }

        normal_hp = default_stats[user_class][0]

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (normal_hp, self.user_id,))
        conn.commit()
        conn.close()

        eco_db = sqlite3.connect("eco.sqlite")
        eco = eco_db.cursor()
        eco.execute("SELECT wallet FROM eco WHERE user_id = ?", (self.user_id,))
        los = eco.fetchone()[0]
        ded = random.randint(200,500)
        los -= ded
        eco.execute("UPDATE eco SET wallet = ? where user_id = ?", (los, self.user_id,))
        eco_db.commit()
        eco_db.close()

        embed = interaction.message.embeds[0]
        embed.add_field(name="Duel Ended", value=f"{interaction.user.display_name} forfeited.. You have lost {ded} gold.. :(", inline=False)

        await interaction.response.edit_message(embed=embed, view=self.view)


class DuelNPC(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.stats_db = sqlite3.connect("stats.sqlite")
        self.stats_cursor = self.stats_db.cursor()

    @commands.Cog.listener()
    async def on_ready(self):
        self.stats_cursor.execute('''CREATE TABLE IF NOT EXISTS npc (
                                    npcname TEXT PRIMARY KEY,
                                    hp INTEGER DEFAULT 0
                                    )''')
        
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Illidari", 100)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Elf", 120)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Warden", 130)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Disciple", 140)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Recruit", 150)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Cleric", 160)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Thief", 170)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Goblin", 180)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Imp", 190)')
        self.stats_cursor.execute('INSERT OR IGNORE INTO npc (npcname, hp) VALUES ("Orc", 200)')
        self.stats_db.commit()

    @commands.command()
    async def duelnpc(self, ctx):
        embed = discord.Embed(title="Battlegrounds", color=0xffcf7e)
        embed.add_field(name="", value="Warrior, welcome to the battleground's edge where steel meets destiny. Beyond these gates lies the crucible of conflict, where valor and strength determine fate. The clash of armies echoes through these lands, and here, every step you take may alter the course of war. Ready your spirit, for within these fields, legends are forged in blood and battle. Will you rise victorious, or become another tale whispered in the winds of war?", inline=False)
        embed.add_field(name="Important Info", value="The NPC's given in the below dropdown are sorted in order of their difficulty", inline=False)
        embed.add_field(name="", value="<:demon_hunter:1255872124195704975> **Illidari** - Easiest ", inline=False)
        embed.add_field(name="", value="<:hunter:1255872272988770346> **Elf** - Easy ", inline=False)
        embed.add_field(name="", value="<:wiz:1255872379918352384> **Warden** - Easy ", inline=False)
        embed.add_field(name="", value="<:Death_Knight:1255873191373701241> **Disciple** - Easy", inline=False)
        embed.add_field(name="", value="<:Paladin:1255872513423048716> **Recruit** - Medium ", inline=False)
        embed.add_field(name="", value="<:priest:1255872554631958729> **Cleric** - Medium ", inline=False)
        embed.add_field(name="", value="<:Rogue:1255872600987664396> **Thief** - Medium ", inline=False)
        embed.add_field(name="", value="<:shaman:1255872632092495933> **Goblin** - Hard ", inline=False)
        embed.add_field(name="", value="<:warlock:1255872668675215380> **Imp** - Hard ", inline=False)
        embed.add_field(name="", value="<:warrior:1255872722551050323> **Orc** - Hard ", inline=False)
        embed.set_image(url="https://static.invenglobal.com/upload/image/2021/05/27/o1622134215623633.png")
        view = discord.ui.View()
        view.add_item(NPCClassDropdown(user_id=ctx.author.id))
        await ctx.send(embed=embed, view=view)

        


async def setup(client):
    await client.add_cog(DuelNPC(client))


