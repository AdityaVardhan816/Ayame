import discord
from discord.ext import commands
import asyncio
import sqlite3
import random

class ShopDropdown(discord.ui.Select):
    def __init__(self, user_id):
        self.user_id = user_id
        options = [
            discord.SelectOption(label="Common Weapons", description="Cheap and Rusty"),
            discord.SelectOption(label="Rare Weapons ", description="Best for Rookies"),
            discord.SelectOption(label="Epic Weapons", description="Immense Output"),
            discord.SelectOption(label="Legendary Weapons", description="Laid by Gods")
            ]
        super().__init__(placeholder="Choose your Weapon..", min_values=1, max_values=1, options=options)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return
        selected_weapon = self.values[0]
        embed = discord.Embed(title=f"{selected_weapon}", color=0x0a0a0a)
        
        
        if selected_weapon == "Common Weapons":
            embed.description = "Greetings champion! Take a look around, tell me what you like, buy it using the ``,blbuy (id)`` command and don't forget to visit again! <:box:1186673907319705844>"
            embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/05/diablo-4-season-4-blacksmith-keyart.jpg")
            embed.set_footer(text="For more info on a particular weapon, head over to the info page")
            
            db=sqlite3.connect("shop.sqlite")
            cursor=db.cursor()
            cursor.execute("SELECT * FROM shop")
            items=cursor.fetchall()[:15]
            shop_list = '\n'.join([f'{item[0]}. **{item[1]}** - {item[2]} Gold' for item in items])
            
            embed.add_field(name="Weapons", value=shop_list)
        if selected_weapon == "Rare Weapons":
            embed.description = "Greetings champion! Take a look around, tell me what you like, buy it using the ``,blbuy (id)`` command and don't forget to visit again! <:box:1186673907319705844>"
            embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/05/diablo-4-season-4-blacksmith-keyart.jpg")
            embed.set_footer(text="For more info on a particular weapon, head over to the info page")
            
            db=sqlite3.connect("shop.sqlite")
            cursor=db.cursor()
            cursor.execute("SELECT * FROM shop")
            items=cursor.fetchall()[15:30]
            shop_list = '\n'.join([f'{item[0]}. **{item[1]}** - {format(item[2], ",")} Gold' for item in items])
            
            embed.add_field(name="Weapons", value=shop_list)
        if selected_weapon == "Epic Weapons":
            embed.description = "Greetings champion! Take a look around, tell me what you like, buy it using the ``,blbuy (id)`` command and don't forget to visit again! <:box:1186673907319705844>"
            embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/05/diablo-4-season-4-blacksmith-keyart.jpg")
            embed.set_footer(text="For more info on a particular weapon, head over to the info page")

            db=sqlite3.connect("shop.sqlite")
            cursor=db.cursor()
            cursor.execute("SELECT * FROM shop")
            items=cursor.fetchall()[30:40]
            shop_list = '\n'.join([f'{item[0]}. **{item[1]}** - {format(item[2], ",")} Gold' for item in items])
            embed.add_field(name="Weapons", value=shop_list)
        if selected_weapon == "Legendary Weapons":
            embed.description = "Greetings champion! Take a look around, tell me what you like, buy it using the ``,blbuy (id)`` command and don't forget to visit again! <:box:1186673907319705844>"
            embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/05/diablo-4-season-4-blacksmith-keyart.jpg")
            embed.set_footer(text="For more info on a particular weapon, head over to the info page")
            embed.add_field(name="Weapons", value="Coming Soon")

        view = ConfirmView(selected_weapon, user_id=interaction.user.id)
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
        super().__init__(label="Exit", style=discord.ButtonStyle.red)
        self.selected_class = selected_class
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Leaving the shop.. ", ephemeral=False)
        await asyncio.sleep(2)
        await interaction.message.delete()
    

class BackButton(discord.ui.Button):
    def __init__(self, user_id):
        super().__init__(label="Back to Weapons..", style=discord.ButtonStyle.blurple)
        self.user_id=user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return
        view = discord.ui.View()
        view.add_item(ShopDropdown(self.user_id))
        await interaction.response.edit_message(view=view)

class shop(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        db=sqlite3.connect("shop.sqlite")
        cursor=db.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS shop (
                       item_id INTERGER PRIMARY KEY,
                       item_name TEXT,
                       item_price INTERGER,
                       item_attack INTERGER
        ) ''')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (1, "Holy_Sword", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (2, "Abyssal_Axe", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (3, "Hunters_Bow", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (4, "Spectral_Mace", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (5, "Long_Greatsword", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (6, "Royal_Staff", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (7, "Corrupted_Daggers", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (8, "Burning_Warblade", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (9, "Shadowy_Ruins", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (10, "Spirit_Claws", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (11, "Death_Mantle", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (12, "Kings_Sabre", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (13, "Sharp_Katar", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (14, "Bloody_Sword", 100, 20)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (15, "Quick_Pick", 100, 20)')

        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (16, "Mithril_Rod", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (17, "Thundering_Hammer", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (18, "Starsung_Bow", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (19, "Incanters_Flow", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (20, "Goblins_Gold", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (21, "Necrium_Blade", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (22, "Tainted_Fork", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (23, "Dragon_Spear", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (24, "Arcanite_Ripper", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (25, "Spectral_Cutlass", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (26, "Runed_Shortsword", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (27, "Calamity_Grasp", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (28, "Boundless_Glaive", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (29, "Runic_Axe", 5000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (30, "Tolins_Goblet", 5000, 40)')

        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (31, "Swinetusk_Shank", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (32, "Super_Collider", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (33, "Trueaim_Crescent", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (34, "Cog_Hammer", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (35, "Primal_Staff", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (36, "Felstring_Harp", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (37, "Argent_Lance", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (38, "Azsharan_Trident", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (39, "Ceremonial_Maul", 15000, 40)')
        cursor.execute('INSERT OR IGNORE INTO shop (item_id, item_name, item_price, item_attack) VALUES (40, "Obsidian_Shard", 15000, 40)')
        


        cursor.execute(''' CREATE TABLE IF NOT EXISTS df (
                       item_id INTERGER PRIMARY KEY,
                       item_name TEXT,
                       item_price INTERGER,
                       item_attack INTERGER,
                       item_defense INTERGER)
        ''')
        cursor.execute('INSERT OR IGNORE INTO df (item_id, item_name, item_price, item_attack, item_defense) VALUES (51, "Blazing_Shield", 300, 0, 40)')
        cursor.execute('INSERT OR IGNORE INTO df (item_id, item_name, item_price, item_attack, item_defense) VALUES (52, "Spiked_Shield", 300, 10, 20)')
        cursor.execute('INSERT OR IGNORE INTO df (item_id, item_name, item_price, item_attack, item_defense) VALUES (53, "Crackling_Shield", 300, 0, 40)')
        cursor.execute('INSERT OR IGNORE INTO df (item_id, item_name, item_price, item_attack, item_defense) VALUES (54, "Wooden_Wheel", 300, 10, 20)')
        cursor.execute('INSERT OR IGNORE INTO df (item_id, item_name, item_price, item_attack, item_defense) VALUES (55, "Amethyst_Dagger", 300, 20, 0)')
        

        print("Shop loaded")
        db.commit()
        cursor.close()
        db.close()


    @commands.command()
    async def shop(self, ctx):
        embed = discord.Embed(title="Marketplace", description="Gather round' Step right up and behold the finest wares in all of Ayame! From enchanted weapons to bulky shields, we have everything you need to conquer your next quest. Dont miss our special deals fortune favors the prepared!", color=0xffcb52)
        embed.set_image(url="https://i.pinimg.com/736x/d1/f4/48/d1f44819a3b44d412def2b20c345566e.jpg")
        embed.add_field(name="Blacksmith", value="The Smithery offers you weapons from all your classes, thus increasing your potential and attack, check out the blacksmith using ``,blacksmith`` or ``,bl``. You can buy items from the smithery using ``,blbuy (id)``. The id of the weapons will be written next to their names.", inline=False)
        embed.add_field(name="Dwarvenfield", value="The Dwarvenfield offers you your off-hand slot equipment, ranging from yet another weapon to shields and armor, forged by the elder dwarves, these equipment are very tough to break, check out the dwarvenfield using ``,dwarvenfield`` or ``,df``. You can buy items from the dwarvenfield using ``,dfbuy (id)``. The id of the weapons will be written next to their names.", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['bl'])
    async def blacksmith(self,ctx):
        db=sqlite3.connect("shop.sqlite")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM shop")
        items=cursor.fetchall()
        embed=discord.Embed(title="The Blacksmith", color=0xc08256, description="Greetings champion! Take a look around, tell me what you like, buy it using the ``,blbuy (id)`` command and don't forget to visit again! <:box:1186673907319705844> ")
        embed.set_image(url="https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/05/diablo-4-season-4-blacksmith-keyart.jpg")
        embed.add_field(name="", value="Take the type of weapon you want from the given dropdown, there are four different types of weapons available at my smithery, namely Common, Rare, Epic and Legendary, of course the last one being the most expensive haha..")
        embed.set_footer(text="For more info on a particular weapon, head over to the info page")
        view = discord.ui.View()
        view.add_item(ShopDropdown(ctx.author.id))
        await ctx.send(embed=embed, view=view)

    @commands.command(aliases=['df'])
    async def dwarvenfield(self,ctx):
        db=sqlite3.connect("shop.sqlite")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM df")
        items=cursor.fetchall()
        shop_list = '\n'.join([f'{item[0]}. **{item[1]}** - {item[2]} Gold' for item in items])
        embed=discord.Embed(title="The Dwarvenfield", color=0x86bee4, description="Welcome to my humble abode, where sturdy goods and stout craftsmanship meet. What can I forge for ye today? My forge stands ready to serve. Take yer time, and to buy something, do ``,dfbuy (id)``. <:box:1186673907319705844> ")
        embed.set_image(url="https://preview.redd.it/mountain-king-fan-art-i-tried-to-mimic-the-hearthstone-art-v0-812sqbhnp6ec1.png?width=1080&crop=smart&auto=webp&s=26f80b982f546a4e26c91ba2632af833bd2b03cf")
        embed.set_footer(text="For more info on a particular weapon, head over to the info page")
        embed.add_field(name="Off-Hands", value=shop_list)
        await ctx.send(embed=embed)



    

async def setup(client):
    await client.add_cog(shop(client))