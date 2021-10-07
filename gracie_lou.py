from Items import robe_of_the_archmagi
from Items import staff_of_the_magi
from Player import celestial
from Player import half_elf
from Player import noble
from Player import PlayerCharacter
from Player import spell_sniper
from Player import warlock
from Player import war_caster
from StatBlock import AbilityScores
from StatBlock import AbilityCheck
from StatBlock import Action
from StatBlock import Attack
from StatBlock import Monster
from StatBlock import Spellcasting
from StatBlock import Trait

baxter = Monster("Baxter Cunningham", 
                 "medium", 
                 "humanoid (Goliath)", 
                 "Lawful Good", 
                 20, "plate armour, shield", 
                 164, "23d8+66", 
                 "30 ft.", 
                 AbilityScores(18, 10, 17, 10, 20, 12), 
                 "passive Perception 21", 
                 "Common, Giant", 
                 "20", 
                 [AbilityCheck("Wisdom Saving Throw", "+11")], 
                 [AbilityCheck("Athletics", "+10"), 
                  AbilityCheck("Insight", "+11"), 
                  AbilityCheck("Medicine", "+11"), 
                  AbilityCheck("Perception", "+11"), 
                  AbilityCheck("Religion", "+6", )], 
                 special_traits=[Trait("Focused Casting", "Taking damage can't break the sidekick's concentration on a spell."), 
                                 Trait("Powerful Build", "The goliath counts as one size larger when determining its carrying capacity and the weight it can push, drag, or lift."), 
                                 Spellcasting("Sidekick", "20th", "Wisdom", 19, 11, "Cleric", "mending, resistance, spare the dying, toll the dead", "cure wounds, healing word, sanctuary", "aid, lesser restoration, spiritual weapon", "reviviify, spirit guardians", "death ward", "greater restoration, mass cure wounds", spell_slots=[4, 3, 3, 3, 2])], 
                 actions=[Attack("Spear", "Melee Weapon Attack", "+10", "reach 5 ft. or range 20/60 ft.", "one target", "1d6", "+4", "piercing", "1d8", "+4", "piercing", "if used with two hands to make a melee attack")],
                 reactions=[Action("Stone's Endurance", "Recharges after a long or short rest", "The goliath can focus itself to occasionally shrug off injury. When it takes damage, it can use its reaction to roll a d12. Add its Constitution modifier to the number rolled, and reduce the damage by that total.")])

gracie = PlayerCharacter("Gracie-Lou de Beauchamp", warlock, celestial, noble,
                         "Dan", half_elf, "Chaotic Good", 355000,
                         AbilityScores(10, 16, 16, 14, 14, 20), 154,
                         ["Flattery and charm are all the tools one needs to get what one wants.",
                          "If you cross me you will suffer, as will your children, and their children, and so on as long as I am able to inflict suffering."],
                         "Ettiquette. Manners before morals, excepting those who forgo civilty themselves.",
                         "I am forever the willing servant of Snifflebumkiss.",
                         "Despite my breezy southern charms I can be violent like a tornado when provoked.",
                         65, "5'4\"", "159 lb.", "solid white",
                         "pale and glittery", "platinum blonde", 
                         gold = 24, 
                         equipment = ["a backpack", "a book of lore", "a bottle of ink", "an ink pen", "10 sheets of parchment", "a little bag of sand", "a small knife", "a set of fine clothes", "a signet ring", "a scroll of pedigree", "three-dragon ante set", "book of shadows", "staff of the magi", "robe of the archmagi"])

gracie.remove_proficiency("one type of gaming set", "tool")
gracie.add_proficiency("Arcana", "skill")
gracie.add_proficiency("Deception", "skill")
gracie.add_proficiency("Insight", "skill")
gracie.add_proficiency("Medicine", "skill")
gracie.add_proficiency("Celestial", "language")
gracie.add_proficiency("Draconic", "language")
gracie.add_proficiency("Sylvan", "language")
gracie.add_proficiency("three-dragon ante set", "tool")
gracie.add_feature(spell_sniper)
gracie.add_feature(war_caster)
gracie.set_invocations(["agonising blast", "ascendent step", "beast speech", "eldritch spear", "gift of the protectors", "lance of lethargy", "master of myriad forms", "relentless hex"])
gracie.set_pact("Pact of The Tome")
gracie.add_spells("eldritch blast, friends, guidance, light, mage hand, mind sliver, sacred flame, shillelagh, shocking grasp, spare the dying", "cantrip", "levelled")
gracie.add_spells("armour of Agathys, blight, charm monster, charm person, counterspell, cure wounds, far step, flame strike, flaming sphere, hex, hunger of Hadar, suggestion, summon fey, wall of fire", kind="levelled")
gracie.add_spells("alter self, levitate, speak with animals", "at will", "innate")
gracie.add_spells("crown of stars, glibness, psychic scream, true seeing", "one day", "innate")
gracie.add_item(robe_of_the_archmagi)
gracie.equip_armour('robe of the archmagi', 18)
gracie.spell_attack += 2
gracie.spell_save += 2
gracie.add_item(staff_of_the_magi)
gracie.spell_attack += 2
eldritch_blast_attack = Attack("Eldritch Blast", "Ranged Spell Attack", gracie.spell_attack, "range 600 ft.", "one target", "1d10", int(gracie.abilities.charisma_mod +2), "force")
staff_of_the_magi_attack = Attack("Staff of the Magi", "Melee Weapon Attack", int(gracie.abilities.strength_mod + 2 + gracie.proficiency_bonus), None, "one target", "1d6", int(gracie.abilities.strength_mod + 2), "bludgeoning", "1d8", int(gracie.abilities.strength_mod + 2), "bludgeoning")
shillelagh_attack = Attack("Shillelagh", "Melee Spell Attack", int(gracie.spell_attack + 2), None, "one target", "1d6", int(gracie.abilities.charisma_mod + 2), "bludgeoning", "1d8", int(gracie.abilities.charisma_mod + 2), "bludgeoning")
gracie.actions_list += [eldritch_blast_attack, shillelagh_attack, staff_of_the_magi_attack]