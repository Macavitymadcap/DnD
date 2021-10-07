"""A package of Monster class instances, and monster_set which contains them 
all for quick access and reference"""

from StatBlock.actions_traits import AbilityCheck
from StatBlock.actions_traits import AbilityScores
from StatBlock.actions_traits import Action
from StatBlock.actions_traits import Attack
from StatBlock.actions_traits import InnateSpellcasting
from StatBlock.actions_traits import LegendaryActions
from StatBlock.actions_traits import PactMagic
from StatBlock.actions_traits import SaveAction
from StatBlock.actions_traits import Spellcasting
from StatBlock.actions_traits import Trait
from StatBlock.monster import Monster

#SRD Monsters
aboleth = Monster("Aboleth", "large", "aberration", "lawful evil", 17, 
                  "natural armour", 135, "18d10 + 36", 
                  "10 ft., swim 40 ft.", 
                  AbilityScores(21, 9, 15, 18, 15, 18), 
                  "darkvision 120 ft., passive Perception 20", 
                  "Deep speech, telepathy 120 ft.", "10", 
                  [AbilityCheck("Con", "+6"), AbilityCheck("Int", "+8"), 
                   AbilityCheck("Wis", "+6")], 
                  [AbilityCheck("History", "+12"), 
                   AbilityCheck("Perception", "+10")], 
                  special_traits=[
                      Trait("Amphibious", "The aboleth can breathe air and water."), 
                      Trait("Mucous Cloud", "While underwater, the aboleth is surrounded by transformative mucous. A creature that touches the aboleth or that hits it with a melee attack while within 5 feet of it must make a DC 14 Constitution saving throw. On a failure, the creature is diseased for 1d4 hours. The diseased creature can breathe only underwater."), 
                      Trait("Probing Telepathy", "If a creature communicates telepathically with the aboleth, the aboleth learns the creature’s greatest desires if the aboleth can see the creature.")], 
                  actions=[
                      Action("Multiattack", description="The aboleth makes three tentacle attacks."), 
                      Attack("Tentacle", "Melee Weapon Attack", 9, "reach 10 ft.", "one target", "2d6", 5, "bludgeoning", text="If the target is a creature, it must succeed on a DC 14 Constitution saving throw or become diseased. The disease has no effect for 1 minute and can be removed by any magic that cures disease. After 1 minute, the diseased creature’s skin becomes translucent and slimy, the creature can’t regain hit points unless it is underwater, and the disease can be removed only by heal or another disease-curing spell of 6th level or higher. When the creature is outside a body of water, it takes 6 (1d12) acid damage every 10 minutes unless moisture is applied to the skin before 10 minutes have passed."), 
                      Attack("Tail", "Melee Weapon Attack", 9, "reach 10 ft.", "one target", "3d6", 5, "bludgeoning"), 
                      Action("Enslave", "3/Day", "The aboleth targets one creature it can see within 30 feet of it. The target must succeed on a DC 14 Wisdom saving throw or be magically charmed by the aboleth until the aboleth dies or until it is on a different plane of existence from the target. The charmed target is under the aboleth’s control and can’t take reactions, and the aboleth and the target can communicate telepathically with each other over any distance.\nWhenever the charmed target takes damage, the target can repeat the saving throw. On a success, the effect ends. No more than once every 24 hours, the target can also repeat the saving throw when it is at least 1 mile away from the aboleth.")], 
                  legendary_actions=LegendaryActions("aboleth", [
                      Action("Detect", description="The aboleth makes a Wisdom (Perception) check."), Action("Tail Swipe", description="The aboleth makes one tail attack."), Action("Psychic Drain", "Costs 2 Actions", "One creature charmed by the aboleth takes 10 (3d6) psychic damage, and the aboleth regains hit points equal to the damage the creature takes.")]))

ettercap = Monster("Ettercap", "medium", "monstrosity", "neutral evil", 13, 
                   "natural armour", 44, "8d8 + 8", "30 ft., climb 30 ft.", 
                   AbilityScores(14, 15, 13, 7, 12, 8),
                   "darkvision 60 ft., passive Perception 13", None, "2", None,
                   [AbilityCheck("Perception", "+3"), AbilityCheck("Stealth", "+4"),
                    AbilityCheck("Survival", "+3")], None, None, None, None,
                   [Trait("Spider Climb", "The ettercap can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."),
                    Trait("Web Sense", "While in contact with a web, the ettercap knows the exact location of any other creature in contact with the same web."),
                    Trait("Web Walker", "The ettercap ignores movement restrictions caused by webbing.")],
                   [Action("Multiattack", description="The ettercap makes two attacks: one with its bite and one with its claws."),
                    Attack("Bite", "Melee Weapon Attack", 5, "reach 5 ft.", "one creature", "1d8", 2, "piercing", "1d8", None, "poison","The target must succeed on a DC 11 Constitution saving throw or be poisoned for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."),
                    Attack("Claws", "Melee Weapon Attack", 4, "reach 5 ft.",
                           "one target", "2d4", 2, "slashing"),
                    Attack("Web (Recharge 5-6)", "Ranged Weapon Attack", 4, "range 30/60 ft.", "one Large or smaller creature",
                           text="The creature is restrained by webbing. As an action, the restrained creature can make a DC 11 Strength check, escaping from the webbing on a success. The effect ends if the webbing is destroyed. The webbing has AC 10, 5 hit points, is vulnerable to fire damage and immune to bludgeoning, poison and psychic damage."),
                    Attack("Variant: Web Garrotte", "Melee Weapon Attack", 4, "reach 5 ft.", "one Medium or Small creature against which the ettercap has advantage on the attack roll", "1d4", 2, "bludgeoning", text=", and the target is grappled (escape DC 12). Until this grapple ends, the target can't breathe, and the ettercap has advantage on attack rolls against it.")])

ghast = Monster("Ghast", "medium", "undead", "chaotic evil", 
                13, None, 36, "3d8", "30 ft.", 
                AbilityScores(16, 17, 10, 11, 10, 8), 
                "darkvision 60 ft., passive Perception 10", 
                "Common", "2", 
                damage_resistances="necrotic", 
                damage_immunities="poison", 
                condition_immunities=" charmed, exhaustion, poisoned", 
                special_traits=[Trait("Stench", "Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creature is immune to the ghast's Stench for 24 hours."), 
                                Trait(
                                    "Turn Defence", "The ghast and any ghouls within 30 feet of it have advantage on saving throws against effects that turn undead.")], 
                actions=[Attack("Bite", "Melee Weapon Attack", 3, "reach 5 ft.", "one creature", "2d8", 3, "piercing"), 
                        Attack(
                            "Claws", "Melee Weapon Attack", 5, "reach 5 ft.", "one target", "2d6", 3, "slashing", 
                            text=" If the target is a creature other than an undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.")])

giant_spider = Monster("Giant Spider", "large", "beast", "unaligned", 14, "natural Armour",
                       26, "4d10+4", "30 ft., climb 30 ft.",
                       AbilityScores(14, 16, 12, 2, 11, 4),
                       "blindsight 10 ft., darkvision 60 ft., passive Perception 10",
                       "-", "1",
                       special_traits=[Trait("Spider Climb", "The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."),
                                       Trait(
                                           "Web Sense", "While in contact with a web, the spider knows the exact location of any other creature in contact with the same web."),
                                       Trait("Web Walker", "The spider ignores movement restrictions caused by webbing.")],
                       actions=[Attack("Bite", "Melee Weapon Attack", 5, "reach 5 ft.", "one creature", "1d8", 3, "piercing", "2d8", None, "poison", text=", and the target must make a DC 11 Constitution saving throw, taking poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."),
                                Attack("Web (Recharge 5-6)", "Ranged Weapon Attack", 5, "Range 30/60 ft.", "one creature", text="The target is restrained by webbing. As an action, the restrained target can make a DC 12 Strength check, bursting the webbing on a success. The webbing can also be attacked and destroyed (AC 10; hp 5; vulnerability to fire damage; immunity to bludgeoning, poison, and psychic damage).")])

giant_wolf_spider = Monster("Giant Wolf Spider", "medium", "beast", "unaligned",
                            13, None, 11, "2d8+2", "40 ft., climb 40 ft.",
                            AbilityScores(12, 16, 13, 3, 12, 4),
                            "blindsight 10 ft., darkvision 60 ft., passive Perception 13", "-", "1/4",
                            skills=[AbilityCheck("Perception", "+3"),
                                    AbilityCheck(
                                        "Stealth", "+7")],
                            special_traits=[Trait("Spider Climb", "The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."),
                                            Trait(
                                "Web Sense", "While in contact with a web, the spider knows the exact location of any other creature in contact with the same web."),
                                Trait("Web Walker", "The spider ignores movement restrictions caused by webbing.")],
                            actions=[Attack("Bite", "Melee Weapon Attack", 3, "reach 5ft.", "one creature", "1d6", 1, "piercing", "2d6", None, "poison", ", and the target must make a DC 11 Constitution saving throw, taking poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.")])

maw_demon = Monster("Maw Demon", "medium", "fiend", "chaotic evil",
                    13, "natural armour", 33, "6d8+6", "30 ft.",
                    AbilityScores(14, 8, 13, 5, 8, 5),
                    "darkvision 60 ft., passive Perception 9",
                    "understands Abyssal but can't speak", "1",
                    damage_resistances="cold, fire, lightning",
                    damage_immunities="poison",
                    condition_immunities="charmed, frightened, poisoned",
                    special_traits=[Trait(
                        "Rampage", "When it reduces a creature to 0 hit points with a melee attack on its turn, the maw demon can take a bonus action to move up to half its speed and make a bite attack.")],
                    actions=[Attack("Bite", "Melee Weapon Attack", 4, "reach 5 ft.", "one target", "2d8", 2, "piercing")])

phase_spider = Monster("Phase Spider", "large", "monstrosity", "unaligned",
                       13, "natural armour", 32, "5d10+5", "30 ft, climb 30 ft.",
                       AbilityScores(15, 15, 12, 6, 10, 6),
                       "darkvision 60 ft., passive Perception 10", "-", "3",
                       skills=[AbilityCheck("Stealth", "+6")],
                       special_traits=[Trait("Ethereal Jaunt", "As a bonus action, the spider can magically shift from the Material Plane to the Ethereal Plane, or vice versa."),
                                       Trait(
                           "Spider Climb", "The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."),
                           Trait("Web Walker", "The spider ignores movement restrictions caused by webbing.")],
                       actions=[Attack("Bite", "Melee Weapon Attack", 4, "reach 5ft.", "one creature", "1d10", 2, "piercing", "4d8", None, "poison", ", and the target must make a DC 11 Constitution saving throw, taking poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.")])

orc = Monster("Orc", "medium", "humanoid (orc)", "chaotic evil", 13, "hide armour",
              15, "2d8+6", "30 ft.", 
              AbilityScores(16,12, 16, 7, 11, 10), 
              "darkvision 60 ft., passive Perception 10",
              "Common, Orc", "1/2", None, [
                  AbilityCheck("Intimidation", "+2")],
              None, None, None, None,
              [Trait("Agressive", "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.")],
              [Attack("Greataxe", "Melee Weapon Attack", 5, "reach 5 ft.", "one target", "1d12", 3, "slashing"),
               Attack("Javelin", "Melee or Ranged Weapon Attack", 5, "reach 5 ft. or range 30/120 ft.", "one target", "1d6", 3, "piercing")])

smoke_mephit = Monster("Smoke Mephit", "medium", "elemental", "neutral evil",
                       12, None, 22, "5d6+5", "30 ft., fly 30 ft.",
                       AbilityScores(6, 14, 12, 10, 10, 11),
                       "darkvision 60 ft., passive Perception 12",
                       "Auran, Ignan", "1/4", None,
                       [AbilityCheck("Perception", "+2"),
                        AbilityCheck("Stealth", "+4")],
                       None, None, "fire, poison", "poisoned",
                       [Trait("Death Burst", "When the mephit dies, it leaves behind a cloud of smoke that fills a 5-foot-radius sphere centered on its space. The sphere is heavily obscured. Wind disperses the cloud, which otherwise lasts for 1 minute."),
                        Trait("Innate Spellcasting (1/Day)", "The mephit can innately cast dancing lights, requiring no material components. Its innate spellcasting ability is Charisma.")],
                       [Attack("Claws", "Melee Weapon Attack", 5, "reach 5 ft.", "one creature", "1d4", 2, "slashing"),
                        Action("Cinder Breath", "Recharge 6", "The mephit exhales a 15-foot cone of smoldering ash. Each creature in that area must succeed on a DC 10 Dexterity saving throw or be blinded until the end of the mephit's next turn.")])

steam_mephit = Monster("Steam Mephit", "medium", "elemental", "neutral evil",
                       10, None, 21, "6d6", "30 ft., fly 30 ft.",
                       AbilityScores(5, 11, 10, 10, 10, 12),
                       "darkvision 60 ft., passive Perception 10",
                       "Aquan, Ignan", "1/4", None, None, None, None,
                       "fire, poison", "poisoned",
                       [Trait("Death Burst", "When the mephit dies, it explodes in a cloud of steam. Each creature within 5 feet of the mephit must succeed on a DC 10 Dexterity saving throw or take 4 (1d8) fire damage."),
                        Trait("Innate Spellcasting (1/Day)", "The mephit can innately cast blur, requiring no material components. Its innate spellcasting ability is Charisma.")],
                       [Attack("Claws", "Melee Weapon Attack", 2, "reach 5 ft.", "one creature", "1d4", None, "slashing"),
                        Action("Steam Breath", "Recharge 6", "The mephit exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one.")])

swarm_of_insects = Monster("Swarm of Insects", "medium", "swarm of tiny beasts", "unaligned",
                           12, "natural armour", 22, "5d8", "20 ft., climb 20 ft.",
                           AbilityScores(3, 13, 10, 1, 7, 1),
                           "blindsight 10 ft., passive Perception 8", "-", "1/2",
                           damage_resistances="bludgeoning, piercing, slashing",
                           condition_immunities="charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
                           special_traits=[Trait(
                               "Swarm", "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points.")],
                           actions=[Attack("Bites", "Melee Weapon Attack", 3, "reach 0 ft.", "one target in the swarm's space.", "4d4", None, "piercing", "2d4", None, "piercing", "4d4 piercing damage, 2d4 piercing damage if the swarm has half of its hit points or fewer.")])

monster_set = set([aboleth, ettercap, ghast, giant_spider, giant_wolf_spider, maw_demon, 
                  phase_spider, orc, smoke_mephit, steam_mephit, 
                  swarm_of_insects])

#Non-SRD MOnsters & NPCs
krell_grohlg = Monster("Krell Grohlg", "medium", "humanoid (half-orc)", "chaotic evil", 
                       11, "16 with barkskin", 27, "5d8+5", "30 ft.", 
                       AbilityScores(18, 12, 13, 12, 15, 11), 
                       "darkvision 60 ft., passive Perception 14", "Common, Druidic, Orc", "2", 
                       skills=[Trait("Medicine", "+4"), Trait("Nature", "+3"), 
                               Trait("Perception", "+4")], 
                       special_traits=[Action("Relentless Endurance", "1/day", "When the half-orc is reduced to 0 hit points but not killed outright, the half-orc can drop to 1 hit point instead."), 
                                       Spellcasting("half-orc", "4th", "Wisdom", 12, 4, "Druid", "druidcraft, produce flame, shillelagh", "entangle, longstrider, speak with animals, thunderwave", "flaming sphere, barkskin", spell_slots=[4, 3])], 
                       actions=[Attack("Quarterstaff", "Melee Weapon Attack", 6, "reach 5 ft.", "one target", "1d6", 4, "bludgeoning", "1d8", 4, "bludgeoning", " if wielded with two hands.")])

skeletal_alchemist = Monster("Skeletal Alchemist", "medium", "undead", "lawful evil", 11,
                             None, 32, "5d8+10", "30 ft.",
                             AbilityScores(9, 13, 15, 14, 10, 9),
                             "darkvision 60ft., passive Perception 10",
                             "understands all languages it knew in life but can't speak",
                             "1/2", None, [AbilityCheck("Arcana", "+4")],
                             "bludgeoning", None, "poison", "exhastion, poisoned",
                             [Trait(
                                 "Magic Resistance", "The skeletal alchemist has advantage on saving throws against spells and other magical effects.")],
                             [Action("Multiattack", None, "The skeletal alchemist makes two Lob Acid attacks."),
                              Attack("Claws", "Melee Weapon Attack", 3, "reach 5 ft.",
                                     "one target", "1d6", 1, "slashing"),
                              Attack("Lob Acid", "Ranged Weapon Attack", 3, "30/120 ft.", "one target", "1d8", 1, "acid")])

