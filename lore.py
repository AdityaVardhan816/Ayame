import discord
from discord.ext import commands
import asyncio

class LoreDropdown(discord.ui.Select):
    def __init__(self, user_id):
        self.user_id = user_id
        options = [
            discord.SelectOption(label="Illidan Stormrage", description="The villainous chronicles", emoji="<:demon_hunter:1255872124195704975> "),
            discord.SelectOption(label="Gul'dan", description="The villanous chronicles", emoji="<:warlock:1255872668675215380> "),
            discord.SelectOption(label="Garrosh Hellscream", description="The villanous chronicles", emoji="<:warrior:1255872722551050323>"),
            discord.SelectOption(label="Sylvanas Windrunner", description="The villanous chronicles", emoji="<:hunter:1255872272988770346>"),
            discord.SelectOption(label="Anduin Wrynn", description="The heroic chronicles", emoji="<:priest:1255872554631958729>"),
            discord.SelectOption(label="Lady Liadrin", description="The heroic chronicles", emoji="<:Paladin:1255872513423048716> "),
            discord.SelectOption(label="Jaina Proudmoore", description="The heroic chronicles", emoji="<:wiz:1255872379918352384> "),
            discord.SelectOption(label="Chen Stormstout", description="The heroic chronicles", emoji="<:Death_Knight:1255873191373701241> "),
            discord.SelectOption(label="Thrall", description="The neutrals chronicles", emoji="<:shaman:1255872632092495933> "),
            discord.SelectOption(label="Valeera Sanguinar", description="The neutrals chronicles", emoji="<:Rogue:1255872600987664396> ")
        ]
        super().__init__(placeholder="A legend awaits..", min_values=1, max_values=1, options=options)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return
        selected_book = self.values[0]
        embed = discord.Embed(title=f"{selected_book}", color=0x0a0a0a)
        
        if selected_book == "Illidan Stormrage":
            embed.description = "**Book of Villains - Illidan Stormrage**"
            embed.add_field(name="Feel the Hatred of Ten Thousand Years..", value="Illidan was born a night elf, twin brother to Malfurion Stormrage and close friend to Tyrande Whisperwind. He was known for his ambition and thirst for power, which set him on a tumultuous path. Early in his life, Illidan fell in love with Tyrande, but she chose his brother Malfurion, leading to a deep-seated rivalry and jealousy between the brothers.", inline=False)
            embed.add_field(name="", value="Driven by a desire to protect his people, Illidan sought arcane power to defend them against the Burning Legion, an ancient demonic threat. However, his methods often clashed with the night elf society's reverence for nature and their strict taboos against arcane magic. His reckless pursuit of power and willingness to sacrifice anything for victory eventually led to his imprisonment by his own people.",inline=False)
            embed.add_field(name="", value="During his captivity, Illidan made a fateful pact with the demon lord Kil'jaeden, gaining demonic abilities and becoming the first demon hunter. He played a crucial role in defeating the Burning Legion in the War of the Ancients but was branded a traitor and outlawed by his own kind.",inline=False)
            embed.add_field(name="", value="Throughout his life, Illidan's actions were often misunderstood. He made difficult choices in his quest to protect Azeroth, even if it meant being labeled a villain by some. His path was one of tragedy and sacrifice, marked by inner turmoil and a constant struggle to balance his noble intentions with his darker impulses.",inline=False)
            embed.add_field(name="", value="Ultimately, Illidan's story is a testament to the complexities of redemption, power, and the eternal battle between light and darkness in the Warcraft universe. His legacy continues to influence the world of Azeroth long after his passing, leaving behind a conflicted and storied reputation as both hero and anti-hero.",inline=False)
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/805/742/532/warcraft-world-of-warcraft-demon-illidan-stormrage-night-elf-hd-wallpaper-preview.jpg")
        elif selected_book == "Gul'dan":
            embed.description = "**Book of Villains - Gul'dan**"
            embed.add_field(name="Everything.. Everything we have done.. has been for nothing", value="Driven by ambition and thirst for power, Gul'dan betrayed his mentor and forged a pact with the demonic Burning Legion, led by Kil'jaeden. This pact led to the corruption of the orcish clans and the formation of the first Horde. Gul'dan played a key role in opening the Dark Portal, allowing the Horde to invade Azeroth.", inline=False)
            embed.add_field(name="", value="Throughout his life, Gul'dan manipulated events to serve his own ambitions, often at the expense of others. He created the first generation of death knights and sought to harness powerful artifacts and magic to increase his own power. However, his schemes often backfired, leading to his downfall multiple times.",inline=False)
            embed.add_field(name="", value="Ultimately, Gul'dan met his end in the Tomb of Sargeras, where he sought to claim the power of the fallen titan. His spirit was later resurrected by the Burning Legion, leading to further chaos and destruction in Azeroth until his final demise during the events of the Broken Shore.",inline=False)
            embed.add_field(name="", value="Gul'dan's legacy is marked by the profound impact he had on the orcish race and Azeroth itself. His actions left a lasting scar on Draenor, transforming the once-shamanistic orcish clans into bloodthirsty warriors under demonic influence. His relentless pursuit of power and willingness to sacrifice anything and anyone for his goals earned him fear and disdain alike.",inline=False)
            embed.add_field(name="", value="Gul'dan's life is characterized by his insatiable hunger for power, manipulation of others, and his pivotal role in shaping the history of the Warcraft universe through dark magic and treachery.",inline=False)  
            embed.set_image(url="https://external-preview.redd.it/L99xP3H8Azr8NZo6-wyEcVup8p9pqloGJaXhZex3dyk.jpg?auto=webp&s=3f02d0a44ade5b63c2df6acd7b5275fd9b035601")
        elif selected_book == "Garrosh Hellscream":
            embed.description = "**Book of Villains - Garrosh Hellscream**"
            embed.add_field(name="HELLSCREAMS EYES ARE UPON YOU!", value="Son of Grommash Hellscream, was born on the shattered world of Draenor. As a young orc, he was afflicted by the Red Pox, which left him weak and despondent until he learned of his father's legendary deeds from Thrall. Inspired by his father's legacy, Garrosh joined the Horde and rapidly rose through the ranks.", inline=False)
            embed.add_field(name="", value="He became Warchief after Thrall's departure, leading with a vision of orcish supremacy and relentless ambition. His aggressive policies and reckless decisions, including the bombing of Theramore, ultimately led to his downfall.",inline=False)
            embed.add_field(name="", value="Hellscream's tenure as Warchief was marked by significant strife and division within the Horde. His hardline stance and brutal tactics alienated many of his allies, including the trolls, tauren, and even some orcs. His obsession with power led him to seek out ancient and dangerous magics, including the Heart of Y'Shaarj, which he used to bolster his strength but at great cost.",inline=False)
            embed.add_field(name="", value="This pursuit of power culminated in the Siege of Orgrimmar, where Garrosh fortified himself with his loyal Kor'kron guards. The combined forces of the Alliance and the rebellious Horde factions besieged the city to depose him. After a fierce battle, Garrosh was finally defeated and taken into custody.",inline=False)
            embed.add_field(name="", value="He was brought to trial in Pandaria for his war crimes, but before justice could be fully served, he escaped with the help of the bronze dragon Kairozdormu. They traveled to an alternate Draenor, where Garrosh's actions created a new Iron Horde, an uncorrupted but still warmongering faction. ",inline=False)  
            embed.set_image(url="https://dotesports.com/wp-content/uploads/2018/08/11204619/garrosh-hellscream-lore-warrior.jpg")
        elif selected_book == "Sylvanas Windrunner":
            embed.description = "**Book of Villains - Sylvanas Windrunner**"
            embed.add_field(name="Victory for the Forsaken!", value="Originally a high elf ranger-general of Silvermoon, had her life irreversibly changed during the Third War. As she valiantly defended her homeland against the invading Scourge, she faced the death knight Arthas Menethil. Defeated and subsequently raised as a banshee under Arthas's control, Sylvanas endured torment and servitude. However, she eventually regained her free will and vowed vengeance against the Lich King.", inline=False)
            embed.add_field(name="", value="Breaking free, she gathered other liberated undead, forming the Forsaken, a faction within the Horde. As their leader, the Dark Lady, Sylvanas led her people with a ruthless pragmatism, always driven by a desire for survival and power. Under her leadership, the Forsaken solidified their presence in the Undercity, formerly the human city of Lordaeron.",inline=False)
            embed.add_field(name="", value="Sylvanas's actions often sparked controversy and conflict. She employed the Blight, a deadly plague, during the Wrathgate incident and later burned the World Tree, Teldrassil, igniting the Fourth War. Her increasing ruthlessness and disregard for both ally and enemy alike caused many within the Horde to question her leadership, culminating in her abandonment of the Horde after the battle of Orgrimmar.",inline=False)
            embed.add_field(name="", value="Seeking a way to avoid her perceived fate of eternal darkness, Sylvanas made a pact with the Jailer, a powerful entity in the Shadowlands. Her actions under this alliance, including the shattering of the Helm of Domination and the tearing of the veil between Azeroth and the Shadowlands, led to widespread chaos and upheaval.",inline=False)
            embed.add_field(name="", value="Ultimately, Sylvanas's journey is one of tragedy, vengeance, and a relentless pursuit of autonomy in a world that continually sought to control or destroy her. Her complex character and morally ambiguous actions have left a profound and lasting impact on Azeroth.",inline=False)  
            embed.set_image(url="https://w0.peakpx.com/wallpaper/1018/906/HD-wallpaper-sylvanas-windrunner-dark-elf-arrow-moon-full-moon-cape-hot-world-of-warcarft-elf-warcraft-sexy-claw-breasts-cool-warrior-dark-skull.jpg")
        elif selected_book == "Anduin Wrynn":
            embed.description = "**Book of Heroes - Anduin Wrynn**"
            embed.add_field(name="The Light guides us, even in the darkest of times.", value="The current King of Stormwind, is a central figure in the Alliance and one of Azeroth's most prominent leaders. Born to King Varian Wrynn and Queen Tiffin Wrynn, Anduin was named after the legendary Anduin Lothar. From a young age, he displayed wisdom and compassion, qualities that set him apart from other leaders.", inline=False)
            embed.add_field(name="", value="In her search for a new source of power, she and her people resorted to siphoning energy from a captured naaru. This led to the formation of the Blood Knights, a controversial order initially viewed with disdain by traditional paladins.",inline=False)
            embed.add_field(name="", value="Anduin's diplomatic approach often saw him seeking peaceful resolutions to conflicts, earning him respect and admiration from various factions, including the Horde. His vision of unity and cooperation was a driving force behind many of his actions, such as his efforts during the Pandaria campaign to bring about a peaceful resolution.",inline=False)
            embed.add_field(name="", value="Tragedy struck when Varian Wrynn was killed during the Battle for Broken Shore, leaving Anduin to ascend to the throne of Stormwind. Though initially overwhelmed by the responsibilities of kingship and the weight of his father's legacy, Anduin quickly grew into his role. He led the Alliance with a firm yet compassionate hand, always striving to honor his father's memory while forging his own path.",inline=False)
            embed.add_field(name="", value="Throughout his journey, Anduin's faith in the Light and his unwavering hope for a better future for all races of Azeroth defined his reign. His ability to balance the demands of war with his vision for peace and unity has made him a beloved and respected leader, not just for the people of Stormwind, but for the entire Alliance.",inline=False)  
            embed.set_image(url="https://i.pinimg.com/originals/b4/27/fe/b427fe80955de1f4d030e5c5b3503a25.jpg")
        elif selected_book == "Lady Liadrin":
            embed.description = "**Book of Heroes - Lady Liadrin**"
            embed.add_field(name="My blade burns with holy fire.", value="Known for her steadfast dedication to the Light and her leadership within the Blood Knights, the elite order of blood elf paladins. Once a high priestess, she turned away from the Light following the devastation of Quel'Thalas by the Scourge.", inline=False)
            embed.add_field(name="", value="Unlike his warrior father, Anduin was drawn to the ways of peace and healing. His path led him to train as a priest, where he excelled in the arts of the Light. Despite his peaceful inclinations, Anduin proved to be a capable and courageous leader, stepping up during times of crisis, such as when his father was missing and presumed dead.",inline=False)
            embed.add_field(name="", value="Liadrin's faith was later restored when she witnessed the selfless sacrifice of the naaru M'uru, who willingly gave his life to empower the Sunwell and restore it as a font of both arcane and holy energies.",inline=False)
            embed.add_field(name="", value="This profound experience renewed her belief in the Light and set her on a path of redemption. She has since become a staunch defender of Quel'Thalas and an ally to both the Horde and the Alliance in their battles against common threats, advocating for unity and understanding. Her journey from doubt and desperation to redemption and leadership exemplifies her resilience and unwavering commitment to her people and the Light.",inline=False)
            embed.add_field(name="", value="As a champion of her people and a beacon of hope, Liadrin continues to inspire those around her, advocating for unity and the greater good. Her legacy is one of strength, compassion, and an enduring commitment to the protection and prosperity of Quel'Thalas.",inline=False)  
            embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/630/199/707/artwork-blizzard-entertainment-city-digital-art-wallpaper-preview.jpg")
        elif selected_book == "Jaina Proudmoore":
            embed.description = "**Book of Heroes - Jaina Proudmoore**"
            embed.add_field(name="Our choices define us, and they shape the future we fight for.", value="Jaina Proudmoore is a powerful sorceress and one of the most prominent human mages in Azeroth's history. Born to Admiral Daelin Proudmoore, ruler of Kul Tiras, Jaina exhibited prodigious magical talent from a young age and studied under the tutelage of Archmage Antonidas in Dalaran. As a key figure in the Alliance, she played a crucial role in the defense of Azeroth against numerous threats, including the Burning Legion and the Scourge.", inline=False)
            embed.add_field(name="", value="Jaina's journey has been marked by significant challenges and personal tragedies. She witnessed the destruction of her homeland, Theramore, which left her deeply scarred and seeking vengeance against the Horde. Over time, she grappled with her anger and sought a path of reconciliation and peace, ultimately emerging as a leader who strives to balance her immense power with wisdom and compassion.",inline=False)
            embed.add_field(name="", value="Her relationships with other key figures, such as Arthas Menethil and Thrall, have been complex and deeply influential in her development as a leader. Jaina's story is one of resilience, intellect, and the constant struggle to align her personal desires with the greater good of Azeroth.",inline=False)
            embed.add_field(name="", value="From her early days as a talented student in Dalaran, under the guidance of the wise Archmage Antonidas, Jaina quickly rose to prominence due to her remarkable command of arcane magic. Her destiny was forever altered by her deep connection with Prince Arthas Menethil, a relationship that turned tragic as Arthas succumbed to darkness and became the Lich King, leaving Jaina heartbroken and burdened with the knowledge of what he had become.",inline=False)  
            embed.add_field(name="", value="As the ruler of Theramore, Jaina sought to foster peace and cooperation between the Alliance and the Horde. Her dream of a harmonious coexistence was shattered when the Horde, under Warchief Garrosh Hellscream, obliterated Theramore with a mana bomb, resulting in immense loss and devastation. This event hardened Jaina, filling her with a burning desire for vengeance and leading her to take a more aggressive stance against the Horde.",inline=False)  
            embed.set_image(url="https://w0.peakpx.com/wallpaper/785/866/HD-wallpaper-jaina-proudmoore-in-blue-background-world-of-warcraft.jpg")
        elif selected_book == "Chen Stormstout":
            embed.description = "**Book of Heroes - Chen Stormstout**"
            embed.add_field(name="Let us raise a toast to new horizons and the endless wonders awaiting us on our journey!", value="Known for his jovial demeanor and profound wisdom. As a pandaren brewmaster, Chen embodies the spirit of adventure and discovery. He travels Azeroth in search of exotic ingredients for his brews, all while sharing tales of his experiences and offering sage advice to those he meets.", inline=False)
            embed.add_field(name="", value="Chen's journey reflects his deep connection to nature, his passion for brewing, and his unwavering belief in harmony and balance. His presence often brings a sense of levity and wisdom to any situation, making him a cherished figure among allies and friends alike.",inline=False)
            embed.add_field(name="", value="The pandaren brewmaster, is celebrated not only for his exceptional skills in brewing but also for his insatiable thirst for adventure. From the lush forests of Pandaria to the bustling cities of Azeroth and beyond, Chen has traversed the world in pursuit of new flavors, experiences, and friendships.",inline=False)  
            embed.add_field(name="", value="In times of need, Chen proves himself to be a stalwart defender and skilled combatant. Despite his jovial demeanor and love for a good brew, he is a formidable opponent when provoked, wielding his mastery of martial arts and chi with precision and strength. His dedication to justice and protecting his allies showcases his unwavering resolve and courage on the battlefield.",inline=False)
            embed.add_field(name="", value="Rooted deeply in pandaren culture and traditions, Chen Stormstout carries the legacy of his ancestors with pride. He often regales others with tales from his family's history, honoring their teachings and upholding the values of respect, humility, and camaraderie. His cultural heritage is not just a part of his identity but also a source of strength that guides his actions and decisions.",inline=False)  
            embed.set_image(url="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/d44be922602893.563156a6832c9.jpg")
        elif selected_book == "Thrall":
            embed.description = "**Book of Neutrals - Thrall**"
            embed.add_field(name="The elements guide me..", value="Also known as Go'el, renowned for his leadership and resilience. Born as the son of Durotan, chieftain of the Frostwolf clan, Thrall was raised by humans after his parents' deaths. As he grew, he discovered his true heritage and embraced his role as a shaman, leading the orcs to a new destiny.", inline=False)
            embed.add_field(name="", value="Thrall's journey is marked by his efforts to reunite the orcish clans, restore their honor, and forge a new identity for his people. He founded the city of Orgrimmar, named after his mentor Orgrim Doomhammer, and played a crucial role in the founding of the Horde. As a wise and compassionate leader, Thrall sought peace between the Alliance and the Horde, believing in cooperation against common threats.",inline=False)
            embed.add_field(name="", value="His abilities as a shaman are legendary, harnessing the elements to aid his allies and defend his people. Thrall's leadership during times of crisis, such as during the Cataclysm and against the Burning Legion, solidified his reputation as one of Azeroth's greatest heroes. His story reflects themes of redemption, unity, and the ongoing struggle for peace in a war-torn world.",inline=False)  
            embed.add_field(name="", value="Early in his life, he was captured and enslaved by humans, experiencing firsthand the brutality of their internment camps. This experience shaped his understanding of both orcish honor and the injustices perpetrated by those in power. Freed by a young human named Taretha Foxton, Thrall began to bridge the gap between his people and the humans, seeking understanding rather than vengeance.",inline=False)
            embed.add_field(name="", value="As Warchief of the Horde, Thrall faced numerous trials, including conflicts within his own ranks and external threats like the Scourge and the Old Gods. His decisions often balanced the needs of his people with the greater good of Azeroth, earning him respect from allies and foes alike. Despite his retirement from active leadership, Thrall remains a symbol of hope and unity for the Horde, a testament to the enduring legacy of his leadership and vision.",inline=False)  
            embed.set_image(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c4d94793-8886-4794-8e3e-e69a0bbbf371/d8gmmub-1b9cf030-dc8b-463a-b772-5b05905dc117.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2M0ZDk0NzkzLTg4ODYtNDc5NC04ZTNlLWU2OWEwYmJiZjM3MVwvZDhnbW11Yi0xYjljZjAzMC1kYzhiLTQ2M2EtYjc3Mi01YjA1OTA1ZGMxMTcuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.H_tRw7fyl8Z9g1LV3b1s7FBwp0j-10yDXl2Nx_tHwNI")
        elif selected_book == "Valeera Sanguinar":
            embed.description = "**Book of Neutrals - Valeera Sanguinar**"
            embed.add_field(name="What's sharper? Your wits? Or your blades..", value="Known for her dual nature as both a skilled rogue and a loyal friend. Born to a family of noble blood in Silvermoon City, she faced adversity early in life when her parents were killed. This tragedy led her to the streets, where she survived by her wit and agility, eventually becoming a skilled rogue under the tutelage of Broll Bearmantle and Varian Wrynn.", inline=False)
            embed.add_field(name="", value="Her loyalty to Varian Wrynn, the King of Stormwind, during his time as a gladiator in the Undercity arena, forged a deep bond between them. This loyalty extended beyond mere duty, as she developed a friendship with him that transcended their roles. Despite her allegiance to the Alliance, Valeera's past as a blood elf and her connections to the Horde occasionally tested her loyalties.",inline=False)
            embed.add_field(name="", value="Valeera's story is one of resilience and adaptability, navigating the complex politics of Azeroth while remaining true to her principles. Her agility in combat and cunning intellect make her a formidable ally and a dangerous adversary. Throughout her adventures, Valeera has faced numerous challenges, from battling enemies in the shadows to confronting her own inner demons. Her journey continues to unfold, revealing layers of her character as she navigates the ever-changing landscape of Warcraft's conflicts and alliances.",inline=False)  
            embed.add_field(name="", value="From aiding Varian Wrynn during his tumultuous reign to participating in crucial battles against formidable foes like the Burning Legion, she has proven herself as a capable and courageous hero. Her skills extend beyond combat.",inline=False)  
            embed.add_field(name="", value="Valeera Sanguinar's journey is one of continual growth and introspection, as she wrestles with her identity as both a blood elf and an Alliance hero. Her story resonates with themes of redemption, loyalty, and the complexities of personal honor in a world torn by conflict. As Azeroth faces new threats and challenges, Valeera stands ready to defend her allies and confront her past, ensuring that her legacy as a skilled rogue and steadfast companion endures.",inline=False)  
            embed.set_image(url="https://e1.pxfuel.com/desktop-wallpaper/330/985/desktop-wallpaper-the-art-of-warcraft-ar-twitter-valeera-sanguinar.jpg")


        view = ConfirmView(selected_book, user_id=interaction.user.id)
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
        await interaction.response.send_message(f"Closing the book.. ", ephemeral=False)
        await asyncio.sleep(2)
        await interaction.message.delete()
    

class BackButton(discord.ui.Button):
    def __init__(self, user_id):
        super().__init__(label="Back to Legends", style=discord.ButtonStyle.blurple)
        self.user_id=user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("You don't have permission to use this button!", ephemeral=True)
            return
        view = discord.ui.View()
        view.add_item(LoreDropdown(self.user_id))
        await interaction.response.edit_message(view=view)



class lore(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=['lorerepository'])
    async def lr(self, ctx):
        embed = discord.Embed(description="Delve into the rich tapestry of stories and histories. The Lore Repository offers adventurers a gateway to explore the deep lore and legends that span across realms. Uncover tales of heroic champions and sinister villains.", color=0xffd48d)
        embed.set_author(name="Lore Repository", icon_url=ctx.author.avatar.url)
        embed.set_image(url="https://static.wikia.nocookie.net/hearthstone_gamepedia/images/a/a8/Athletic_Studies_full.jpg/revision/latest?cb=20200815063037")
        embed.add_field(name="<:rightarrow:1256528979871924265> Legends of Heros", value="Discover the valiant deeds and epic journeys of the greatest champions. Learn about their heroic exploits, their struggles against overwhelming odds, and the legacies they left behind. From fearless warriors to wise mages, these heroes inspire and shape the destiny of realms.", inline=False)
        embed.add_field(name="<:rightarrow:1256528979871924265> Legends of Villains", value="Uncover the dark and twisted tales of the most notorious villains. Delve into their rise to power, their malevolent schemes, and the chaos they have sown. These legends reveal the dark side of the world, highlighting the relentless battle between good and evil", inline=False) 
        embed.add_field(name="An Important Note", value="The icons next to the legends given in the list represent their original classes", inline=False) 
        view = discord.ui.View()
        view.add_item(LoreDropdown(ctx.author.id))
        await ctx.send(embed=embed, view=view)

async def setup(client):
    await client.add_cog(lore(client))