"""Module containg class for creating Monster objects.

The Module contains one class, Monster, which is used to create an object
representing a creature that allows for access to its stats and rollable 
features.

The class makes use of the classes from the actions_traits module to constitute
its ability scores, actions, attacks, traits, legendary actions and other 
rollable and none rollable traits."""

from copy import deepcopy
import json
from os import system

from DiceBox import d20
from DiceBox import roll
from DiceBox import roll_advantage
from DiceBox import roll_disadvantage
from DiceBox import roll_string
from Data import stats_by_cr_df

class Monster:

    """Class returns an object of a creature that is modifiable and rollable.
    
    The class makes use of classes from the actions_traits module to implement
    the instance's ability scores, actions, attacks, spellcasting and traits, 
    and allows for access to their class methods through its own methods.

    The instance can be used to represent a creature during combat, with methods
    allowing for it's HP and other stats to be updated.
    """

    def __init__(self, name, size, monster_type, alignment, armour_class, armour_type,
                 average_hp, hit_dice, speed, abilities, senses, languages,
                 challenge_rating, saves=None, skills=None, damage_vulnerabilities=None,
                 damage_resistances=None, damage_immunities=None,
                 condition_immunities=None, special_traits=None,
                 actions=None, reactions=None, legendary_actions=None):
        """Initialise the Monster instance.
        Args:
            name (str): String of the creature's name
            size (str): String of the creature's size
            monster_type (str): String of the creature's type
            alignment (str): String of the creature's alignment, if any
            armour_class (int): Number of the creature's armour class
            armour_type, (str): String of the armour's type, if any
            average_hp (int): Number of the creature's average HP
            hit_dice (str): String of the creature's hit dice
            speed (str): String of the creature's speed in feet
            abilities (obj): AbilityScores instance for the creature's scores
            senses (str): String listing the creature's senses
            languages (str): String listing the creature's known languages
            challenge_rating (str): String of creature's challenge rating
            saves (lst): List of AbilityCheck instances for creature's saves
            skills (lst): List of AbilityCheck instances for creature's skills
            damage_vulnerabilities (str): String listing vulnerabilities
            damage_resistances (str): String listing resistances
            damage_immunities (str): String listing damage immunities
            condition_immunities (str): String listing condition immunities
            special_traits (lst): List of trait and spellcasting instances 
            actions (lst): List of Action, Attack and SaveAction instances
            reactions (lst): List of trait class actions
            legendary_actions (obj): LegendaryActions class instance
        
        Attributes:
            current_hp (int): Number deepcopied from average_hp for modifying
            temporary_hp (int): Number of temporary hit points creature has
            skills_dict (dict): Dictionary of skills based on abilities
            json_object(obj): Javascript object of the instance
            """
        self.name = name
        self.size = size
        self.monster_type = monster_type
        self.alignment = alignment
        self.armour_class = armour_class
        self.armour_type = armour_type
        self.average_hp = average_hp
        self.hit_dice = hit_dice
        self.current_hp = deepcopy(self.average_hp)
        self.temporary_hp = 0
        self.speed = speed
        self.abilities = abilities
        self.saves = saves
        self.skills = skills
        self.skills_dict = {
            "Athletics": self.abilities.strength_mod,
            "Acrobatics": self.abilities.dexterity_mod,
            "Sleight of Hand": self.abilities.dexterity_mod,
            "Stealth": self.abilities.dexterity_mod,
            "Arcana": self.abilities.intelligence_mod,
            "History": self.abilities.intelligence_mod,
            "Investigation": self.abilities.intelligence_mod,
            "Nature": self.abilities.intelligence_mod,
            "Religion": self.abilities.intelligence_mod,
            "Animal Handling": self.abilities.wisdom_mod,
            "Insight": self.abilities.wisdom_mod,
            "Medicine": self.abilities.wisdom_mod,
            "Perception": self.abilities.wisdom_mod,
            "Survival": self.abilities.wisdom_mod,
            "Deception": self.abilities.charisma_mod,
            "Intimidation": self.abilities.charisma_mod,
            "Performance": self.abilities.charisma_mod,
            "Persuasion": self.abilities.charisma_mod
        }
        self.damage_vulnerabilities = damage_vulnerabilities
        self.damage_resistances = damage_resistances
        self.damage_immunities = damage_immunities
        self.condition_immunities = condition_immunities
        if senses is None:
            self.senses = f"passive Perception {str(10 + self.abilities.wisdom_mod)}"

        else:
            self.senses = senses

        self.languages = languages
        self.challenge_rating = challenge_rating
        self.experience_points = stats_by_cr_df.at[self.challenge_rating, "XP"]
        self.special_traits = special_traits
        self.actions = actions
        self.reactions = reactions
        self.legendary_actions = legendary_actions
        #self.json_object = json.dumps(self.__dict__, cls=MonsterEncoder)

    def roll_skill_check(self, skill_name, advantage=False, disadvantage=False):
        """Return int of roll of skill check with advantage/disadantage.
        
        Args:
            skill_name (str): String of the name pf skill to be rolled
            advantage (bool) Bool indicating whether to roll advantage
            disadvantage (bool) Bool indicating whether to roll disadvantage
        
        Returns:
            int: An int if advantage/disadvantage are false, else a list of ints."""

        if advantage is False and disadvantage is False:

            if self.skills is None:
                return roll(1, d20) + self.skills_dict[skill_name]

            else:
                for skill in self.skills:

                    if skill.name.lower() == skill_name.lower():
                        return skill.roll_to_DC()

                    else:
                        return roll(1, d20) + self.skills_dict[skill_name]

        elif advantage is True and disadvantage is False:

            if self.skills is None:
                rolls = [roll(1, d20) + self.skills_dict[skill_name]
                         for i in range(2)]
                rolls.sort(reverse=True)
                return rolls

            else:

                for skill in self.skills:

                    if skill.name.lower() == skill_name.lower():
                        return skill.roll_advantage()

                    else:
                        rolls = [roll(1, d20) + self.skills_dict[skill_name]
                                 for i in range(2)]
                        rolls.sort(reverse=True)
                        return rolls
        else:

            if self.skills is None:
                rolls = [roll(1, d20) + self.skills_dict[skill_name]
                         for i in range(2)]
                rolls.sort()
                return rolls

            else:

                for skill in self.skills:

                    if skill.name.lower() == skill_name.lower():
                        return skill.roll_disadvantage()

                    else:
                        rolls = [roll(1, d20) + self.skills_dict[skill_name]
                                 for i in range(2)]
                        rolls.sort()
                        return rolls

        rolls = []
        for i in range(2):
            rolls.append(self.roll_skill_check(skill_name))

        rolls.sort()
        return rolls


    def roll_saving_throw(self, save_name, advantage=False, disadvantage=False):
        """Return int of roll of saving throw with advantage/disadantage.

        The method makes use of the inner function saving throw to roll the
        dice, which is then fed through the main function with advantage or
        disadvantage applied.
        
        Args:
            Save_name (str): String of the name pf skill to be rolled
            advantage (bool) Bool indicating whether to roll advantage
            disadvantage (bool) Bool indicating whether to roll disadvantage
        
        Returns:
            int: An int if advantage/disadvantage are false, else a list of ints."""

        def saving_throw(save_name):
            """Return int of roll of specified saving throw.

            The function checks if the given save_name is in saves, return a
            roll of that save if it is or a roll based on the creature's 
            appropriate ability score.

            Args:
                save_name (str): Name of saving throw to be rolled"""
            if self.saves is None:

                if save_name.lower() == "strength":
                    return roll(1, d20) + self.abilities.strength_mod

                elif save_name.lower() == "dexterity":
                    return roll(1, d20) + self.abilities.dexterity_mod

                elif save_name.lower() == "constitution":
                    return roll(1, d20) + self.abilities.constitution_mod

                elif save_name.lower() == "intelligence":
                    return roll(1, d20) + self.abilities.intelligence_mod

                elif save_name.lower() == "wisdom":
                    return roll(1, d20) + self.abilities.wisdom_mod

                elif save_name.lower() == "charisma":
                    return roll(1, d20) + self.abilities.charisma_mod

            else:

                for save in self.saves:

                    if save.name == save_name:
                        return save.roll_to_DC()

                    else:
                        if save_name.lower() == "strength":
                            return roll(1, d20) + self.abilities.strength_mod

                        elif save_name.lower() == "dexterity":
                            return roll(1, d20) + self.abilities.dexterity_mod

                        elif save_name == "constitution":
                            return roll(1, d20) + self.abilities.constitution_mod

                        elif save_name.lower() == "intelligence":
                            return roll(1, d20) + self.abilities.intelligence_mod

                        elif save_name.lower() == "wisdom":
                            return roll(1, d20) + self.abilities.wisdom_mod

                        elif save_name.lower() == "charisma":
                            return roll(1, d20) + self.abilities.charisma_mod

        if advantage is False and disadvantage is False:
            return saving_throw(save_name)

        elif advantage is True and disadvantage is False:
            rolls = [saving_throw(save_name) for i in range(2)]
            rolls.sort(reverse=True)
            return rolls

        else:
            rolls = [saving_throw(save_name) for i in range(2)]
            rolls.sort()
            return rolls

 
    def roll_action(self, action_name, advantage=False, disadvantage=False):
        """Return a int of an Attack's roll or and Action's string.
        
        Args:
            action_name (str): String of the name of action to be rolled
            advantage (bool) Bool indicating whether to roll advantage
            disadvantage (bool) Bool indicating whether to roll disadvantage
        
        Returns:
            int: An int or list of ints if action is rollable, else a string"""
        for action in self.actions:
            if action_name.lower() == action.name.lower():

                try:
                    if advantage == False and disadvantage == False:
                        return action.roll_to_hit()

                    elif advantage is True and disadvantage is False:
                        return action.roll_advantage()

                    else:
                        return action.roll_disadvantage()

                except:
                    return action.__str__()


    def roll_action_damage(self, action_name, crit=False):
        """Return int of standard or critical damage roll.
        
        Args:
            action_name (str):String of the action damage to be rolled
            crit (bool): Boolean to represent whther damage is crit or standard
        
        Returns:
            int: Critical damage if crit is True, else standard"""
        for action in self.actions:

            if action_name.lower() == action.name.lower():

                if crit is True:
                    return action.roll_damage(crit=True)

                return action.roll_damage()


    def roll_initiative(self, advantage=False, disadvantage=False):
        """Return in of initiative roll with advantage/disadvantage.
        
        Args:
            advantage (bool) Roll twice high to low if True, else roll once
            disadvantage (bool) Roll twice low to high if True, else roll once
        
        Returns:
            int: Int if advantage/disadvantage False, else list of ints"""

        if advantage is True:
            return roll_advantage("1d20" + self.abilities.dexterity_mod)

        elif disadvantage is True:
            return roll_disadvantage("1d20" + self.abilities.dexterity_mod)

        else:
            return roll(1, d20) + self.abilities.dexterity_mod


    def roll_hp(self):
        """Set creature's current and average hp to a roll of their hit_dice."""
        roll = roll_string(self.hit_dice)
        self.current_hp = deepcopy(roll)
        self.average_hp = deepcopy(roll)


    def add_temp_hp(self, num):
        """Update the creature's temporary_hp.

        Args:
            num (int): Number by which to increase the temporary_hp"""
        self.temporary_hp += num


    def take_damage(self, num):
        """Decrease the creature's current_hp and temporary_hp.

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
            num (int): Number by which to increase current_hp, up to average_hp"""
        if self.current_hp + num > self.average_hp:
            self.current_hp = deepcopy(self.average_hp)

        else:
            self.current_hp += num


    def __str__(self):
        """Return formatted string of creature's stat block.
        
        Returns:
            string: All of the Monster's attributes in the stat block format."""
        string = f"\n{self.name.upper()}\n{self.size.capitalize()} {self.monster_type}, {self.alignment}\n"
        if self.armour_type is None:
            string += f"Armour Class {self.armour_class}\n" 
        else:
            string += f"Armour Class {self.armour_class} ({self.armour_type})\n"

        string += f"Hit Points {self.current_hp}/{self.average_hp} ({self.hit_dice})\nSpeed {self.speed}\n{self.abilities.__str__()}\n"

        if self.saves is not None:
            string += "Saving Throws"
            for save in self.saves:
                string += f"{save.__str__()}, "

        string += "\n"
        if self.skills is not None:
            string += "Skills "
            for skill in self.skills:
                string += f"{skill.__str__()}, "

        string += "\n"
        if self.damage_vulnerabilities is not None:
            string += f'Damage Vulnerabilities {self.damage_vulnerabilities}\n'

        if self.damage_resistances is not None:
            string += f'Damage Resitances {self.damage_resistances}\n'

        if self.damage_immunities is not None:
            string += f'Damage Immunities {self.damage_immunities}\n'
        
        if self.condition_immunities is not None:
            string += f'Condition Immunities {self.condition_immunities}\n'

        string += f'Senses {self.senses}\nLanguages {self.languages}\nChallenge {self.challenge_rating} ({self.experience_points} XP)\n\n'

        if self.special_traits is not None:
            for trait in self.special_traits:
                string += trait.__str__() + "\n"

        if self.actions is not None:
            string += "\nACTIONS\n"
            for action in self.actions:
                string += action.__str__() + "\n"

        if self.reactions is not None:
            string += "\nREACTIONS\n"
            for reaction in self.reactions:
                string += reaction.__str__() + "\n"
                
        if self.legendary_actions is not None:
            string += "\nLEGENDARY ACTION\n"
            string += self.legendary_actions.__str__() + "\n"

        return string

    def print_sheet(self):
        """Print statblock to a txt file and open with less."""
        with open(f"{self.name}.txt", "w") as writer:
            writer.write(self.__str__())
        system(f"less '{self.name}.txt'")


class MonsterEncoder(json.JSONEncoder):
    """Class for converting a monster instance into a javascript object."""
    def default(self, obj):
        if hasattr(obj, 'json_object'):
            return obj.json_object
        else:
            return json.JSONEncoder.default(self, obj)