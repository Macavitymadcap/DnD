"""A Package containing functions and classes for planning and running a game.

The package is comprised of two modules; EncounterDifficulty and 
InitiativeTracker.The first contains class for calculating encounter 
difficulty. The second contains Classes and functions for running encounters
in a python shell

Classes:
    CRCalculator: A class for calculating encounter difficulty
    Combatant: Return a combatant to be used in an Encounter instance
    Encounter: Return an Encounter instance for tracking combat

Functions
    copy_monster: Return a copy of a Monster instances with rolled max hit points
    set_combatants: Return a Combatant instance from a Monster instance.
"""

from DMTools.EncounterDifficulty import CRCalculator
from DMTools.InitiativeTracker import Combatant, copy_monster
from DMTools.InitiativeTracker import  Encounter
from DMTools.InitiativeTracker import  set_combatant