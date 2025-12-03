import discord
from discord.ext import commands
from discord.ext import commands
from discord.ui import Button, View
import sqlite3
import asyncio
import random
import aiosqlite

class AvailableActionsButton(View):
    def __init__(self, challenger, challengee):
        super().__init__(timeout=None)
        self.challenger = challenger
        self.challengee = challengee
        self.challenger_id = challenger.id
        self.challengee_id = challengee.id
        self.challenger_action = None
        self.challengee_action = None
        self.challenger_move_selected = False

    async def fetch_user_skills(self, user_id):
        conn = sqlite3.connect('skills.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT skill_name FROM user_skills WHERE user_id = ?", (user_id,))
        skills = cursor.fetchall()
        conn.close()
        return [skill[0] for skill in skills]

    async def show_available_actions(self, interaction):
        skills = await self.fetch_user_skills(interaction.user.id)
        action_view = View(timeout=None)
        action_view.add_item(AttackButton(self))
        for i, skill in enumerate(skills[:5]):
            action_view.add_item(SkillButton(skill, i+1, self))
        action_view.add_item(ForfeitButton(self))

        desc = "Choose your Action:"
        await interaction.response.send_message(desc, view=action_view, ephemeral=True)

    @discord.ui.button(label="Available Actions", style=discord.ButtonStyle.primary)
    async def available_actions_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user not in [self.challenger, self.challengee]:
            await interaction.response.send_message("You can't view the available actions for this duel!", ephemeral=True)
            return
        
        if interaction.user == self.challengee and not self.challenger_move_selected:
            await interaction.response.send_message(f"Hold on lil bro, wait till {self.challenger} picks their move, one by one.", ephemeral=True)
            return
        
        await self.show_available_actions(interaction)

    async def check_both_actions_selected(self, interaction: discord.Interaction):
        if self.challenger_action and self.challengee_action:
            embed = discord.Embed(
                title=f"{self.challenger} and {self.challengee} have exchanged blows!",
                description="",
                color=discord.Color.green()
            )

        player1_damage_dealt = 1
        player2_damage_dealt = 1
        player1_damage_taken = 1
        player2_damage_taken = 1
        
        player1_desc = ""
        player2_desc = ""
        player1_sideeff = ""
        player2_sideeff = ""

        conn = sqlite3.connect("stats.sqlite")
        c = conn.cursor()
        c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (self.challenger.id,))
        challenger_hp = c.fetchone()[0]
        c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (self.challengee.id,))
        challengee_hp = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT speed FROM stats WHERE user_id = ?", (self.challenger.id,))
        user_speed = c.fetchone()[0]
        conn.close()

        conn = sqlite3.connect('stats.sqlite')
        c = conn.cursor()
        c.execute("SELECT speed FROM stats WHERE user_id = ?", (self.challengee.id,))
        opp_speed = c.fetchone()[0]
        conn.close()

# IF BOTH FORFEIT --------------------------------------------------------------------------------------------

        if self.challenger_action == "forfeit" and self.challengee_action == "forfeit":
            user = interaction.user
            winner = self.challengee if user == self.challenger else self.challenger
            loser = user

            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("SELECT hp FROM stats WHERE user_id = ?", (self.challenger_id,))
            original_challenger_hp = c.fetchone()[0]
            c.execute("SELECT hp FROM stats WHERE user_id = ?", (self.challengee_id,))
            original_challengee_hp = c.fetchone()[0]
            conn.close()


            embed_damage = discord.Embed(
            title="The Mask of Humiliation..",
                color=discord.Color.red()
            )
            embed_damage.add_field(name="Forfeit!", value=f"{loser.mention} and {winner.mention} have both forfeited!", inline=False)
            embed_damage.add_field(name="", value="What a bunch of losers xd")
            embed_damage.set_image(url="https://hearthstone.wiki.gg/images/thumb/5/54/Helm_of_Humiliation_full.jpg/462px-Helm_of_Humiliation_full.jpg")

            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("UPDATE tempstats SET hp = ? WHERE user_id = ?", (original_challenger_hp, self.challenger_id))
            c.execute("UPDATE tempstats SET hp = ? WHERE user_id = ?", (original_challengee_hp, self.challengee_id))
            conn.commit()
            conn.close()

            await interaction.channel.send(embed=embed_damage)
            return

# IF 1 USER FORFEITS --------------------------------------------------------------------------------------------

        elif self.challenger_action == "forfeit" or self.challengee_action == "forfeit":
            user = interaction.user
            if self.challenger_action == "forfeit":
                winner = self.challengee
                loser = self.challenger
            elif self.challengee_action == "forfeit":
                winner = self.challenger
                loser = self.challengee

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT hp FROM stats WHERE user_id = ?", (self.challenger_id,))
                original_challenger_hp = c.fetchone()[0]
                c.execute("SELECT hp FROM stats WHERE user_id = ?", (self.challengee_id,))
                original_challengee_hp = c.fetchone()[0]
                conn.close()


                embed_damage = discord.Embed(
                title="The Mask of Humiliation..",
                    color=discord.Color.red()
                )
                embed_damage.add_field(name="Forfeit!", value=f"{loser.mention} has forfeited!", inline=False)
                embed_damage.add_field(name="Victory by Resignation!", value=f"{winner.mention} has won the battle!", inline=False)
                embed_damage.set_image(url="https://hearthstone.wiki.gg/images/thumb/5/54/Helm_of_Humiliation_full.jpg/462px-Helm_of_Humiliation_full.jpg")

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id = ?", (original_challenger_hp, self.challenger_id))
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id = ?", (original_challengee_hp, self.challengee_id))
                conn.commit()
                conn.close()

                await interaction.channel.send(embed=embed_damage)
                return
        
# IF BOTH THE USERS ATTACK --------------------------------------------------------------------------------------------
        elif self.challenger_action == "atk" and self.challengee_action == "atk":
            user = self.challenger
            opp = self.challengee

            if self.challenger_action and self.challengee_action:
                user_id = user.id
                opp_id = opp.id 
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT base_attack FROM stats WHERE user_id=?", (user_id,))
                user_attack = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT strength FROM stats WHERE user_id=?", (user_id,))
                user_strength = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT speed FROM stats WHERE user_id=?", (user_id,))
                user_speed = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT base_attack FROM stats WHERE user_id=?", (opp_id,))
                opp_attack = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT strength FROM stats WHERE user_id=?", (opp_id,))
                opp_strength = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT speed FROM stats WHERE user_id=?", (opp_id,))
                opp_speed = c.fetchone()[0]
                conn.close()

                user_damage_min = ((user_attack - 30) - (opp_armor)) + (user_strength)*2 - 100
                user_damage_max = ((user_attack + 30) - (opp_armor)) + (user_strength)*2 - 120
                if user_damage_min < 0:
                    user_damage_min = 0
                if user_damage_max < 0:
                    user_damage_max = 10

                opp_damage_min = ((opp_attack - 30) - (user_armor)) + (opp_strength)*2 - 100
                opp_damage_max = ((opp_attack + 30) - (user_armor)) + (opp_strength)*2 - 120
                if opp_damage_min < 0:
                    opp_damage_min = 0
                if opp_damage_max < 0:
                    opp_damage_max = 10
                
                user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                opp_damage_dealt = random.randint(opp_damage_min, opp_damage_max)

                self.user_hp -= opp_damage_dealt
                self.opp_hp -= user_damage_dealt

                player1_damage_dealt = user_damage_dealt
                player2_damage_taken = self.opp_hp
                player2_damage_dealt = opp_damage_dealt
                player1_damage_taken = self.user_hp

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.user_hp, user_id,))
                conn.commit()
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

                if user_damage_dealt < 50:
                    player1_desc = f"**{user}** dealt a measly normal blow"
                elif user_damage_dealt < 100 and user_damage_dealt > 50:
                    player1_desc = f"**{user}** did a crazy swing and hit **{opp}**"
                elif user_damage_dealt < 150 and user_damage_dealt > 100:
                    player1_desc = f"**{user}** dealt a crushing blow to **{opp}**"
                elif user_damage_dealt < 200 and user_damage_dealt > 150:
                    player1_desc = f"**{user}** massacred **{opp}** with a godly strike"
                elif user_damage_dealt > 200:
                    player1_desc = f"**{user}** obliterated the hell out of **{opp}**"
                player1_sideeff = ""

                if opp_damage_dealt < 50:
                    player2_desc = f"**{opp}** dealt a measly normal blow"
                elif opp_damage_dealt < 100 and opp_damage_dealt > 50:
                    player2_desc = f"**{opp}** did a crazy swing and hit **{user}**"
                elif opp_damage_dealt < 150 and opp_damage_dealt > 100:
                    player2_desc = f"**{opp}** dealt a crushing blow to **{user}**"
                elif opp_damage_dealt < 200 and opp_damage_dealt > 150:
                    player2_desc = f"**{opp}** massacred **{user}** with a godly strike"
                elif opp_damage_dealt > 200:
                    player2_desc = f"**{opp}** obliterated the hell out of **{user}**"
                player2_sideeff = ""

        
# IF 1 USER ATTACKS --------------------------------------------------------------------------------------------

        elif self.challenger_action == "atk" or self.challengee_action == "atk":
            if self.challenger_action == "atk":
                user = self.challenger
                opp = self.challengee
            else:
                user = self.challengee
                opp = self.challenger
            if self.challenger_action and self.challengee_action:
                user_id = user.id
                opp_id = opp.id 
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT base_attack FROM stats WHERE user_id=?", (user_id,))
                user_attack = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT strength FROM stats WHERE user_id=?", (user_id,))
                user_strength = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT speed FROM stats WHERE user_id=?", (user_id,))
                user_speed = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT base_attack FROM stats WHERE user_id=?", (opp_id,))
                opp_attack = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT strength FROM stats WHERE user_id=?", (opp_id,))
                opp_strength = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT speed FROM stats WHERE user_id=?", (opp_id,))
                opp_speed = c.fetchone()[0]
                conn.close()

                user_damage_min = ((user_attack - 30) - (opp_armor)) + (user_strength)*2 - 100
                user_damage_max = ((user_attack + 30) - (opp_armor)) + (user_strength)*2 - 120
                if user_damage_min < 0:
                    user_damage_min = 0
                if user_damage_max < 0:
                    user_damage_max = 10

                user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                self.opp_hp -= user_damage_dealt

                if user == self.challenger:
                    player1_damage_dealt = user_damage_dealt
                    player2_damage_taken = self.opp_hp  
                else:
                    player2_damage_dealt = user_damage_dealt
                    player1_damage_taken = self.opp_hp

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

                desc = f"{user} barely scratched {opp}"

                if user_damage_dealt < 50:
                    desc = f"{user} dealt a measly normal blow"
                elif user_damage_dealt < 100 and user_damage_dealt > 50:
                    desc = f"{user} did a crazy swing and hit {opp}"
                elif user_damage_dealt < 150 and user_damage_dealt > 100:
                    desc = f"{user} dealt a crushing blow to {opp}"
                elif user_damage_dealt < 200 and user_damage_dealt > 150:
                    desc = f"{user} massacred {opp} with a godly strike"
                elif user_damage_dealt > 200:
                    desc = f"{user} obliterated the hell out of {opp}"

                if user == self.challenger:
                    player1_desc = desc
                    player1_sideeff = ""
                else:
                    player2_desc = desc
                    player2_sideeff = ""

                

# IF 1 USER SKILLS ----------------------------------------------------------------------------------------------

#CRUSADER STRIKE (#13) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Crusader Strike" or self.challengee_action == "Crusader Strike":
            if self.challenger_action == "Crusader Strike":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Crusader Strike":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 40

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                a = (f"{opp} is Stunned!", f"{opp} is Stunned!", f"{opp} is Stunned!", f"{opp} can still stand up..", f"{opp} can still stand up..", f"{opp} is still in their senses..", f"{opp} didn't get a concussion yet..", f"{opp} didn't faint yet..", f"{opp} didn't faint yet..", f"{opp} is still standing..")
                b = random.choice(a)
                if user == self.challenger:
                    player1_desc = f"**{user}** used **Crusader Strike**, {b}"
                else:
                    player2_desc = f"**{user}** used **Crusader Strike**, {b}"
                if b == f"{opp} is Stunned!":
                    cstrike_sideeff = f"**{opp}** is **STUNNED**, they are too dizzy!"
                    if user == self.challenger:
                        player1_sideeff = cstrike_sideeff
                        player2_damage_dealt = 0
                        player1_damage_taken = challenger_hp
                        conn = sqlite3.connect('stats.sqlite')
                        c = conn.cursor()
                        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (challenger_hp, user_id,))
                        conn.commit()
                        conn.close()
                    else:
                        player2_sideeff = cstrike_sideeff
                        player1_damage_dealt = 0
                        player2_damage_taken = challengee_hp
                        conn = sqlite3.connect('stats.sqlite')
                        c = conn.cursor()
                        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (challengee_hp, user_id,))
                        conn.commit()
                        conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#DIVINE LIGHT (#14) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Divine Light" or self.challengee_action == "Divine Light":
            if self.challenger_action == "Divine Light":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Divine Light":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                opp_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                opp_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                
                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    conn = sqlite3.connect('stats.sqlite')
                    c = conn.cursor()
                    c.execute("SELECT rightm FROM tempstats WHERE user_id = ?", (user_id,))
                    right = c.fetchone()[0]
                    conn.close()

                    if right == 0:
                        skill_damage = 40
                    elif right != 0:
                        skill_damage = 60
                        right -= 1
                    conn = sqlite3.connect('stats.sqlite')
                    c = conn.cursor()
                    c.execute("UPDATE tempstats SET rightm = ? WHERE user_id=?", (right, user_id,))
                    conn.commit()
                    conn.close()
                    opp_damage_min = skill_damage + ((opp_energy - 30) - (user_armor)) + (opp_intelligence/2)
                    opp_damage_max = skill_damage + ((opp_energy + 30) - (user_armor)) + (opp_intelligence/2)
                    if opp_damage_min < 0:
                        opp_damage_min = 0
                    if opp_damage_max < 0:
                        opp_damage_max = 10

                    opp_damage_dealt = random.randint(opp_damage_min, opp_damage_max)
                    opp_damage_dealt += 30
                    user_damage_dealt = 0
                    self.user_hp -= opp_damage_dealt

                health = sqlite3.connect("stats.sqlite")
                h_cur = health.cursor()
                h_cur.execute("SELECT hp FROM stats WHERE user_id = ?", (user_id,))
                hp = h_cur.fetchone()[0]
                ahp = hp/2
                bhp = int(ahp)
                health.close()
                
                if user == self.challenger:
                    player1_damage_dealt = user_damage_dealt
                    player2_damage_taken = self.opp_hp
                    player1_damage_taken = self.user_hp
                    if player1_damage_taken < 0:
                        player1_damage_taken = self.user_hp
                    else:
                        player1_damage_taken = self.user_hp + bhp
                        if self.user_hp > hp:
                            player1_damage_taken = hp
                        upd_cur = sqlite3.connect("stats.sqlite")
                        hea_cur = upd_cur.cursor()
                        hea_cur.execute("UPDATE tempstats SET hp = ? WHERE user_id = ?", (player1_damage_taken, user_id,))
                        upd_cur.commit()
                        upd_cur.close()
                    player2_damage_dealt = opp_damage_dealt
                else:
                    player2_damage_dealt = user_damage_dealt
                    player1_damage_taken = self.opp_hp
                    player2_damage_taken = self.user_hp
                    if player2_damage_taken < 0:
                        player2_damage_taken = self.user_hp
                    else:
                        player2_damage_taken = self.user_hp + bhp
                        if self.user_hp > hp:
                            player2_damage_taken = hp
                        upd_cur = sqlite3.connect("stats.sqlite")
                        hea_cur = upd_cur.cursor()
                        hea_cur.execute("UPDATE tempstats SET hp = ? WHERE user_id = ?", (player1_damage_taken, user_id,))
                        upd_cur.commit()
                        upd_cur.close()
                    player1_damage_dealt = opp_damage_dealt

                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Divine Light**, {self.challenger} has called upon the light and healed themselves by **{bhp}**"
                else:
                    player2_desc = f"**{self.challengee}** used **Divine Light**, {self.challengee} has called upon the light and healed themselves by **{bhp}**"

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#AVENGING WRATH (#15) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Avenging Wrath" or self.challengee_action == "Avenging Wrath":
            if self.challenger_action == "Avenging Wrath":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Avenging Wrath":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                noofturns = random.randint(2,4)

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET rightm = ? WHERE user_id=?", (noofturns, user_id,))
                conn.commit()
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 40
                    
                    conn = sqlite3.connect('stats.sqlite')
                    c = conn.cursor()
                    c.execute("SELECT rightm FROM tempstats WHERE user_id = ?", (user_id,))
                    right = c.fetchone()[0]
                    conn.close()

                    if right == 0:
                        skill_damage = 40
                        
                    elif right != 0:
                        skill_damage = 60
                        right -= 1
                    conn = sqlite3.connect('stats.sqlite')
                    c = conn.cursor()
                    c.execute("UPDATE tempstats SET rightm = ? WHERE user_id=?", (right, user_id,))
                    conn.commit()
                    conn.close()

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                if user == self.challenger:
                    player1_desc = f"**{user}** used **Avenging Wrath**, {self.challenger} has entered the righteousness mode and will deal increased spell damage for **{noofturns}** turns"
                else:
                    player2_desc = f"**{user}** used **Avenging Wrath**, {self.challengee} has entered the righteousness mode and will deal increased spell damage for **{noofturns}** turns"
                
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#VANISH (#19)----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Vanish" or self.challengee_action == "Vanish":
            if self.challenger_action == "Vanish":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Vanish":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 0
                    user_damage_dealt = 0
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                        player1_damage_taken = self.user_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp
                        player2_damage_taken = self.user_hp

                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Vanish**, {self.challenger} has enshrouded themself in a concealing smoke"
                else:
                    player2_desc = f"**{user}** used **Vanish**, {self.challengee} has enshrouded themself in a concealing smoke"

                player1_damage_dealt = 0
                player2_damage_dealt = 0
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.user_hp, user_id,))
                conn.commit()
                conn.close()
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#EVISCERATE (#20)----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Eviscerate" or self.challengee_action == "Eviscerate":
            if self.challenger_action == "Eviscerate":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Eviscerate":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                evi = sqlite3.connect("eco.sqlite")
                evi_cur = evi.cursor()
                evi_cur.execute("SELECT zan FROM eco WHERE user_id = ?", (user_id,))
                wep = evi_cur.fetchone()[0]
                evi.close()

                evi = sqlite3.connect("eco.sqlite")
                evi_cur = evi.cursor()
                evi_cur.execute("SELECT arm FROM eco WHERE user_id = ?", (user_id,))
                off = evi_cur.fetchone()[0]
                evi.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 20

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                if user == self.challenger:
                    if not wep or wep == "Unidentified Weapon":
                        player1_desc = f"**{self.challenger}** used **Eviscerate**, sadly they aren't holding a weapon.."
                        user_damage_dealt = 0
                    elif wep and (not off or off == "Unidentified Weapon"):
                        player1_desc = f"**{self.challenger}** used **Eviscerate**, they are holding a single weapon.."
                    elif wep and off:
                        player1_desc = f"**{self.challenger}** used **Eviscerate**, they are holding dual weapons! Damage is **doubled!**"
                        user_damage_dealt = user_damage_dealt*2 - 50
                else:
                    if not wep or wep == "Unidentified Weapon":
                        player2_desc = f"**{self.challengee}** used **Eviscerate**, sadly they aren't holding a weapon.."
                        user_damage_dealt = 0
                    elif wep and (not off or off == "Unidentified Weapon"):
                        player2_desc = f"**{self.challengee}** used **Eviscerate**, they are holding a single weapon.."
                    elif wep and off:
                        player2_desc = f"**{self.challengee}** used **Eviscerate**, they are holding dual weapons! Damage is **doubled!**"
                        user_damage_dealt = user_damage_dealt*2 - 25

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#SHADOWSTEP (#23) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Shadowstep" or self.challengee_action == "Shadowstep":
            if self.challenger_action == "Shadowstep":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Shadowstep":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 30

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                a = (f"{opp} is bleeding!", f"{opp} is bleeding!", f"{opp} is bleeding!", f"{opp} didn't get cut enough..", f"{opp} hasn't suffered a blood loss yet..", f"{opp} hasn't suffered a blood loss yet..", f"The wound isn't too deep to make {opp} bleed..", f"{opp} is not dead with blood loss yet..", f"{opp} is still standing.. so far..", f"{opp} hasn't been cut..")
                b = random.choice(a)
                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Shadowstep**, {b}"
                else:
                    player2_desc = f"**{self.challengee}** used **Shadowstep**, {b}"
                
                if user_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    if b == f"{opp} is bleeding!":
                        sstep_sideeff = f"**{opp}** is **BLEEDING**, they take an additional **30** damage this turn!"
                        if user == self.challenger:
                            player1_sideeff = sstep_sideeff
                            player1_damage_dealt += 30
                            player2_damage_taken = self.opp_hp - 30    
                        else:
                            player2_sideeff = sstep_sideeff
                            player2_damage_dealt += 30
                            player1_damage_taken = self.opp_hp - 30

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#THUNDERBOLT (#22) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Thunderbolt" or self.challengee_action == "Thunderbolt":
            if self.challenger_action == "Thunderbolt":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Thunderbolt":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 40

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                a = (f"{opp} is paralysed!", f"{opp} is paralysed!", f"{opp} is paralysed!", f"{opp} didn't get a good shock yet..", f"{opp} didn't get a good shock yet..", f"{opp} didn't get a good shock yet..", f"{opp} didn't get a good shock yet..", f"{opp} didn't get a good shock yet..", f"{opp} didn't get a good shock yet..", f"{opp} didn't get a good shock yet..")
                b = random.choice(a)
                if user == self.challenger:
                    player1_desc = f"**{user}** used **Thunderbolt**, {b}"
                else:
                    player2_desc = f"**{user}** used **Thunderbolt**, {b}"
                if b == f"{opp} is paralysed!":
                    tbolt_sideeff = f"**{opp}** is **PARALYSED**, they can't move this turn!"
                    if user == self.challenger:
                        player1_sideeff = tbolt_sideeff
                        player2_damage_dealt = 0
                        player1_damage_taken = challenger_hp
                        conn = sqlite3.connect('stats.sqlite')
                        c = conn.cursor()
                        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (challenger_hp, user_id,))
                        conn.commit()
                        conn.close()
                    else:
                        player2_sideeff = tbolt_sideeff
                        player1_damage_dealt = 0
                        player2_damage_taken = challengee_hp
                        conn = sqlite3.connect('stats.sqlite')
                        c = conn.cursor()
                        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (challengee_hp, user_id,))
                        conn.commit()
                        conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#FLAME BURST (#23) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Flame Burst" or self.challengee_action == "Flame Burst":
            if self.challenger_action == "Flame Burst":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Flame Burst":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 40

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                a = (f"{opp} is burned!", f"{opp} is burned!", f"{opp} is burned!", f"{opp} didn't taste the flames yet..", f"{opp} isn't burnt yet..", f"{opp} survived the flames heat..", f"{opp} is not cooked alive yet..", f"{opp} is not cooked alive..", f"{opp} isn't burnt yet..", f"{opp} hasn't been burnt..")
                b = random.choice(a)
                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Flame Burst**, {b}"
                else:
                    player2_desc = f"**{self.challengee}** used **Flame Burst**, {b}"
                
                if user_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    if b == f"{opp} is burned!":
                        fburst_sideeff = f"**{opp}** is **BURNING**, they take an additional **30** damage this turn!"
                        if user == self.challenger:
                            player1_sideeff = fburst_sideeff
                            player1_damage_dealt += 30
                            player2_damage_taken = self.opp_hp - 30    
                        else:
                            player2_sideeff = fburst_sideeff
                            player2_damage_dealt += 30
                            player1_damage_taken = self.opp_hp - 30

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#EARTHEN TOTEM (#24) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Earthen Totem" or self.challengee_action == "Earthen Totem":
            if self.challenger_action == "Earthen Totem":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Earthen Totem":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT speed FROM stats WHERE user_id = ?", (opp_id,))
                opp_speed = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 10

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** has summoned an **Earthen Totem**, {self.challengee}'s speed has been greatly reduced!"
                    opp_speed = opp_speed / 2
                else:
                    player2_desc = f"**{self.challengee}** has summoned an **Earthen Totem**, {self.challengee}'s speed has been greatly reduced!"
                    opp_speed = opp_speed / 2

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#HELLFIRE (#25) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Hellfire" or self.challengee_action == "Hellfire":
            if self.challenger_action == "Hellfire":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Hellfire":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 20

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                a = (f"{opp} is burned!", f"{opp} is burned!", f"{opp} is burned!", f"{opp} didn't taste the flames of hell yet..", f"{opp} isn't burnt yet..", f"{opp} survived the flames heat..", f"{opp} is not cooked alive yet..", f"{opp} almost reached hell, alive..", f"{opp} isn't burnt yet..", f"{opp} hasn't been burnt..")
                b = random.choice(a)
                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Hellfire**, {b}"
                else:
                    player2_desc = f"**{self.challengee}** used **Hellfire**, {b}"
                if user_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    if b == f"{opp} is burned!":
                        hfire_sideeff = f"**{opp}** is **BURNING**, they take an additional **30** damage this turn!"
                        if user == self.challenger:
                            player1_sideeff = hfire_sideeff
                            player1_damage_dealt += 30
                            player2_damage_taken = self.opp_hp - 30    
                        else:
                            player2_sideeff = hfire_sideeff
                            player2_damage_dealt += 30
                            player1_damage_taken = self.opp_hp - 30

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#CURSE OF AGONY (#25) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Curse of Agony" or self.challengee_action == "Curse of Agony":
            if self.challenger_action == "Curse of Agony":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Curse of Agony":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    coa = sqlite3.connect("stats.sqlite")
                    coac = coa.cursor()
                    coac.execute("SELECT curse_of_agony FROM tempstats WHERE user_id = ?", (opp_id,))
                    curse_of_agony_count = coac.fetchone()[0]
                    coa.close()

                    curse_of_agony_count += 1

                    coa = sqlite3.connect("stats.sqlite")
                    coac = coa.cursor()
                    coac.execute("UPDATE tempstats SET curse_of_agony = ? WHERE user_id = ?", (curse_of_agony_count ,opp_id,))
                    coa.commit()
                    coa.close()

                    skill_damage = skill_damage * curse_of_agony_count
                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Curse of Agony**, {self.challengee} is now cursed and will take more damage after every curse, Current Curse: **{curse_of_agony_count}**"
                else:
                    player2_desc = f"**{self.challengee}** used **Curse of Agony**, {self.challengee} is now cursed and will take more damage after every curse, Current Curse: **{curse_of_agony_count}**"

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#SHADOW BOLT ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Shadow Bolt" or self.challengee_action == "Shadow Bolt":
            if self.challenger_action == "Shadow Bolt":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Shadow Bolt":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 30
                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Shadow Bolt**, {self.challengee} is being enveloped by the shadows"
                else:
                    player2_desc = f"**{self.challengee}** used **Shadow Bolt**, {self.challenger} is being enveloped by the shadows"

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#SHIELD SLAM  ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Shield Slam" or self.challengee_action == "Shield Slam":
            if self.challenger_action == "Shield Slam":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Shield Slam":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 50
                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_armor/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_armor/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                if user == self.challenger:
                    player1_desc = f"**{self.challenger}** used **Shield Slam**, {self.challengee} has been crushed!"
                else:
                    player2_desc = f"**{self.challengee}** used **Shield Slam**, {self.challenger} has been crushed"

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#HEROIC STRIKE (#13) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Heroic Strike" or self.challengee_action == "Heroic Strike":
            if self.challenger_action == "Heroic Strike":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Heroic Strike":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 40

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                a = (f"{opp} is Stunned!", f"{opp} is Stunned!", f"{opp} is Stunned!", f"{opp} can still stand up..", f"{opp} can still stand up..", f"{opp} is still in their senses..", f"{opp} didn't get a concussion yet..", f"{opp} didn't faint yet..", f"{opp} didn't faint yet..", f"{opp} is still standing..")
                b = random.choice(a)
                if user == self.challenger:
                    player1_desc = f"**{user}** used **Heroic Strike**, {b}"
                else:
                    player2_desc = f"**{user}** used **Heroic Strike**, {b}"
                if b == f"{opp} is Stunned!":
                    cstrike_sideeff = f"**{opp}** is **STUNNED**, they are too dizzy!"
                    if user == self.challenger:
                        player1_sideeff = cstrike_sideeff
                        player2_damage_dealt = 0
                        player1_damage_taken = challenger_hp
                        conn = sqlite3.connect('stats.sqlite')
                        c = conn.cursor()
                        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (challenger_hp, user_id,))
                        conn.commit()
                        conn.close()
                    else:
                        player2_sideeff = cstrike_sideeff
                        player1_damage_dealt = 0
                        player2_damage_taken = challengee_hp
                        conn = sqlite3.connect('stats.sqlite')
                        c = conn.cursor()
                        c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (challengee_hp, user_id,))
                        conn.commit()
                        conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

#WHIRLWIND (#13) ----------------------------------------------------------------------------------------------------
        if self.challenger_action == "Whirlwind" or self.challengee_action == "Whirlwind":
            if self.challenger_action == "Whirlwind":
                user = self.challenger
                opp = self.challengee
            elif self.challengee_action == "Whirlwind":
                user = self.challengee
                opp = self.challenger
            user_id = user.id
            opp_id = opp.id 

            if self.challenger_action and self.challengee_action:
                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (user_id,))
                self.user_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT intelligence FROM stats WHERE user_id=?", (user_id,))
                user_intelligence = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (user_id,))
                user_armor = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT energy FROM stats WHERE user_id=?", (user_id,))
                user_energy = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect("stats.sqlite")
                c = conn.cursor()
                c.execute("SELECT hp FROM tempstats WHERE user_id = ?", (opp_id,))
                self.opp_hp = c.fetchone()[0]
                conn.close()

                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("SELECT armor FROM stats WHERE user_id=?", (opp_id,))
                opp_armor = c.fetchone()[0]
                conn.close()

                if player1_damage_dealt == 0 or player2_damage_dealt == 0:
                    user_damage_dealt = 0
                else:
                    skill_damage = 20

                    user_damage_min = skill_damage + ((user_energy - 30) - (opp_armor)) + (user_intelligence/2)
                    user_damage_max = skill_damage + ((user_energy + 30) - (opp_armor)) + (user_intelligence/2)
                    if user_damage_min < 0:
                        user_damage_min = 0
                    if user_damage_max < 0:
                        user_damage_max = 10

                    user_damage_dealt = random.randint(user_damage_min, user_damage_max)
                    self.opp_hp -= user_damage_dealt

                    if user == self.challenger:
                        player1_damage_dealt = user_damage_dealt
                        player2_damage_taken = self.opp_hp
                    else:
                        player2_damage_dealt = user_damage_dealt
                        player1_damage_taken = self.opp_hp

                if user == self.challenger:
                    player1_desc = f"**{user}** used **Whirlwind**, {self.challengee} is being tossed around with blades!"
                else:
                    player2_desc = f"**{user}** used **Whirlwind**, {self.challenger} is being tossed around with blades!"
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (self.opp_hp, opp_id,))
                conn.commit()
                conn.close()

# FINAL EMBED SENT --------------------------------------------------------------------------------------------

        user_id = self.challenger.id
        opp_id = self.challengee.id
        

        if self.challenger_action and self.challengee_action:
            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("SELECT hp FROM stats WHERE user_id = ?", (user_id,))
            original_user_hp = c.fetchone()[0]
            conn.close()

            conn = sqlite3.connect('stats.sqlite')
            c = conn.cursor()
            c.execute("SELECT hp FROM stats WHERE user_id = ?", (opp_id,))
            original_opp_hp = c.fetchone()[0]
            conn.close()

            img = ["https://wallpapers.com/images/hd/hearthstone-rastakhan-s-rumble-2560-x-1440-psz606u2cedv34ln.jpg","https://s1.1zoom.me/b5050/636/Hearthstone_Heroes_of_Warcraft_Battles_Dragons_529821_1366x768.jpg",
                "https://d1lss44hh2trtw.cloudfront.net/assets/article/2018/12/04/rastakhan-s-rumble-cinematic-still-7-png-jpgcopy_feature.jpg", "https://dotesports.com/wp-content/uploads/2018/11/24030406/Screenshot-140.png",
                    "https://cdn.mos.cms.futurecdn.net/JgySFGeQcRRH3zf6QecaJM-1200-80.jpg", "https://dotesports.com/wp-content/uploads/2018/11/26075329/Screenshot-163.png" ]

            if opp_speed > user_speed:
                speed = f"{self.challengee} is faster! They get to move first.."
            elif user_speed > opp_speed:
                speed = f"{self.challenger} is faster! They get to move first.."
            else:
                speed = f"Ladies and Gentlemen, its a speed tie!"

            available_actions_view = (AvailableActionsButton(self.challenger, self.challengee))

            clrs = [0x0a0a0a, 0x9fd2ff, 0xff5151, 0xffffff, 0xffdbaf]
            # Create embed with damage dealt and updated stats
            final_embed = discord.Embed(title="Boom Bam Bow", color=random.choice(clrs))
            final_embed.add_field(name="", value=speed, inline=False)
            final_embed.add_field(name="", value="", inline=False)
            final_embed.add_field(name="", value=player1_desc, inline=False)
            final_embed.add_field(name="", value=player2_desc, inline=False)
            final_embed.add_field(name="", value="", inline=False)
            final_embed.add_field(name="", value=player1_sideeff, inline=False)
            final_embed.add_field(name="", value=player2_sideeff, inline=False)
            final_embed.add_field(name="", value="", inline=False)
            final_embed.add_field(name=f"{self.challenger}'s Damage Dealt", value=f"{player1_damage_dealt} HP", inline=True)
            final_embed.add_field(name=f"{self.challengee}'s Damage Dealt", value=f"{player2_damage_dealt} HP", inline=True)
            final_embed.add_field(name="", value="", inline=False)
            final_embed.add_field(name=f"{self.challenger}'s Remaining HP", value=f"{player1_damage_taken} HP", inline=True)
            final_embed.add_field(name=f"{self.challengee}'s Remaining HP", value=f"{player2_damage_taken} HP", inline=True)
            final_embed.set_image(url= random.choice(img))

            if player1_damage_taken <= 0 or player2_damage_taken <= 0:
                final_embed.add_field(name="Duel Ended", value="The duel has ended!", inline=False)
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (original_user_hp, user_id,))
                conn.commit()
                conn.close()
                coa = sqlite3.connect("stats.sqlite")
                coac = coa.cursor()
                coac.execute("UPDATE tempstats SET curse_of_agony = 0 WHERE user_id = ?", (opp_id,))
                coa.commit()
                coa.close()
                coa = sqlite3.connect("stats.sqlite")
                coac = coa.cursor()
                coac.execute("UPDATE tempstats SET curse_of_agony = 0 WHERE user_id = ?", (user_id,))
                coa.commit()
                coa.close()
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET rightm = 0 WHERE user_id = ?", (user_id,))
                conn.commit()
                conn.close()
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET rightm = 0 WHERE user_id = ?", (opp_id,))
                conn.commit()
                conn.close()
                conn = sqlite3.connect('stats.sqlite')
                c = conn.cursor()
                c.execute("UPDATE tempstats SET hp = ? WHERE user_id=?", (original_opp_hp, opp_id,))
                conn.commit()
                conn.close()
                for item in available_actions_view.children:
                        item.disabled = True

            if player1_damage_taken >= 0 and player2_damage_taken < 0:
                    final_embed.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                    final_embed.add_field(name="", value=f"{self.challenger} has won the battle", inline=False)
                    for item in available_actions_view.children:
                        item.disabled = True
            elif player1_damage_taken <= 0 and player2_damage_taken > 0:
                    final_embed.add_field(name="", value=f"{self.challengee} has won the battle", inline=False)
                    final_embed.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                    for item in available_actions_view.children:
                        item.disabled = True
            elif player1_damage_taken <= 0 and player2_damage_taken <= 0:
                    if opp_speed > user_speed:
                        final_embed.add_field(name="", value=f"{self.challengee} was faster than {self.challenger} and strook first..\n {self.challengee} has won the battle!", inline=False)
                        final_embed.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                        for item in available_actions_view.children:
                            item.disabled = True
                    elif user_speed > opp_speed:
                        final_embed.add_field(name="", value=f"{self.challenger} was faster than {self.challengee} and strook first..\n {self.challenger} has won the battle!", inline=False)
                        final_embed.set_image(url="https://wallpapers.com/images/hd/hearthstone-heroes-of-warcraft-2560-x-1440-y19lk8egxqj2xsmc.jpg")
                        for item in available_actions_view.children:
                            item.disabled = True
                    elif user_speed == opp_speed:
                        final_embed.add_field(name="Tie..?", value=f"They tied.. how unamusing, both struck at the same time..", inline=False)
                        for item in available_actions_view.children:
                            item.disabled = True
        
            await interaction.channel.send(embed=final_embed, view=available_actions_view)

            if self.user_hp > 0 and self.opp_hp > 0:
                pass

class ForfeitButton(Button):
    def __init__(self, parent_view: AvailableActionsButton):
        super().__init__(label="Forfeit", style=discord.ButtonStyle.danger, custom_id="ff")
        self.parent_view = parent_view

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        for item in self.view.children:
            item.disabled = True

        if user.id == self.parent_view.challenger_id:
            self.parent_view.challenger_action = "forfeit"
            self.parent_view.challenger_move_selected = True
        elif user.id == self.parent_view.challengee_id:
            self.parent_view.challengee_action = "forfeit"

        await interaction.response.edit_message(content="Waiting for opponent to select a move...", view=None)
        await self.parent_view.check_both_actions_selected(interaction)


class AttackButton(Button):
    def __init__(self, parent_view: AvailableActionsButton):
        super().__init__(label="Attack", style=discord.ButtonStyle.danger, custom_id="attack")
        self.parent_view = parent_view

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        for item in self.view.children:
            item.disabled = True

        if user == self.parent_view.challenger:
            self.parent_view.challenger_action = "atk"
            self.parent_view.challenger_move_selected = True
        elif user == self.parent_view.challengee:
            self.parent_view.challengee_action = "atk"

        await interaction.response.edit_message(content="Waiting for opponent to select a move...", view=None)
        await self.parent_view.check_both_actions_selected(interaction)

class SkillButton(Button):
    def __init__(self, skill_name, skill_id, parent_view: AvailableActionsButton):
        super().__init__(label=skill_name, style=discord.ButtonStyle.primary, custom_id=f"skill_{skill_id}")
        self.skill_name = skill_name
        self.skill_id = skill_id
        self.parent_view = parent_view

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        for item in self.view.children:
            item.disabled = True

        if self.skill_name == "Crusader Strike":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Crusader Strike"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Crusader Strike"
        
        if self.skill_name == "Divine Light":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Divine Light"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Divine Light"

        if self.skill_name == "Avenging Wrath":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Avenging Wrath"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Avenging Wrath"
        
        if self.skill_name == "Vanish":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Vanish"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Vanish"

        if self.skill_name == "Eviscerate":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Eviscerate"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Eviscerate"

        if self.skill_name == "Shadowstep":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Shadowstep"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Shadowstep"

        if self.skill_name == "Thunderbolt":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Thunderbolt"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Thunderbolt"

        if self.skill_name == "Flame Burst":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Flame Burst"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Flame Burst"

        if self.skill_name == "Earthen Totem":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Earthen Totem"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Earthen Totem"

        if self.skill_name == "Hellfire":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Hellfire"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Hellfire"

        if self.skill_name == "Curse of Agony":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Curse of Agony"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Curse of Agony"

        if self.skill_name == "Shadow Bolt":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Shadow Bolt"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Shadow Bolt"

        if self.skill_name == "Shield Slam":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Shield Slam"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Shield Slam"

        if self.skill_name == "Heroic Strike":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Heroic Strike"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Heroic Strike"

        if self.skill_name == "Whirlwind":
            user = interaction.user
            if user == self.parent_view.challenger:
                self.parent_view.challenger_action = "Whirlwind"
                self.parent_view.challenger_move_selected = True
            elif user == self.parent_view.challengee:
                self.parent_view.challengee_action = "Whirlwind"

        await interaction.response.edit_message(content="Waiting for opponent to select a move...", view=None)
        await self.parent_view.check_both_actions_selected(interaction)

class DuelChallengeButton(View):
    def __init__(self, challenger, challengee):
        super().__init__(timeout=None)
        self.challenger = challenger
        self.challengee = challengee

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success)
    async def accept_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.challengee:
            await interaction.response.send_message("You can't accept this challenge!", ephemeral=True)
            return
        
        await interaction.response.send_message("Challenge accepted! The duel will start now.")
        # Proceed to start the duel
        await self.start_duel(interaction)

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.danger)
    async def decline_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.challengee:
            await interaction.response.send_message("You can't decline this challenge!", ephemeral=True)
            return
        
        await interaction.response.send_message(f"{self.challengee.mention} has declined the duel.", ephemeral=False)
        await interaction.message.delete()

    async def start_duel(self, interaction):
        embed = discord.Embed(title=f"Battle between {self.challenger} and {self.challengee} is now commencing..", description="Preparing the Grounds..", color=0x707070)
        embed.set_image(url="https://images2.alphacoders.com/131/1315144.jpg")
        await interaction.channel.send(embed=embed)
        await self.display_stats(interaction)

    async def display_stats(self, interaction):
        async with aiosqlite.connect('stats.sqlite') as conn:
            async with conn.execute("SELECT hp, base_attack, energy, intelligence, strength, speed, armor FROM stats WHERE user_id = ?", (self.challenger.id,)) as cursor:
                challenger_stats = await cursor.fetchone()

            async with conn.execute("SELECT hp, base_attack, energy, intelligence, strength, speed, armor FROM stats WHERE user_id = ?", (self.challengee.id,)) as cursor:
                challengee_stats = await cursor.fetchone()
        await asyncio.sleep(2)
        if challenger_stats and challengee_stats:
            embed = discord.Embed(title="The Battle has begun!", description="Here are the stats of both the duelers", color=0xffffff)
            
            embed.add_field(name=f"{self.challenger.display_name}'s Stats", value=(
                f"**HP**: {challenger_stats[0]}\n"
                f"**Attack**: {challenger_stats[1]}\n"
                f"**Energy**: {challenger_stats[2]}\n"
                f"**Intelligence**: {challenger_stats[3]}\n"
                f"**Strength**: {challenger_stats[4]}\n"
                f"**Speed**: {challenger_stats[5]}\n"
                f"**Armor**: {challenger_stats[6]}"
            ), inline=True)

            embed.add_field(name=f"{self.challengee.display_name}'s Stats", value=(
                f"**HP**: {challengee_stats[0]}\n"
                f"**Attack**: {challengee_stats[1]}\n"
                f"**Energy**: {challengee_stats[2]}\n"
                f"**Intelligence**: {challengee_stats[3]}\n"
                f"**Strength**: {challengee_stats[4]}\n"
                f"**Speed**: {challengee_stats[5]}\n"
                f"**Armor**: {challengee_stats[6]}"
            ), inline=True)

            embed.set_image(url="https://e0.pxfuel.com/wallpapers/262/138/desktop-wallpaper-knight-vs-demon.jpg")

            view = AvailableActionsButton(self.challenger, self.challengee)
            await interaction.channel.send(embed=embed, view=view)
        else:
            await interaction.channel.send("Failed to retrieve stats for one or both users.")

class duel(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.command(name="dueluser")
    async def dueluser(self, ctx, member: discord.Member):
        if member == ctx.author:
            await ctx.send("You cannot duel yourself!")
            return

        description=f"{ctx.author.mention} has challenged {member.mention} to a duel! Let's see who comes out on the top!"
        
        view = DuelChallengeButton(ctx.author, member)
        await ctx.send(description, view=view)


async def setup(client):
    await client.add_cog(duel(client))

