import re
class Cookie:
  def __init__(self, name, skill, type, position, rarity):
    self.name = name
    self.skill = skill
    self.type = type
    self.position = position
    self.rarity = rarity

#cd = 99

c25_1 = Cookie(
            "Shadow Milk", 
            "Shadow Milk Cookie channels the energy of his other-realm to begin a grand spectacle of Deceit. Inflicts Puppet Show at the enemy with the lowest Max HP \
(targets Cookies first excluding Safeguarded Cookies). The opponent's Shadow Milk Cookie cannot become a target unless no other possible targets are left. \
Puppet Show can also be applied to Cookies who are resistant to interrupting effects. For the duration of Puppet Show, both the target and the \
nearby enemies sustain periodic damage. The effect ends with a Grand Finale. Grand Finale deals damage to all enemies, deals damage proportional \
to Puppet Show's target, and applies Taint on them. If the target is defeated before the end of Puppet Show's duration, a Soul Phantom will appear \
in their place. A portion of the damage sustained by the Soul Phantom until the end of Puppet Show will be inflicted as Grand Finale's extra damage. \
If Shadow Milk Cookie is defeated, he will assume his Shadow Form. He will summon his Puppets to fool the enemies and retreat to the other-realm \
where he will gain Power of Deceit. The Shadow Form effect will last until the Puppets are defeated. At the beginning of the battle, Shadow Milk Cookie \
will summon the Eye of Truth. Depending on the number of debuffs received by the team, including Shadow Milk Cookie himself, \
the Eye of Truth will gain stacks of Truth. More stacks of Truth will be gained whenever Shadow Milk Cookie uses his skill. \
At a certain number of stacks, the Eye of Truth will remove all debuffs from the team and increase the amount of damage dealt by \
Shadow Milk Cookie at the expense of a greater amount of damage received. When Shadow Milk Cookie gains Power of Deceit, the Eye of Truth \
will transform into the Eye of Deceit, periodically gaining new stacks of Truth. At a certain number of stacks, it will emit a Tenet of \
Deceit, dealing damage and resetting the duration of Taint on the target (damage proportional to Max HP is capped at 300000).",
            "Magic",
            "Middle",
            "Beast")

c25_2 = Cookie(
            "Candy Apple", 
            "Candy Apple Cookie slams down a giant lollipop with a heave. Enemies hit will receive the ATK Reduction and DMG Amplification debuffs. \
The lollipop will shatter, granting HP Shields for all allies, and candy fragments will deal DMG to enemies and inflict the DMG Amplification debuff.",
            "Bomber",
            "Middle",
            "Epic")

c25_3 = Cookie(
            "Black Sapphire", 
            "Black Sapphire Gems appear on the battlefield and explode after a certain period of time, inflicting Poison, amplifying debuffs and Poison-type \
damage. Additionally, the gems decrease enemies' DEF depending on the number of Poison-type Cookies on the team, including Black Sapphire Cookie. \
The gems will also heal all Poison-type Cookies and increase their DMG Resist. Black Sapphire Cookie amplifies Poison-type DMG as long as he \
is present on the battlefield. The Deceitful Trio buff will activate partially when entering a battle with Candy Apple Cookie, and the buff \
will activate fully when entering with Shadow Milk Cookie.",
            "Support",
            "Middle",
            "Epic")

c25_4 = Cookie(
            "Pure Vanilla (Compassionate)", 
            "Pure Vanilla Cookie fully heals the team and reduces Injury. He will further heal the team for the amount of HP recovered \
from the reduced Injury. Provides HP Shield for all members of the team. Whenever these HP Shields are dispelled, or the \
target becomes unable to have an HP Shield, periodically heals the team for a certain period of time. Next, he will summon \
Shards of Light that will heal your team and deal damage to enemies, applying the Shards of Light debuff.\
As long as Pure Vanilla Cookie participates in the battle, he will select a Cookie and illuminate them with the Light of \
Truth to restore their HP when it drops below a certain point. Pure Vanilla Cookie will keep restoring their HP periodically \
for some more time. This effect can trigger only once in a certain period of time. As someone who has witnessed both the Truth \
and Deceit, Pure Vanilla Cookie will grant the team immunity from Silence and Cooldown debuffs at the beginning of battle if \
there are no other Healing Cookies in the rear row. Once per battle, when his own HP drops below a certain point, he will restore his HP, \
gain an HP Shield, and dispel all possible debuffs on himself. Additionally, once per battle, Pure Vanilla Cookie will revive one team member, \
himself included. However, this effect will not trigger if the entire team is defeated mid-revival or if the target has already been revived \
The higher Pure Vanilla Cookie's DMG Resist stat, the stronger Cooldown buff he will receive at the beginning of the battle. \
His regular attacks will heal up to 5 targets and increase their Amplify Buffs.",
            "Healing",
            "Rear",
            "Awakened")

c25_5 = Cookie(
            "Wedding Cake", 
            "Turns the battlefield into a luxurious Wedding Aisle. The guests—your team—receive Periodic Healing \
while the enemies sustain Periodic Damage. Summoned Creatures become Stunned. Additionally, Wedding Cake Cookie \
will increase the team's ATK and CRIT DMG. Wedding Fireworks deal Additional DMG to enemies and Stun Summoned Creatures. \
If Black Forest Cookie is on the team, she will gain the Star of the Hour buff.",
            "Magic",
            "Middle",
            "Epic")

c25_6 = Cookie(
            "Black Forest", 
            "Black Forest Cookie uses the power granted by the Witches to Transform. In this form, Black Forest Cookie gains increased ATK SPD \
and DMG Resist, and Immunity. Also, she will deal Area Damage with her Regular Attacks. If the target is a Summoned Creature, \
Black Forest Cookie will deal Additional Damage and Stun them with a certain chance. At the end of her transformation, she will \
summon Thorns to deal wide-range Area Damage and Stun her enemies. If Wedding Cake Cookie is on the team, she will gain the Star of the Hour buff.",
            "Charge",
            "Front",
            "Epic")