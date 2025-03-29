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

#2021 

c21_1 = Cookie(
            "Snow Sugar", 
            "Waves the Snow Sugar Wand to summon the Snow King that causes a snowstorm, dealing periodic area damage, \
and applying the Frost debuff with a certain chance upon each hit. Enemies suffer lowered ATK SPD. Snow King is resistant to certain \
action and movement-impairing effects. While Snow Sugar Cookie is using their skill, they will briefly become resistant to interrupting effects.", 
            "Magic", 
            "Middle",
            "Epic")

#DEBUG
#print(vars(c21_1)) #Get all obj attributes of c21_1
#print(c21_1.rarity == "Epic") #Check if c21_1's rarity is Epic

c21_2 = Cookie(
            "Vampire", 
            "Turns into a bat and attacks the rearmost enemy, drinking their blood and restoring some HP \
depending on the amount of damage caused. Restores some HP with each regular attack.",
            "Ambush",
            "Rear",
            "Epic")

c21_3 = Cookie(
            "Tiger Lily", 
            "Charges forward on the back of the Butter Tiger, causing damage to nearby enemies and stunning them. \
While the effect is active, the Cookie deals more damage with faster Regular Attacks.",
            "Ranged",
            "Rear",
            "Epic")

c21_4 = Cookie(
            "Werewolf", 
            "Takes his wolf form, causing area damage. In the wolf form, Werewolf Cookie has increased HP, becomes resistant to interrupting effects, \
and does more powerful double-strike regular attacks. Targets hit by double strikes may be stunned.",
            "Charge",
            "Front",
            "Epic")

c21_5 = Cookie(
            "Mint Choco", 
            "Mint Choco Cookie plays a sublime melody that increases the team's ATK SPD, applies the Warm Breeze buff, \
and grants HP Shield to Wind-type Cookies. Upon playing a melodic tune, he inflicts damage on enemies with his Mint Gust and heals allies'\
HP equal to a portion of the damage inflicted. Once Mint Choco Cookie gains enough Tailwind stacks, \
he will heal his allies once more with a refreshing performance.",
            "Support",
            "Rear",
            "Epic")

c21_6 = Cookie(
            "Herb", 
            "Turns the ground into a wonderful little garden, removing all debuffs and restoring some HP for the whole party. \
Standing near sprouts also restores some HP over time.",
            "Healing",
            "Rear",
            "Epic")

c21_7 = Cookie(
            "Dark Choco", 
            "Strikes the ground with his great sword, inflicting chain lightning upon the enemies. Those unfortunate, \
affected by this dark lightning suffer from great damage and lowered Defense.",
            "Charge",
            "Front",
            "Epic")

c21_8 = Cookie(
            "Sparkling", 
            "Throws refreshing healing cocktails at two allies with the lowest HP. \
The cocktail's divine aroma raises the whole squad's morale, increasing their Critical Strike Chance.",
            "Healing",
            "Rear",
            "Epic")

c21_9 = Cookie(
            "Chili Pepper", 
            "Chili Pepper Cookie increases her CRIT DMG based on her CRIT%. Sneaks behind the enemy, \
causing area damage to the rearmost line with 4 strikes. The final strike always deals critical damage.",
            "Ambush",
            "Middle",
            "Epic")

c21_10 = Cookie(
            "Pomegranate", 
            "Even dark spells can become a formidable ally! The Cookie's crimson magic \
applies a buff restoring some HP over time for the whole squad and increases their ATK.",
            "Support",
            "Middle",
            "Epic")

c21_11 = Cookie(
            "Purple Yam", 
            "Ravages the battlefield in a deadly Purple Tornado, causing substantial periodic area damage. \
While Purple Yam Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Charge",
            "Front",
            "Epic")

c21_12 = Cookie(
            "Milk", 
            "Stands at the front line, causing area damage, and taunts the enemies, forcing them to attack himself. \
While the skill is active, Milk Cookie's Divine Milk Shield decreases incoming damage. \
While Milk Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Defense",
            "Front",
            "Epic")

c21_13 = Cookie(
            "Poison Mushroom", 
            "Plants mushrooms that release purple poison clouds around themselves. \
Poisoned enemies become disoriented and suffer from a debuff reducing Healing, \
but Poison Mushroom Cookie claims that was never the intention... Poison clouds deal extra Poison DMG to monsters and bosses.",
            "Bomber",
            "Middle",
            "Epic")

c21_14 = Cookie(
            "Licorice", 
            "Summons a powerful Black Lightning and Licorice Servants. The potent spell briefly increases the party's Defense. \
Licorice Servants are resistant to certain movement interrupting effects. If the skill is used before the \
summoned Licorice Servants disappear, new additional Licorice Servants will be summoned. While Licorice Cookie is using his skill, \
he will briefly become resistant to interrupting effects.",
            "Magic",
            "Middle",
            "Epic")

c21_15 = Cookie(
            "Madeline", 
            "Calls upon the Celestial Light that allows performing ranged area attacks instead of regular attacks. \
While under the Celestial Light, Madeleine Cookie receives a buff making him immune to debuffs.",
            "Defense",
            "Front",
            "Epic")

c21_16 = Cookie(
            "Espresso", 
            "Precise and even grinding is key for a magically delicious cup of coffee! \
A giant whirlwind inflicts periodic area damage to enemies and pulls them from afar to its center even if they are resistant to interrupts. \
The final burst of damage may interrupts skills. While Espresso Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Magic",
            "Middle",
            "Epic")

c21_17 = Cookie(
            "Rye", 
            "Shoot first if you don't wanna be shot! The Cookie aims both pistols at the enemy with the lowest Max HP \
(targets Cookies first) and shoots a round, dealing a great amount of damage several times. The Cookie's focus is so high, the \
Cookie will become resistant to interrupting effects. The Cookie's ATK SPD is increased greatly for the whole Showdown duration.",
            "Ranged",
            "Rear",
            "Epic")

c21_18 = Cookie(
            "Kumiho", 
            "Transforms into a Cookie and causes area damage and charming nearby enemies, while charming them and reducing their DEF. \
Afterward, fires a powerful Fox Spirit Flame up to 5 enemies near Kumiho Cookie and turns back into marshmallow fox.",
            "Charge",
            "Front",
            "Epic")

c21_19 = Cookie(
            "Latte", 
            "Conjures a Latte Glyph attracting enemies to its center, dealing damage, and silencing them. \
The Glyph remains on the ground, dealing periodic damage and even greater damage to enemies in its center.",
            "Magic",
            "Middle",
            "Epic")

c21_20 = Cookie(
            "Cream Puff", 
            "Conjures a tornado of Jellies over a large area, causing area damage and restoring the party's HP. \
The spell cannot cause CRIT DMG, but instead, there is a chance to conjure it with great success depending on the CRIT%. \
Cast with great success, the spell will inflict greater DMG and heal a greater amount of HP. \
While Cream Puff Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Support",
            "Rear",
            "Epic")

c21_21 = Cookie(
            "Almond", 
            "Uses magical handcuffs to apprehend the enemy with the lowest max HP (targets Cookies first), \
dealing damage and applying the Damage Link debuff, which disperses a portion of \
damage the apprehended enemy receives between up to five linked enemies (cannot be applied to summoned creatures). Cannot be interrupted.",
            "Support",
            "Rear",
            "Epic")

c21_22 = Cookie(
            "Pure Vanilla", 
            "Illuminates the battlefield with his Vanilla Orchid Staff, \
granting Amplify Buffs to regular healing targets. The light reaches all corners of the battlefield, \
replenishing the party's HP and reducing the effects of Injury. Pure Vanilla Cookie heals the amount of HP \
proportional to the reduction of Injury's effects. He then casts an HP Shield absorbing an amount of damage proportional to their Max HP. \
If the Shield is removed or the target cannot receive it, Pure Vanilla Cookie instead grants a buff that restores HP over time. \
While Pure Vanilla Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Healing",
            "Rear",
            "Ancient")

c21_23 = Cookie(
            "Black Raisin", 
            "No one can hide from the keen Black Raisin Eye! The Cookie vanishes into the shadows, \
appears amidst the enemy ranks (targets Cookies first), and strikes several times, dealing substantial area damage.",
            "Ambush",
            "Middle",
            "Epic")

c21_24 = Cookie(
            "Strawberry Crepe", 
            "Uses the giant crepe arms to cause area damage. Reduces DMG received by two allies (targets Cookies first) with the lowest current HP.",
            "Defense",
            "Front",
            "Epic")

c21_25 = Cookie(
            "Fig", 
            "The sound of Fig Cookie's Jelly Horn summons a flock of angered Fig Birds that swarm at the enemies, dealing damage. \
Surprised by this sudden attack, the enemies suffer from reduced ATK.",
            "Support",
            "Middle",
            "Epic")

c21_26 = Cookie(
            "Pastry", 
            "Injustice shall be purged! After Pastry Cookie uses her skill, her regular attacks become stronger, \
and she will fire Lightbringer Bolts at up to two enemies, dealing damage. The bolts will later ricochet, dealing additional damage. \
Pastry Cookie will gain the Battle Prayer buff, increasing the number of targets according to her ATK SPD boost rate. \
She will also increase her ATK SPD and allied Wind-type Cookies' CRIT%.",
            "Ranged",
            "Rear",
            "Epic")

c21_27 = Cookie(
            "Red Velvet", 
            "Face the might of the Cakes! The Cookie grasps the rearmost enemy, brings it in front of the Cookie squad, \
dealing great damage and stunning them for a short time. Cannot be interrupted.",
            "Charge",
            "Front",
            "Epic")

c21_28 = Cookie(
            "Sea Fairy", 
            "Fires a stream of water, inflicting damage and stunning 5 closest enemies (targets Cookies first). \
After a certain time, a full moon-shaped pool of water created underneath the targets bursts up with the power of eternity, dealing heavy damage.",
            "Bomber",
            "Middle",
            "Legendary")

c21_29 = Cookie(
            "Mango", 
            "Sends forward a wave of tropical mango juice, inflicting damage to enemies. The fresh, sweet waves also increase the allies' \
ATK for a short time. While Mango Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Magic",
            "Middle",
            "Epic")

c21_30 = Cookie(
            "Lilac", 
            "Lilac Cookie throws his chakrams in several rounds over a period of time. Friendly units are impressed by the graceful movements, \
and gain increased regular attack DMG proportional to their ATK SPD boost rate.",
            "Support",
            "Middle",
            "Epic")

c21_31 = Cookie(
            "Squid Ink", 
            "Where did Squid Ink Cookie go? And what is this giant squid doing here?! The monster is about to make anyone \
flat as a Cookie with a series of rapid slaps dealing area damage.",
            "Magic",
            "Middle",
            "Epic")

c21_32 = Cookie(
            "Sorbet Shark", 
            "The Cookie ambushes the frontmost enemies in shark form, dealing area damage. Deals additional damage to the two enemies \
(targets Cookies first) with the highest Max HP within the skill's area of effect. For enemies that are Cookies, the additional attack will be dealt as \
true damage relative to the enemies' Max HP and cannot exceed 300000. For other enemies, the additional damage will be regular damage.",
            "Ambush",
            "Middle",
            "Epic")

c21_33 = Cookie(
            "Parfait", 
            "Grabs the microphone and belts her heart out. Touched by the earnest and sincere song, \
all allies will recover some HP and receive a buff that increases DEF and resistance to debuffs. \
While Parfait Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Support",
            "Rear",
            "Epic")

c21_34 = Cookie(
            "Hollyberry", 
            "Let out a war cry of fury! Hollyberry Cookie charges forward and becomes a shield to her Cookie allies, \
absorbing a portion of the damage they take, excluding periodic and indirect damage. While her DMG Focus is active, she will reduce CRIT \
received by her allies and herself, and gain a stack of Seed of Life for every CRIT hit she receives. \
Once she gains enough Seed of Life stacks, the Seed of Life will bloom into Berry of Life, enhancing the succeeding skill. \
The cooldown for Hollyberry Cookie's first skill is reduced, allowing her to use it faster. While Hollyberry Cookie is using her skill, \
she will briefly become resistant to interrupting effects.",
            "Defense",
            "Front",
            "Ancient")

c21_35 = Cookie(
            "Raspberry", 
            "Quickly dashes at the enemy with the highest ATK and continuously stabs them. \
The attack briefly reduces the hit target's ATK for a while. While Raspberry Cookie is using her skill, \
she will be more resistant to interrupting effects.",
            "Charge",
            "Front",
            "Epic")

c21_36 = Cookie(
            "Moon Rabbit", 
            "After transforming into a Giant Rice Cake Bunny, Moon Rabbit Cookie jumps up and down, \
dealing DMG to all enemies. Enemies hit with this skill will be marked with a Healing Rice Cake, \
and when the marked enemies are defeated, the Healing Cake will restore the HP of all allies. The healing amount will depend on the target. \
While Moon Rabbit Cookie is using her skill, she will be more resistant to interrupting effects.",
            "Defense",
            "Front",
            "Epic")

c21_37 = Cookie(
            "Mala Sauce", 
            "Strikes the ground with her mace, rupturing it and dealing area damage. \
Spicy Mala Sauce lava will erupt from the crack and apply the Burn debuff dealing periodic damage to the enemies. \
In addition, this skill increases the CRIT of the two allies (targets Cookies first) with the highest CRIT stat. \
While Mala Sauce Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Charge",
            "Front",
            "Epic")

c21_38 = Cookie(
            "Twizzly Gummy", 
            "Twizzly Gummy Cookie overloads her Electrojelly Gun and fires a powerful electrifying laser beam. \
While Twizzly Gummy Cookie is using her skill, her CRIT DMG is increased and enemies hit by her laser beam will \
be Zapped. This is a non-stackable debuff that deals periodic damage and temporarily disrupts HP Shields. \
While Twizzly Gummy Cookie is charging her laser, she will briefly become resistant to interrupting effects.",
            "Ranged",
            "Rear",
            "Epic")

c21_39 = Cookie(
            "Pumpkin Pie", 
            "Pumpkin Pie Cookie's Pompon grows to a giant size, causing area damage. \
For a given period of time, Giant Pompon inflicts melee area damage up to 3 enemies and applies a non-stackable debuff, \
decreasing the amount of healing the enemies receive. While on the battlefield, Giant Pompon increases ATK SPD for all allied summoned \
creatures. Giant Pompon will be more resistant to interrupting effects while performing the first special attack. \
Also, Pumpkin Pie Cookie can use her decreased first cooldown to use the skill sooner. Pompon is resistant to certain interruption effects.",
            "Magic",
            "Middle",
            "Epic")

c21_40 = Cookie(
            "Cotton", 
            "While Cotton Cookie's lantern shines, the warm light will periodically restore the allies' HP \
and increase the summoned creatures' ATK. Additionally, Cotton Cookie summons sheep that will charge at the enemies, \
dealing area damage and stunning them. The summoned sheep will fight alongside the Cookies for a certain time. \
While Cotton Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Support",
            "Rear",
            "Epic")

c21_41 = Cookie(
            "Frost Queen", 
            "Casts an ice squall, dealing damage, freezing all enemies, and applying the Frost debuff. \
Once Frozen, the targets' Cooldown will be paused and will receive an additional portion of damage when thawed. \
Targets resistant to Freezing receive only a portion of the DMG. If the Freeze debuff is dispelled, the targets will not receive the additional damage. \
Frost Queen Cookie herself is immune to freezing. While Frost Queen Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Magic",
            "Middle",
            "Legendary")

c21_42 = Cookie(
            "Cocoa", 
            "Cocoa Cookie jumps into a giant cocoa mug and happily spins around for a given time, attacking the enemies. \
At the same time, Cocoa Cookie restores the HP for all allied Cookies except for summoned creatures and makes them \
immune to stunning. While Cocoa Cookie is using her skill, she will briefly become resistant to \
interrupting effects. Cocoa Cookie's regular attack will heal 3 allies (targets Cookies first) with the lowest HP.",
            "Defense",
            "Front",
            "Epic")


