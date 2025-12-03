import discord
from discord.ext import commands
import sqlite3
import aiosqlite

class skills(commands.Cog):

    def __init__(self, client):
        self.client=client


    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("skills.sqlite")
        cursor = db.cursor()

        try:
            # Create the skills table if it doesn't exist
            cursor.execute('''CREATE TABLE IF NOT EXISTS skills (
                            skill_id INTEGER PRIMARY KEY,
                            class TEXT,
                            skill_name TEXT,
                            description TEXT,
                            damage INTEGER,
                            effects TEXT,
                            energy INTEGER,
                            UNIQUE(class, skill_name)
                        )''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS user_skills (
                            user_id INTEGER NOT NULL,
                            skill_id INTEGER NOT NULL,
                            skill_name TEXT NOT NULL,
                            FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
                        );''')

            # Insert default skills for Mage if they don't exist
            default_skills = [
                ("Demon Hunter", "Fel Rush", "Charges forward and deals damage to all opponents within the dash", 30, "Speed is increased by 50% of your current speed", 20),
                ("Demon Hunter", "Chaos Strike", "Launches a flurry of fel damage in an area.", 20, "20% chance to hit twice", 20),
                ("Demon Hunter", "Blur", "Evasion ability that reduces damage", 20, "No extra effect", 20),
                ("Hunter", "Steady Shot", "Shoot an arrow or a bullet at your opponent", 30, "Can't miss", 20),
                ("Hunter", "Kill Command", "Deal damage to your opponent", 30, "Deal additional damage if you control a beast", 20),
                ("Hunter", "Multishot", "Shoot 3 arrows at your opponent", 10, "No extra effect", 20),
                ("Mage", "Fireball", "Launches a fiery ball that causes fire damage.", 40, "Burns the target", 30),
                ("Mage", "Frostbolt", "Hurls a bolt of frost at the enemy, causing frost damage.", 20, "Freezes the target", 20),
                ("Mage", "Arcane Missiles", "Launches magical missiles at the target.", 10, "Multiple hits", 20),
                ("Monk", "Tiger Palm", "Strike your opponent with your palm", 50, "Chance to stun ", 40),
                ("Monk", "Chi Wave", "Send chi energy and heal allies and deal damage to opponents", 20, "No extra effect", 20),
                ("Monk", "Jab", "Regular jab at your opponent", 20, "No extra effect", 10),
                ("Paladin", "Crusader Strike", "Strike your opponent with your weapon imbued with holy light", 40, "Chance to stun", 30), 
                ("Paladin", "Divine Light", "Heals you with half of your max health", 0, "No extra effect", 20),
                ("Paladin", "Avenging Wrath", "Enter righteousness mode, dealing increased damage", 40, "No extra effect", 20),
                ("Priest", "Mind Blast", "Assault your opponents mind dealing shadow damage", 40, "Burns the target", 40),
                ("Priest", "Serenity", "Restore health based on your energy", 0, "No extra effect", 10),
                ("Priest", "Resurrect", "Resurrect a dead ally", 0, "No extra effect", 20),
                ("Rogue", "Vanish", "Conceal yourself in a smoke, making you invisible", 0, "No extra effect", 20),
                ("Rogue", "Eviscerate", "Deal damage to your opponent with a single weapon", 20, "Damage doubles if you have two weapons", 20),
                ("Rogue", "Shadowstep", "Teleport behind your opponent and stab them in the back", 30, "Can apply bleed effect", 30),
                ("Shaman", "Thunderbolt", "Electrocute your opponent with a bolt of lightning", 40, "Can apply paralysis effect", 30),
                ("Shaman", "Flame Burst", "Scorch your opponent with flames", 40, "Can apply burn effect", 30),
                ("Shaman", "Earthen Totem", "Summon a totem that slows down your opponents", 10, "No extra effects", 20),
                ("Warlock", "Hellfire", "Summons flames from hells to damage the opponent", 20, "Burns the target.", 20),
                ("Warlock", "Shadow Bolt", "Shoots a bolt at opponent dealing shadow damage", 30, "No extra effect", 20),
                ("Warlock", "Curse of Agony", "Curses the opponent dealing exponentially more damage", 20, "No extra effect", 30),
                ("Warrior", "Shield Slam", "Deal damage to your opponent based on your armor", 50, "No extra effect", 30),
                ("Warrior", "Heroic Strike", "Strike your opponent with a mighty blow", 40, "Chane to stun", 40),
                ("Warrior", "Whirlwind", "Deal damage in an area", 20, "No extra effect", 20),
            ]

            for skill_data in default_skills:
                cursor.execute("INSERT OR IGNORE INTO skills (class, skill_name, description, damage, effects, energy) VALUES (?, ?, ?, ?, ?, ?)", skill_data)

            db.commit()
            print("Skills loaded")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
        finally:
            cursor.close()
            db.close()

    @commands.command()
    async def study(self, ctx):
        user_id = ctx.author.id
        user_class = await self.get_user_class(user_id)

        if not user_class:
            await ctx.send("You need to choose a class first using the `start` command.")
            return

        db = sqlite3.connect("skills.sqlite")
        cursor = db.cursor()

        cursor.execute("SELECT * FROM skills WHERE class = ?", (user_class,))
        skills = cursor.fetchall()

        if not skills:
            await ctx.send("No skills available for your class.")
            return

        skills_list = "\n".join([f"{skill[0]}. **{skill[2]}** - \n**Damage**: {skill[4]} \n**Effect**: {skill[3]} \n**Bonus Effects**: {skill[5]}\n" for skill in skills])
        embed = discord.Embed(title="Available Skills", description=f"Choose a skill to study using `,learn (skill_id)`:", color=0xaaaaaa)
        embed.add_field(name=f"{user_class} Skills:", value=skills_list, inline=False)
        embed.set_footer(text=f"Choose wisely, {self.get_class_quote(user_class)}")
        embed.set_image(url="https://assetsio.gnwcdn.com/hearthstone-scholomance-decks-1.jpg?width=1200&height=1200&fit=bounds&quality=70&format=jpg&auto=webp")
        
        await ctx.send(embed=embed)

        cursor.close()
        db.close()

    async def get_user_class(self, user_id):
        db = sqlite3.connect("eco.sqlite")
        cursor = db.cursor()

        cursor.execute("SELECT class FROM eco WHERE user_id = ?", (user_id,))
        user_class = cursor.fetchone()

        cursor.close()
        db.close()

        return user_class[0] if user_class else None

    def get_class_quote(self, user_class):
        quotes = {
            "Demon Hunter": "The hunt never ends.",
            "Hunter": "Let the hunt begin!",
            "Mage": "Knowledge is power.",
            "Monk": "Balance is key.",
            "Paladin": "For justice and glory!",
            "Priest": "May the Light guide you.",
            "Rogue": "Subtlety is our strength.",
            "Shaman": "The elements obey me.",
            "Warlock": "Power is everything.",
            "Warrior": "Victory or death!",
        }

        return quotes.get(user_class, "Choose your path wisely.")
    


    @commands.command()
    async def learn(self, ctx, skill_id: int):
        user_id = ctx.author.id
        user_class = await self.get_user_class(user_id)  # Fetch user_class here

        if not user_class:
            await ctx.send("You need to choose a class first using the `start` command.")
            return

        async with aiosqlite.connect("skills.sqlite") as db:
            async with db.execute("SELECT * FROM skills WHERE skill_id = ? AND class = ?", (skill_id, user_class)) as cursor:
                skill = await cursor.fetchone()

            if not skill:
                await ctx.send("Either the skill ID is wrong or you are trying to learn a skill from another class.")
                return

            async with aiosqlite.connect("skills.sqlite") as db:
                async with db.execute("SELECT COUNT(*) FROM user_skills WHERE user_id = ?", (user_id,)) as cursor:
                    count = await cursor.fetchone()

                if count[0] >= 5:
                    await ctx.send("You have already learned the maximum number of skills, 5.")
                    return

                async with db.execute("SELECT * FROM user_skills WHERE user_id = ? AND skill_id = ?", (user_id, skill_id)) as cursor:
                    if await cursor.fetchone():
                        await ctx.send("You have already learned this skill you gotta chill out")
                        return

                    await db.execute("INSERT INTO user_skills (user_id, skill_id, skill_name) VALUES (?, ?, ?)", (user_id, skill_id, skill[2]))
                    await db.commit()

            await ctx.send(f"You have successfully learned **{skill[2]}**")



    @commands.command()
    async def discard(self, ctx, skill_id: int):
        user_id = ctx.author.id

        db = sqlite3.connect('skills.sqlite')
        cursor = db.cursor()

        cursor.execute("SELECT * FROM user_skills WHERE user_id = ? AND skill_id = ?", (user_id, skill_id))
        if not cursor.fetchone():
            await ctx.send("You haven't learned this skill yet.")
            return

        # Remove the skill from the user's learned skills
        cursor.execute("DELETE FROM user_skills WHERE user_id = ? AND skill_id = ?", (user_id, skill_id))
        db.commit()
        db.close()

        await ctx.send(f"You have discarded the skill with ID: {skill_id}")




async def setup(client):
    await client.add_cog(skills(client))