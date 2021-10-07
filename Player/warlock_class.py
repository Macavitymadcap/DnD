from copy import deepcopy

from Data import warlock_table
from Data import warlock_expanded_spell_list
from Player.character_traits import Archetype
from Player.character_traits import CharacterFeature
from Player.character_traits import CharacterClass

warlock = CharacterClass("Warlock", warlock_table, "d8",
                      "8 + your Constitution modifier",
                      "1d8 (or 5) + your Constitution modifier per Warlock level after 1st",
                      "light armour", "simple weapons", None, "Wisdom, Charisma",
                      "Choose 2 from Arcana, Deception, History, Intimidation, Investigation, Nature, and Religion.",
                      ["(a) a light crossbow and 20 bolts or (b) any simple weapon",
                       "(a) a component pouch or (b) an arcane focus",
                       "(a) a scholar's pack or (b) a dungeoneer's pack"
                                                "Leather armour, any simple weapon, and two daggers"],
                      "4d4 x 10",
                      {"Ability Score Minimum": "Charisma 13",
                       "Armour": "light armour", "weapons": "simple weapons"},
                      [CharacterFeature("Pact Magic", "Your arcane research and the magic bestowed on you by your patron have given you facility with spells.",
                                    [CharacterFeature("Cantrips", "You know two cantrips of your choice from the warlock spell list. You learn additional warlock cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Warlock table."),
                                     CharacterFeature("Spell Slots", "The Warlock table shows how many spell slots you have to cast your warlock spells of 1st through 5th level. The table also shows what the level of those slots is; all of your spell slots are the same level. To cast one of your warlock spells of 1st level or higher, you must expend a spell slot. You regain all expended spell slots when you finish a short or long rest.\nFor example, when you are 5th level, you have two 3rd-level spell slots. To cast the 1st-level spell witch bolt, you must spend one of those slots, and you cast it as a 3rd-level spell."),
                                     CharacterFeature("Spells Known of 1st Level and Higher", "At 1st level, you know two 1st-level spells of your choice from the warlock spell list.\nThe Spells Known column of the Warlock table shows when you learn more warlock spells of your choice of 1st level and higher. A spell you choose must be of a level no higher than what's shown in the table's Slot Level column for your level. When you reach 6th level, for example, you learn a new warlock spell, which can be 1st, 2nd, or 3rd level.\nAdditionally, when you gain a level in this class, you can choose one of the warlock spells you know and replace it with another spell from the warlock spell list, which also must be of a level for which you have spell slots."),
                                     CharacterFeature("Spellcasting Ability", "Charisma is your spellcasting ability for your warlock spells, so you use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a warlock spell you cast and when making an attack roll with one.\nSpell save DC = 8 + your proficiency bonus + your Charisma modifier\nSpell attack modifier = your proficiency bonus + your Charisma modifier"),
                                     CharacterFeature("Arcane Focus", "You can use an arcane focus as a spellcasting focus for your warlock spells.")], 1),
                       CharacterFeature(
                          "Otherworldly Patron", "At 1st level, you have struck a bargain with an otherworldly being chosen from the list of available patrons. Your choice grants you features at 1st level and again at 6th, 10th, and 14th level.", None, 1),
                       CharacterFeature("Eldritch Invocations", "In your study of occult lore, you have unearthed eldritch invocations, fragments of forbidden knowledge that imbue you with an abiding magical ability.\nAt 2nd level, you gain two eldritch invocations of your choice. When you gain certain warlock levels, you gain additional invocations of your choice, as shown in the Invocations Known column of the Warlock table.\nAdditionally, when you gain a level in this class, you can choose one of the invocations you know and replace it with another invocation that you could learn at that level.\nIf an eldritch invocation has prerequisites, you must meet them to learn it. You can learn the invocation at the same time that you meet its prerequisites. A level prerequisite refers to your level in this class.",
                                    [CharacterFeature("Agonising Blast", "When you cast eldritch blast, add your Charisma modifier to the damage it deals on a hit.", None, None, None, "eldrtich blast cantrip"),
                                     CharacterFeature(
                                        "Armour of Shadows", "ou can cast mage armour on yourself at will, without expending a spell slot or material components."),
                                     CharacterFeature(
                                        "Ascendant Step", "You can cast levitate on yourself at will, without expending a spell slot or material components.", None, 9, None, "th level"),
                                     CharacterFeature(
                                        "Aspect of the Moon", "You no longer need to sleep and can't be forced to sleep by any means. To gain the benefits of a long rest, you can spend all 8 hours doing light activity, such as reading your Book of Shadows and keeping watch.", None, None, None, "Pact of the Tome feature"),
                                     CharacterFeature(
                                        "Beast Speech", "You can cast speak with animals at will, without expending a spell slot."),
                                     CharacterFeature(
                                        "Bewitching Whispers", "You can cast compulsion once using a warlock spell slot. You can't do so again until you finish a long rest.", None, 7, None, "th level"),
                                     CharacterFeature("Bond of the Talisman", "While someone else is wearing your talisman, you can use your action to teleport to the unoccupied space closest to them, provided the two of you are on the same plane of existence. The wearer of your talisman can do the same thing, using their action to teleport to you. The teleportation can be used a number of times equal to your proficiency bonus, and all expended uses are restored when you finish a long rest.", None, 12, None, "th level, Pact of the Talisman feature"),
                                     CharacterFeature("Book of Ancient Secrets", "You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the ritual tag from any class's spell list. The spells needn't be from the same spell list. The spells appear in the book and don't count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can't cast the spells except as rituals, unless you've learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the ritual tag.\nOn your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell's level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it.", None, None, None, "Pact of the Tome feature"),
                                     CharacterFeature(
                                        "Chains of Carceri", "You can cast hold monster at will—targeting a celestial, fiend, or elemental—without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again.", None, 15, None, "th level, Pact of the Chain feature"),
                                     CharacterFeature("Cloak of Flies", "As a bonus action, you can surround yourself with a magical aura that looks like buzzing flies. The aura extends 5 feet from you in every direction, but not through total cover. It lasts until you're incapacitated or you dismiss it as a bonus action.\nThe aura grants you advantage on Charisma (Intimidation) checks but disadvantage on all other Charisma checks. Any other creature that starts its turn in the aura takes poison damage equal to your Charisma modifier (minimum of 0 damage).", None, 5, None, "level"),
                                     CharacterFeature(
                                        "Devil's Dight", "You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet."),
                                     CharacterFeature(
                                        "Dreadful Word,", "You can cast confusion once using a warlock spell slot. You can't do so again until you finish a long rest.", None, 1, None, "level"),
                                     CharacterFeature(
                                        "Eldritch Mind", "You have advantage on Constitution saving throws that you make to maintain your concentration on a spell."),
                                     CharacterFeature(
                                        "Eldritch Sight", "You can cast detect magic at will, without expending a spell slot."),
                                     CharacterFeature(
                                        "Eldritch Smite", "Once per turn when you hit a creature with your pact weapon, you can expend a warlock spell slot to deal an extra 1d8 force damage to the target, plus another 1d8 per level of the spell slot, and you can knock the target prone if it is Huge or smaller.", None, 5, None, "th level, Pact of the Blade feature"),
                                     CharacterFeature(
                                        "Eldritch Spear", "When you cast eldritch blast, its range is 300 feet.", None, None, None, "eldritch blast cantrip"),
                                     CharacterFeature(
                                        "Eyes of the Rune Keeper", "You can read all writing."),
                                     CharacterFeature("Far Scribe", "A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your proficiency bonus.\nYou can cast the sending spell, targeting a creature whose name is on the page, without using a spell slot and without using material components. To do so, you must write the message on the page. The target hears the message in their mind, and if the target replies, their message appears on the page, rather than in your mind. The writing disappears after 1 minute.\nAs an action, you can magically erase a name on the page by touching it.", None, 5, None, "th level, Pact of the Tome feature"),
                                     CharacterFeature(
                                        "Fiendish Vigor", "You can cast false life on yourself at will as a 1st-level spell, without expending a spell slot or material components."),
                                     CharacterFeature("Gaze of Two Minds", "You can use your action to touch a willing humanoid and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can use your action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. While perceiving through the other creature's senses, you benefit from any special senses possessed by that creature, and you are blinded and deafened to your own surroundings."),
                                     CharacterFeature(
                                        "Ghostly Gaze", "As an action, you gain the ability to see through solid objects to a range of 30 feet. Within that range, you have darkvision if you don't already have it. This special sight lasts for 1 minute or until your concentration ends (as if you were concentrating on a spell). During that time, you perceive objects as ghostly, transparent images.\nOnce you use this invocation, you can't use it again until you finish a short or long rest.", None, 7, None, "th level"),
                                     CharacterFeature(
                                        "Gift of the Depths", "You can breathe underwater, and you gain a swimming speed equal to your walking speed.\nYou can also cast water breathing once without expending a spell slot. You regain the ability to do so when you finish a long rest.", None, 5, None, "th level"),
                                     CharacterFeature(
                                        "Gift of the Ever-Living Ones", "Whenever you regain hit points while your familiar is within 100 feet of you, treat any dice rolled to determine the hit points you regain as having rolled their maximum value for you.", None, None, None, "Pact of the Chain feature"),
                                     CharacterFeature("Gift of the Protectors", "A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your proficiency bonus.\nWhen any creature whose name is on the page is reduced to 0 hit points but not killed outright, the creature magically drops to 1 hit point instead. Once this magic is triggered, no creature can benefit from it until you finish a long rest.\nAs an action, you can magically erase a name on the page by touching it.", None, 9, None, "th level, Pact of the Tome feature"),
                                     CharacterFeature(
                                        "Grasp of Hadar", "Once on each of your turns when you hit a creature with your eldritch blast, you can move that creature in a straight line 10 feet closer to you.", None, None, None, "eldritch blast cantrip"),
                                     CharacterFeature("Improved Pact Weapon", "You can use any weapon you summon with your Pact of the Blade feature as a spellcasting focus for your warlock spells.\nIn addition, the weapon gains a +1 bonus to its attack and damage rolls, unless it is a magic weapon that already has a bonus to those rolls.\nFinally, the weapon you conjure can be a shortbow, longbow, light crossbow, or heavy crossbow.", None, None, None, "Pact of the Blade feature"),
                                     CharacterFeature("Investment of the Chain", "When you cast find familiar, you infuse the summoned familiar with a measure of your eldritch power, granting the creature the following benefits:\n* The familiar gains either a flying speed or a swimming speed (your choice) of 40 feet.\n* As a bonus action, you can command the familiar to take the Attack action.\n* The familiar's weapon attacks are considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks.\n* If the familiar forces a creature to make a saving throw, it uses your spell save DC.\n* When the familiar takes damage, you can use your reaction to grant it resistance against that damage.", None, None, None, "Pact of the Chain feature"),
                                     CharacterFeature(
                                        "Lance of Lethargy", "Once on each of your turns when you hit a creature with your eldritch blast, you can reduce that creature's speed by 10 feet until the end of your next turn.", None, None, None, "eldritch blast cantrip"),
                                     CharacterFeature(
                                        "Lifedrinker", "When you hit a creature with your pact weapon, the creature takes extra necrotic damage equal to your Charisma modifier (minimum of 1).", None, 12, None, "th level, Pact of the Blade feature"),
                                     CharacterFeature("Maddening Hex", "As a bonus action, you cause a psychic disturbance around the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. When you do so, you deal psychic damage to the cursed target and each creature of your choice that you can see within 5 feet of it. The psychic damage equals your Charisma modifier (minimum of 1 damage). To use this invocation, you must be able to see the cursed target, and it must be within 30 feet of you.", None, 5, None, "th level, hex spell or a warlock feature that curses"),
                                     CharacterFeature(
                                        "Mask of Many Face", "You can cast disguise self at will, without expending a spell slot."),
                                     CharacterFeature(
                                        "Master of Myriad Forms", "You can cast alter self at will, without expending a spell slot.", None, 15, None, "th level"),
                                     CharacterFeature(
                                        "Minions of Chaos", "You can cast conjure elemental once using a warlock spell slot. You can't do so again until you finish a long rest.", None, 9, None, "th level"),
                                     CharacterFeature(
                                        "Mire the Mind", "You can cast slow once using a warlock spell slot. You can't do so again until you finish a long rest.", None, 5, None, "th level"),
                                     CharacterFeature(
                                        "Misty Visions", "You can cast silent image at will, without expending a spell slot or material components."),
                                     CharacterFeature(
                                        "One with Shadows", "When you are in an area of dim light or darkness, you can use your action to become invisible until you move or take an action or a reaction.", None, 5, None, "th level"),
                                     CharacterFeature(
                                        "Otherworldly Leap", "You can cast jump on yourself at will, without expending a spell slot or material components.", None, 9, None, "th level"),
                                     CharacterFeature(
                                        "Protection of the Talisman", "When the wearer of your talisman fails a saving throw, they can add a d4 to the roll, potentially turning the save into a success. This benefit can be used a number of times equal to your proficiency bonus, and all expended uses are restored when you finish a long rest.", None, 7, None, "th level, Pact of the Talisman feature"),
                                     CharacterFeature(
                                        "Rebuke of the Talisman", "When the wearer of your talisman is hit by an attacker you can see within 30 feet of you, you can use your reaction to deal psychic damage to the attacker equal to your proficiency bonus and push it up to 10 feet away from the talisman's wearer.", None, None, None, "Pact of the Talisman feature"),
                                     CharacterFeature("Relentless Hex", "Your curse creates a temporary bond between you and your target. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see within 5 feet of the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. To teleport in this way, you must be able to see the cursed target.", None, 7, None, "th level, hex spell or a warlock feature that curses"),
                                     CharacterFeature(
                                        "Repelling Blast", "When you hit a creature with eldritch blast, you can push the creature up to 10 feet away from you in a straight line.", None, None, None, "eldritch blast cantrip"),
                                     CharacterFeature(
                                        "Sculptor of Flesh", "You can cast polymorph once using a warlock spell slot. You can't do so again until you finish a long rest.", None, 7, None, "th level"),
                                     CharacterFeature(
                                        "Shroud of Shadow", "You can cast invisibility at will, without expending a spell slot.", None, 15, None, "th level"),
                                     CharacterFeature(
                                        "Sign of Ill Omen", "You can cast bestow curse once using a warlock spell slot. You can't do so again until you finish a long rest.", None, 5, None, "th level"),
                                     CharacterFeature(
                                        "Thief of Five Fates", "You can cast bane once using a warlock spell slot. You can't do so again until you finish a long rest."),
                                     CharacterFeature(
                                        "Thirsting Blade", "You can attack with your pact weapon twice, instead of once, whenever you take the Attack action on your turn.", None, 5, None, "th level, Pact of the Blade feature"),
                                     CharacterFeature("Tomb of Levistus", "As a reaction when you take damage, you can entomb yourself in ice, which melts away at the end of your next turn. You gain 10 temporary hit points per warlock level, which take as much of the triggering damage as possible. Immediately after you take the damage, you gain vulnerability to fire damage, your speed is reduced to 0, and you are incapacitated. These effects, including any remaining temporary hit points, all end when the ice melts.\nOnce you use this invocation, you can't use it again until you finish a short or long rest.", None, 5, None, "th level"),
                                     CharacterFeature(
                                        "Trickster's Escape", "You can cast freedom of movement once on yourself without expending a spell slot. You regain the ability to do so when you finish a long rest.", None, 7, None, "th level"),
                                     CharacterFeature(
                                        "Undying Servitude", "You can cast animate dead without using a spell slot. Once you do so, you can't cast it in this way again until you finish a long rest.", None, 5, None, "th level"),
                                     CharacterFeature(
                                        "Visions of Distant Realms", "You can cast arcane eye at will, without expending a spell slot.", None, 15, None, "th level"),
                                     CharacterFeature("Voice of the Chain Master", "You can communicate telepathically with your familiar and perceive through your familiar's senses as long as you are on the same plane of existence. Additionally, while perceiving through your familiar's senses, you can also speak through your familiar in your own voice, even if your familiar is normally incapable of speech.", None, None, None, "Pact of the Chain feature"),
                                     CharacterFeature(
                                        "Whispers of the Grave", "You can cast speak with dead at will, without expending a spell slot.", None, 9, None, "th level"),
                                     CharacterFeature("Witch Sight", "You can see the true form of any shapechanger or creature concealed by illusion or transmutation magic while the creature is within 30 feet of you and within line of sight.", None, 15, None, "th level")], 2),
                       CharacterFeature("Pact Boon", "At 3rd level, your otherworldly patron bestows a gift upon you for your loyal service. You gain one of the following features of your choice.",
                                    [CharacterFeature("Pact of the Blade", "You can use your action to create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it (see chapter 5 for weapon options). You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.\nYour pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die.\nYou can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. You can then dismiss the weapon, shunting it into an extradimensional space, and it appears whenever you create your pact weapon thereafter. You can't affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extradimensional space when the bond breaks."),
                                     CharacterFeature("Pact of the Chain", "You learn the find familiar spell and can cast it as a ritual. The spell doesn't count against your number of spells known.\nWhen you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: imp, pseudodragon, quasit, or sprite.\nAdditionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to use its reaction to make one attack of its own."),
                                     CharacterFeature("Pact of the Talisman", "Your patron gives you an amulet, a talisman that can aid the wearer when the need is great. When the wearer fails an ability check, they can add a d4 to the roll, potentially turning the roll into a success. This benefit can be used a number of times equal to your proficiency bonus, and all expended uses are restored when you finish a long rest.\nIf you lose the talisman, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous amulet. The talisman turns to ash when you die."),
                                     CharacterFeature("Pact of the Tome", "Your patron gives you a grimoire called a Book of Shadows. When you gain this feature, choose three cantrips from any class's spell list. The cantrips do not need to be from the same spell list. While the book is on your person, you can cast those cantrips at will. They don't count against your number of cantrips known. Any cantrip you cast with this feature is considered a warlock cantrip for you. If you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die.")], 3),
                       CharacterFeature("Ability Score Improvement", "When you reach 4th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat.", None, 4),
                       CharacterFeature("Eldritch Versatility", "Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, representing a change of focus in your occult studies:\n* Replace one cantrip you learned from this class's Pact Magic feature with another cantrip from the warlock spell list.\n* Replace the option you chose for the Pact Boon feature with one of that feature's other options.\n* If you're 12th level or higher, replace one spell from your Mystic Arcanum feature with another warlock spell of the same level.\nIf this change makes you ineligible for any of your Eldritch Invocations, you must also replace them now, choosing invocations for which you qualify.", None, 1),
                       CharacterFeature("Ability Score Improvement", "When you reach 8th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat.", None,  8),
                       CharacterFeature("Mystic Arcanum (6th level)", "At 11th level, your patron bestows upon you a magical secret called an arcanum. Choose one 6th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.\nAt higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th-level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest.", None, 11),
                       CharacterFeature("Ability Score Improvement", "When you reach 12th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat.", None, 12),
                       CharacterFeature("Mystic Arcanum (7th level)", "At 13th level, your patron bestows upon you a magical secret called an arcanum. Choose one 7th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.\nAt higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th-level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest.", None, 13),
                       CharacterFeature("Mystic Arcanum (8th level)", "At 15th level, your patron bestows upon you a magical secret called an arcanum. Choose one 8th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.\nAt higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th-level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest.", None, 15),
                       CharacterFeature("Ability Score Improvement", "When you reach 16th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat.", None, 16),
                       CharacterFeature("Mystic Arcanum (9th level)", "At 17th level, your patron bestows upon you a magical secret called an arcanum. Choose one 9th-level spell from the warlock spell list as this arcanum.\nYou can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.\nAt higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th-level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest.", None, 17),
                       CharacterFeature("Ability Score Improvement", "When you reach 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.\nIf your DM allows the use of feats, you may instead take a feat.", None, 19),
                       CharacterFeature("Eldritch Master", "At 20th level, you can draw on your inner reserve of mystical power while entreating your patron to regain expended spell slots. You can spend 1 minute entreating your patron for aid to regain all your expended spell slots from your Pact Magic feature. Once you regain spell slots with this feature, you must finish a long rest before you can do so again.")],
                      ["celestial"], None, None)

celestial = Archetype("Celestial", "Warlock", None, None, None, None,
                      [CharacterFeature("The Celestial", "Your patron is a powerful being of the Upper Planes. You have bound yourself to an ancient empyrean, solar, ki-rin, unicorn, or other entity that resides in the planes of everlasting bliss. Your pact with that being allows you to experience the barest touch of the holy light that illuminates the multiverse.\nBeing connected to such power can cause changes in your behavior and beliefs. You might find yourself driven to annihilate the undead, to defeat fiends, and to protect the innocent. At times, your heart might also be filled with a longing for the celestial realm of your patron, and a desire to wander that paradise for the rest of your days. But you know that your mission is among mortals for now, and that your pact binds you to bring light to the dark places of the world.",
                                    [CharacterFeature("Expanded Spell List", "The Celestial lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.", None, deepcopy(warlock_expanded_spell_list[["Celestial"]])),
                                     CharacterFeature(
                                         "Bonus Cantrips", "At 1st level, you learn the sacred flame and light cantrips. They count as warlock cantrips for you, but they don't count against your number of cantrips known."),
                                     CharacterFeature("Healing Light", "At 1st level, you gain the ability to channel celestial energy to heal wounds. You have a pool of d6s that you spend to fuel this healing. The number of dice in the pool equals 1 + your warlock level.\nAs a bonus action, you can heal one creature you can see within 60 feet of you, spending dice from the pool. The maximum number of dice you can spend at once equals your Charisma modifier (minimum of one die). Roll the dice you spend, add them together, and restore a number of hit points equal to the total.\nYour pool regains all expended dice when you finish a long rest.")], 1),
                       CharacterFeature("Radiant Soul", "Starting at 6th level, your link to the Celestial allows you to serve as a conduit for radiant energy. You have resistance to radiant damage, and when you cast a spell that deals radiant or fire damage, you can add your Charisma modifier to one radiant or fire damage roll of that spell against one of its targets.", None, 6),
                       CharacterFeature("Celestial Radiance", "Starting at 10th level, you gain temporary hit points whenever you finish a short or long rest. These temporary hit points equal your warlock level + your Charisma modifier. Additionally, choose up to five creatures you can see at the end of the rest. Those creatures each gain temporary hit points equal to half your warlock level + your Charisma modifier.", None, 10),
                       CharacterFeature("Searing Vengence", "Starting at 14th level, the radiant energy you channel allows you to resist death. When you have to make a death saving throw at the start of your turn, you can instead spring back to your feet with a burst of radiant energy. You regain hit points equal to half your hit point maximum, and then you stand up if you so choose. Each creature of your choice that is within 30 feet of you takes radiant damage equal to 2d8 + your Charisma modifier, and it is blinded until the end of the current turn.\nOnce you use this feature, you can't use it again until you finish a long rest.", None, 14)])

fiend = Archetype("Fiend", "Warlock", None, None, None, None, 
                  [CharacterFeature("The Fiend", "You have made a pact with a fiend from the lower planes of existence, a being whose aims are evil, even if you strive against those aims. Such beings desire the corruption or destruction of all things, ultimately including you. Fiends powerful enough to forge a pact include demon lords such as Demogorgon, Orcus, Fraz’Urb-luu, and Baphomet; archdevils such as Asmodeus, Dispater, Mephistopheles, and Belial; pit fiends and balors that are especially mighty; and ultroloths and other lords of the yugoloths.",
                                 [CharacterFeature("Expanded Spell List", "The Fiend lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.", None, deepcopy(warlock_expanded_spell_list[["Fiend"]]))], 1), 
                  CharacterFeature("Dark One’s Blessing", "Starting at 1st level, when you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level (minimum of 1).", None, 1), 
                  CharacterFeature("Dark One’s Own Luck", "Starting at 6th level, you can call on your patron to alter fate in your favor. When you make an ability check or a saving throw, you can use this feature to add a d10 to your roll. You can do so after seeing the initial roll but before any of the roll’s effects occur.\nOnce you use this feature, you can’t use it again until you finish a short or long rest.", None, 6), 
                  CharacterFeature("Fiendish Resilience", "Starting at 10th level, you can choose one damage type when you finish a short or long rest. You gain resistance to that damage type until you choose a different one with this feature. Damage from magical weapons or silver weapons ignores this resistance.", None, 10), 
                  CharacterFeature("Hurl Through Hell", "Starting at 14th level, when you hit a creature with an attack, you can use this feature to instantly transport the target through the lower planes. The creature disappears and hurtles through a nightmare landscape.\nAt the end of your next turn, the target returns to the space it previously occupied, or the nearest unoccupied space. If the target is not a fiend, it takes 10d10 psychic damage as it reels from its horrific experience.\nOnce you use this feature, you can’t use it again until you finish a long rest.", None, 14)])
