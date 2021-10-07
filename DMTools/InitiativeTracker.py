"""Classes and functions for running encounters in python shell.

The module contains two functions, copy_monster and set_combatant. The first
copies a Monster instance and returns it with rolled max hit points. The
second function takes a Monster instance and returns a Combatant instance.

The module also contains two classes, Combatant and Encounter. The first
creates an object that can be used to track an individual's  
armour class, conditions, hit points and initiative. The second creates an 
object that can be loaded with combatants allow for the tracking and updating 
of a combat encounter."""
from copy import deepcopy


class Combatant():
    """A Class that returns a combatant to be used in an Encounter instance.

    A class for monsters/pcs/npcs to be loaded into the tracker. It contains
    key stats and provides functionality for setting initiative, taking or
    healing damage and adding or removing conditions. 

    Note that the instances' initiative can be be a float or a num, incase
    of a tie.

    Attributes::
        name (str): String of the combatant's name
        initiative (int): The combatant's initiative order, usually rolled.
        ac (int): The combatant's armour class
        max_hp (int): The combatant's hit point maximum
        temporary_hp (int): The combatant's temporary hit points, default 0
        conditions (lst): List of combatant's conditions, default None
        current_hp (int): The combatant's current hit points"""

    def __init__(self, name, initiative, ac, max_hp, temporary_hp=0,
                 conditions=None):
        """Initialise the Combatant instance.

        Args:
            name (str): String of the combatant's name
            initiative (int): The combatant's initiative order, usually rolled.
            ac (int): The combatant's armour class
            max_hp (int): The combatant's hit point maximum
            temporary_hp (int): The combatant's temporary hit points, default 0
            conditions (lst): List of combatant's conditions, default None

        Attributes:
            current_hp (int): The combatant's current hit points"""
        self.name = name
        self.initiative = initiative
        self.ac = ac
        self.max_hp = max_hp
        self.current_hp = deepcopy(self.max_hp)
        self.temporary_hp = temporary_hp
        if conditions is None:
            self.conditions = []

        else:
            self.conditions = conditions


    def __str__(self):
        """Return the instance as a string of their key stats."""
        if len(self.conditions) is 0:
            conditions = "None"

        else:
            conditions = ", ".join(self.conditions)

        return f"{self.initiative}\t\t{self.name}\t\t{self.ac}\t\t{self.current_hp}/{self.max_hp} + {self.temporary_hp} temp hp\t{conditions}"


    def add_temp_hp(self, num):
        """Update the instance's temporary_hp.

        Args:
            num (int): Number by which to increase the temporary_hp"""
        self.temporary_hp += num


    def take_damage(self, num):
        """Decrease the instance's current_hp and temporary_hp.

        Args:
            num (int): Number used to decrease the current_hp and temporary_hp"""
        if self.temporary_hp > 0:

            if num <= self.temporary_hp:
                self.temporary_hp -= num

            else:
                self.current_hp -= (num - self.temporary_hp)
                self.temporary_hp = 0

        else:
            self.current_hp -= num


    def heal(self, num):
        """Increase the combatant's current_hp.

        Args:
            num (int): Number by which to increase current_hp, up to max_hp"""
        if self.current_hp + num > self.max_hp:
            self.current_hp = deepcopy(self.max_hp)

        else:
            self.current_hp += num


    def add_condition(self, condition):
        """Add a condition to the Combatant's conditions list.

        Args:
            condition (str): String of a condition affecting the combatant"""
        self.conditions.append(condition)


    def remove_condition(self, condition):
        """Remove a condition from the Combatant's conditions list.

        Args:
            condition (str): String of condition not affecting the combatant"""
        if condition in self.conditions:

            self.conditions.remove(condition)


    def set_initiative(self, num):
        """Modifiy the instance's initiative.

        Args:
            num (int): An int or float to which the initiative is changed"""
        self.initiative = num


class Encounter():
    """An Encounter instance for tracking combat and modifying combatants.

    The class takes in a list of Combatant instances and tracks their
    initiative order over the course of an encounter, providing methods for
    updating combatants from within the Encounter and progressing the
    initiative order.

    Attributes:
        combatants (lst): A list of Combatantant instances 
        current_initiative (int): Combatant's initiative at current index
        initiative_order (lst): Combatant initiatives sorted high to low
        initiative_index (int): Starts at 0 incremented with the round
        round (int): Starts at 1 increases once order is iterated through"""

    def __init__(self, combatants):
        """Initialise the Encounter instance.

        A method that initialises the tracker taking a list
        of Combatant instances as arguments and creates an initiative 
        order from ther initiatives.

        Args:
            combatants (lst): A list of Combatantant instances 

        Atrributes:
            initiative_order (lst): Combatant initiatives sorted high to low
            initiative_set (set): Set of initiative order for weeding doubles
            initiative_index (int): Starts at 0 incremented with the round
            current_initiative (int): Combatant's initiative at current index
            round (int): Starts at 1 increases once order is iterated through"""
        if combatants is None:
            self.combatants = []
            self.initiative_order = []

        else:
            self.combatants = combatants
            self.initiative_order = [
                combatant.initiative for combatant in self.combatants]
            self.initiative_order.sort(reverse=True)

        self.initiative_set = set(self.initiative_order)
        self.initiative_index = 0
        self.current_initiative = self.initiative_order[self.initiative_index]
        self.round = 1

    def __str__(self):
        """Return string of current state of encounter.

        A method rendering a table of the encounter as a string indicating
        the round and current initiative on top followed by a header. Then 
        each Combatant instance is returned as a new line in descending 
        initiative order."""
        self.initiative_order = [
                combatant.initiative for combatant in self.combatants]
        self.initiative_order.sort(reverse=True)
        self.initiative_set = set(self.initiative_order)
        header = f"\n\t\t\tRound: {self.round}\tInitiative: {self.current_initiative}\n"
        initiative_string = header + \
            "\nInitiative\tName\t\tArmour Class\tHit Points\t\tConditions"
        combatant_list = []

        for initiative in self.initiative_set:
            for combatant in self.combatants:
                if combatant.initiative is initiative:
                    combatant_list += [combatant.__dict__]

        combatant_list.sort(key=lambda i:i['initiative'], reverse=True)
        for combatant in combatant_list:
            initiative_string += f"\n{combatant['initiative']}\t\t{combatant['name']}\t\t{combatant['ac']}\t\t{combatant['current_hp']}/{combatant['max_hp']} + {combatant['temporary_hp']} temp hp\t\t{', '.join(combatant['conditions'])}"

        return initiative_string

    def add_combatant(self, combatant):
        """Add a Combatant instance to the Encounter.

        Args:
            combatant (object): Instance of the Combatant class"""
        self.combatants.append(combatant)
        self.initiative_order.append(combatant.initiative)
        self.initiative_order.sort(reverse=True)


    def remove_combatant(self, combatant):
        """Remove a Combatant instance to the Encounter.

        Args:
            combatant (object): Instance of the Combatant class"""
        self.initiative_order.remove(combatant.initiative)
        self.combatants.remove(combatant)


    def set_initiative(self, combatant, num):
        """Modifiy a specified combatant's initiative.

        Args:
            combatant (object): Combatant instance for initiative to modify
            num (int): An int or float to which the initiative is changed"""
        combatant.set_initiative(num)
        self.initiative_order = [
            combatant.initiative for combatant in self.combatants]
        self.initiative_order.sort(reverse=True)


    def add_temp_hp(self, combatant, num):
        """Update the combatant's temporary_hp.

        Args:
            combatant (object): Combatant instance for hit points to modify
            num (int): Number by which temporary_hp increases"""
        combatant.add_temp_hp(num)


    def take_damage(self, combatant, num):
        """Decrease the combatant's current_hp and temporary_hp.

        Args:
            combatant (object): Combatant instance for hit points to modify
            num (int): Number by which temporary_hp and current_hp decreases"""
        combatant.take_damage(num)


    def heal(self, combatant, num):
        """Increase the combatant's current_hp up to max_hp.

        Args:
            combatant (object): Combatant instance for hit points to modify
            num (int): Number by which current_hp increases"""
        combatant.heal(num)


    def add_condition(self, combatant, condition):
        """Add a condition to a Combatant's conditions list.

        Args:
            combatant (object): Combatant instance for conditions to modify
            condition (str): String appended to combatant's conditions list"""
        combatant.add_condition(condition)


    def remove_condition(self, combatant, condition):
        """Remove a condition from a Combatant's conditions list.

        Args:
            combatant (object): Combatant instance for conditions to modify
            condition (str): String removed from combatant's conditions list"""
        combatant.remove_condition(condition)


    def next_turn(self):
        """Progress initiative_order and print the new turn.

        A method for advancing the instance's initiative_order by increasing
        its initiative_index by 1. In the event of the an IndexError the 
        method increments the instance's round by 1 and resets its 
        initiative_order.

        The method then prints the Encounter instance displaying the
        change in order and any combatant key stats."""

        try:
            self.initiative_index += 1
            self.current_initiative = self.initiative_order[self.initiative_index]
            print(self.__str__())

        except IndexError:
            self.initiative_index = 0
            self.round += 1
            self.current_initiative = self.initiative_order[self.initiative_index]
            print(self.__str__())


def copy_monster(monster):
    """Return a copy of a Monster instances with rolled max hit points.

    Args:
        monster (object): An instance of the Monster Class

    Returns:
        monster_copy: A deepcopy of a Monster instance with rolled hit points."""
    monster_copy = deepcopy(monster)
    monster_copy.roll_hp()

    return monster_copy


def set_combatant(monster, name, temp_hp=None, conditions=None):
    """Return a Combatant instance from a Monster instance.

    Args:
        monster (object): An instance of the Monster class
        name (str): String used to identify returned Combatant
        temp_hp (int): Number of temporary_hp for Combatant, default 0
        conditions (lst): List of conditions affecting combatant, default None

    Return:
        Combatant: A Combatant instance from a Monster instance"""

    if temp_hp is None and conditions is None:
        return Combatant(name, monster.roll_initiative(), monster.armour_class, monster.current_hp)

    elif temp_hp is not None and conditions is None:
        return Combatant(name, monster.roll_initiative(), monster.armour_class, monster.current_hp, temp_hp)

    elif temp_hp is None and conditions is not None:
        return Combatant(name, monster.roll_initiative(), monster.armour_class, monster.current_hp, conditions=conditions)

    else:
        return Combatant(name, monster.roll_initiative(), monster.armour_class, monster.current_hp, temp_hp, conditions)
