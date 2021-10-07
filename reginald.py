from Player import fiend
from Player import tiefling
from Player import criminal
from Player import PlayerCharacter
from Player import warlock
from StatBlock import AbilityScores
from StatBlock import Attack

reginald = PlayerCharacter("Reginald Cornflake", warlock, fiend, criminal, 
                           "Dan", tiefling, "Chaotic Good", 6500, 
                           AbilityScores(8, 16, 14, 11, 10, 20), 39, 
                           ["I don't pay attention to the risks in a situation. Never tel me the odds.", 
                            "I have a 'tell' that reveals when I'm lying."], "Charity. I steal from the wealthy so that I can help people in need. (Good)", 
                            "My ill-gotten gains got to support my family.", 
                            "I turn tail and run when things look bad.", 
                            14, "4'2\"", "85 lb.", "Yellow", "Red", "Purple", gold=15, 
                            equipment=["leather armour", "dagger", "dagger", 
                            "crossbow, light", "crystal", "book", "ink (1 ounce bottle)",
                            "ink pen", "parchment (one sheet)", "backpack", "clothes, common", 
                            "crowbar", "little bag of sand", "small knife"])

reginald.remove_proficiency("one type of gaming set", "tool")
reginald.add_proficiency("playing card set", "tool")
reginald.add_proficiency("Arcana", "skill")
reginald.add_proficiency("Investigation", "skill")
reginald.set_invocations(["agonising blast", "one with shadows", "repelling blast"])
reginald.set_pact("Pact of the Tome")
reginald.add_spells("booming blade, eldritch blast, prestidigitation, spare the dying, thaumaturgy, thunderclap, vicious mockery", "cantrip", "leelled")
reginald.add_spells("command, counterspell, hellish rebuke, misty step, vampiric touch", kind="levelled")
reginald.equip_armour("leather armour", 14)
eldritch_blast_attack = Attack("Eldritch Blast", "Ranged Spell Attack", reginald.spell_attack, "range 120 ft.", "one target", "1d10", int(reginald.abilities.charisma_mod +2), "force")
reginald.actions_list += [eldritch_blast_attack]