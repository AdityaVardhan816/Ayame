import discord
from discord.ext import commands
import asyncio
import sqlite3
import random

class inv(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        db=sqlite3.connect("inv.sqlite")
        cursor=db.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS inv (
                       user_id INTERGER, item_name TEXT, qty INTERGER
        ) ''')
        cursor.execute(''' CREATE TABLE IF NOT EXISTS armor (
                       user_id INTERGER, item_name TEXT, qty INTERGER)
        ''')
        cursor.execute(''' CREATE TABLE IF NOT EXISTS weapons (
                        weapon_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        atk INTEGER NOT NULL,
                        defense INTEGER NOT NULL,
                        strength INTEGER NOT NULL,
                        intelligence INTEGER NOT NULL,
                        hp INTEGER NOT NULL,
                        speed INTEGER NOT NULL
        );''')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (1, "Holy_Sword", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (2, "Abyssal_Axe", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (3, "Hunters_Bow", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (4, "Spectral_Mace", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (5, "Long_Greatsword", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (6, "Royal_Staff", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (7, "Corrupted_Daggers", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (8, "Burning_Warblade", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (9, "Shadowy_Ruins", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (10, "Spirit_Claws", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (11, "Death_Mantle", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (12, "Kings_Sabre", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (13, "Sharp_Katar", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (14, "Bloody_Sword", 20, 0, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (15, "Quick_Pick", 20, 0, 0, 0, 0, 0)')

        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (16, "Mithril_Rod", 30, 0, 0, 40, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (17, "Thundering_Hammer", 50, 0, 20, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (18, "Starsung_Bow", 40, 0, 0, 0, 0, 30)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (19, "Incanters_Flow", 40, 0, 0, 30, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (20, "Goblins_Gold", 30, 0, 30, 0, 0, 10)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (21, "Necrium_Blade", 60, 0, 0, 0, 0, 10)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (22, "Tainted_Fork", 40, 0, 20, 10, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (23, "Dragon_Spear", 50, 0, 0, 0, 20, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (24, "Arcanite_Ripper", 50, 0, 20, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (25, "Spectral_Cutlass", 30, 0, 10, 20, 0, 10)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (26, "Runed_Shortsword", 30, 0, 0, 0, 0, 40)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (27, "Calamity_Grasp", 30, 0, 0, 0, 40, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (28, "Boundless_Glaive", 60, 0, 10, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (29, "Runic_Axe", 50, 0, 20, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (30, "Tolins_Goblet", 40, 0, 0, 20, 0, 10)')

        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (31, "Swinetusk_Shank", 60, 0, 0, 20, 40, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (32, "Super_Collider", 80, 0, 40, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (33, "Trueaim_Crescent", 70, 0, 0, 0, 0, 50)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (34, "Cog_Hammer", 80, 0, 20, 0, 0, 20)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (35, "Primal_Staff", 60, 0, 0, 60, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (36, "Felstring_Harp", 60, 0, 0, 0, 60, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (37, "Argent_Lance", 60, 0, 30, 0, 0, 30)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (38, "Azsharan_Trident", 60, 0, 20, 0, 0, 40)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (39, "Ceremonial_Maul", 60, 0, 20, 0, 40, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp ,speed) VALUES (40, "Obsidian_Shard", 60, 0, 0, 40, 0, 20)')



        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (51, "Blazing_Shield", 0, 40, 0, 0, 0 ,0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (52, "Spiked_Shield", 10, 20, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (53, "Crackling_Shield", 0, 40, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (54, "Wooden_Wheel", 10, 20, 0, 0, 0, 0)')
        cursor.execute('INSERT OR IGNORE INTO weapons (weapon_id, name, atk, defense, strength, intelligence, hp, speed) VALUES (55, "Amethyst_Dagger", 20, 0, 0, 0, 0, 0)')
    
        print("Inventory loaded")
        db.commit()
        cursor.close()
        db.close()


    @commands.command(aliases=["inv", "bag"])
    async def inventory(self, ctx):
        user_id = ctx.author.id

        db = sqlite3.connect("inv.sqlite")
        cursor = db.cursor()

        cursor.execute("SELECT item_name, qty FROM inv WHERE user_id = ?", (user_id,))
        inventory = cursor.fetchall()

        if not inventory:
            await ctx.send("Your inventory is empty.")
        else:
            inventory_text = "**Your Inventory**:\n"
            for item, qty in inventory:
               inventory_text += f"{item}: {qty}\n"

            await ctx.send(inventory_text)


    @commands.command()
    async def equip(self, ctx, zanpa_name):
        dbi = sqlite3.connect("inv.sqlite", timeout=50)
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor=dbe.cursor()
        inv_cursor=dbi.cursor()
        user_id = ctx.author.id
        
        inv_cursor.execute("SELECT item_name FROM inv WHERE user_id = ? AND item_name = ?", (user_id, zanpa_name ))
        zanpakuto_exists = inv_cursor.fetchone()

        if not zanpakuto_exists:
            await ctx.send(f"Tough guy thinks he got {zanpa_name} in his inventory")
            return

        eco_cursor.execute("SELECT zan FROM eco WHERE user_id = ?", (user_id,))
        current_equipped = eco_cursor.fetchone()

        if current_equipped and current_equipped[0] == zanpa_name:
            await ctx.send(f"You already have {zanpa_name} equipped.")
            return
        # If there's a currently equipped Zanpakuto, return it to the inventory
        if current_equipped and current_equipped[0] is not None:
            inv_cursor.execute("UPDATE inv SET qty = qty + 1 WHERE user_id = ? AND item_name = ?", (user_id, current_equipped[0]))
        eco_cursor.execute("UPDATE eco SET zan = ? WHERE user_id = ?", (zanpa_name, user_id))
        inv_cursor.execute("UPDATE inv SET qty = qty - 1 WHERE user_id = ? AND item_name = ?", (user_id, zanpa_name))

        dbi.commit()
        dbi.close()
        dbe.commit()
        dbe.close()
        await ctx.send(f"You're now wielding {zanpa_name}..")
        async with ctx.typing():
            await ctx.send(f"Check out your stats using ,view to update them")


    @commands.command()
    async def unequip(self, ctx):
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        dbi = sqlite3.connect("inv.sqlite", timeout=50)
        eco_cursor = dbe.cursor()
        inv_cursor = dbi.cursor()
        user_id = ctx.author.id

        eco_cursor.execute("SELECT zan FROM eco WHERE user_id = ?", (user_id,))
        current_equipped = eco_cursor.fetchone()

        if not current_equipped or current_equipped[0] is None:
            await ctx.send("You don't have any weapon equipped.")
            return

        eco_cursor.execute("UPDATE eco SET zan = NULL WHERE user_id = ?", (user_id,))
        
        inv_cursor.execute("UPDATE inv SET qty = qty + 1 WHERE user_id = ? AND item_name = ?", (user_id, current_equipped[0]))

        dbe.commit()
        dbi.commit()
        dbe.close()
        dbi.close()

        await ctx.send(f"You have unequipped {current_equipped[0]} and returned it to your inventory.")
        async with ctx.typing():
            await ctx.send(f"Go see your stats and cry how much they decreased using ,view :D")


    @commands.command(aliases=["arsenal", "ars"])
    async def armory(self, ctx):
        user_id = ctx.author.id

        db = sqlite3.connect("inv.sqlite")
        cursor = db.cursor()

        cursor.execute("SELECT item_name, qty FROM armor WHERE user_id = ?", (user_id,))
        inventory = cursor.fetchall()

        if not inventory:
            await ctx.send("Your armory is empty, champion")
        else:
            inventory_text = "**Your Armory**:\n"
            for item, qty in inventory:
               inventory_text += f"{item}: {qty}\n"

            await ctx.send(inventory_text)


    @commands.command()
    async def armup(self, ctx, armor_name):
        dbi = sqlite3.connect("inv.sqlite", timeout=50)
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor=dbe.cursor()
        inv_cursor=dbi.cursor()
        user_id = ctx.author.id
        
        inv_cursor.execute("SELECT item_name FROM armor WHERE user_id = ? AND item_name = ?", (user_id, armor_name))
        armor_exists = inv_cursor.fetchone()

        if not armor_exists:
            await ctx.send(f"You don't have {armor_name} in your inventory lil guy")
            return

        eco_cursor.execute("SELECT arm FROM eco WHERE user_id = ?", (user_id,))
        current_equipped = eco_cursor.fetchone()

        if current_equipped and current_equipped[0] == armor_name:
            await ctx.send(f"You already have {armor_name} equipped.")
            return
        # If there's a currently equipped Zanpakuto, return it to the inventory
        if current_equipped and current_equipped[0] is not None:
            inv_cursor.execute("UPDATE armor SET qty = qty + 1 WHERE user_id = ? AND item_name = ?", (user_id, current_equipped[0]))
        eco_cursor.execute("UPDATE eco SET arm = ? WHERE user_id = ?", (armor_name, user_id))
        inv_cursor.execute("UPDATE armor SET qty = qty - 1 WHERE user_id = ? AND item_name = ?", (user_id, armor_name))

        dbi.commit()
        dbi.close()
        dbe.commit()
        dbe.close()
        await ctx.send(f"You are now using {armor_name}")
        async with ctx.typing():
            await ctx.send(f"Go update your stats using ,view")

    @commands.command()
    async def unarm(self, ctx):
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        dbi = sqlite3.connect("inv.sqlite", timeout=50)
        eco_cursor = dbe.cursor()
        inv_cursor = dbi.cursor()
        user_id = ctx.author.id

        eco_cursor.execute("SELECT arm FROM eco WHERE user_id = ?", (user_id,))
        current_equipped = eco_cursor.fetchone()

        if not current_equipped or current_equipped[0] is None:
            await ctx.send("You aren't armed with any off-hand equipment")
            return

        eco_cursor.execute("UPDATE eco SET arm = NULL WHERE user_id = ?", (user_id,))
        
        inv_cursor.execute("UPDATE armor SET qty = qty + 1 WHERE user_id = ? AND item_name = ?", (user_id, current_equipped[0]))

        dbe.commit()
        dbi.commit()
        dbe.close()
        dbi.close()

        await ctx.send(f"You have unequipped {current_equipped[0]} and returned it to your arsenal")
        async with ctx.typing():
            await ctx.send(f"Removed your {current_equipped[0]} and decreased ur stats, go check em using ,view")

async def setup(client):
    await client.add_cog(inv(client))