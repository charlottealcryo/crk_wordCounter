import re
class Cookie:
  def __init__(self, name, skill, type, position, rarity):
    self.name = name
    self.skill = skill
    self.type = type
    self.position = position
    self.rarity = rarity


c24_1 = Cookie(
            "Rebel", 
            "Rebel Cookie uses his magic, decreasing the enemies' DEF, making them more vulnerable to all types of damage, \
and dealing damage. Enemies with decreased DEF will receive additional damage. Rebel Cookie will increase the allies \
CRIT and provide an HP Shield for them, blocking damage equal to a portion of the damage he has dealt. After finishing \
using his skill, he will create 2 decoys that will Push enemies back with each Regular Attack. The decoys have a \
number of Hits instead of HP. While Rebel Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Ambush",
            "Front",
            "Epic")

c24_2 = Cookie(
            "White Lily", 
            "A pure white lily bud bursts open, dealing periodic damage to enemies and additional damage depending on the number of buffs \
White Lily Cookie has on herself. Enemies affected by the skill will become entangled in Vines, becoming unable to move or use skills. \
Whenever her or an ally Cookie gains a debuff, she will gain the Lily Restoration buff, and whenever White Lily Cookie uses her skill, \
she will gain Lily Restoration buffs. Once Lily Restoration reaches a certain number of stacks, it will purify all current debuffs on the \
allies and heal them. White Lily Cookie is immune to the Spore Dispersal and Mushroom Mutation effects.",
            "Bomber",
            "Middle",
            "Ancient")

c24_3 = Cookie(
            "Silverbell", 
            "Silverbell flowers bloom, periodically healing the allies and granting a DMG Resist buff. Healing targets will also \
receive bonus healing depending on the number of buffs they currently have. Enemies will receive damage and gain the \
Silverbell Pollen debuff dealing periodic damage. When Silverbell Pollen's duration is over, it will cause area damage \
and Stun the targets in range. Silverbell Cookie is immune to the Spore Dispersal and Mushroom Mutation effects. \
Entering the battle with Head Icon Mercurial Knight Cookie will activate the Silver Knighthood effect.",
            "Support",
            "Rear",
            "Epic")

c24_4 = Cookie(
            "Mercurial Knight", 
            "With the power of mercury, Mercurial Knight Cookie's regular attacks are strengthened, dealing area damage to enemies and casting \
Mercury Poisoning. Mercurial Knight Cookie will then land his final strike, dealing damage and additional damage based on the number \
of Mercury Poisoning stacks. When Mercurial Knight Cookie is inflicted with a debuff, he will gain an Amalgamation buff, and when he \
gains enough stacks, he'll dispel all debuffs and enter Mercury Storm mode. In Mercury Storm mode, Mercurial Knight Cookie will not \
receive an Amalgamation buff. Due to his mercurial armor, Mercurial Knight Cookie is immune to the Spore Dispersal and Mushroom Mutation \
effects. While Mercurial Knight Cookie is using his skill, he will briefly become resistant to interrupting effects. When Mercurial Knight \
Cookie enters the battlefield with Head Icon Silverbell Cookie, the Silver Knighthood buff will activate.",
            "Charge",
            "Front",
            "Epic")

c24_4 = Cookie(
            "Elder Faerie", 
            "Elder Faerie Cookie strikes down with his sword containing Prism Energy to deal damage, taunt enemies, and purify debuffs on himself. \
Then, the energy in the sword causes an explosion, dealing more damage, applying Injury, and reducing the amount of Healing enemies receive. \
He shields his allies with an HP Shield proportional to his ally Cookies' Max HP, and the shield capacity increases with more buffs applied on \
Elder Faerie Cookie Elder Faerie Cookie grants a Prism Shard and applies a DMG Resist buff to himself, White Lily Cookie, and a Cookie with the \
highest ATK (or two Cookies with the highest ATK if White Lily Cookie is not in the team). If Elder Faerie Cookie has the Beascuit HP upgrade, \
he can apply Prism Shards to more allies. Using a Prism Shard charge will heal the target's HP for a certain amount of time. Unlike other Cookies, \
White Lily Cookie will gain two Prism Shards. Elder Faerie's DMG Resist will increase when affected by a debuff. \
While Elder Faerie Cookie is using his skill, he will briefly become resistant to interrupting effects and immune to ATK SPD changes.",
            "Defense",
            "Front",
            "Super Epic")

c24_5 = Cookie(
            "Matcha", 
            "Matcha Cookie summons Tea Seeds at the enemies' location and causes an explosion. The Tea Seeds poison enemies, \
amplify debuff effects, and increase the duration of Poison-type Periodic DMG inflicted by the team. At times, Matcha \
Malice may manifest from a Tea Seed, shackling a random enemy, dealing damage, Cursing them and applying Healing, Poison, \
and Amplify DMG debuffs. Matcha Malice is even applied to Cookies who are resistant to interrupting effects. At the end of \
the skill's duration, Matcha Malice will deal explosion DMG and apply Silence. The chance of Matcha Malice's appearance will \
increase with more debuffs applied to Matcha Cookie. While Matcha Cookie is using her skill, she will briefly become resistant \
to interrupting effects.",
            "Magic",
            "Middle",
            "Epic")

c24_6 = Cookie(
            "Butter Roll", 
            "Butter Roll Cookie spins his whisk, dealing damage and sucking in enemies at the center of the whisk vortex, \
reducing their ATK and ATK SPD, and increasing Butter Roll Cookie's DMG Resist. He then deals more damage with \
his whisk and Stuns his enemies, dealing extra damage to enemies resistant to Stuns. \
While Butter Roll Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Charge",
            "Front",
            "Epic")

c24_7 = Cookie(
            "Caramel Choux", 
            "Caramel Choux Cookie uses I've Got Choux to heal allies. She applies DMG Resist, Amplify Buff to targets receiving healing, \
and applies an HP Shield to an ally Cookie with the lowest Max HP. As the Town Square supervisor, Caramel Choux Cookie applies \
the Friendly Helper buff to all ally Cookies when entering battle. While Caramel Choux Cookie is using her skill, she will \
briefly become resistant to interrupting effects.",
            "Support",
            "Rear",
            "Epic")

c24_8 = Cookie(
            "Street Urchin", 
            "Street Urchin Cookie rides her motorbike into her enemies, dealing DMG, inflicting Stun, and causing additional explosion DMG if \
the target is affected by Burn. Her CRIT increases and inflicts Burn and Fire-type DMG amplification debuff to enemies. If Street \
Urchin Cookie or her allies inflict Burn on an enemy, her Fire-type ATK DMG increases. While Street Urchin Cookie is using her skill, \
she will briefly become resistant to interrupting effects.",
            "Bomber",
            "Middle",
            "Epic")

c24_9 = Cookie(
            "Stormbringer", 
            "Stormbringer Cookie, the ruler of the skies and lightning, becomes Supercharged when her CRIT exceeds \
a certain percentage at the start of the battle, granting Supercharge buffs to Electricity-type ally Cookies.\
When Stormbringer Cookie becomes Supercharged, her regular attacks trigger Chain Lightning after a certain number of hits. \
Upon using her skill, she swings her Heaven Splitter, dealing damage to enemies and inflicting Zap.\
Whenever ally Cookies deal Electricity-type damage, it activates Stormbringer's Aura and inflicts Stormbringer's Punishment \
upon a certain amount of stacks. Stormbringer's Punishment deals damage and inflicts Overcurrent on enemies. If enemies are \
inflicted with Zap, they receive extra damage and their status changes to Overcurrent. Stormbringer's Aura resets when Stormbringer's \
Punishment is activated.",
            "Charge",
            "Front",
            "Legendary")

c24_10 = Cookie(
            "Mystic Flour", 
            "Creates the Realm of Apathy, shielding the allies with the Cocoon of Futility. Allies within the Realm of Apathy have their HP \
periodically restored. They will also gain the Touch of Meaninglessness buff. Once the duration of the Realm of Apathy is over, the \
allies will be Healed for a portion of the DMG they have dealt. The Cocoon of Futility cannot be Dispelled or removed by Zap or Overcurrent. \
The effect will remain even after the HP Shield reaches 0 capacity. If the target is at Max HP, incoming Healing will restore the HP Shield instead. \
If an enemy Cookie enters the Realm of Apathy, their Cooldown will be increased, otherwise their ATK SPD will be reduced. \
They will also be debuffed with the Pale Plague, increasing the remaining Cooldown when dispelled. Mystic Flour Cookie will \
increase her own DMG Resist based on the decreased amount of Cooldown. Her Lantern of Apathy will keep healing the allies regardless \
of Mystic Flour Cookie's current status and will be further enhanced when she is defeated. \
If there are no Safeguarded Cookies in the team, Mystic Flour Cookie cannot be incapacitated, and gains increased Max HP. \
The amount of Healing coming from the Lantern of Apathy and its trigger rate will also greatly increase. Ally Cookies will \
also be provided with Buff Protection. Mystic Flour Cookie is immune to Apathy along with all targets of the Cocoon of Futility \
and disrupts the Power of Apathy effect affecting enemies.",
            "Healing",
            "Rear",
            "Beast")

c24_11 = Cookie(
            "Cloud Haetae", 
            "Takes the form of a Cloud Haetae. After transforming, gains an increased DEF and DMG Resist and grants HP Shields for the entire team. \
With their regular attacks, Cloud Haetae Cookie charges at the enemies, dealing area damage. Cloud Haetae Cookie will also heal the ally \
with the lowest HP with Cloud Rolls (except Cloud Haetae Cookie themselves). When the transformation is over, Cloud Haetae Cookie will \
perform a last forceful charge to deal greater damage and Stun the enemies. While in the Cloud Haetae form, the Cookie will disable Debuff \
Immunity applied on enemy Cookies. Belonging to the Realm of Apathy, Cloud Haetae Cookie can briefly disrupt the Power of Apathy effect \
when using their skill and grant the Visions of Apathy buff to the team. When in the same team with Mystic Flour Cookie, Cloud Haetae \
Cookie will gain the Haetae's Loyalty buff. Cloud Haetae Cookie will regain HP with each 3 regular attacks in the Cookie form.",
            "Defense",
            "Front",
            "Epic")

c24_12 = Cookie(
            "Peach Blossom", 
            "With a gentle flick of a peach tree branch, Peach Blossom Cookie summons a Peach Tree that will periodically heal the team and bear Peach Bao fruits. \
The ally with the lowest Current HP will receive additional Healing. Peach Blossom Cookie will give Heavenly Fruits to the allies to increase their \
DMG Resist and Debuff Resist. The fruit will also grant resistance to Apathy, and ATK and DMG Resist buffs when affected by Apathy. Enemies will \
receive Unripe Peach Baos, inflicting DMG, reducing their ATK SPD and MOV SPD. Peach Fragrance will protect Peach Blossom Cookie,\
making him immune to Apathy.",
            "Support",
            "Middle",
            "Epic")

c24_13 = Cookie(
            "Dark Cacao (Dragon Lord)", 
            "With his newly found strength, swings the Chocoblade to deal damage, inflict Injury and Fatal Wound, and apply a CRIT DMG debuff. \
After this, Dark Cacao Cookie will borrow the strength of the Twin Dragons for a forceful downward strike, increasing Darkness-type \
damage and applying Consuming Darkness and Gloom. At the beginning of battle, Dark Cacao Cookie will increase the allies' DMG Resist \
with a Royal Decree. Inspired by his Kingly Presence, he will gain increased DEF and Max HP and Charge Cookies will gain increased ATK. \
Channel Darkness will become more efficient for Dark Choco Cookie, and his DMG Resist will increase.",
            "Charge",
            "Front",
            "Awakened")

c24_14 = Cookie(
            "Cream Ferret", 
            "Transforms into their animal form, healing allies and granting DMG Resist, CRIT%, and CRIT DMG buffs. Cream Ferret Cookie hops on to the Cookie with \
the highest ATK (excluding Safeguarded Cookies), granting them the Fuzzy Scarf buff; then returns to their Cookie form and grants themselves a Debuff \
Resist buff. The friendly critter scurries to a Cookie whose HP is below a certain point and grants them the Precious Friend buff and Fuzzy Scarf buff. \
They cannot use their skill temporarily while scurrying to a Cookie. Cream Ferret Cookie is immune to damage while in their animal form.",
            "Support",
            "Rear",
            "Special")

c24_15 = Cookie(
            "Star Coral", 
            "Summons a twinkling coral to heal her allies, provide an HP Shield, and increase their CRIT%, ATK SPD, and Amplify Buff. The Cookie's lantern will \
shine towards the enemies, dealing periodic damage. Star Coral Cookie's Lunar Lantern makes her immune to Sleep and Drowsy, and will periodically \
restore the allies' HP instead.",
            "Support",
            "Rear",
            "Epic")

c24_16 = Cookie(
            "Wind Archer", 
            "Upon transforming, Wind Archer Cookie removes all debuffs from himself, then shoots his Arrow of Gale, pushing back and stunning enemies, \
and applies the Trace of the Wind and Pursuer debuffs. While transformed, he will become immune to debuffs except for Curse and will shoot \
his Pursuer's Arrows with his attacks. The Pursuer's Arrow attacks up to five enemies with the highest ATK and applies the Trace of the Wind \
and Pursuer debuffs to its targets. Once Pursuer reaches max stacks, it will explode and inflict damage proportional to the targets' Max HP, \
damage nearby enemies, and apply the Trace of the Wind debuff. Wind Archer Cookie applies the Mighty Gale buff to himself whenever he shoots \
the Pursuer's Arrow. This Guardian Cookie casts Last Wind, which partially ignores the target's DMG Resist and inflicts additional damage to \
enemies proportional to the number of Mighty Gale stacks. Affected enemies will be trapped in a Cyclone. When entering the battle, Wind Archer \
Cookie's Max HP increases. (DMG proportional to Max HP is capped at 300000.)",
            "Ranged",
            "Rear",
            "Legendary")

c24_17 = Cookie(
            "Burning Spice", 
            "In exchange of his own lifeforce, Burning Spice Cookie releases his inner God of Destruction, dispelling debuffs \
and gaining the Berserker buff. While transformed, he will become immune to all debuffs except for Curse and will absorb the ATK of the three \
allies (targets Cookies first) with the highest ATK. Burning Spice Cookie will gain the Spice Rampage buff depending on the target of his basic \
attacks and will gain the Enrage buff after reaching a certain threshold. After, he will slam down the ground with his great axe, dealing damage \
with the final blow. The axe will create a pool of lava for a certain period of time and deal periodic damage. Enemies' ATK SPD and ATK are reduced \
in the lava, while the Sarcophagus of Gold and summons receive a great amount of damage. The Great Destroyer, Burning Spice Cookie, \
activates Firestorm periodically, inflicting Burn to all targets (excluding Safeguarded Cookies) and providing CRIT and CRIT DMG buffs \
for his allies. Additionally, he applies The Destroyer's Gaze debuff on the enemy Cookie with the highest ATK. Upon entering the battle, \
Burning Spice Cookie applies the Revelry of Flames buff on Fire-type allies, which increases their ATK and DMG Resist by the number of Burn \
stacks. Additionally, Burning Spice Cookie's CRIT increases according to the number of nearby targets with Burn. When hit by Water-type attacks \
for a certain number of times, a Burn debuff is removed. If Burning Spice Cookie is defeated, he becomes Immortal \
for a certain period of time and dispels debuffs. (DMG proportional to Max HP is capped at 300000))",
            "Charge",
            "Front",
            "Beast")

c24_18 = Cookie(
            "Nutmeg Tiger", 
            "Nutmeg Tiger Cookie orders her Elite Guard to charge forward. The Elite Guard deals Fire damage, causing Burn, heals the allies for a \
portion of the damage dealt, increasing their Fire-type Periodic DMG duration, and applying the Great General buff to all Fire-type Cookies \
and summoned creatures. The Elite Guard consists of a Rider and Fighters. The Rider will cause area damage with their regular attacks and heal \
your team for a portion of the damage dealt. The Fighters will taunt enemies upon summoning, protect themselves with an HP Shield, and gain a \
DMG Resist buff. After summoning the Elite Guard, Nutmeg Tiger Cookie will attack up to 5 enemies with each regular attack and gain an ATK \
SPD buff. If Burning Spice Cookie is in the team, he will absorb the dust of the fallen Elite Guards and gain the Burning Nutmeg buff.",
            "Support",
            "Rear",
            "Epic")

c24_19 = Cookie(
            "Smoked Cheese", 
            "Smoked Cheese Cookie uses his smoke to Charm enemies, amplifying the damage received and dealing multiple damage to enemies within the smoke.\
Then, with an explosion, he deals more damage and extra damage to enemies in PvE. Upon using his skill, he applies the Guardian's Return buff \
to an ally with the highest ATK. If Golden Cheese Cookie is in the team, he will prioritize her instead. The Protector of the Golden City buff \
will activate when entering a battle together with Golden Cheese Cookie. This effect is applied to Golden Cheese Cookie, Burnt Cheese Cookie, \
and Smoked Cheese Cookie.",
            "Magic",
            "Rear",
            "Epic")

c24_20 = Cookie(
            "Golden Cheese (Immortal)", 
            "Upon using her skill, Golden Cheese Cookie spreads her wings and throws her Spears of the Immortal, dealing damage up to 8 times \
when there are five or more enemies. For each enemy defeated, she gains an extra Spear of the Immortal. The number of Spears can \
increase to up to 12 in total. When hit by the Spear, enemies receive a debuff amplifying Earth-type damage and decreasing CRIT and CRIT DMG \
While Golden Cheese Cookie is using her skill, she will inflict Immortal's Retribution on the enemy with the lowest HP, applying Curse, \
Immortal's Punishment, Healing Prevention, and dealing damage. She then deals explosion damage to nearby enemies and additional damage \
proportional to her Spear of the Immortal stacks. Once per battle, Golden Cheese Cookie will revive and enter the Immortal's Return state. \
In this state, her DMG Resist, ATK, and DEF will increase. Golden Cheese Cookie will also cover the team with the Dome of Gold that will \
 take damage instead of the allies and make them immune to Knockback. The great Immortal Golden Cheese Cookie increases all Ranged Cookies' \
DMG Resist and ATK. (DMG proportional to Max HP is capped at 300000.)",
            "Ranged",
            "Middle",
            "Awakened")

c24_21 = Cookie(
            "Camellia", 
            "Upon using the skill, Camellia Cookie will increase his own Debuff Resist and the team's CRIT%. Then, he will charge at the enemies, \
brandishing his painting brush. With his final stroke, Camellia Cookie will deal greater damage and Stun all enemies affected by it. \
He will also remove all buffs from the two Cookies with the highest ATK. If Camellia Cookie deals damage with the skill, \
enemies will receive a DMG-increasing debuff.",
            "Charge",
            "Front",
            "Super Epic")

c24_22 = Cookie(
            "Golden Osmanthus", 
            "Golden Osmanthus Cookie creates an incense sachet, healing allies and covering them with an HP Shield. \
The incense burner floats towards enemies and then bursts with flower petals, \
dealing damage. Additionally, enemies become Charmed by the mesmerizing scent.",
            "Bomber",
            "Middle",
            "Epic")

c24_23 = Cookie(
            "Red Osmanthus", 
            "Red Osmanthus Cookie plays the pipa and sends a gust of petals, dealing damage and decreasing enemies' ATK. \
While using her skill, Red Osmanthus Cookie will increase her own CRIT DMG and deal additional damage with each CRIT hit. \
DMG proportional to Max HP is capped at 300,000.",
            "Ranged",
            "Middle",
            "Epic")

c24_24 = Cookie(
            "Pudding a la Mode", 
            "Pudding a la Mode Cookie's arms transform into plasma cannons and emit powerful plasma beams towards enemies. Next, \
the Cookie will call upon her drones, which attack the same targets during her regular attacks. Drone attacks are regarded as Pudding \
a la Mode Cookie's regular attacks. Drones will prioritize targets with a Penumbral Mark. The Team Drizzle effect will activate \
when entering battle with Choco Drizzle Cookie and Green Tea Mousse Cookie.",
            "Bomber",
            "Rear",
            "Epic")

c24_25 = Cookie(
            "Choco Drizzle", 
            "Choco Drizzle Cookie hides amidst the shadows and applies a Penumbral Mark and Consuming Darkness upon the farthest enemy \
(targets Cookies first), then deals a series of 8 hits to the target and nearby enemies. If the target has a Penumbral Mark, \
it will trigger Drizzle Strike, dealing additional damage. If the Penumbral Mark is on a Cookie, it will carry over to the nearest \
Cookie after the original target is eliminated, decreasing Choco Drizzle Cookie's remaining Cooldown. The Cooldown decrease can trigger up \
to 3 times per battle. If the Penumbral Mark is on a non-Cookie target, the carry-over effect and a decrease in Cooldown will not be triggered. \
If an enemy's HP falls below a certain level, Choco Drizzle Cookie will identify their weakness and perform Drizzle Strike immediately, \
dealing greater damage. This effect can trigger only once for each enemy. Upon using her skill, Choco Drizzle Cookie will prioritize targets \
with a Penumbral Mark, ignoring any taunt effects. The Team Drizzle effect will activate when entering battle with Green Tea Mousse \
Cookie and Pudding a la Mode Cookie.",
            "Ambush",
            "Middle",
            "Epic")

c24_26 = Cookie(
            "Green Tea Mousse", 
            "Green Tea Mousse Cookie Taunts enemies and combines her shields into one. Her regular ATK SPD decreases, \
but she becomes able to attack all nearby enemies, Push them back, and then Stun with a certain probability. After that, \
Green Tea Mousse Cookie will apply a DMG Resist buff to her allies and gain the Mousse Shield buff and an HP Shield. If she \
receives a certain number of hits while her Mousse Shield is active, Green Tea Mousse Cookie will heal the team in proportion \
to her DEF. This effect will activate once over a certain period of time. The Team Drizzle effect will activate when entering battle \
with Choco Drizzle Cookie and Pudding a la Mode Cookie.",
            "Defense",
            "Front",
            "Epic")

c24_27 = Cookie(
            "Okchun", 
            "Okchun Cookie rides a giant okchun pouch and heals allies every time she jumps. Her third jump will heal allies \
more than the first and second jumps, and grants the CRIT and CRIT DMG buffs to allies. She also applies the Okchun \
Candy buff, which disappears after healing targets with Max HP lower than 50%. Okchun Cookie applies the Okchun Gift buff \
to allies when entering battle. Okchun Cookie creates speech bubbles every three days in the kingdom, and rewards can be \
claimed by tapping on them. The higher the level, the better the rewards.",
            "Healing",
            "Middle",
            "Epic")



