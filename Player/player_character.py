from copy import deepcopy
from os import system

from Data import beyond_1st_level_df
from DiceBox import d20
from DiceBox import roll
from DiceBox import roll_advantage
from DiceBox import roll_disadvantage
from DiceBox import roll_string
from Utilities import format_mod
from Utilities import format_num
from Utilities import format_text
from Player.warlock_class import celestial
from Player.warlock_class import warlock
from StatBlock import InnateSpellcasting
from StatBlock import PactMagic

class PlayerCharacter:
    """An object that contain's a player character's stats and features.
    
    The class takes multiple PlayerFeature instances, Gear instances and Trait
    subclass instances as arguments and derives core stats from them. The
    player's class, race and background must be specified on startup. The
    archetype for the class can be also chosen upon initialising.

    Once the instance is initialised, the class provides methods for adding 
    aditional actions, proficiencies, spells and other instances of objects 
    from the DnD module. These can be used to finish creating the character 
    and for levelling up.
    
    There are also methods for changing hit points, rolling initiative, 
    to hit and damage and other related functions that can be used for 
    running the character in combat. 
    
    The class also has features for managing inventory, differentiating 
    between mundane items or those not rendered as a Gear instance with 
    equipment being the first and items being the latter.
    
    Lastly there are methods for returning strings of the character's
    stats and features, including print_sheet that creates a txt file in 
    the same directory as the instance with a full print out of their 
    character sheet."""
    def __init__(self, name, character_class, archetype, background, 
                 player_name, race, alignment, experience_points, abilities, 
                 max_hp, personality_traits, ideals, bonds, flaws, age, 
                 height, weight, eyes, skin, hair, copper=0, silver=0, 
                 electrum=0, gold=0, platinum=0, equipment=None, 
                 treasure=None, backstory=None, allies_organisations=None):
        """Initialise the PlayerCharacter instance.
        
        Args:
            name (str): The character's name
            character_class (obj): A CharacterClass instance
            archetype (obj): An Archetype instance
            background (obj): a Background instance
            player_name (str): The player's name
            race (obj): A Race instance
            alignment (str): The character's alignment
            experience_points (int): The player's current experience points
            abilities (obj): An AbilityScores instance
            max_hp (int): The character's maximum hit points
            personality_traits (lst): Strings of the character's traits
            ideals (str): The character's ideals
            bonds (str): The chaarcter's bonds
            flaws (str): The character's flaws
            age (int): The character's age
            height (str): The character's height in feet and inches
            weight (str): The character's weight in pounds
            eyes (str): The character's eye colour and shape
            skin (str): The character's skin colour
            hair (str): The character's hairstyle and colour
            copper (int): The character's copper pieces, starts at 0
            silver (int): The character's silver pieces, starts at 0
            electrum (int): The character's electrum pieces, starts at 0
            gold (int): The character's gold pieces, starts at 0
            platinum (int): The character's platinum pieces, starts at 0
            equipment (lst): Strings of the character's equipment
            treasure  (lst): Strings of the character's treasure
            backstory (str): The character's backstory as text
            allies_organisations (str): The character's memberships and pacts
        
        Attributes:
            level (int): The character's current level, derived from xp
            proficiency_bonus (int): The character's proficiency bonus
            inspiration (bool): True for inspiration, default False
            armour_class (int): The character's armour class, starts at 0
            armour_type (str): The type of armour (leather, natural etc)
            initiative (int): The character's initiative modifier
            speed (str): The character's speed, derived from race
            hit_die (str): The character's hit die, derived from class
            hit_dice (str): The character's total hitdice with constitution mod
            current_hd (int): Copied from character's level
            spent_hd (int): Number of dice spent when healing, starts at 0
            current_hp (int): Copied from caharacter's max_hp
            temp_hp (int): Character's temporary hit points, starts at 0
            exhaustion (int): Character's level of exhaustion, starts at 0
            death_saves_dict (dict): Ints of failed and successful death saves
            saves_dict (dict): Ints for saving throw rolls 
            saving_throw_proficiencies (str): The character's save proficiencies
            ability_checks_dict (dict): Ints for ability check rolls
            skills_dict (dict): Ints for skill check rolls
            skill_proficiencies (str): The chacater's skill proficiencies
            passive_perception (int): The character's passive perception
            armour_proficiencies (lst): Strings of armour proficiencies
            weapon_proficiencies (lst): Strings of weapon proficiencies
            tool_proficiencies (lst): Strings of tool proficiencies
            languages (lst): Strings of character's known languages
            features_traits (lst): CharacterFeatures from class, race etc
            features_traits_strings (lst): Strings of the feature's names
            spell_attack (int): The character's spell atack bonus
            spell_save (int): The character's spell save DC
            spell_slots (int or lst) Int for warlock else list of ints
            current_spell_slots (int of lst): Int for warlock else list of ints
            slot_level (str): The highest level of spell slots available
            pact_magic (obj): PactMagic instance for warlock
            pact_magic_innate (obj): InnateSpellcasting for warlock
            healing_light_pool (str): Available dice pool for celestial
            actions_list (lst): Action, Attack and SaveAction instances 
            items (lst): Gear instances for detailed/magic items"""
        self.name = name
        self.character_class = character_class
        self.archetype = archetype
        self.background = background
        self.player_name = player_name
        self.race = race
        self.alignment = alignment
        self.experience_points = experience_points
        self.abilities = abilities
        self.max_hp = max_hp
        self.personality_traits = personality_traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.age = age
        self.height = height
        self.weight = weight
        self.eyes = eyes
        self.skin = skin
        self.hair = hair
        self.copper = copper
        self.silver = silver
        self.electrum = electrum
        self.gold = gold
        self.platinum = platinum
        self.equipment = equipment
        self.treasure = treasure
        self.backstory = backstory
        self.allies_organisations = allies_organisations

        # Attributes derived from arguments
        self.level = abs(
            beyond_1st_level_df["Experience Points"] - self.experience_points).idxmin()
        self.proficiency_bonus = beyond_1st_level_df.at[self.level,
                                                        "Proficiency Bonus"]

        # Inspiration
        self.inspiration = False

        # Defense
        self.armour_class = 0
        self.armour_type = None
        self.initiative = self.abilities.dexterity_mod
        self.speed = self.race.speed

        # Hit Points & Dice
        self.hit_die = self.character_class.hit_dice
        self.hit_dice = f"{self.level}{self.hit_die} + {self.abilities.constitution_mod * self.level}"
        self.current_hd = deepcopy(self.level)
        self.spent_hd = 0
        self.current_hp = deepcopy(self.max_hp)
        self.temp_hp = 0
        self.exhaustion = 0

        # Saving Throws
        self.death_saves_dict = {
            "Saves": 0, 
            "Fails": 0
        }
        self.saves_dict = {
            "Strength": self.abilities.strength_mod,
            "Dexterity": self.abilities.dexterity_mod,
            "Constitution": self.abilities.constitution_mod,
            "Intelligence": self.abilities.intelligence_mod,
            "Wisdom": self.abilities.wisdom_mod,
            "Charisma": self.abilities.charisma_mod
        }
        self.saving_throw_proficiencies = self.character_class.saving_throws.split(
            ", ")
        for saving_throw in self.saving_throw_proficiencies:
            for key, value in self.saves_dict.items():
                if saving_throw.lower() == key.lower():
                    self.saves_dict.update(
                        {key: value + self.proficiency_bonus})

        # Ability Checks
        self.ability_checks_dict = {
            "Strength": self.abilities.strength_mod,
            "Dexterity": self.abilities.dexterity_mod,
            "Constitution": self.abilities.constitution_mod,
            "Intelligence": self.abilities.intelligence_mod,
            "Wisdom": self.abilities.wisdom_mod,
            "Charisma": self.abilities.charisma_mod
        }

        # Skill Proficiencies
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
        self.skill_proficiencies = self.background.skills.split(", ")
        if self.race.skills is not None:
            self.skill_proficiencies += deepcopy(self.race.skills).split(", ")

        for skill in self.skill_proficiencies:
            for key, value in self.skills_dict.items():
                if skill.lower() == key.lower():
                    self.skills_dict.update(
                        {key: value + self.proficiency_bonus})
        
        self.passive_perception = 10 + self.skills_dict["Perception"]

        # Armour Proficiencies
        self.armour_proficiencies = []
        if self.race.armour is not None:
            self.armour_proficiencies += deepcopy(self.race.armour).split(", ")

        if self.character_class.armour is not None:
            self.armour_proficiencies += deepcopy(self.character_class.armour).split(
                ", ")

        if self.archetype.armour is not None:
            self.armour_proficiencies += deepcopy(self.archetype.armour).split(", ")

        if len(self.armour_proficiencies) == len(set(self.armour_proficiencies)):
            pass

        else:
            armour_set = set(self.armour_proficiencies)
            self.armour_proficiencies = sorted(armour_set)

        # Weapon Proficiencies
        self.weapon_proficiencies = []
        if self.race.weapons is not None:
            self.weapon_proficiencies += deepcopy(self.race.weapons).split(", ")

        if self.character_class.weapons is not None:
            self.weapon_proficiencies += deepcopy(self.character_class.weapons).split(
                ", ")

        if self.archetype.weapons is not None:
            self.weapon_proficiencies += deepcopy(self.archetype.weapons).split(", ")
        
        if len(self.weapon_proficiencies) == len(set(self.weapon_proficiencies)):
            pass

        else:
            weapon_set = set(self.weapon_proficiencies)
            self.weapon_proficiencies = sorted(weapon_set)

        # Tool Proficiencies
        self.tool_proficiencies = []
        if self.race.tools is not None:
            self.tool_proficiencies += deepcopy(self.race.tools).split(", ")

        if self.background.tools is not None:
            self.tool_proficiencies += deepcopy(self.background).tools.split(", ")

        if self.character_class.tools is not None:
            self.tool_proficiencies += deepcopy(self.character_class.tools).split(", ")

        if self.archetype.tools is not None:
            self.tool_proficiencies += deepcopy(self.archetype.tools).split(", ")
        
        if len(self.tool_proficiencies) == len(set(self.tool_proficiencies)):
            pass

        else:
            tool_set = set(self.tool_proficiencies)
            self.tool_proficiencies = sorted(tool_set)

        #Language Proficiencies
        self.languages = []
        if self.race.language_list is not None:
            self.languages += deepcopy(self.race.language_list)
        
        #Features and Traits
        self.features_traits = []
        self.features_traits_strings = []
        if self.race.traits is not None:
            self.features_traits += deepcopy(self.race.traits)

        if self.background.features is not None:
            self.features_traits += deepcopy(self.background.features)

        # CharacterClass Features
        if self.character_class is warlock:
            self.spell_attack = self.abilities.charisma_mod + self.proficiency_bonus
            self.spell_save = 8 + self.abilities.charisma_mod + self.proficiency_bonus
            self.spell_slots = self.character_class.table.at[format_num(self.level), "Spell Slots"]
            self.current_spell_slots = deepcopy(self.spell_slots)
            self.slot_level =self.character_class.table.at[format_num(self.level), "Slot Level"]
            self.pact_magic = PactMagic(format_num(self.level), self.spell_save, self.spell_attack,
                                        "", "",
                                        self.character_class.table.at[format_num(
                                            self.level), "Spell Slots"],
                                        self.character_class.table.at[format_num(self.level), "Slot Level"], )
            self.pact_magic_innate = InnateSpellcasting("Warlock", "Charisma", "", "", "",
                                                        save_DC=f"{self.spell_save}",
                                                        spell_attack=self.spell_attack)

            for feature in self.character_class.features:
                if feature.level in range(1, self.level + 1):
                    self.features_traits.append(deepcopy(feature))

        # Archetype Features
        if self.archetype is celestial:
            self.healing_light_pool = [deepcopy(self.level), "d6"]
            for feature in self.archetype.features:
                if feature.level in range(1, self.level + 1):
                    self.features_traits.append(feature)

        self.features_traits_strings += [
            feature.name for feature in self.features_traits]
        
        #Action Attributes
        self.actions_list = []

        #Inventory Attributes
        self.items = []


    # General Methods
    def roll_initiative(self, advantage=False, disadvantage=False):
        """Return int of initiative roll with advantage/disadvantage.
        
        Args:
            advantage (bool) Roll twice high to low if True, else roll once
            disadvantage (bool) Roll twice low to high if True, else roll once
        
        Returns:
            int: Int if advantage/disadvantage False, else list of ints"""
        if advantage is True:
            return roll_advantage("1d20" + self.initiative)

        elif disadvantage is True:
            return roll_disadvantage("1d20" + self.initiative)

        else:
            return roll(1, d20) + self.initiative


    def roll_ability(self, ability, advantage=False, disadvantage=False, 
                     proficient=False):
        """Return int or list of ints for rolls of given ability check.
        Args:
            ability (str): String of check to be rolled from ability_checks_dict
            advantage (bool): True to roll twice sorted highest to lowest
            disadvantage (bool): True to roll twice sorted lowest to highest
            proficient (bool): True to add proficiency_bonus to roll, else not
        
        Returns:
            (int): Number from roll of d20 plus check mod from ability_checks_dict
            (lst): Two rolls highest to lowest if advantage
            (lst): Two rolls lowest to highest if disadvantage"""
        if advantage is False and disadvantage is False:
            for item in self.ability_checks_dict.items():
                if item[0].lower() == ability.lower():
                    if proficient is True:
                        return d20() + item[1] + self.proficiency_bonus

                    else:
                        return d20() + item[1]
        
        elif advantage is True and disadvantage is False:
            for item in self.ability_checks_dict.items():
                if item[0].lower() == ability.lower():
                    if proficient is True:
                        return roll_advantage(f"d20+{item[1]}+{self.proficiency_bonus}")
                    
                    else:
                        return roll_advantage(f"d20+{item[1]}")
        
        elif advantage is False and disadvantage is True:
            for item in self.ability_checks_dict.items():
                if item[0].lower() == ability.lower():
                    if proficient is True:
                        return roll_disadvantage(f"d20+{item[1]}+{self.proficiency_bonus}")
                    
                    else:
                        return roll_disadvantage(f"d20+{item[1]}")


    def roll_save(self, save, advantage=False, disadvantage=False):
        """Return int or list of ints for rolls of given save.
        Args:
            save (str): String of saving throw to be rolled from saves_dict
            advantage (bool): True to roll twice sorted highest to lowest
            disadvantage (bool) True to roll twice sorted lowest to highest
        
        Returns:
            (int): Number from roll of d20 plus save mod from saves_dict
            (lst): Two rolls highest to lowest if advantage
            (lst): Two rolls lowest to highest if disadvantage"""
        if advantage is False and disadvantage is False:
            for item in self.saves_dict.items():
                if item[0].lower() == save.lower():
                    return d20() + item[1]
    
        
        elif advantage is True and disadvantage is False:
            for item in self.saves_dict.items():
                if item[0].lower() == save.lower():
                    return roll_advantage(f"d20+{item[1]}")
        
        elif advantage is False and disadvantage is True:
            for item in self.saves_dict.items():
                if item[0].lower() == save.lower():
                    return roll_disadvantage(f"d20+{item[1]}")


    def roll_skill(self, skill, advantage=False, disadvantage=False):
        """Return int or list of ints for rolls of given save.
        Args:
            save (str): String of skill check to be rolled from skills_dict
            advantage (bool): True to roll twice sorted highest to lowest
            disadvantage (bool) True to roll twice sorted lowest to highest
        
        Returns:
            (int): Number from roll of d20 plus save mod from skills_dict
            (lst): Two rolls highest to lowest if advantage
            (lst): Two rolls lowest to highest if disadvantage"""
        if advantage is False and disadvantage is False:
            for item in self.skills_dict.items():
                if item[0].lower() == skill.lower():
                    return d20() + item[1]
            
        elif advantage is True and disadvantage is False:
            for item in self.skills_dict.items():
                if item[0].lower() == skill.lower():
                    return roll_advantage(f"d20+{item[1]}")
        
        elif advantage is False and disadvantage is True:
            for item in self.skills_dict.items():
                if item[0].lower() == skill.lower():
                    return roll_disadvantage(f"d20+{item[1]}")


    def roll_action(self, action_name, advantage=False, disadvantage=False):
        """Return a int of an Attack's roll or and Action's string.
        
        Args:
            action_name (str): String of the name of action to be rolled
            advantage (bool) Bool indicating whether to roll advantage
            disadvantage (bool) Bool indicating whether to roll disadvantage
        
        Returns:
            int: An int or list of ints if action is rollable, else a string"""
        for action in self.actions_list:
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
        for action in self.actions_list:

            if action_name.lower() == action.name.lower():

                if crit is True:
                    return action.roll_damage(crit=True)

                return action.roll_damage()


    def roll_death_save(self, advantage=False, disadvantage=False):
        """Return an int of a death save roll that modifies death_saves_dict.

        Roll is evealuated and the appropriate list in the death_saves_dict
        is modified accordingly; a 1 for a roll above 10 in the Saves list;
        a 1 for each roll of 9 or below in the Fails list
        
        Args:
            advantage (bool) Result is higest of two d20 rolls 
            disadvantage (bool) Result is lowest of two d20 rolls
        
        Attributes:
            roll (int/lst): Result of rolling advantage/disadvantage or not
            result (int): Number from d20() or advan/disad to be eavluated
        
        Returns:
            str: string of result and state of death_saves_dict"""
        if advantage is False and disadvantage is False:
            roll = d20()
            result = deepcopy(roll)

        elif advantage is True and disadvantage is False:
            roll = roll_advantage("1d20")
            result = deepcopy(roll[0])

        elif advantage is False and disadvantage is True:
            roll = roll_disadvantage("1d20")
            result = deepcopy(roll[0])
        
        if result == 1:
            self.death_saves_dict["Fails"] += 2
        
        elif result in range(2, 10):
            self.death_saves_dict["Fails"] += 1
        
        elif result in range(10, 20):
            self.death_saves_dict["Saves"] += 1
        
        elif result == 20:
            self.death_saves_dict["Saves"] += 2
        
        string = f"Rolled: {roll}  Saves: {self.death_saves_dict['Saves']}  Fails: {self.death_saves_dict['Fails']}"
        if self.death_saves_dict["Fails"] >= 3:
            self.death_saves_dict["Fails"] = 0
            self.death_saves_dict["Saves"] = 0
            return f"Rolled: {roll}. You die."
        
        elif self.death_saves_dict["Saves"] >= 3:
            self.death_saves_dict["Fails"] = 0
            self.death_saves_dict["Saves"] = 0
            return f"Rolled: {roll}. You are stable."
        
        else:
            return string
        

    def roll_hp(self):
        """Add roll of hit_die + constitution_mod to max_hp for levelling up."""
        roll = roll_string(f"{self.hit_die}+{self.abilities.constitution_mod}")
        self.current_hp += deepcopy(roll)
        self.max_hp += deepcopy(roll)
    

    def roll_hd(self, num):
        """Decrement current_hd by num and heal by result of roll."""
        if self.current_hd - num <= 0:
            pass

        else:
            self.current_hd -= num
            self.spent_hd += num
            self.heal(roll_string(f"{num}{self.hit_die}+{self.abilities.constitution_mod}"))


    def add_temp_hp(self, num):
        """Update the PlayerCharacter's temp_hp.

        Args:
            num (int): Number by which to increase the temp_hp"""
        self.temp_hp += num


    def take_damage(self, num):
        """Decrease the PlayerCharacter's current_hp and temp_hp.

        Args:
            num (int): Number used to decrease the current_hp and temp_hp"""
        if self.temp_hp > 0:

            if num <= self.temp_hp:
                self.temp_hp -= num

            else:
                self.current_hp -= (num - self.temp_hp)
                self.temp_hp = 0

        else:
            self.current_hp -= num


    def heal(self, num):
        """Increase the PlayerCharcter's current_hp.

        Args:
            num (int): Number by which to increase current_hp, up to max_hp"""
        if self.current_hp + num > self.max_hp:
            self.current_hp = deepcopy(self.max_hp)

        else:
            self.current_hp += num



    def short_rest(self, roll_hd=None):
        """Complete short rest with healing and feature/spell slot recharges.
        
        Args:
            roll_hd (int): Number of hit dice to roll, default is None"""
        if self.character_class is warlock:
            self.current_spell_slots = deepcopy(self.spell_slots)

        if roll_hd is not None:
            self.heal(roll_hd)


    def long_rest(self):
        """Complete long rest with hit point/hit dice/feature/spell slot regain."""
        self.current_hp = deepcopy(self.max_hp)
        if self.exhaustion > 0:
            self.exhaustion -= 1

        if self.character_class is warlock:
            self.current_spell_slots = deepcopy(self.spell_slots)
        
        if self.archetype is celestial:
            self.healing_light_pool[0] = deepcopy(self.level)
            

        if self.current_hd + int(self.level / 2) > self.level:
            pass

        else:
            self.current_hd += int(self.level / 2)


    def add_proficiency(self, proficiency, kind, expertise=False):
        """Add given proficiency to it's respective lst or dict with expertise.
        
        Args:
            proficiency (str): The proficiency's name, in title case
            kind (str): The type of proficiency; langauge; tool; skill etc
            expertise (bool): Proficiency bonus * 2 + mod if true, else once"""
        if kind.lower() == "save":
            for key, value in self.saves_dict.items():
                if proficiency.lower() == key.lower():
                    self.saves_dict.update(
                        {key: value + self.proficiency_bonus})

        elif kind.lower() == "skill":
            if expertise is False:
                for key, value in self.skills_dict.items():
                    if proficiency.lower() == key.lower():
                        self.skills_dict.update(
                            {key: value + self.proficiency_bonus})
            
            else:
                for key, value in self.skills_dict.items():
                    if proficiency.lower() == key.lower():
                        self.skills_dict.update(
                            {key: value + (self.proficiency_bonus * 2)})

        elif kind.lower() == "armour":
            if proficiency.lower() not in self.armour_proficiencies:
                self.armour_proficiencies += [proficiency]
                armour_set = set(self.armour_proficiencies)
                self.armour_proficiencies = sorted(armour_set)
        
        elif kind.lower() == "weapon":
            if proficiency.lower() not in self.weapon_proficiencies:
                self.weapon_proficiencies += [proficiency]
                weapon_set = set(self.weapon_proficiencies)
                self.weapon_proficiencies = sorted(weapon_set)

        elif kind.lower() == "tool":
            if proficiency.lower() not in self.tool_proficiencies:
                self.tool_proficiencies += [proficiency]
                tool_set = set(self.tool_proficiencies)
                self.tool_proficiencies = sorted(tool_set)

        elif kind.lower() == "language":
            if proficiency.lower() not in self.languages:
                self.languages += [proficiency]
                language_set = set(self.languages)
                self.languages = sorted(language_set)
        
        else:
            pass


    def remove_proficiency(self, proficiency, kind):
        """Remove given proficiency from its corresponding list or dict.
        
        Args:
            proficiency (str): Name of proficiency to be removed in title case
            kind (str): They type of proficiency; langauge; tool; skill etc"""
        if kind.lower() == "save":
            for key, value in self.saves_dict.items():
                if proficiency.lower() == key.lower():
                    self.saves_dict.update(
                        {key: value - self.proficiency_bonus})

        elif kind.lower() == "skill":
            for key, value in self.skills_dict.items():
                    if proficiency.lower() == key.lower():
                        self.skills_dict.update(
                            {key: value - self.proficiency_bonus})
        
        elif kind.lower() == "armour":
            if proficiency.lower() in self.armour_proficiencies:
                self.armour_proficiencies.remove(proficiency)
                armour_set = set(self.armour_proficiencies)
                self.armour_proficiencies = sorted(armour_set)

        elif kind.lower() == "weapon":
            if proficiency.lower() in self.weapon_proficiencies:
                self.weapon_proficiencies.remove(proficiency)
                weapon_set = set(self.weapon_proficiencies)
                self.weapon_proficiencies = sorted(weapon_set)

        elif kind.lower() == "tool":
            if proficiency.lower() in self.tool_proficiencies:
                self.tool_proficiencies.remove(proficiency)
                tool_set = set(self.tool_proficiencies)
                self.tool_proficiencies = sorted(tool_set)

        elif kind.lower() == "language":
            if proficiency.lower() in self.languages:
                self.languages.remove(proficiency)
                language_set = set(self.languages)
                self.languages = sorted(language_set)


    def add_feature(self, feature):
        """Add a CharacterFeature instance to features_traits.
        
        Args:
            feat (obj): A CharacterFeature instance"""
        self.features_traits += [feature]

    
    def remove_feature(self, feature):
        """Remove a CharacterFeature instance from features_traits.
        
        Args:
            feat(obj): A CharacterFeature instance from the feats package"""
        self.features_traits.remove(feature)


    def search_features(self, feature):
        """Return string of feature if found in features_traits.

        Args:
            feature (str): String of feature to be searched
            
        Returns:
            (str): String of feature if found else not found string"""
        for trait in self.features_traits:
            if trait.name.lower() == feature.lower():
                return "\n" + str(trait)
    

    def add_item(self, item):
        """Add a Gear instance to items.
        
        Args:
            item (obj): An instance of the Gear class or one of its subclasses"""
        self.items.append(item)
    

    def remove_item(self, item):
        """Remove a Gear instance from items.
        
        Args:
            item (obj): An instance of the Gear class or one of its subclasses"""
        self.items.remove(item)
    

    def equip_armour(self, kind, num):
        """Apply attributes from Gear instance in itmes to character stats.
        
        Args:
            type (str): String of the armour's name
            AC (int): Number to which the instance's armour_class is set"""
        self.armour_class = num
        self.armour_type = kind
                

    def get_core(self):
        """Return string of character's core traits and scores."""
        string = f"\t\t\t{self.name.upper()}\n\nClass: {self.character_class.name} ({self.archetype.name})  Level: {self.level}  Background: {self.background.name}  Player: {self.player_name}"
        string += f"\nRace: {self.race.name}  Alignment: {self.alignment}  Experience Points: {self.experience_points}\n"
        string += f"\n{self.abilities}"
        string += f"\n{format_mod(self.saves_dict['Strength'])} Save\t{format_mod(self.saves_dict['Dexterity'])} Save\t{format_mod(self.saves_dict['Constitution'])} Save\t{format_mod(self.saves_dict['Intelligence'])} Save\t{format_mod(self.saves_dict['Wisdom'])} Save\t{format_mod(self.saves_dict['Charisma'])} Save"
        string += f"\n\nArmour Class: {self.armour_class}  Initiative: {format_mod(self.initiative)}  Speed: {self.speed}  Proficiency Bonus: {format_mod(self.proficiency_bonus)}"
        string += f"\nHit Points: {self.current_hp}/{self.max_hp}  Temporary Hit Points: {self.temp_hp}  Hit Dice: {self.current_hd}/{self.hit_dice}"
        string += f"\n\t\t  Death Saves: Saves {self.death_saves_dict['Saves']}  Fails {self.death_saves_dict['Fails']}"
        string += f"\n\nSKILLS"
        string += f"\nAcrobatics (Dex): {format_mod(self.skills_dict['Acrobatics'])}\tAnimal Handling (Wis): {format_mod(self.skills_dict['Animal Handling'])}"
        string += f"\nArcana (Int): {format_mod(self.skills_dict['Arcana'])}\tAthletics (Str): {format_mod(self.skills_dict['Athletics'])}"
        string += f"\nDeception (Cha): {format_mod(self.skills_dict['Deception'])}\tHistory (Int): {format_mod(self.skills_dict['History'])}"
        string += f"\nInsight (Wis): {format_mod(self.skills_dict['Insight'])}\tIntimidation (Cha): {format_mod(self.skills_dict['Intimidation'])}"
        string += f"\nInvestigation: {format_mod(self.skills_dict['Investigation'])}\tMedicine (Wis): {format_mod(self.skills_dict['Medicine'])}"
        string += f"\nNature (Int): {format_mod(self.skills_dict['Nature'])}\tPerception: {format_mod(self.skills_dict['Perception'])}"
        string += f"\nPerformance (Cha): {format_mod(self.skills_dict['Performance'])}\tPersuasion (Cha): {format_mod(self.skills_dict['Persuasion'])}"
        string += f"\nReligion (Int): {format_mod(self.skills_dict['Religion'])}\tSleight of Hand (Dex): {format_mod(self.skills_dict['Sleight of Hand'])}"
        string += f"\nStealth (Dex): {format_mod(self.skills_dict['Stealth'])}\tSurvival (Wis): {format_mod(self.skills_dict['Survival'])}"
        string += f"\n\tPassive Wisdom (Perception): {self.passive_perception}"
        string += f"\n\nOTHER PROFICIENCIES & LANGUAGES"
        string += format_text(f"\n{', '.join(self.languages)}, {', '.join(self.weapon_proficiencies)}, {', '.join(self.armour_proficiencies)}, {', '.join(self.tool_proficiencies)}")
        string += f"\n\nATTACKS & SPELLCASTING"
        for action in self.actions_list:
            string += f"\n{str(action)}"
        string += f"\n\nEQUIPMENT\nCOINS:\t{self.copper} cp\t{self.silver} sp\t{self.electrum} ep\t{self.gold} gp\t{self.platinum} pp"
        string += f"\n{format_text('INVENTORY: ' + ', '.join(self.equipment))}"
        if len(self.items) > 0:
            for item in self.items:
                string += f"\n\n{item}"

        string += f"\n\nPERSONALITY TRAITS"
        for trait in self.personality_traits:
            string += f"\n{format_text('* ' + trait)}"
        string += f"\n\nIDEALS\n{format_text(self.ideals)}"
        string += f"\n\nBONDS\n{format_text(self.bonds)}"
        string += f"\n\nFLAWS\n{format_text(self.flaws)}"

        return string

    
    def get_features(self):
        """Return string of PlayerCharacter's features and traits."""
        string_list = [str(trait) for trait in self.features_traits]
        string = "\n\n".join(string_list)

        return string


    def get_sheet(self, full=False):
        """Return formatted string of character sheet.
        
        Args:
            full (bool): full strings of each feature if false, else just names
        
        Returns:
            string (str): Formatted sting of character sheet"""
        string = ""
        string += self.get_core()
        string += f"\n\nFEATURES & TRAITS\n"
        if full is True:
            string += self.get_features()
        
        else:
            trait_names = []
            for trait in self.features_traits:
                trait_names += [trait.name]
            string += format_text(", ".join(trait_names))

        string += f"\n\nDESCRIPTION\nAge: {self.age}\t\t\tHeight: {self.height}\t\tWeight: {self.weight}\nEyes: {self.eyes}\tSkin: {self.skin}\tHair: {self.hair}"
        string += f"\n\nBACKSTORY\n{self.backstory}"
        string += f"\n\nALLIES & ORGANISATIONS\n{self.allies_organisations}"
        string += f"\n\nTREASURE\n{self.treasure}"

        if self.spell_attack is not None:
            string += f"\n\nSPELLCASTING - {self.character_class.name.upper()}\n{self.get_spellcasting()}"
        
        return string


    def print_sheet(self):
        """Write a txt file of the character sheet and view with less."""
        with open(f"{self.name}.txt", "w") as writer:
            writer.write(self.get_sheet(full=True))
        system(f"less '{self.name}.txt'")


    # Warlock Methods
    def set_invocations(self, chosen_invocations):
        """Set invocations choosing from PlayerClass.features.
        
        Args:
            chosen_invocation (lst): List of strings of chosen invocations"""
        if self.character_class is not warlock:
            pass

        else:
            instances = []
            for trait in self.features_traits:
                if trait.name == "Eldritch Invocations":
                    for sub_string in trait.sub_strings:
                        for invocation in chosen_invocations:
                            if sub_string.name.lower() == invocation.lower():
                                instances.append(sub_string)
                                trait.sub_strings = instances


    def set_pact(self, pact):
        """Set Pact Boon granted by Otherworldly Patron in features_traits.
        
        Args:
            pact (str): String of Pact's name in full"""
        if self.character_class is not warlock:
            pass

        else:
            chosen_pact = []
            for trait in self.features_traits:
                if trait.name.lower() == "Pact Boon".lower():
                    for sub_string in trait.sub_strings:
                        if sub_string.name.lower() == pact.lower():
                            chosen_pact.append(sub_string)
                            trait.sub_strings = chosen_pact


    #Spellcasting Methods
    def add_spells(self, spells, level_rate=None, kind=None):
        """Add given string to spells known in spellcasting Trait.
        
        Args:
            spells (str): String list of spells to be added
            level_rate (str): Spell's level or rate of casting per day
            mind (str): String of type of Trait to which to add spell"""
        if self.character_class is warlock:
            if kind == "innate":
                if level_rate == "at will":
                    self.pact_magic_innate.at_will += spells

                if level_rate == "one day":
                    self.pact_magic_innate.one_day += spells

                if level_rate == "two day":
                    self.pact_magic_innate.two_day += spells

                if level_rate == "three day":
                    self.pact_magic_innate.three_day += spells

            elif kind == "levelled":

                if level_rate == "cantrip":
                    self.pact_magic.cantrips += spells

                else:
                    self.pact_magic.spells += spells
    

    def use_spell_slot(self):
        """Decrement current_spell_slots by by one in given slot.
        
        Args:
            slot (int): level of slot to be decremented default to None
        
        Returns:
            (str): string of current spell slots or no more slots message."""
        if self.character_class is warlock:
            if self.current_spell_slots == 0:
                return "No more spell slots"
            
            else:
                self.current_spell_slots -= 1
                return f"{self.current_spell_slots}/{self.spell_slots}"
    

    def get_spellcasting(self):
        """Return string of spellcasting bonus, save, slots and known spells."""
        if self.character_class is warlock:
            string = f"Spellcasting Ability Charisma   Spell Save DC {self.spell_save}   Spell Attack Bonus {format_mod(self.spell_attack)}\n\n"
            if self.pact_magic_innate.at_will is not None and self.pact_magic_innate.at_will != "":
                string += format_text(f"At will: {self.pact_magic_innate.at_will}\n\n")

            if self.pact_magic_innate.three_day is not None and self.pact_magic_innate.three_day != "":
                string += format_text(f"3/day each: {self.pact_magic_innate.three}\n\n")

            if self.pact_magic_innate.two_day is not None and self.pact_magic_innate.two_day != "":
                string += format_text(f"2/day each: {self.pact_magic_innate.two_day}\n\n")

            if self.pact_magic_innate.one_day is not None and self.pact_magic_innate.one_day != "":
                string += format_text(f"1/day each: {self.pact_magic_innate.one_day}\n\n")
            
            if self.pact_magic.cantrips is not None and self.pact_magic.cantrips != "":
                string += format_text(f"Cantrips (at will): {self.pact_magic.cantrips}\n\n")

            if self.pact_magic.spells is not None and self.pact_magic.spells != "":
                string += format_text(f"1st-{self.slot_level} level ({self.current_spell_slots}/{self.spell_slots} {self.slot_level}-level slots): {self.pact_magic.spells}")

            return string


    #Celestial Methods
    def roll_healing_light(self, num):
        """Return int of roll of given num of d6s and subtract num from pool.
        Args:
            num (int): Number of dice to be rolled and subtracted from pool"""
        if self.archetype is not celestial:
            pass

        else:
            if num >= self.abilities.charisma_mod:
                return f"Over limit Max dice at once {self.abilities.charisma_mod}"

            if self.healing_light_pool[0] - num >= 0:
                self.healing_light_pool[0] -= num
                return roll_string(f"{num}{self.healing_light_pool[1]}")
            
            else:
                return f"Not enough dice left in pool ({self.healing_light_pool[0]}{self.healing_light_pool[1]})"

