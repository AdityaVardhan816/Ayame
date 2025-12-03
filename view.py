import discord
from discord.ext import commands
import sqlite3

class view(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.stats_db = sqlite3.connect("stats.sqlite")
        self.stats_cursor = self.stats_db.cursor()

        self.class_images = {
            "Demon Hunter": "https://cdn.oneesports.gg/cdn-data/wp-content/uploads/2020/04/Hearthstone_DemonHunter.jpg",
            "Hunter": "https://wallpapers.com/images/hd/hearthstone-sylvannas-windrunner-hunter-skin-fqrd3o92mmw6ebyr.jpg",
            "Mage": "https://c4.wallpaperflare.com/wallpaper/832/894/537/hearthstone-khadgar-mage-wallpaper-preview.jpg",
            "Monk": "https://cdn.mos.cms.futurecdn.net/9tJa276UV7BJ5VqT7HhhaK.jpg",
            "Paladin": "https://pics.craiyon.com/2023-05-31/5924e0a741c548cab463273d51b8bbaf.webp",
            "Priest": "https://cdn.mos.cms.futurecdn.net/g2TjYTjBrJ9RZgMz75isXe.jpg",
            "Rogue": "https://www.bhmpics.com/downloads/hearthstone-rogue-wallpaper-/4.diao-chan-valeera.jpg",
            "Shaman": "https://cdn.mos.cms.futurecdn.net/gXyKA44jc8Q5XKQB3awu2D.jpg",
            "Warlock": "https://d1lss44hh2trtw.cloudfront.net/assets/article/2021/09/20/hs23-016_feature.jpeg",
            "Warrior": "https://d1lss44hh2trtw.cloudfront.net/assets/article/2018/12/01/war-master-voone-cropped_feature.jpg"
        }

        self.class_footer = {
            "Demon Hunter": "In shadows deep and infernal flames, I hunt the darkness that threatens to consume our world, my blades thirsting for the blood of demons.",
            "Hunter": "Through the wilderness and under the stars, my bow sings the song of the wild, tracking prey with every silent step.",
            "Mage": "Through arcane mastery, I command the elements and shape reality itself, unraveling mysteries as ancient as time.",
            "Monk": "Balance is found in discipline and harmony. Through focused mind and agile movements, I embrace the flow of combat.",
            "Paladin": "With righteousness as my shield and faith as my sword, I stand vigilant against darkness, a beacon of hope and justice.",
            "Priest": "Through faith and prayer, I heal the wounded, shield the weak, and banish the shadows that threaten our world.",
            "Rogue": "In shadows we thrive, unseen and deadly. Trust not what you see, for deceit is our art and silence our weapon.",
            "Shaman": "Feel the elements' embrace, hear their whispers on the wind. Balance in nature, power in harmony—our connection runs deep, like roots in the earth.",
            "Warlock": "In the dark embrace of forbidden arts, power flows like dark rivers, bending reality to my whims.",
            "Warrior": "With each battle, honor and strength are forged like steel, unyielding in the face of adversity. Stand firm, for courage is our armor, and victory, our destiny."
        }

    @commands.Cog.listener()
    async def on_ready(self):
        self.stats_cursor.execute('''CREATE TABLE IF NOT EXISTS stats (
                                    user_id INTEGER PRIMARY KEY,
                                    hp INTEGER DEFAULT 0,
                                    base_attack INTEGER DEFAULT 0,
                                    energy INTEGER DEFAULT 0,
                                    intelligence INTEGER DEFAULT 0,
                                    strength INTEGER DEFAULT 0,
                                    speed INTEGER DEFAULT 0,
                                    armor INTEGER DEFAULT 0
                                    )''')
        self.stats_cursor.execute('''CREATE TABLE IF NOT EXISTS tempstats (
                                  user_id INTEGER,
                                  hp INTEGER,
                                  class TEXT)''')
        
        print("Stats database loaded")
        self.stats_db.commit()

    @commands.command()
    async def view(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        user_id = member.id

        # Retrieve class from eco database
        eco_db = sqlite3.connect("eco.sqlite")
        eco_cursor = eco_db.cursor()
        eco_cursor.execute("SELECT class, zan, arm FROM eco WHERE user_id = ?", (user_id,))
        class_info = eco_cursor.fetchone()

        if not class_info:
            await ctx.send("You haven't selected a class yet.")
            eco_db.close()
            return

        user_class, equipped_weapon, off_hand = class_info

        # Define default stats based on the class
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
        

        if user_class not in default_stats:
            await ctx.send(f"Invalid class '{user_class}'.")
            eco_db.close()
            return

        hp = default_stats[user_class][0]

        # Insert or update stats in the stats database
        self.stats_cursor.execute("INSERT OR IGNORE INTO stats (user_id, hp, base_attack, energy, intelligence, strength, speed, armor) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                (user_id,) + default_stats[user_class])

        self.stats_cursor.execute("INSERT OR IGNORE INTO tempstats (user_id, hp, class) VALUES (?, ?, ?)",
                                   (user_id, hp, user_class))

        # Fetch current stats from the stats database
        self.stats_cursor.execute("SELECT hp, base_attack, energy, intelligence, strength, speed, armor FROM stats WHERE user_id = ?", (user_id,))
        stats = self.stats_cursor.fetchone()

        # Fetch item attack from the shop database
        item_attack = 0
        if equipped_weapon:
            shop_db = sqlite3.connect("inv.sqlite")
            shop_cursor = shop_db.cursor()
            shop_cursor.execute("SELECT atk FROM weapons WHERE name = ?", (equipped_weapon,))
            item_info = shop_cursor.fetchone()
            if item_info:
                item_attack = item_info[0]
            shop_db.close()

        item_strength = 0
        if equipped_weapon:
            shop_db = sqlite3.connect("inv.sqlite")
            shop_cursor = shop_db.cursor()
            shop_cursor.execute("SELECT strength FROM weapons WHERE name = ?", (equipped_weapon,))
            item_info = shop_cursor.fetchone()
            if item_info:
                item_strength = item_info[0]
            shop_db.close()

        item_intelligence = 0
        if equipped_weapon:
            shop_db = sqlite3.connect("inv.sqlite")
            shop_cursor = shop_db.cursor()
            shop_cursor.execute("SELECT intelligence FROM weapons WHERE name = ?", (equipped_weapon,))
            item_info = shop_cursor.fetchone()
            if item_info:
                item_intelligence = item_info[0]
            shop_db.close()

        item_hp = 0
        if equipped_weapon:
            shop_db = sqlite3.connect("inv.sqlite")
            shop_cursor = shop_db.cursor()
            shop_cursor.execute("SELECT hp FROM weapons WHERE name = ?", (equipped_weapon,))
            item_info = shop_cursor.fetchone()
            if item_info:
                item_hp = item_info[0]
            shop_db.close()

        item_speed = 0
        if equipped_weapon:
            shop_db = sqlite3.connect("inv.sqlite")
            shop_cursor = shop_db.cursor()
            shop_cursor.execute("SELECT speed FROM weapons WHERE name = ?", (equipped_weapon,))
            item_info = shop_cursor.fetchone()
            if item_info:
                item_speed = item_info[0]
            shop_db.close()

        off_attack = 0
        if off_hand:
            df_db = sqlite3.connect("inv.sqlite")
            df_cursor = df_db.cursor()
            df_cursor.execute("SELECT atk FROM weapons WHERE name = ?", (off_hand,))
            df_info = df_cursor.fetchone()
            if df_info:
                off_attack = df_info[0]
            df_db.close()

        off_defense = 0
        if off_hand:
            df_db = sqlite3.connect("inv.sqlite")
            df_cursor = df_db.cursor()
            df_cursor.execute("SELECT defense FROM weapons WHERE name = ?", (off_hand,))
            df_info = df_cursor.fetchone()
            if df_info:
                off_defense = df_info[0]
            df_db.close()

        if equipped_weapon == "Swinetusk_Shank" and user_class == "Rogue":
            item_speed += 20
        if equipped_weapon == "Super_Collider" and user_class == "Warrior":
            item_strength += 20
        if equipped_weapon == "Trueaim_Crescent" and user_class == "Demon Hunter":
            item_attack += 20
        if equipped_weapon == "Cog_Hammer" and user_class == "Hunter":
            item_speed += 20
        if equipped_weapon == "Primal_Staff" and user_class == "Mage":
            item_intelligence += 20
        if equipped_weapon == "Felstring_harp" and user_class == "Warlock":
            item_hp += 20
        if equipped_weapon == "Argent_Lance" and user_class == "Paladin":
            item_strength += 20
        if equipped_weapon == "Azsharan_Trident" and user_class == "Shaman":
            item_intelligence += 20
        if equipped_weapon == "Ceremonial_Maul" and user_class == "Monk":
            item_attack += 20
        if equipped_weapon == "Obsidian_Shard" and user_class == "Priest":
            item_hp += 20

        # Calculate total attack
        total_hp = default_stats[user_class][0] + item_hp
        total_attack = default_stats[user_class][1] + item_attack + off_attack
        total_intelligence = default_stats[user_class][3] + item_intelligence
        total_strength = default_stats[user_class][4] + item_strength
        total_speed = default_stats[user_class][5] + item_speed
        total_defense = default_stats[user_class][6] + off_defense

        self.stats_cursor.execute("UPDATE tempstats SET hp = ? where user_id = ?", (total_hp, user_id))
        self.stats_cursor.execute("UPDATE stats SET base_attack = ? WHERE user_id = ?", (total_attack, user_id))
        self.stats_cursor.execute("UPDATE stats SET hp = ? WHERE user_id = ?", (total_hp, user_id))
        self.stats_cursor.execute("UPDATE stats SET intelligence = ? WHERE user_id = ?", (total_intelligence, user_id))
        self.stats_cursor.execute("UPDATE stats SET strength = ? WHERE user_id = ?", (total_strength, user_id))
        self.stats_cursor.execute("UPDATE stats SET speed = ? WHERE user_id = ?", (total_speed, user_id))
        self.stats_cursor.execute("UPDATE stats SET armor = ? WHERE user_id = ?", (total_defense, user_id))
        self.stats_db.commit()

        # Retrieve learned skills
        skills_db = sqlite3.connect("skills.sqlite")
        skills_cursor = skills_db.cursor()
        skills_cursor.execute("SELECT skills.skill_name FROM skills INNER JOIN user_skills ON skills.skill_id = user_skills.skill_id WHERE user_skills.user_id = ?", (user_id,))
        learned_skills = skills_cursor.fetchall()
        learned_skills_list = [skill[0] for skill in learned_skills]
        skills_db.close()

        # Format stats into an embed
        if stats:
            hp, base_attack, energy, intelligence, strength, speed, armor = stats
            embed = discord.Embed(title=f"Stats for {member}'s {user_class}", color=member.color)
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="Class", value=user_class, inline=False)
            embed.add_field(name="HP", value=total_hp, inline=True)
            embed.add_field(name="Attack", value=total_attack, inline=True)
            embed.add_field(name="Energy", value=energy, inline=False)
            embed.add_field(name="Intelligence", value=total_intelligence, inline=True)
            embed.add_field(name="Strength", value=total_strength, inline=False)
            embed.add_field(name="Speed", value=total_speed, inline=True)
            embed.add_field(name="Armor", value=total_defense, inline=False)
            embed.add_field(name="Equipped Weapon", value=equipped_weapon if equipped_weapon else "None", inline=True)
            embed.add_field(name="Equipped Off-Hand", value=off_hand if off_hand else "None", inline=True)
            if learned_skills_list:
                embed.add_field(name="Learned Skills", value="\n".join(learned_skills_list), inline=False)
            if user_class in self.class_images:
                embed.set_image(url=self.class_images[user_class])
            if user_class in self.class_footer:
                embed.set_footer(text=self.class_footer[user_class])
            await ctx.send(embed=embed)
        else:
            await ctx.send("Failed to retrieve stats.")

        eco_db.close()


async def setup(client):
    await client.add_cog(view(client))
