import re
class Cookie:
  def __init__(self, name, skill, type, position, rarity):
    self.name = name
    self.skill = skill
    self.type = type
    self.position = position
    self.rarity = rarity


c23_1 = Cookie(
            "Prophet", 
            "Prophet Cookie delivers one out of seven prophecies. Upon invoking a prophecy,  \
Prophet Cookie will heal an ally and amplify buffs they receive. Additionally, an extra skill effect will be activated \
depending on the symbol of the prophecy, dealing damage to the enemies and amplifying debuffs they receive. The debuffs \
applied by the prophecies are weaker than those of the original skills and does not inflict elemental type DMG. Some \
prophecies do not have any additional effects. You can lock the effect of the prophecy, guaranteeing a specific \
effect, by equipping Toppings. While Prophet Cookie is using his skill, he will briefly become resistant to \
interrupting effects. Wandering around the Kingdom, Prophet Cookie will come up with Fortune Cookies every three days. \
Tap the Fortune Cookie to obtain a gift. The higher Prophet Cookie's rank, the better gift!",
            "Support",
            "Rear",
            "Epic")

c23_2 = Cookie(
            "Milky Way",
            "Milky Way Cookie jumps onto her dream train, gaining a DMG Reduction buff and providing a Stun Resistance buff \
for the entire team. Then she will push back the enemies several times, applying a DEF Reduction debuff and dealing damage. \
Once she's done with her shift, Milky Way Cookie will cast a Shield onto herself and the rest of the team. While Milky Way \
Cookie is using her skill, she will briefly become resistant to interrupting effects. Being a dweller of the World of Dreams, \
Milky Way Cookie is not susceptible to the Beckoning Dreams & Dream of Doom effect.",
            "Charge",
            "Front",
            "Epic")

c23_3 = Cookie(
            "Moonlight",
            "Moonlight Cookie falls asleep in the night sky and dreams a dream where stars fall onto the enemies' heads, dealing damage and applying a DMG \
Increase debuff. Then, bright moonlight illuminates the battlefield, dealing damage to the enemies and putting them to Sleep. Enemies that didn't \
fall Asleep become Drowsy and will eventually fall Asleep when their resistance statuses wear off. \
When Moonlight Cookie awakens, she will restore her own HP. She will also restore her own HP upon awakening from Sleep effects cast by enemies. \
Being a dweller of the World of Dreams, Moonlight Cookie is not susceptible to the Beckoning Dreams & Dream of Doom effect. (DMG relative \
            to Max HP is capped at 300000)",
            "Magic",
            "Middle",
            "Legendary")

c23_4 = Cookie(
            "Blueberry Pie",
            "An evil spirit appears from the Tome, dealing damage to the enemies and inflicting them with the Greed of the Tome debuff. \
It will also heal Blueberry Pie Cookie's HP and increase her DMG Resist. The Tome will gain a stack of Greed whenever the spirit deals \
damage to Cookies, or the target inflicted with the Greed of the Tome debuff becomes incapacitated. Once the Tome has enough stacks of Greed \
it will unleash its Sealed Power, increasing Blueberry Pie Cookie's ATK and dealing DMG to the enemies. \
While Blueberry Pie Cookie is using her skill, she will briefly become resistant to interrupting effects. DMG proportional to Max HP is capped at 300000.",
            "Magic",
            "Middle",
            "Epic")

c23_5 = Cookie(
            "Stardust",
            "Stardust Cookie soars in the sky and marks the enemy with the highest ATK (targets Cookies first) with the Sign of the Stars. \
Then he will descend to deal area damage to the enemies, amplifying debuffs they receive. Targets will receive additional damage \
depending on the number of buffs they currently have. The Sign of the Stars prevents the target from gaining buffs, decreases their \
ATK and Healing, and increases the DMG received. If the skill delivers a critical hit, the target will fall Asleep. \
If the Sign of the Stars is dispelled, the target and the nearby enemies will receive damage. \
After casting his skill, Stardust Cookie will gain a DMG Resist buff himself. If the enemies are Asleep, Stardust Cookie summons meteors to attack them.",
            "Ambush",
            "Middle",
            "Super Epic")


c23_6 = Cookie(
            "Space Doughnut",
            "Fires the Doughnut Beam, dealing damage, reducing the targets' DEF, and amplifying debuffs they receive. \
Hit targets will turn into donuts (excluding bosses and Cookies). The target will receive extra damage if they are \
already afflicted with a DEF-reducing debuff. When the targets turned to donuts reach a certain number, Space Doughnut will \
use Super Doughnut Blast, rolling over the enemies, dealing damage and Stunning them. Space Doughnut does not take damage while using their skill.",
            "Charge",
            "Front",
            "Epic")


c23_7 = Cookie(
            "Capsaicin",
            "Capsaicin Cookie transforms with the surge of magma power. When he has transformed, his regular attacks will cause Lava Eruptions, \
inflicting Burn and Magma debuffs to enemies. While transformed, Capsaicin Cookie will briefly become resistant to interrupting effects. \
After his transformation, Capsaicin Cookie will enter Spice Overlord mode with all the intense magma power and deliver his final strike. \
If Capsaicin Cookie is defeated for the first time, he will become Immortal, \
dispelling his debuffs and cannot be defeated for a certain period. The first cooldown of Capsaicin Cookie's skill will be shortened, \
allowing for faster skill use.",
            "Charge",
            "Front",
            "Super Epic")


c23_8 = Cookie(
            "Prune Juice",
            "For Prune Juice Cookie's regular attack, he throws a Prune Juice Bottle at the farthest enemy, \
poisoning the target and nearby enemies. Upon using his Skill, Prune Juice Cookie will throw a \
giant Prune Juice Bottle containing poison. When the bottle shatters, it will inflict Poison DMG Boost, \
Sticky Goo, Poison, and summon Prune Jellies. The HP of summoned Prune Jellies are reduced by the number of hits. \
Summoned Prune Jellies will spread Prune Gas from time to time, poisoning nearby enemies. \
Summoned Prune Jellies are consisted of poison, immune to any kind of periodic effects and are not affected by Shield or Healing.",
            "Bomber",
            "Middle",
            "Epic")

c23_9 =  Cookie(
            "Kouign-Amann",
            "After using the skill, Kouign-Amann Cookie channels the Power of the Light, enhancing her regular attacks: they deal \
Light-type DMG and extra DMG depending on the number of buffs she has on herself. Kouign-Amann Cookie will also increase \
the ATK SPD of the two Cookies with the highest ATK SPD, make all her allies resistant to ATK SPD debuffs, and increase the \
Light-type DMG dealt by other Cookies. When the skill's duration reaches its end, Kouign-Amann Cookie will gather the Power of \
the Light and perform a powerful attack, partially ignoring the target's DMG Resist with a swing of her sword. Having no fear of defeat, \
Kouign-Amann Cookie will increase her DMG Resist whenever she gains a debuff, and increase her ATK SPD whenever she uses a regular attack. \
While Kouign-Amann Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Defense",
            "Front",
            "Epic")

c23_10 =  Cookie(
            "Pitaya Dragon",
            "Pitaya Dragon Cookie fires off two waves of draconic blade energy, dealing damage and reducing the amount of Healing the targets receive. \
After this, the Cookie assumes their dragon form and spews flaming breath, applying Burn and reducing the targets' ATK. Whenever Pitaya Dragon \
Cookie uses their skill, they gain a stack of Pitaya Fury that will enhance the skill upon reaching the maximum stacks. \
When using the enhanced skill, Pitaya Dragon Cookie's flaming breath will deal damage and decrease the target's resistance \
to Burn and Fire-type DMG. In their dragon form, the Cookie will gain increased CRIT and remove all debuffs applied to themselves. \
As a Dragon Cookie, Pitaya Dragon Cookie will receive less damage from other Dragon Cookies and have their DMG Resist increased in \
proportion to their ATK enhanced with Toppings. While Pitaya Dragon Cookie is using their skill \
they will briefly become resistant to interrupting effects.",
            "Charge",
            "Front",
            "Legendary")

c23_11 =  Cookie(
            "Royal Margarine",
            "Royal Margarine Cookie soars on Buttercream's back and fires Buttercream Blasts at the 3 enemies with the \
highest ATK thrice. Buttercream Blasts deal damage, Poison the targets, reduce their ATK and DEF, \
and amplify debuffs they gain. Next, Buttercream swoops down towards the enemies, dealing damage and \
additional damage in proportion to the number of periodic damage effects the targets' have applied. Buttercream Blasts target boss monsters first. \
While Royal Margarine Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Ambush",
            "Middle",
            "Epic")

c23_12 =  Cookie(
            "Tarte Tatin",
            "When Tarte Tatin Cookie fires her cannon, she reduces her own Cooldown and Shackles her enemies after a certain number of hits. \
Upon using her skill, she will fire a cannonball straight towards the center of the enemy team. Hit enemies suffer from Burn and \
Bosses receive extra damage. After a certain number of skill uses, Tarte Tatin Cookie will fire an enhanced cannonball. During the \
battle, when Tarte Tatin Cookie or any ally successfully defeats an enemy or a boss, her ATK will increase. While Tarte Tatin Cookie \
is using her skill, she will briefly become resistant to interrupting effects.",
            "Ranged",
            "Rear",
            "Epic")

c23_13 =  Cookie(
            "Snapdragon",
            "As an ancient entity, Snapdragon Cookie is safeguarded and invulnerable to enemy attacks. The elder magic of their \
skill will bloom snapdragons, periodically healing the team's HP and granting a buff providing Stun resist, increased \
Debuff Resist, increased ATK, increased DMG Resist, and an HP Shield. Elder magic grants Dragon Cookies Draconic Lifeforce, \
increasing the Max HP of Dragon Cookies.",
            "Support",
            "Rear",
            "Special")

c23_14 =  Cookie(
            "Shining Glitter",
            "Shining Glitter Cookie begins singing the Glittering Song, dispelling all debuffs from herself, applying the Glittering Rock \
Spirit buff to her allies, and dealing damage to the enemies. Whenever the song lands a critical hit, it will partially ignore \
the target's DMG Resist and Zap them. If Shining Glitter Cookie manages to deal a certain number of critical hits with the Glittering Song, \
she will provide a CRIT Resist buff for the entire team. While Shining Glitter Cookie is using her skill, \
she will briefly become resistant to interrupting effects.",
            "Magic",
            "Middle",
            "Super Epic")

c23_15 =  Cookie(
            "Rockstar",
            "Rockstar Cookie performs a rock anthem, periodically Healing the team's HP and applies the Legendary Rock Spirit buff, Curse Protection buff, \
and a CRIT buff for the whole team excluding himself based on his CRIT boost from equipped Toppings. Under Legendary Rock Spirit, the target \
will have their HP restored whenever they deal five critical hits. If Rockstar Cookie is defeated for the first time, he will have all active \
debuffs on himself removed and begin his Encore. During Encore, Rockstar Cookie will provide extra Healing and increase the Healing the team receives. \
While Rockstar Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Healing",
            "Middle",
            "Epic")

c23_16 =  Cookie(
            "Black Lemonade",
            "Black Lemonade Cookie plays her electric guitar, dealing damage to the enemy with the highest HP (targets Cookies first), \
inflicting Zap, and applying debuffs that increase CRIT DMG the enemy receives and decrease their DEF. She then deals damage to \
the nearby enemies and inflicts a debuff reducing their ATK. Black Lemonade Cookie grants the Electrifying Rock Spirit buff to the \
team and strengthens her next regular attacks to target the enemy with the highest HP and enemies near them. When Ally Cookies with \
the Electrifying Rock Spirit buff deal Zap damage or a critical hit, their Electrifying Rock! charge increases. Once the Electrifying Rock! \
is charged, they deal additional damage to enemies. While Black Lemonade Cookie is using her skill, she will briefly become resistant \
to interrupting effects.",
            "Bomber",
            "Middle",
            "Epic")

c23_17 =  Cookie(
            "Peppermint",
            "Peppermint Cookie blows the conch shell to summon the Peppermint Whale. The refreshing sound of the conch shell heals the team, \
increasing their DMG Resist and Debuff Resist. The Peppermint Whale creates a wave, dealing Water-type damage to enemies in front of it, \
and also Heals the allies for an amount equal to a portion of the damage dealt. Fresh water brought by the whale covers the team with an HP Shield. \
Peppermint Cookie will briefly become resistant to interrupting effects while using the skill.",
            "Support",
            "Rear",
            "Epic")

c23_18 =  Cookie(
            "Crimson Coral",
            "Crimson Coral Cookie's sisters will lend their powers to the crimson spear, piercing enemies and dealing damage. \
Afterwards, Crimson Coral Cookie will cast an HP Shield to the 2 allies with the highest ATK (excluding herself) equal \
to a portion of her Water-type Skill damage. If Crimson Coral Cookie is the only Cookie in the front line, she and her \
allies will gain the Coral Armor buff. Additionally, her Coral Armor's size and weight will reduce the effect of Knockback \
and Flying. When Crimson Coral Cookie is using her skill, she is not affected by \
ATK SPD changes and will become resistant to interrupting effects.",
            "Defense",
            "Front",
            "Super Epic")

c23_19 =  Cookie(
            "Frilled Jellyfish",
            "Upon using her skill, Frilled Jellyfish Cookie Shackles up to 5 enemies (targets Cookies first) with her tentacles, \
dealing Sea Foam damage and reducing their MOV SPD. The targets are inflicted with Zap and take increased Water-type DMG. \
Additionally, Frilled Jellyfish Cookie will burrow in the ground and protect herself with a DMG Resist buff. When Frilled \
Jellyfish Cookie uses her skill, ATK SPD changes don't affect her actions. If Frilled Jellyfish Cookie is defeated, she will \
dissipate into several little jellyfish, who will periodically provide Healing for the team.",
            "Support",
            "Middle",
            "Epic")

c23_20 =  Cookie(
            "Golden Cheese",
            "Upon using her skill, Golden Cheese Cookie throws her Spears of Radiance, dealing damage up to 8 times when there are five or more \
enemies. For each enemy defeated, she gains an extra Spear of Radiance. The number of Spears can increase to up to 12 in total. \
When hit by the spear, enemies receive a debuff amplifying the Earth-type damage received. \
While Golden Cheese Cookie is using her skill, she harnesses her Light of Abundance and hurls the Spear of the Absolute to \
the enemy Cookie with the highest ATK. The Spear of Absolute removes the target's buffs, deals DMG, Explosion DMG, \
and additional DMG based on the current number of Spears of Radiance to all enemies in range. \
Once per battle, if Golden Cheese Cookie is about to be defeated, she encloses herself in a Sarcophagus \
for a certain period of time. While enclosed in her Sarcophagus, she casts a Shield around herself. This Shield \
takes the DMG dealt to nearby allies covered by it and provides Knockback Immunity. \
When using her skill, Golden Cheese Cookie is not affected by ATK Speed changes and is \
protected from the Glitch: Data Corruption effect by her Light of Abundance.",
            "Ranged",
            "Middle",
            "Ancient")

c23_21 =  Cookie(
            "Burnt Cheese",
            "Summons giant boulders from beneath the earth, dealing DMG to nearby enemies and granting Earth-type CRIT DMG buff for all allies. \
Afterwards, the boulders explode, dealing DMG and Stunning enemies. Burnt Cheese Cookie grants the Protector of the Golden City and \
the Curse Protection buffs to himself and the ally Cookie with the highest ATK, absorbing part of the damage they take with DMG Focus \
and making them Immune to Debuffs. Burnt Cheese Cookie and Golden Cheese Cookie's DMG Resist increases when entering a battle together. \
If Golden Cheese Cookie becomes enclosed in her Sarcophagus or enters the Immortal's Return state during battle, Burnt Cheese Cookie's ATK \
and ATK SPD will temporarily increase, and his Cooldown will reset. The Protector of the Golden City and Curse Protection buffs will be \
applied to Golden Cheese Cookie enclosed in her Sarcophagus or Immortal's Return state first. While using his skill, Burnt Cheese Cookie \
will briefly become resistant to interrupting effects.",
            "Charged",
            "Front",
            "Epic")

c23_22 =  Cookie(
            "Fettuccine",
            "Fettuccine Cookie taunts enemies and smacks them down with her giant fettuccine arms, dealing DMG, making the enemies prone \
to Earth-type DMG and reducing their ATK. Next, she restores her HP and gains a Fettuccine Wraps buff. This slightly confused \
Cookie's Unstable Aura reduces enemies' ATK within its range and restores the team's HP after a given number of enemies within \
said range are defeated. The more Fettuccine Cookie's Max HP is reduced, the more her DMG Resist increases. Once per battle, after \
being defeated, Fettuccine Cookie becomes Immortal and decreases enemies' ATK SPD with her Unstable Aura at the expense of her own ATK \
SPD for the duration of her Immortal state. While Fettuccine Cookie is using her skill, she will become resistant to interrupting effects.",
            "Defense",
            "Front",
            "Epic")

c23_23 = Cookie(
            "Mozzarella",
            "Mozzarella Cookie rings her bell to apply buffs to allies and summon her Mozzarella Bird. The bird deals damage to enemies and flies \
off to create a Mozzarella Puddle. Enemies fallen in the puddle will have their movement speed and attack speed reduced.",
            "Magic",
            "Middle",
            "Epic")

c23_24 = Cookie(
            "Olive",
            "Olive Cookie runs off as though she's forgotten her exploration equipment, then returns chased by a cauldron of bats. \
She trips, and the bats fly over her to attack enemies in front of Olive Cookie. \
The bats differ in types depending on their color, they apply debuffs, and Stun enemies with a certain chance.",
            "Support",
            "Rear",
            "Epic")

c23_25 = Cookie(
            "Icicle Yeti",
            "Icicle Yeti Cookie buffs the allies and periodically restores their HP. They will assume the yeti form, \
jump towards the nearest enemy, and create a Shield of Ice to protect them. The Shield of Ice will absorb a portion of \
all incoming direct non-periodic damage and make the team resistant to Freezing. Then, Icicle Yeti Cookie will return to \
their position and deal a portion of the damage received in the yeti form with an icicle attack.",
            "Healing",
            "Front",
            "Special")

c23_26 = Cookie(
            "Creme Brulee",
            "Creme Brulee Cookie's passionate, captivating performance deals Light-type damage to enemies and enhances his \
regular attacks with the Accelerando buff. Creme Brulee Cookie's regular attacks target the enemy with the highest ATK \
and, when enhanced, apply the Mysterious Melody buff to nearby Cookies. The pianist will also create Crème Brûlée Pieces \
depending on the number of Accelerando stacks. Crème Brûlée Pieces will deal damage to enemies in the order of highest ATK, \
deal additional damage to targets vulnerable to elemental damage, and partially ignore enemies' DMG Resist at maximum Accelerando \
stacks. Creme Brulee Cookie will lose x2 Accelerando stacks if the skill effect ends with the maximum number of stacks. \
While Creme Brulee Cookie is using his skill, he will briefly become resistant to interrupting effects.",
            "Ranged",
            "Rear",
            "Epic")

c23_27 = Cookie(
            "Linzer",
            "Linzer Cookie gains Deduction stacks instead of regular attacks. Upon using her skill, she increases the CRIT of \
her allies and applies the Suspect debuff to the enemy with the highest ATK, dealing damage to the target and area \
damage to the enemies nearby. The Suspect debuff is enhanced with Deduction stacks, and when using the skill with \
the maximum number of stacks, the debuff will decrease the target's DEF and apply a CRIT DMG buff for allies. \
The renowned writer's impeccable deduction allows the Suspect debuff to be applied even to targets with debuff immunity. \
While Linzer Cookie is using her skill, she will briefly become resistant to interrupting effects.",
            "Support",
            "Rear",
            "Epic")

