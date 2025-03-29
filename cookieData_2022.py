#A comparison between all Cookies' word length per skill
#CREAM PUFF IS HERE TWICE FOR THEIR TWO VERSIONS (PRE-BUFF AND POST-BUFF). Apologies for the fact if there's another Cookie that got similar treatment like them,
#to essentially have 2 different versions without external buffs that I missed
#Ditched the Cookie Legion thing because it hasn't been updated since 2022

import re
class Cookie:
  def __init__(self, name, skill, type, position, rarity):
    self.name = name
    self.skill = skill
    self.type = type
    self.position = position
    self.rarity = rarity

#2022 

c22_1 = Cookie(
            "Eclair", 
            "With all the knowledge and research accumulated over the years, analyzes and identifies the opponent's weakness. \
Casts 'Weakness' debuff to 3 enemies with the highest ATK (targets Cookies first), amplifying the DMG they receive, and deals DMG. \
If the enemy is defeated while under the Weakness debuff, all allies gain an HP shield.",
            "Support",
            "Middle",
            "Epic")

c22_2 = Cookie(
            "Tea Knight", 
            "Inflicts damage to the nearest enemy (targets Cookies first) and leads the battle on, providing a buff for his allies. \
There are several kinds of available buffs; each kind is applied to the Cookie meeting the required conditions. Whenever \
an allied Cookie is defeated, the Wrath of the Commander effect is triggered. Wrath of the Commander cannot be dispelled and \
stacks up to four times. At maximum stacks, Tea Knight Cookie will become resistant to interrupting effects.",
            "Charge",
            "Front",
            "Epic")

c22_3 = Cookie(
            "Dark Cacao", 
            "Swings the Grapejam Chocoblade with great force, causing thunder and lightning to inflict damage upon foes in range. \
This mighty attack reduces enemies' ATK, DEF, and inflicts Zap and Injury. Injured foes will have reduced Max HP, and the Injury debuff ignores \
immunity and dispelling effects not mentioning Injury specifically. While Dark Cacao Cookie is using his skill, he will briefly become resistant \
            to interrupting effects.",
            "Charge",
            "Front",
            "Ancient")

c22_4 = Cookie(
            "Affogato", 
            "Secretly curses the enemy with the highest ATK (targets Cookies first). \
The cursed target cannot receive any buff effects for a certain time (limited to buffs that can be dispelled). \
It will also receive amplified debuffs and will spread Poison inflicting periodic damage to nearby enemies and \
themselves. If Poison is dispelled, it will cause great damage to nearby enemies.",
            "Bomber",
            "Middle",
            "Epic")

c22_5 = Cookie(
            "Caramel Arrow", 
            "Few enemies can keep their wits when they see the twin blades turning into a bow! Caramel Arrow Cookie performs \
a ranged attack (targets Cookies first) and leaves an Arrow Mark on the hit enemy. After the ranged attack, the Arrow Mark explodes when Caramel \
Arrow Cookie rushes towards the enemy, dealing DMG proportional to the enemy's Max HP (this DMG is capped at 300000). During the ranged attack, \
Caramel Arrow Cookie receives a buff that makes her immune to debuffs. While Caramel Arrow Cookie is using her skill, she will become resistant \
to interrupting effects.",
            "Ranged",
            "Front",
            "Epic")

c22_6 = Cookie(
            "Cherry Blossom", 
            "Get ready for a storm of cherry blossoms! Cherry Blossom Cookie flies up to shower her enemies \
with a rain of cherry blossoms, dealing area damage. She will deal additional damage to non-Cookie opponents and increase the ATK of all allies: \
the bonus value will depend on the number of enemies hit with the skill.",
            "Ambush",
            "Rear",
            "Epic")

c22_7 = Cookie(
            "Wildberry", 
            "Wildberry Cookie unleashes his Battle Rage, dealing more powerful attacks and activating his Wild buff that \
cannot be dispelled. At the end of the Battle Rage mode, Wildberry Cookie musters all his strength, dealing an uppercut \
and a final blow. The Wild buff will stack with each hit Wildberry Cookie receives: the more stacks he has, the more powerful \
his final blow's DMG will be. While Wildberry Cookie is dealing an uppercut and his final blow, he will become resistant to \
interrupting effects. Being a large Cookie, Wildberry Cookie is less affected by Knockback or Flying.",
            "Defense",
            "Front",
            "Epic")

c22_8 = Cookie(
            "Clotted Cream", 
            "The Cloak of Light, a marvel of the Republic's cutting-edge technology, \
provides unquestionable advantages in battle. Upon using his skill, Clotted Cream Cookie projects the \
Light Cage onto the nearest enemy (targets Cookies first), blocking buffs and dealing area damage. \
The Light Cage cannot be dispelled and can be projected onto Cookies resistant to interrupting effects \
and prevents them from receiving removable buffs. The Light Cage will also inflict extra damage \
relative to the target's HP at the end of its duration. While Clotted Cream Cookie is using his skill, \
he will become resistant to interrupting effects. DMG proportional to Max HP is capped at 300000.",
            "Magic",
            "Middle",
            "Super Epic")

c22_9 = Cookie(
            "Crunchy Chip", 
            "Crunchy Chip Cookie's regular attacks leave the Claw Mark on the enemy with the highest ATK. \
Upon using the skill, the Cookie charges towards the enemies, slamming them and summoning his \
Cream Wolf. When Crunchy Chip Cookie is defeated, the Cream Wolf becomes enraged and continues \
fighting alone. In this state, the Cream Wolf becomes resistant to incapacitating effects. If Crunchy Chip Cookie is revived, \
he will hop back onto the Cream Wolf. Crunchy Chip Cookie and his wolves are less affected by Knockbacks and Flying. \
While Crunchy Chip Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Charge",
            "Front",
            "Epic")

c22_10 = Cookie(
            "Oyster", 
            "The first Cooldown of Oyster Cookie's skill will be shortened, allowing for faster skill use. \
Summons soldiers of House Oyster and increases the 'CRIT%' and CRIT DMG for herself and nearby allies \
for a certain amount of time. The summoned soldiers will immediately charge at the enemies, dealing damage. \
The soldiers will have extra DEF until the HP of their shields hits zero. Their shields will also resist Knockbacks \
and Flying. When Oyster Cookie receives a cooldown reduction buff, instead of cooldown reduction, the number of Oyster Soldiers \
and their ATK will increase. While Oyster Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Support",
            "Rear",
            "Super Epic")

c22_11 = Cookie(
            "Financier", 
            "Like a true Paladin of unfaltering belief, Financier Cookie protects an ally cookie from the start of the battle \
until the moment she hits the ground. Financier Cookie's top priority is Clotted Cream Cookie, but if he is not present, \
she'll protect the allied Cookie with the highest ATK. Upon using her skill, Financier Cookie's regular attack will deal \
area damage, she will also heal the Cookie she is protecting in addition to herself, increase the ATK, DMG and CRIT Resist, \
as well as grant Light's Shield against her enemies. The Light's Shield will act as a Shield and deliver the Light's Judgment \
to those who dare to damage it when it disappears. \
While Financier Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Defense",
            "Front",
            "Epic")

c22_12 = Cookie(
            "Cream Unicorn", 
            "The music starts, and Cream Unicorn Cookie transforms into the Dreamy Unicorn. The Dreamy Unicorn reduces CRIT DMG \
received by the team and charges towards the enemies, silencing them. While silenced, the enemies skill Cooldown will be paused. \
The Dreamy Unicorn will leave Dancing Butterflies behind itself. These butterflies will fly towards the allies and heal them. \
The amount of Healing received depends on the amount of HP lost. Regular Healing targets will receive a DMG-reducing buff.",
            "Healing",
            "Rear",
            "Epic")

c22_13 = Cookie(
            "Black Pearl",
            "Dives into the abyss and shifts into her true form, creating a whirlpool storm that \
deals periodic damage and drags in even enemies resistant to interruptions. Enemies, \
terrified of the Cookie's giant size, suffer from Terror of the Abyss. If Terror of the Abyss is dispelled, \
the target will be inflicted with true damage proportional to the target's Max HP. Being the ruler of the abyss herself, \
Black Pearl Cookie is resistant to all Fear effects. (Maximum amount of damage proportional to the target's HP is 300000)",
            "Ambush",
            "Middle",
            "Legendary")

c22_14 = Cookie(
            "Captain Caviar", 
            "Captain's orders! The Black Shark submarine will appear at Captain Caviar Cookie's call, \
shoot 3 Black Shark Torpedoes at the enemies, and increase the team's Debuff Resist. Augmented with the latest technology \
of the Republic, the torpedoes will aim for the enemy with the lowest HP (targets Cookies first) in descending order. \
Once the torpedo hits the target, it will cause an explosion, dealing area damage and inflicting DEF Reduction. Captain \
Caviar Cookie is immune to any type of Fear, for he is a fearless sea wolf. While Captain Caviar Cookie is using his skill, \
he will briefly become resistant to interrupting effects.",
            "Bomber",
            "Middle",
            "Epic")

c22_15 = Cookie(
            "Candy Diver", 
            "While wandering the depths of the Duskgloom Sea, Candy Diver Cookie has become immune to enemy attacks \
by obtaining the Safeguarded ability. Their regular attacks reduce the DEF and increase DMG received by the nearest \
enemy. Upon using the skill, Candy Diver Cookie will discover various relics from the deep sea, providing buffs and healing to the Cookie's allies \
The super success rate will increase depending on Candy Diver Cookie's Amplify Buff rate. Every relic provides a different effect.",
            "Support",
            "Rear",
            "Epic")

c22_16 = Cookie(
            "Schwarzwälder",
            "Each one of Schwarzwälder's regular attacks has a chance to stun the target. The first cooldown of his skill will be shortened, \
allowing for faster skill use. Upon using the skill, Schwarzwälder will receive the Howling effect, increasing his own ATK SPD, \
and DMG Resist, and increasing the team's ATK. When the effect duration is over, Schwarzwälder will charge at the enemies, strike them \
with his hammer, stun them, and inflict the Hammer Shock debuff. The debuff will reduce the enemies’ ATK and cause them to receive more \
damage from the next Schwarzwälder's skill attacks with the hammer. While Schwarzwälder is using his skill, he will briefly become \
resistant to interrupting effects.",
            "Charge",
            "Front",
            "Epic")

c22_17 = Cookie(
            "Macaron",
            "Following Macaron Cookie's exciting cheer, the Macaron Animals will start marching, dealing DMG to nearby enemies. \
Non-Cookie enemies will receive additional DMG. Her contagious enthusiasm will increase the ATK and CRIT of her allies \
and restore their HP. Depending on the number of hits from the Macaron Animals, Macaron Cookie will gain a stack of the \
Happy Parade buff. Macaron Cookie will then restore the HP of her allies proportional to the number of stacks of \
Happy Parade once the parade is over. While Macaron Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Magic",
            "Middle",
            "Epic")

c22_18 = Cookie(
            "Carol", 
            "Sings the Song of Joy to restore the team's HP and increase their 'CRIT%' and CRIT DMG. \
When only two or fewer Cookies are left, including Carol Cookie, switches to the Song of Change instead, \
having her Cooldown immediately reset and decreased for the remainder of the battle. The Song of Change damages the enemies, \
increases the team's CRIT and CRIT DMG, and reduces the Cooldown for the remaining team members. With each regular attack, \
Carol Cookie sings the Song of Energy and restores the entire team's HP. However, the fewer team members she needs to heal, \
the more healing each individual member will receive. \
While Carol Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Healing",
            "Rear",
            "Epic")

c22_19 = Cookie(
            "Sherbet", 
            "Summons 15 frost shards, divides them based on the number of targets, and attacks the enemies, cycling between them in the order of the highest ATK. \
Frost shards deal additional damage depending on the number of Frost stacks. Targets hit with frost shards are inflicted with Frost and Debuff Resist \
Bypass. There is a chance of hit targets to become Frozen as well. Frozen targets receive additional damage when thawed. The amount of this additional \
damage and the chance of becoming Frozen increases depending on the number of Frost stacks. Sherbet Cookie is partially immune to Freezing and, \
thanks to the Warm Light of Life effect, will convert healing that exceeds his Max HP to an HP Shield. While Sherbet Cookie is using his skill, \
he will briefly become resistant to interrupting effects.",
            "Ranged",
            "Middle",
            "Super Epic")

c22_20 = Cookie(
            "Pinecone", 
            "Pinecone Cookie gets up on the tree golem and simultaneously heals themselves and the two allies with the highest ATK. \
While Pinecone Cookie is riding the tree golem, their Max HP is increased. Pinecone Cookie then throws Pinecone bombs at \
the enemy Cookie with the highest ATK, Stunning them. The Pinecone Bombs deal area damage to nearby enemies. If there are \
targets suffering from Frost within the area damage range, they will also become Stunned. If a target is immune to Stun, \
it will receive additional DMG.",
            "Bomber",
            "Front",
            "Epic") 

