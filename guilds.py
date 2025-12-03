import discord
from discord.ext import commands
import sqlite3
import asyncio

class guild(commands.Cog):
    def __init__(self, client):
         self.client = client
         self.guild_db = sqlite3.connect("guilds.sqlite")
         self.guild_cursor = self.guild_db.cursor()
         self.guild_cursor.execute('''CREATE TABLE IF NOT EXISTS guilds (
                                    guild_id INTEGER PRIMARY KEY,
                                    guild_name TEXT,
                                    guild_description TEXT,
                                    guild_leader_id INTEGER,
                                    guild_status TEXT,
                                    guild_verification TEXT
                                   )''')
         self.guild_cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                                    id INTEGER PRIMARY KEY,
                                    user_id INTEGER,
                                    guild_name TEXT,
                                    role TEXT
                                );''')

         print("Guilds loaded")
         self.guild_db.commit()
         
                                

    @commands.command(aliases=['cg'])
    async def createguild(self, ctx):
        user_id = ctx.author.id
        guild_leader_id = user_id  
        guild_name = None
        guild_description = None

        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = dbe.cursor()
            
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(user_id),))
        current_guild = eco_cursor.fetchone()[0]

        if current_guild and current_guild != 'Wandering Traveler':
            await ctx.send('You are already in a guild, you shall not create another one while being in one.')
            dbe.close()
            return

        eco_cursor.execute('SELECT wallet FROM eco WHERE user_id=?', (str(user_id),))
        user_balance = eco_cursor.fetchone()[0]

        if user_balance < 10000:
            await ctx.send('You need at least 10,000 gold to create a guild, sire.')
            dbe.close()
            return

        await ctx.send('Welcome, Traveler.. Please give me a guild name')
        try:
            msg = await self.client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60.0)
            guild_name = msg.content

            dbe_check = sqlite3.connect("guilds.sqlite", timeout=50)
            guild_cursor_check = dbe_check.cursor()
            guild_cursor_check.execute("SELECT guild_name FROM guilds WHERE guild_name = ?", (guild_name,))
            existing_guild = guild_cursor_check.fetchone()
            dbe_check.close()

            if existing_guild:
                await ctx.send(f'The guild name "{guild_name}" already exists.. Sadge, kindly choose another name..')
                return

        except asyncio.TimeoutError:
            await ctx.send('Guild creation timed out.. Please try again..')
            return

        await ctx.send('Nice one, now give me a description for your guild')
        try:
            msg = await self.client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60.0)
            guild_description = msg.content
        except asyncio.TimeoutError:
            await ctx.send('Guild creation timed out.. Please try again..')
            return

        guild_db = sqlite3.connect("guilds.sqlite", timeout=50)
        guild_cursor = guild_db.cursor()
        guild_cursor.execute("INSERT INTO guilds (guild_name, guild_description, guild_leader_id, guild_status, guild_verification) VALUES (?, ?, ?, 'Open', 'Unverified')",
                            (guild_name, guild_description, guild_leader_id))
        guild_db.commit()
        guild_db.close()

        eco_cursor.execute('UPDATE eco SET wallet=wallet-10000 WHERE user_id=?', (str(user_id),))
        dbe.commit()
        dbe.close()

        eco_db = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = eco_db.cursor()
        eco_cursor.execute("UPDATE eco SET guild = ? WHERE user_id = ?", (guild_name, user_id))
        eco_db.commit()
        eco_db.close()

        await ctx.send(f'Congratulations {ctx.author.display_name}! You have successfully created the guild **{guild_name}**.')




    @commands.command(aliases=['lg'])
    async def leaveguild(self, ctx):
        user_id = ctx.author.id

        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = dbe.cursor()
        
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(user_id),))
        current_guild = eco_cursor.fetchone()[0]

        if not current_guild or current_guild == 'Wandering Traveler':
            await ctx.send('You are not currently in a guild.')
            dbe.close()
            return

        guild_db = sqlite3.connect("guilds.sqlite", timeout=50)
        guild_cursor = guild_db.cursor()
        guild_cursor.execute("SELECT guild_leader_id FROM guilds WHERE guild_name=?", (current_guild,))
        guild_leader_id = guild_cursor.fetchone()[0]

        is_guild_leader = guild_leader_id == user_id

        await ctx.send(f"Are you sure you want to leave the guild **{current_guild}**? Type 'Y' to confirm or 'N' to cancel.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.strip().lower() in ['y', 'n']

        try:
            msg = await self.client.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send('Confirmation timed out. Guild leave cancelled.')
            dbe.close()
            guild_db.close()
            return
        
        if msg.content.strip().lower() == 'n':
            await ctx.send('Guild leave cancelled, returning back to work..')
        elif msg.content.strip().lower() == 'y':
            if is_guild_leader:
                # Disband the guild
                guild_cursor.execute("DELETE FROM guilds WHERE guild_name=?", (current_guild,))
                guild_db.commit()

                # Delete all members of the disbanded guild from members table
                guild_cursor.execute("DELETE FROM members WHERE guild_name=?", (current_guild,))
                guild_db.commit()
                
                # Update all members of the disbanded guild in eco table
                eco_cursor.execute("UPDATE eco SET guild = 'Wandering Traveler' WHERE guild = ?", (current_guild,))
                dbe.commit()
                
                await ctx.send(f"The guild **{current_guild}** has been disbanded. Yet another demise :(")
            else:
                # Remove user from members table
                guild_cursor.execute("DELETE FROM members WHERE user_id=?", (user_id,))
                guild_db.commit()

                # Update user's guild status in eco table
                eco_cursor.execute("UPDATE eco SET guild = 'Wandering Traveler' WHERE user_id = ?", (user_id,))
                dbe.commit()
                
                await ctx.send(f"You have left the guild **{current_guild}**. How sad :(")

        dbe.close()
        guild_db.close()



    @commands.command(aliases=['jg'])
    async def joinguild(self, ctx):
        user_id = ctx.author.id

        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = dbe.cursor()
        
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(user_id),))
        current_guild = eco_cursor.fetchone()[0]

        if current_guild and current_guild != 'Wandering Traveler':
            await ctx.send('You are already in a guild. You cannot join another guild.')
            dbe.close()
            return

        guild_db = sqlite3.connect("guilds.sqlite", timeout=50)
        guild_cursor = guild_db.cursor()
        
        # Fetch available guilds and their member count
        guild_cursor.execute("""
            SELECT guild_name, (SELECT COUNT(*) FROM members WHERE members.guild_name = guilds.guild_name) AS member_count
            FROM guilds WHERE guild_status = 'Open'
        """)
        available_guilds = guild_cursor.fetchall()

        if not available_guilds:
            await ctx.send('There are no open guilds available to join at the moment.')
            dbe.close()
            guild_db.close()
            return

        guild_list = "\n".join([f"**{guild[0]}** ({guild[1] + 1}/30 members)" for guild in available_guilds])
        embed = discord.Embed(title="Available Guilds", description="Type the name of the guild to join it (case-sensitive).", color=0x8ac2cc)
        embed.set_image(url="https://images.wallpapersden.com/image/download/diablo-immortal-2022-gaming_bWllbm2UmZqaraWkpJRobWllrWdlZ2w.jpg")
        embed.add_field(name="Open Guilds", value=guild_list)
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', check=check, timeout=60.0)
            selected_guild = msg.content.strip()

            for guild in available_guilds:
                if selected_guild == guild[0]:
                    if guild[1] + 1>= 30:
                        await ctx.send('This guild has reached the maximum number of members (30). You cannot join this guild.')
                        dbe.close()
                        guild_db.close()
                        return
                    
                    # Insert into members table
                    guild_cursor.execute("INSERT INTO members (user_id, guild_name, role) VALUES (?, ?, 'Member')", (user_id, selected_guild))
                    guild_db.commit()

                    # Update eco table with guild
                    eco_cursor.execute("UPDATE eco SET guild = ? WHERE user_id = ?", (selected_guild, user_id))
                    dbe.commit()

                    await ctx.send(f"You have successfully joined the guild **{selected_guild}**.")
                    break
            else:
                await ctx.send('Invalid guild name. Guild join cancelled.')

        except asyncio.TimeoutError:
            await ctx.send('Guild join timed out. Please try again later.')

        dbe.close()
        guild_db.close()

    @commands.command(aliases=['gi'])
    async def guildinfo(self, ctx):
        user_id = ctx.author.id

        # Connect to the eco database
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = dbe.cursor()

        # Fetch the current guild of the user
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(user_id),))
        current_guild = eco_cursor.fetchone()[0]

        if not current_guild or current_guild == 'Wandering Traveler':
            await ctx.send('You are not currently in a guild.')
            dbe.close()
            return

        # Connect to the guilds database
        guild_db = sqlite3.connect("guilds.sqlite", timeout=50)
        guild_cursor = guild_db.cursor()

        # Fetch guild details
        guild_cursor.execute("SELECT guild_description, guild_leader_id, guild_status, guild_verification FROM guilds WHERE guild_name=?", (current_guild,))
        guild_info = guild_cursor.fetchone()

        guild_description = guild_info[0]
        guild_leader_id = guild_info[1]
        guild_status = guild_info[2]
        guild_verification = guild_info[3]

        # Set default values for optional roles
        vice_guild_leader = "Not Appointed"
        number_of_officers = "0"

        # Fetch the number of members and officers
        guild_cursor.execute("SELECT COUNT(*) FROM members WHERE guild_name=?", (current_guild,))
        number_of_members = guild_cursor.fetchone()[0]

        guild_cursor.execute("SELECT COUNT(*) FROM members WHERE guild_name=? AND role='Officer'", (current_guild,))
        number_of_officers_count = guild_cursor.fetchone()[0]
        if number_of_officers_count > 0:
            number_of_officers = number_of_officers_count

        guild_cursor.execute("SELECT user_id FROM members WHERE guild_name=? AND role='Vice_Leader'", (current_guild,))
        vice_guild_leader_info = guild_cursor.fetchone()
        if vice_guild_leader_info:
            vice_guild_leader = f"<@{vice_guild_leader_info[0]}>"

        # Create the embed message
        embed = discord.Embed(title=f"Guild Information", color=0x0a0a0a)
        embed.set_image(url="https://cdnb.artstation.com/p/assets/images/images/000/105/793/large/ricardo-luiz-mariano-final-ok.jpg?1443930209")
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text="Check out more guild related commands using ,helpguild or ,hg. Also make sure to look out for guild wars!")
        embed.add_field(name="Guild Name", value=current_guild)
        embed.add_field(name="Guild Description", value=guild_description, inline=False)
        embed.add_field(name="Guild Leader", value=f"<@{guild_leader_id}>", inline=False)
        embed.add_field(name="Vice Guild Leader", value=vice_guild_leader, inline=False)
        embed.add_field(name="Status", value=guild_status.capitalize(), inline=True)
        embed.add_field(name="Verification", value=guild_verification.capitalize(), inline=True)
        embed.add_field(name="Number of Members", value=f"{number_of_members + 1}/30", inline=False)
        embed.add_field(name="Number of Officers", value=f"{number_of_officers}/5", inline=False)
        
        # Send the embed message
        await ctx.send(embed=embed)

        # Close the database connections
        dbe.close()
        guild_db.close()


    @commands.command(aliases=['gp'])
    async def guildpromote(self, ctx, member: discord.Member):
        user_id = ctx.author.id
        member_id = member.id

        # Connect to the eco database
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = dbe.cursor()

        # Fetch the current guild of the user
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(user_id),))
        current_guild = eco_cursor.fetchone()[0]

        if not current_guild or current_guild == 'Wandering Traveler':
            await ctx.send('You are not currently in a guild.')
            dbe.close()
            return

        # Connect to the guilds database
        guild_db = sqlite3.connect("guilds.sqlite", timeout=50)
        guild_cursor = guild_db.cursor()

        # Check if the user is the guild leader
        guild_cursor.execute("SELECT guild_leader_id FROM guilds WHERE guild_name=?", (current_guild,))
        guild_leader_id = guild_cursor.fetchone()[0]

        if guild_leader_id != user_id:
            await ctx.send('Only the guild leader can use this command.')
            dbe.close()
            guild_db.close()
            return

        # Check if the member is in the same guild
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(member_id),))
        member_guild = eco_cursor.fetchone()[0]

        if member_guild != current_guild:
            await ctx.send('The member is not in your guild.')
            dbe.close()
            guild_db.close()
            return

        # Fetch the current role of the member
        guild_cursor.execute('SELECT role FROM members WHERE user_id=? AND guild_name=?', (member_id, current_guild))
        member_role = guild_cursor.fetchone()[0]

        # Determine the new role
        if member_role == 'Member':
            new_role = 'Officer'
        elif member_role == 'Officer':
            new_role = 'Vice_Leader'
        else:
            await ctx.send('The member cannot be promoted further.')
            dbe.close()
            guild_db.close()
            return

        # Update the member's role in the members table
        guild_cursor.execute('UPDATE members SET role=? WHERE user_id=? AND guild_name=?', (new_role, member_id, current_guild))
        guild_db.commit()

        await ctx.send(f'{member.display_name} has been promoted to {new_role}.')

        # Close the database connections
        dbe.close()
        guild_db.close()


    @commands.command(aliases=['gd'])
    async def guilddemote(self, ctx, member: discord.Member):
        user_id = ctx.author.id
        member_id = member.id

        # Connect to the eco database
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = dbe.cursor()

        # Fetch the current guild of the user and the target member
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(user_id),))
        user_guild = eco_cursor.fetchone()[0]

        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(member_id),))
        member_guild = eco_cursor.fetchone()[0]

        if user_guild != member_guild:
            await ctx.send(f'{member.display_name} is not in your guild.')
            dbe.close()
            return

        # Connect to the guilds database
        guild_db = sqlite3.connect("guilds.sqlite", timeout=50)
        guild_cursor = guild_db.cursor()

        # Check if the command issuer is the guild leader
        guild_cursor.execute("SELECT guild_leader_id FROM guilds WHERE guild_name=?", (user_guild,))
        guild_leader_id = guild_cursor.fetchone()[0]

        if user_id != guild_leader_id:
            await ctx.send('Only the guild leader can demote members.')
            dbe.close()
            guild_db.close()
            return

        # Fetch the role of the target member
        guild_cursor.execute("SELECT role FROM members WHERE user_id=? AND guild_name=?", (member_id, user_guild))
        current_role = guild_cursor.fetchone()[0]

        if current_role == "Member":
            await ctx.send(f'{member.display_name} is already a member and cannot be demoted further.')
            dbe.close()
            guild_db.close()
            return

        new_role = "Member" if current_role == "Officer" else "Officer"

        # Update the role of the member in the members table
        guild_cursor.execute("UPDATE members SET role=? WHERE user_id=? AND guild_name=?", (new_role, member_id, user_guild))
        guild_db.commit()

        await ctx.send(f'{member.display_name} has been demoted to {new_role}.')

        dbe.close()
        guild_db.close()


    @commands.command(aliases=['gk'])
    async def guildkick(self, ctx, member: discord.Member):
        user_id = ctx.author.id
        target_id = member.id

        # Connect to the eco database
        dbe = sqlite3.connect("eco.sqlite", timeout=50)
        eco_cursor = dbe.cursor()

        # Fetch the current guild of the user
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(user_id),))
        current_guild = eco_cursor.fetchone()[0]

        if not current_guild or current_guild == 'Wandering Traveler':
            await ctx.send('You are not currently in a guild.')
            dbe.close()
            return

        # Connect to the guilds database
        guild_db = sqlite3.connect("guilds.sqlite", timeout=50)
        guild_cursor = guild_db.cursor()

        # Fetch guild leader ID
        guild_cursor.execute("SELECT guild_leader_id FROM guilds WHERE guild_name=?", (current_guild,))
        guild_leader_id = guild_cursor.fetchone()[0]

        # Check if the command issuer is the guild leader
        if user_id != guild_leader_id:
            await ctx.send('Only the guild leader can kick members from the guild, you peasant.')
            dbe.close()
            guild_db.close()
            return

        # Check if trying to kick oneself
        if user_id == target_id:
            await ctx.send('You cannot kick yourself from the guild, sire.')
            dbe.close()
            guild_db.close()
            return

        # Fetch the guild of the target member
        eco_cursor.execute('SELECT guild FROM eco WHERE user_id=?', (str(target_id),))
        target_guild = eco_cursor.fetchone()[0]

        if target_guild != current_guild:
            await ctx.send('The specified user is not a member of your guild.')
            dbe.close()
            guild_db.close()
            return

        # Remove the member from the guild
        eco_cursor.execute("UPDATE eco SET guild = 'Wandering Traveler' WHERE user_id = ?", (str(target_id),))
        dbe.commit()

        guild_cursor.execute("DELETE FROM members WHERE user_id = ?", (str(target_id),))
        guild_db.commit()

        await ctx.send(f"{member.mention} has been kicked from the guild **{current_guild}**.")

        # Close the database connections
        dbe.close()
        guild_db.close()

   
async def setup(client):
    await client.add_cog(guild(client))

