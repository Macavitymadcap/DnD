"""Classes for the traits of a Monster or PlayerCharacter instance.

The module contains 11 classes. The first of which is Trait, used to represent
a feature or trait and from which all trait classes intended for use in a 
Monster class and/or PlayerCharacter class inherit attributes and methods.

The AbilityCheck class is a trait to represent a check or save against DC using
an ability score. Action is a trait that does not have rolls attached to it but 
is used in combat. Attack is a trait tha can be rolled to hit an armour class
and can deal damage, and SaveAction is a trait against which an oppenent rolls
a saving throw and can deal damage.

The InnateSpellcasting trait represents a creature's innate spellcasting and
allows for rolling to hit based on the creature's spell_attack modifier.
Spellcasting represents a creature's learnt or innate abilty to cast levelled
spells, allowing for rolls to hit based on the creature's spell_attack modifier
and PactMagic does the same, but for warlock spell casters with 1 level of 
spell slot.

AbilityScores is a class that does not inherit from Trait that represent's a 
creature or object's six ability scores and their respective modifers. Spell
is also a class that does not inherit from Trait that represents a spell and 
it's constituents."""

from copy import deepcopy
import json

from DiceBox import roll_advantage
from DiceBox import roll_crit
from DiceBox import roll_disadvantage
from DiceBox import roll_string
from Data import modifiers
from Utilities import format_mod
from Utilities import format_text


class Trait:
    """Class returns on object representing a monster or character trait.

    This is the base class from which all other StatBlock trait classes
    inherit attributes and methods.

    Attributes:
        name (str): String of the trait's name
        description (str): String describing the trait's features
        json (obj): JSON object of the instance"""

    def __init__(self, name=None, description=None):
        """Initialise the Trait class.

        Args:
        name (str): String of the trait's name. Defaults to None
        description (str): String of the trait's features. Defaults to None"""
        if name is None:
            pass

        else:
            self.name = name

        if description is None:
            pass

        else:
            self.description = description
        
        self.json = json.dumps(self.__dict__)

    def __str__(self):
        """Return string of instance 80 characters to a line in a paragraph."""
        return format_text(self.name + ". " + self.description)


class AbilityCheck(Trait):
    """Class returns rolls against a DC with modifier

    Attributes:
        name (str): String of the ability check's name
        modifier (str): String of modifier applied to roll of d20
        roll_to_DC (func): Return int of d20 + modifier
        roll_advantage (func): Return list of 2 d20 + modifier highest first
        roll_disadvantage (func): Return list of 2 d20 + modifier lowest first"""

    def __init__(self, name, modifier):
        """Initialise the AbilityCheck instance.

        Args:
            name (str): String of the ability check's name
            modifier (str): String of modifier applied to roll of d20"""
        self.name = name
        self.modifier = modifier

    def __str__(self):
        """Return string of check with name and modifier."""
        return self.name + " " + self.modifier

    def roll_to_DC(self):
        """Return int of d20 + modifier."""
        return roll_string("1d20" + self.modifier)

    def roll_advantage(self):
        """Return list of 2 d20 + modifier highest first."""
        return roll_advantage("1d20" + self.modifier)

    def roll_disadvantage(self):
        """Return list of 2 d20 + modifier lowest first."""
        return roll_disadvantage("1d20" + self.modifier)


class AbilityScores:
    """Class of ability scores and their modifiers.

    This class does not inherit from trait, but is to be used by the 
    Monster and PlayerCharacter classes to hold the instance's ability 
    scores and modifiers.
    It is also to be used by subsequent traits to determine skill checks, 
    ability checks, saving throws and other rolls.

    The AbilityScores instance returns a string tabling the scores and 
    modifiers, used in the print out of a Monster instance's stat block.

    Attributes:
        strength (int): Number representing an object's strength
        dexterity (int): Number representing an object's dexterity
        constitution (int): Number representing an object's constitution
        intelligence (int): Number representing an object's intelligence
        wisdom (int): Number representing an object's wisdom
        charisma (int): Number representing an object's charisma
        strength_mod (int): Number for strength modifier from DataFrame
        dexterity_mod (int): Number for dexterity modifier from DataFrame
        constitution_mod (int): Number for constitution modifier from DataFrame
        intelligence_mod (int): Number for intelligence modifier from DataFrame
        wisdom_mod (int): Number for wisdom modifier from DataFrame
        charisma_mod (int): Number for charisma modifier from DataFrame
        json (obj): JSON object of the instance"""

    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        """Initialise the AbilityScores instance.

        Args:
            strength (int): Number representing an object's strength
            dexterity (int): Number representing an object's dexterity
            constitution (int): Number representing an object's constitution
            intelligence (int): Number representing an object's intelligence
            wisdom (int): Number representing an object's wisdom
            charisma (int): Number representing an object's charisma

        Attributes:
            strength_mod (int): Number for strength modifier from DataFrame
            dexterity_mod (int): Number for dexterity modifier from DataFrame
            constitution_mod (int): Number for constitution modifier from DataFrame
            intelligence_mod (int): Number for intelligence modifier from DataFrame
            wisdom_mod (int): Number for wisdom modifier from DataFrame
            charisma_mod (int): Number for charisma modifier from DataFrame
            json (obj): JSON object of the instance"""
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.strength_mod = modifiers[self.strength]
        self.dexterity_mod = modifiers[self.dexterity]
        self.constitution_mod = modifiers[self.constitution]
        self.intelligence_mod = modifiers[self.intelligence]
        self.wisdom_mod = modifiers[self.wisdom]
        self.charisma_mod = modifiers[self.charisma]
        self.json = json.dumps(self.__dict__)

    def __str__(self):
        """Return string tabling the instance's scores and modifiers."""
        stringa = "STR\tDEX\tCON\tINT\tWIS\tCHA"
        stringb = f"{self.strength} ({format_mod(self.strength_mod)})\t{self.dexterity} ({format_mod(self.dexterity_mod)})\t{self.constitution} ({format_mod(self.constitution_mod)})\t{self.intelligence} ({format_mod(self.intelligence_mod)})\t{self.wisdom} ({format_mod(self.wisdom_mod)})\t{self.charisma} ({format_mod(self.charisma_mod)})"

        return stringa + '\n' + stringb


class Action(Trait):
    """Class returns an action as text with recharge or rest criteria.

    Attributes:
        name (str): String of name of the instance
        cost_recharge (str): String for recharge or rest period of instance
        description (str): String describing the instance's features."""

    def __init__(self, name, cost_recharge=None, description=None):
        """Initialise the Action instance.

        Args:
            name (str): String of name of the instance
            cost_recharge (str): String for recharge or rest period of instance
            description (str): String describing the instance's features"""
        super().__init__(name, description)
        self.cost_recharge = cost_recharge

    def __str__(self):
        """Return string of instance with 80 characters a line per paragraph."""
        if self.cost_recharge == None:
            return format_text(f"{self.name}. {self.description}")

        else:
            return format_text(f"{self.name} ({self.cost_recharge}). {self.description}")


class Attack(Trait):
    """Class returns an action that can be rolled to hit and damage.

    Attributes:
        name (str): String of the attack's name
        attack_type (str): String for what type of attack the instance is
        modifier (str): String of the modifier applied to the to hit rolls
        reach_range (str): String of the reach and or range of the attack
        target (str): String for number of objects or creatures targetted
        damage_die (str): String of dice or die rolled for damage
        damage_mod (str): String of modifier applied to damage
        damage_roll (str): String of damage dice and modifier combined
        damage_type (str): String of the damage's type
        x_damage_die (str): String of extra dice or die rolled for damage
        x_damage_mod (str): String of modifier applied to extra damage
        x_damage_roll (str): String of extra damage dice and modifier combined
        x_damage_type (str): String of the extra damage's type
        text (str): String of additional text for the attack
        roll_to_hit (func) Return int of roll to hit armour class:
        roll_advantage (func): Return list of ints to hit armour class with advantage
        roll_disadvantage (func): Return list of ints to hit armour class with disadvantage
        roll_damage (func): Return int of damage roll for Attack"""

    def __init__(self, name, attack_type, modifier, reach_range, target,
                 damage_die=None, damage_mod=None, damage_type=None,
                 x_damage_die=None, x_damage_mod=None,
                 x_damage_type=None, text=None):
        """Initialise the Attack class instance.

        Args:
            name (str): String of the attack's name
            attack_type (str): String for what type of attack the instance is
            modifier (int): Numberapplied to the to hit rolls
            reach_range (str): String of the reach and or range of the attack
            target (str): String for number of objects or creatures targetted
            damage_die (str): String of dice or die rolled for damage
            damage_mod (int): String of modifier applied to damage
            damage_type (str): String of the damage's type
            x_damage_die (str): String of extra dice or die rolled for damage
            x_damage_mod (int): String of modifier applied to extra damage
            x_damage_type (str): String of the extra damage's type
            text (str): String of additional text for the attack
        
        Attributes:
            damage_roll (str): String of damage dice and modifier combined
            x_damage_roll (str): String of extra damage dice and modifier combined"""
        self.name = name
        self.attack_type = attack_type
        self.modifier = format_mod(modifier)
        self.reach_range = reach_range
        self.target = target
        self.damage_die = damage_die
        if damage_mod is None:
            self.damage_roll = self.damage_die
        
        else:
            self.damage_mod = format_mod(damage_mod)
            self.damage_roll = f"{self.damage_die}{self.damage_mod}"

        self.damage_type = damage_type
        self.x_damage_die = x_damage_die
        self.x_damage_mod = x_damage_mod
        if x_damage_mod is None:
            self.x_damage_roll = self.x_damage_die
        
        else:
            self.x_damage_mod = format_mod(x_damage_mod)
            self.x_damage_roll = f"{self.x_damage_die}{self.x_damage_mod}"

        self.x_damage_type = x_damage_type
        self.text = text

    def __str__(self):
        """Return string of the Attack with 80 characters a line per paragraph."""
        if self.damage_die is None:
            return format_text(f"{self.name} {self.attack_type}: {self.modifier} to hit, {self.reach_range}, {self.target}. Hit: {self.text}")

        stringa = f"{self.name}. {self.attack_type}: {self.modifier} to hit, {self.reach_range}, {self.target}. Hit: ({self.damage_roll}) {self.damage_type} damage"

        if self.x_damage_die is None:
            pass

        else:
            stringa += f", ({self.x_damage_roll}) {self.x_damage_type} damage"

        if self.text is None:
            return format_text(f"{stringa}.")

        else:
            return format_text(f"{stringa}. {self.text}")

    def roll_to_hit(self):
        """Return int of roll to hit armour class."""
        return roll_string("1d20" + self.modifier)

    def roll_advantage(self):
        """Return list of ints to hit armour class with advantage."""
        return roll_advantage("1d20" + self.modifier)

    def roll_disadvantage(self):
        """Return list of ints to hit armour class with disadvantage."""
        return roll_disadvantage("1d20" + self.modifier)

    def roll_damage(self, crit=False):
        """Return int of damage roll for Attack.

        Args:
            crit (bool): Roll critical damage if False, normal damage if True

        Returns:
            int: Total critical damage if crit False, normal damage if True"""
        roll_0 = f"{roll_string(self.damage_roll)} {self.damage_type} damage"
        if self.damage_mod is None:
            roll_0_crit = f"{roll_crit(self.damage_die)} {self.damage_type} damage"
        
        else:
            roll_0_crit = f"{roll_crit(self.damage_die, self.damage_mod)} {self.damage_type} damage"

        if self.x_damage_die is None:

            if crit == False:
                return f"{roll_0}."

            else:
                return f"{roll_0_crit}."

        else:
            roll_x = f"{roll_string(self.x_damage_roll)} {self.x_damage_type} damage"
            if self.x_damage_mod is None:
                roll_x_crit = f"{roll_crit(self.x_damage_die)} {self.x_damage_type} damage"
            
            else:
                roll_x_crit = f"{roll_crit(self.x_damage_die, self.x_damage_mod)} {self.x_damage_type} damage"

            if crit == False:
                return f"{roll_0} and {roll_x}."

            else:
                return f"{roll_0_crit} and {roll_x_crit}."


class SaveAction(Trait):
    """Class returns an action with a DC against which a save is rolled.

    Attributes:
        name (str): String of the attack's name
        save_DC (str): String of the difficulty class of the action
        saving_throw (str): String of the saving throw to roll against the DC
        reach_range (str): String of the reach and or range of the attack
        target (str): String for number of objects or creatures targetted
        damage_die (str): String of dice or die rolled for damage
        damage_mod (str): String of modifier applied to damage
        damage_roll (str): String of damage dice and modifier combined
        damage_type (str): String of the damage's type
        x_damage_die (str): String of extra dice or die rolled for damage
        x_damage_mod (str): String of modifier applied to extra damage
        x_damage_roll (str): String of extra damage dice and modifier combined
        x_damage_type (str): String of the extra damage's type
        text (str): String of additional text for the attack
        roll_damage (func): Return int of damage roll for SaveAction"""

    def __init__(self, name, save_DC, saving_throw, reach_range=None, target=None,
                 damage_die=None, damage_mod=None, damage_type=None, 
                 x_damage_die=None, x_damage_mod=None, x_damage_type=None, text=None):
        """Initialise the SaveActtion instance.

        Args:
            name (str): String of the attack's name
            save_DC (str): String of the difficulty class of the action
            saving_throw (str): String of the saving throw to roll against the DC
            reach_range (str): String of the reach and or range of the attack
            target (str): String for number of objects or creatures targetted
            damage_die (str): String of dice or die rolled for damage
            damage_mod (int): String of modifier applied to damage
            damage_type (str): String of the damage's type
            x_damage_die (str): String of extra dice or die rolled for damage
            x_damage_mod (int): String of modifier applied to extra damage
            x_damage_type (str): String of the extra damage's type
            text (str): String of additional text for the attack
        
        Attributes
            damage_roll (str): String of damage dice and modifier combined
            x_damage_roll (str): String of extra damage dice and modifier combined"""
        self.name = name
        self.save_DC = save_DC
        self.saving_throw = saving_throw
        self.reach_range = reach_range
        self.target = target
        self.damage_die = damage_die
        if self.damage_mod is None:
            self.damage_roll = self.damage_die
        
        else:
            self.damage_mod = format_mod(damage_mod)
            self.damage_roll = f"{self.damage_die}{self.damage_mod}"

        self.damage_type = damage_type
        self.x_damage_die = x_damage_die
        if self.x_damage_mod is None:
            self.x_damage_roll = self.x_damage_die
        
        else:
            self.x_damage_mod = format_mod(x_damage_mod)
            self.x_damage_roll = f"{self.x_damage_die}{self.x_damage_mod}"

        self.x_damage_type = x_damage_type
        self.text = text

    def __str__(self):
        """Return string of the SaveAction 80 characters a line per paragraph."""
        if self.damage_die is None:
            return f"{self.name}: DC {self.save_DC} {self.saving_throw} Saving Throw, {self.reach_range}, {self.target}. Hit: {self.text}"

        stringa = f"{self.name}. DC {self.save_DC} {self.saving_throw} Saving Throw, {self.reach_range}, {self.target}. Hit: ({self.damage_roll}) {self.damage_type} damage"

        if self.x_damage_die is None:
            pass

        else:
            stringa += f", plus ({self.x_damage_roll}) {self.x_damage_type} damage"

        if self.text is None:
            return format_text(f"{stringa}.")

        else:
            return format_text(f"{stringa}{self.text}")


    def roll_damage(self, crit=False):
        """Return int of damage roll for SaveAction.

        Args:
            crit (bool): Roll critical damage if False, normal damage if True

        Returns:
            int: Total critical damage if crit False, normal damage if True"""
        roll_0 = f"{roll_string(self.damage_roll)} {self.damage_type} damage"
        if self.damage_mod is None:
            roll_0_crit = f"{roll_crit(self.damage_die)} {self.damage_type} damage"
        
        else:
            roll_0_crit = f"{roll_crit(self.damage_die, self.damage_mod)} {self.damage_type} damage"

        if self.x_damage_die is None:

            if crit == False:
                return f"{roll_0}."

            else:
                return f"{roll_0_crit}."

        else:
            roll_x = f"{roll_string(self.x_damage_roll)} {self.x_damage_type} damage"
            if self.x_damage_mod is None:
                roll_x_crit = f"{roll_crit(self.x_damage_die)} {self.x_damage_type} damage"
            
            else:
                roll_x_crit = f"{roll_crit(self.x_damage_die, format_mod(self.x_damage_mod))} {self.x_damage_type} damage"

            if crit == False:
                return f"{roll_0} and {roll_x}."

            else:
                return f"{roll_0_crit} and {roll_x_crit}."


class LegendaryActions(Trait):
    """Class returns a container of legendary actions.

    Attributes:
        name (str): String of the instance's name
        actions (lst): List of Action, Attack and SaveAction instances
        text (int): String that proceeds the actions."""

    def __init__(self, name, actions):
        """Initialise the LegendaryActions instance.

        Args:
            name (str): String of the instance's name
            actions (lst): List of Action, Attack and SaveAction instances

        Attributes:
            text (int): String that proceeds the actions"""
        super().__init__(name)
        self.actions = actions
        self.text = f"The {self.name} can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature’s turn. The {self.name} regains spent legendary actions at the start of its turn."

    def __str__(self):
        """Return a string of the legendary action text followed by the action's names."""
        stringa = ""
        for action in self.actions:
            stringa += "\n" + action.__str__() + "\n"

        return format_text(self.text) + "\n" + stringa


class Spell():
    """Class returns an object representing a spell.

    Attributes:
        name (str): String of the spell's name
        level (int): Number representing the spell's level
        school (str): String of the school of magic to which the spell belongs
        casting_time (str): String of the time taken to cast the spell
        range (str): String of the spell's range
        components (str): String of the components required to cast the spell
        duration (str): String of the time the spell's effects last
        text (str): String describing the effects of the spell
        higher_levels (str): String of the spell's effects at higher levels
        json (obj): JSON object of the instance"""

    def __init__(self, name, level, school, casting_time, range, components,
                 duration, text, higher_levels):
        """Initialise the Spell class instance.
        Args:
            name (str): String of the spell's name
            level (int): Number representing the spell's level
            school (str): String of the school of magic to which the spell belongs
            casting_time (str): String of the time taken to cast the spell
            range (str): String of the spell's range
            components (str): String of the components required to cast the spell
            duration (str): String of the time the spell's effects last
            text (str): String describing the effects of the spell
            higher_levels (str): String of the spell's effects at higher levels
        
        Attributes:
            json (obj): JSON object of the instance"""
        self.name = name
        self.level = level
        self.school = school
        self.casting_time = casting_time
        self.range = range
        self.components = components
        self.duration = duration
        self.text = text
        self.higher_levels = higher_levels
        self.json = json.dumps(self.__dict__)

    def __repr__(self):
        """Retun a string representation of the object."""
        return f'Spell("{self.name}", "{self.level}", "{self.school}", "{self.casting_time}", "{self.range}", "{self.components}", "{self.duration}", "{self.text}", "{self.higher_levels}")'

    def __str__(self):
        """Return a formatted string representation of the object."""
        stringa = f"\n{self.name}\n"
        stringb = ""
        if self.level == "Cantrip":
            stringb = f"{self.school.title()} cantrip\n"

        else:
            stringb = f"{self.level} level {self.school}\n"

        stringc = f"Casting Time {self.casting_time}\nRange {self.range}\n"
        stringd = f"Components {self.components}\nDuration {self.duration}\n"
        with_text = stringa + stringb + stringc + \
            stringd + format_text(self.text)

        if self.higher_levels is None:
            return with_text

        else:
            return with_text + "\n" + format_text(self.higher_levels)


# InnateSpellcasting - trait containing list of spellcasting stats and spells
class InnateSpellcasting(Trait):
    """Class returns a trait representing a creature's innate spellcasting.

    Attributes:
        name (str): String representing the creature's name
        ability (str): String of the creature's ability used for spellcasting
        at_will (str): String listing spells the creature can cast at will 
        one_day (str): string listing spells the creature can cast 1/day
        two_day (str): string listing spells the creature can cast 2/day
        three_day (str): string listing spells the creature can cast 3/day
        save_DC (int): Number of the DC to roll against fthe creature's spells
        spell_attack: (str): String modifier of the creature's spell attacks
        extra (str): String of additional text for the stat block of instance
        stat_string (str): String combing all the stats for spellcasting
        text (str): String detailing the creature's stats and introduces spells
        roll_to_hit (func) Return int of roll to hit armour class:
        roll_advantage (func): Return list of ints to hit armour class with advantage
        roll_disadvantage (func): Return list of ints to hit armour class with disadvantage"""

    def __init__(self, name, ability, at_will=None, one_day=None, two_day=None,
                 three_day=None, save_DC=None, spell_attack=None, extra=None):
        """Initialise the InnateSpellcasting instance.

        Args:
            name (str): String representing the creature's name
            ability (str): String of the creature's ability used for spellcasting
            at_will (str): String listing spells the creature can cast at will 
            one_day (str): string listing spells the creature can cast 1/day
            two_day (str): string listing spells the creature can cast 2/day
            three_day (str): string listing spells the creature can cast 3/day
            save_DC (int): Number of the DC to roll against fthe creature's spells
            spell_attack: (int): Number applied to the creature's spell attack rolls
            extra (str): String of additional text for the stat block of instance

        Attributes:
            stat_string (str): String combing all the stats for spellcasting
            text (str): String detailing the creature's stats and introduces spells"""
        super().__init__(name)
        self.ability = ability
        self.at_will = at_will
        self.one_day = one_day
        self.two_day = two_day
        self.three_day = three_day
        self.save_DC = save_DC
        if spell_attack is None:
            pass

        else:
            self.spell_attack = format_mod(spell_attack)

        self.extra = extra
        if self.save_DC is None and self.spell_attack is None:
            self.stat_string = ""

        elif self.save_DC is not None and self.spell_attack is None:
            self.stat_string = f"(spell save DC {self.save_DC})"

        elif self.save_DC is not None and self.spell_attack is not None:
            self.stat_string = f"(spell save DC {self.save_DC}, {self.spell_attack} to hit with spell attacks)"

        else:
            self.stat_string = f"({self.spell_attack} to hit with spell attacks)"

        self.text = f"The {self.name.lower()}'s innate spellcasting ability is {self.ability} {self.stat_string}. It can innately cast the following spells, requiring no material components:\n"

    def __str__(self):
        """Return formatted string detailing the InnateSpellcasting instance."""
        string = format_text(self.text) + "\n"
        if self.at_will is not None and self.at_will != "":
            string += format_text(f"At will: {self.at_will}\n")

        if self.three_day is not None and self.three_day != "":
            string += format_text(f"3/day each: {self.three_day}\n")

        if self.two_day is not None and self.two_day != "":
            string += format_text(f"2/day each: {self.two_day}\n")

        if self.one_day is not None and self.one_day != "":
            string += format_text(f"1/day each: {self.one_day}\n")

        return string

    def roll_to_hit(self):
        """Return int of roll to hit armour class."""
        return roll_string("1d20" + self.spell_attack)

    def roll_advantage(self):
        """Return list of ints to hit armour class with advantage."""
        return roll_advantage("1d20" + self.spell_attack)

    def roll_disadvantage(self):
        """Return list of ints to hit armour class with disadvantage."""
        return roll_disadvantage("1d20" + self.spell_attack)


class Spellcasting(Trait):
    """Class returns an object representing a creature's spellcasting.

    The instance's current_spell_slots can be altered with the use_spell_slot 
    method.

    Attributes:
        name (str): String representing the creature's name
        caster_level (str): String of the level the creature can casts spells
        ability (str): String of the creature's ability used for spellcasting
        save_DC (int): Number of the DC to roll against fthe creature's spells
        spell_attack: (str): String modifier of the creature's spell attacks
        stat_string (str): String combing all the stats for spellcasting
        spell_class (str): String of the class the creature's spells are of
        cantrips (str): String of the cantrips the creature knows
        level_1 (str): String of the level 1 spells the creature has prepared
        level_2 (str): String of the level 2 spells the creature has prepared
        level_3 (str): String of the level 3 spells the creature has prepared
        level_4 (str): String of the level 4 spells the creature has prepared
        level_5 (str): String of the level 5 spells the creature has prepared
        level_6 (str): String of the level 6 spells the creature has prepared
        level_7 (str): String of the level 7 spells the creature has prepared
        level_8 (str): String of the level 8 spells the creature has prepared
        level_9 (str): String of the level 9 spells the creature has prepared
        spell_slots (lst): list of the slots available to each level of spell
        current_spell_slots (lst): List of current spell slots available
        extra (str): String of additional text for the stat block of instance
        text(str): String detailing the creature's stats and introduces spells
        roll_to_hit (func) Return int of roll to hit armour class:
        roll_advantage (func): Return list of ints to hit armour class with advantage
        roll_disadvantage (func): Return list of ints to hit armour class with disadvantage
        use_spell_slot (func): Update current_spell_slot after casting a levelled spell"""

    def __init__(self, name, caster_level, ability=None, save_DC=None, spell_attack=None,
                 spell_class=None, cantrips=None, level_1=None, level_2=None, level_3=None,
                 level_4=None, level_5=None, level_6=None, level_7=None, level_8=None,
                 level_9=None, spell_slots=None, extra=None):
        """Initialise the Spellcasting instance.

        Args:
            name (str): String representing the creature's name
            caster_level (str): String of the level the creature can casts spells
            ability (str): String of the creature's ability used for spellcasting
            save_DC (int): Number of the DC to roll against fthe creature's spells
            spell_attack: (str): String modifier of the creature's spell attacks
            spell_class (str): String of the class the creature's spells are of
            cantrips (str): String of the cantrips the creature knows
            level_1 (str): String of the level 1 spells the creature has prepared
            level_2 (str): String of the level 2 spells the creature has prepared
            level_3 (str): String of the level 3 spells the creature has prepared
            level_4 (str): String of the level 4 spells the creature has prepared
            level_5 (str): String of the level 5 spells the creature has prepared
            level_6 (str): String of the level 6 spells the creature has prepared
            level_7 (str): String of the level 7 spells the creature has prepared
            level_8 (str): String of the level 8 spells the creature has prepared
            level_9 (str): String of the level 9 spells the creature has prepared
            spell_slots (lst): list of the slots available to each level of spell
            extra (str): String of additional text for the stat block of instance

        Attributes:
            stat_string (str): String combing all the stats for spellcasting
            current_spell_slots (lst): List of current spell slots available
            text(str): String detailing the creature's stats and introduces spells"""
        super().__init__(name)
        self.caster_level = caster_level
        self.ability = ability
        self.save_DC = save_DC
        if spell_attack is None:
            pass

        else:
            self.spell_attack = format_mod(spell_attack)

        if self.save_DC is None and self.spell_attack is None:
            self.stat_string = ""

        elif self.save_DC is not None and self.spell_attack is None:
            self.stat_string = f"(spell save DC {self.save_DC})"

        elif self.save_DC is not None and self.spell_attack is not None:
            self.stat_string = f"(spell save DC {self.save_DC}, {self.spell_attack} to hit with spell attacks)"

        else:
            self.stat_string = f"({self.spell_attack} to hit with spell attacks)"

        self.spell_class = spell_class
        self.cantrips = cantrips
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = level_3
        self.level_4 = level_4
        self.level_5 = level_5
        self.level_6 = level_6
        self.level_7 = level_7
        self.level_8 = level_8
        self.level_9 = level_9
        if spell_slots is None:
            pass

        else:
            self.spell_slots = spell_slots
            self.current_spell_slots = deepcopy(self.spell_slots)

        self.extra = extra
        self.text = f"The {self.name} is a {self.caster_level}-level spellcaster. Its spellcasting ability is {self.ability} {self.stat_string}. The {self.name} has the following {self.spell_class} spells prepared:\n"

    def __str__(self):
        """Return formatted string of the Spellcasting instance."""
        string = format_text(f"Spellcasting. {self.text}")

        if self.cantrips is not None:
            string += format_text(f"\nCantrips (at will): {self.cantrips}")

        if self.level_1 is not None:
            string += format_text(
                f"\n1st level ({self.current_spell_slots[0]}/{self.spell_slots[0]} slots): {self.level_1}")

        if self.level_2 is not None:
            string += format_text(
                f"\n2nd level ({self.current_spell_slots[1]}/{self.spell_slots[1]} slots): {self.level_2}")

        if self.level_3 is not None:
            string += format_text(
                f"\n3rd level ({self.current_spell_slots[2]}/{self.spell_slots[2]} slots): {self.level_3}")

        if self.level_4 is not None:
            string += format_text(
                f"\n4th level ({self.current_spell_slots[3]}/{self.spell_slots[3]} slots): {self.level_4}")

        if self.level_5 is not None:
            string += format_text(
                f"\n5th level ({self.current_spell_slots[4]}/{self.spell_slots[4]} slots): {self.level_5}")

        if self.level_6 is not None:
            string += format_text(
                f"\n6th level ({self.current_spell_slots[5]}/{self.spell_slots[5]} slots): {self.level_6}")

        if self.level_7 is not None:
            string += format_text(
                f"\n7th level ({self.current_spell_slots[6]}/{self.spell_slots[6]} slots): {self.level_7}")

        if self.level_8 is not None:
            string += format_text(
                f"\n8th level ({self.current_spell_slots[7]}/{self.spell_slots[7]} slots): {self.level_8}")

        if self.level_9 is not None:
            string += format_text(
                f"\n9th level ({self.current_spell_slots[8]}/{self.spell_slots[8]} slots): {self.level_9}")

        return string

    def roll_to_hit(self):
        """Return int of roll to hit armour class."""
        return roll_string("1d20" + self.spell_attack)

    def roll_advantage(self):
        """Return list of ints to hit armour class with advantage."""
        return roll_advantage("1d20" + self.spell_attack)

    def roll_disadvantage(self):
        """Return list of ints to hit armour class with disadvantage."""
        return roll_disadvantage("1d20" + self.spell_attack)

    def use_spell_slot(self, slot_level):
        """Update current_spell_slot after casting a levelled spell."""
        self.current_spell_slots[slot_level-1] -= 1


class PactMagic:
    """Class returns an object representing a creature's pact magic feature.

    The instance's current_spell_slots can be altered with the use_spell_slot 
    method.

    Attributes:
        name (str): String representing the creature's name
        caster_level (str): String of the level the creature can casts spells
        save_DC (int): Number of the DC to roll against fthe creature's spells
        spell_attack: (int): Number applied to the creature's spell attacks
        stat_string (str): String combing all the stats for spellcasting
        spell_class (str): String of the class the creature's spells are of
        cantrips (str): String of the cantrips the creature knows
        spells (str): String of the levelled spells the creature knows
        spell_slots (int): Number of the slots available to cast levelled spells
        current_spell_slots (int): Number of current spell slots available
        text(str): String detailing the creature's stats and introduces spells
        roll_to_hit (func) Return int of roll to hit armour class:
        roll_advantage (func): Return list of ints to hit AC with advantage
        roll_disadvantage (func): Return list of ints to hit AC with disadvantage
        use_spell_slot (func): Update current_spell_slot after casting a levelled spell"""

    def __init__(self, caster_level, save_DC, spell_attack, cantrips, spells,
                 spell_slots, slot_level):
        """initialise the PactMagic instance.

        Args:
            name (str): String representing the creature's name
            caster_level (str): String of the caster levels of the creature
            save_DC (int): Number to roll against the creature's spells
            spell_attack: (int): Number applied to the creature's spell attacks
            spell_class (str): String of the class the creature's spells are of
            cantrips (str): String of the cantrips the creature knows
            spells (str): String of the levelled spells the creature knows
            spell_slots (int): Number of the slots for casting levelled spells

        Attributes:
            stat_string (str): String combing all the stats for spellcasting
            current_spell_slots (int): Number of current spell slots available
            text(str): String of the creature's stats and spellcasting rules"""
        self.caster_level = caster_level
        self.save_DC = save_DC
        self.spell_attack = format_mod(spell_attack)
        self.cantrips = cantrips
        self.spells = spells
        if self.save_DC is None and self.spell_attack is None:
            self.stat_string = ""

        elif self.save_DC is not None and self.spell_attack is None:
            self.stat_string = f"(spell save DC {self.save_DC})"

        elif self.save_DC is not None and self.spell_attack is not None:
            self.stat_string = f"(spell save DC {self.save_DC}, {self.spell_attack} to hit with spell attacks)"

        else:
            self.stat_string = f"({self.spell_attack} to hit with spell attacks)"

        self.spell_slots = spell_slots
        self.current_spell_slots = deepcopy(self.spell_slots)
        self.slot_level = slot_level
        self.text = f"The warlock is a {self.caster_level}-level spellcaster. Its spellcasting ability is Charisma {self.stat_string}. It regains its expended spell slots when it finishes a short or long rest. It knows the following warlock spells:\n"


    def __str__(self):
        """Return formatted string summarising the pact magic instance."""
        string = format_text(self.text) + "\n"

        if self.cantrips is not None:
            string += format_text(f"Cantrips (at will): {self.cantrips}\n")

        if self.spells is not None:
            string += format_text(
                f"1st-{self.slot_level} level ({self.current_spell_slots}/{self.spell_slots} {self.slot_level}-level slots): {self.spells}")

        return string


    def roll_to_hit(self):
        """Return int of roll to hit armour class."""
        return roll_string(f"1d20{self.spell_attack}")


    def roll_advantage(self):
        """Return list of ints to hit armour class with advantage."""
        return roll_advantage(f"1d20{self.spell_attack}")


    def roll_disadvantage(self):
        """Return list of ints to hit armour class with disadvantage."""
        return roll_disadvantage(f"1d20{self.spell_attack}")


    def use_spell_slot(self):
        """Update current_spell_slot after casting a levelled spell."""
        self.current_spell_slots -= 1
