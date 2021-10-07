
from Player.character_traits import Background
from Player.character_traits import CharacterFeature

from Data import charlatan_schemes

acolyte = Background("Acolyte", "Insight, Religion", None, "Two of your choice", 
                     "A holy symbol (a gift to you when you entered the priesthood), a prayer book or prayer wheel, 5 sticks of incense, vestments, a set of common clothes, and a belt pouch containing 15 gp", 
                     [CharacterFeature("Shield of the Faithful", "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle.\nYou might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple.")])

charlatan = Background("Charlatan", "Deception, Sleight of Hand", "Disguise kit, Forgery kit", None,
                       "A set of fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke), and a belt pouch containing 15 gp", 
                       [CharacterFeature("False Identity", "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy."), 
                       CharacterFeature(
                           "Favourite Schemes", f"Every charlatan has an angle he or she uses in preference to other schemes. Choose a favorite scam or roll on the table below.\n{charlatan_schemes}")])

criminal = Background("Criminal", "Deception, Stealth", "One type of gaming set, thieves' tools", None, 
                     "A crowbar, a set of dark common clothes including a hood, and a belt pouch containing 15 gp", 
                     [CharacterFeature("Criminal Contact", "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you.")])

noble = Background("Noble", "History, Persuasion", "one type of gaming set", 
                   "one of your choice", 
                   "A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp", 
                   [CharacterFeature("Position of Privilege", "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to.")])
