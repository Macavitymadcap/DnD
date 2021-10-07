from DiceBox import d4
from DiceBox import d6
from DiceBox import d8
from DiceBox import d10
from DiceBox import d12
from DiceBox import d100
from DiceBox import roll
from DiceBox import roll_advantage
from DiceBox import roll_array
from DiceBox import roll_crit
from DiceBox import roll_disadvantage
from DiceBox import roll_string
from DMTools import Combatant
from DMTools import Encounter
from DMTools import copy_monster
from DMTools import set_combatant
from StatBlock import ettercap
from StatBlock import ghast
from StatBlock import giant_spider
from StatBlock import giant_wolf_spider
from StatBlock import krell_grohlg
from StatBlock import maw_demon
from StatBlock import phase_spider
from StatBlock import swarm_of_insects
from Spellbook import barkskin
from Spellbook import druidcraft
from Spellbook import entangle
from Spellbook import flaming_sphere
from Spellbook import longstrider
from Spellbook import produce_flame
from Spellbook import shillelagh
from Spellbook import speak_with_animals
from Spellbook import thunderwave


#2. Altar of Lolth

ettercap0 = copy_monster(ettercap)
etter_1 = set_combatant(ettercap0, "etter_1")
giant_spider0 = copy_monster(giant_spider)
spi_1 = set_combatant(giant_spider0, "spi 1")
swarm_of_insects0 = copy_monster(swarm_of_insects)
swar_1 = set_combatant(swarm_of_insects0, "swar_1")
swarm_of_insects1 = copy_monster(swarm_of_insects)
swar_2 = set_combatant(swarm_of_insects1, "swar_2")
swarm_of_insects2 = copy_monster(swarm_of_insects)
swar_3 = set_combatant(swarm_of_insects2, "swar_3")
swarm_of_insects3 = copy_monster(swarm_of_insects)
swar_4 = set_combatant(swarm_of_insects3, "swar_4")

altar = Encounter([etter_1, spi_1, swar_1, swar_2, swar_3, swar_4])

#3. Navigator's Room

ettercap1 = copy_monster(ettercap)
etter_2 = set_combatant(ettercap1, "etter_2")
giant_spider1 = copy_monster(giant_spider)
spi_2 = set_combatant(giant_spider0, "spi_2")
swarm_of_insects4 = copy_monster(swarm_of_insects)
swar_5 = set_combatant(swarm_of_insects4, "swar_5")
swarm_of_insects5 = copy_monster(swarm_of_insects)
swar_6 = set_combatant(swarm_of_insects5, "swar_6")
swarm_of_insects6 = copy_monster(swarm_of_insects)
swar_7 = set_combatant(swarm_of_insects6, "swar_7")
swarm_of_insects7 = copy_monster(swarm_of_insects)
swar_8 = set_combatant(swarm_of_insects7, "swar_8")

navroom = Encounter([etter_2, spi_2])

#5. Spider Nest

ettercap2 = copy_monster(ettercap)
etter_3 = set_combatant(ettercap2, "etter_3")
giant_wolf_spider0 = copy_monster(giant_wolf_spider)
wolf_1 = set_combatant(giant_wolf_spider0, "wolf_1")
giant_wolf_spider1 = copy_monster(giant_wolf_spider)
wolf_2 = set_combatant(giant_spider1, "wolf_2")
swarm_of_insects8 = copy_monster(swarm_of_insects)
swar_9 = set_combatant(swarm_of_insects8, "swar_9")
swarm_of_insects9 = copy_monster(swarm_of_insects)
swar_10 = set_combatant(swarm_of_insects9, "swar_10")
swarm_of_insects10 = copy_monster(swarm_of_insects)
swar_11 = set_combatant(swarm_of_insects10, "swar_11")
swarm_of_insects11 = copy_monster(swarm_of_insects)
swar_12 = set_combatant(swarm_of_insects11, "swar_12")
swarm_of_insects12 = copy_monster(swarm_of_insects)
swar_13 = set_combatant(swarm_of_insects12, "swar_13")
swarm_of_insects13 = copy_monster(swarm_of_insects)
swar_14 = set_combatant(swarm_of_insects13, "swar_14")

nest = Encounter([etter_3, wolf_1, wolf_2])

#6. Food Storage

maw_demon0 = copy_monster(maw_demon)
maw_1 = set_combatant(maw_demon0, "maw_1")
maw_demon1 = copy_monster(maw_demon)
maw_2 = set_combatant(maw_demon1, "maw_2")
maw_demon2 = copy_monster(maw_demon)
maw_3 = set_combatant(maw_demon0, "maw_3")
maw_demon3 = copy_monster(maw_demon)
maw_4 = set_combatant(maw_demon3, "maw_4")

food = Encounter([maw_1, maw_2, maw_3, maw_4])

#10. Unholy Shrine

giant_spider2 = copy_monster(giant_spider)
spi_3 = set_combatant(giant_spider2, "spi_3")
giant_spider3 = copy_monster(giant_spider)
spi_4 = set_combatant(giant_spider3, "spi_4")
phase_spider0 = copy_monster(phase_spider)
roil = set_combatant(phase_spider0, "roil")
krell_grohlg0 = copy_monster(krell_grohlg)
krell = set_combatant(krell_grohlg0, "krell")

shrine = Encounter([spi_3, spi_4, roil, krell])

#12. Cargo Hold

ghast0 = copy_monster(ghast)
ghast_1 = set_combatant(ghast0, "ghast_1")
ghast1 = copy_monster(ghast)
ghast_2 = set_combatant(ghast1, "ghast_2")
ghast2 = copy_monster(ghast)
ghast_3 = set_combatant(ghast2, "ghast_3")
ghast3 = copy_monster(ghast)
ghast_4 = set_combatant(ghast3, "ghast_4")

cargo = Encounter([ghast_1, ghast_2, ghast_3, ghast_4])

#Death of the Emperor
