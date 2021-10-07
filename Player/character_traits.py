from copy import deepcopy

from Data import backgrounds_bonds
from Data import backgrounds_flaws
from Data import backgrounds_ideals
from Data import backgrounds_personality_traits
from DiceBox import d6
from DiceBox import d8
from DiceBox import roll_string
from Utilities import format_text


class Background:
    """Class returns a background object with rollable traits.
    
    The class takes arguments to set up its features, proficiencies and traits
    and retrieves personality traits, bonds, flaws and ideals from a DataFrame.
    """

    def __init__(self, name, skills, tools, languages, equipment, features):
        """Initialise the Background instance.
        
        Args:
            name (str): String of the background's name
            skills (str): String listing the background's 2 skill proficiencies
            tools (str): String listing the background's tool proficiencies
            languages (str): String listing the background's known languages
            equipment (str): String listing the background's starting equipment
            features (lst) List of Trait instance for the background's features
            
        Attributes:
            personality_trait (DataFrame): Table of suggested personality traits
            ideal (DataFrame): Table of suggested ideals
            bond (DataFrame) Table of suggested bonds
            flaw (DataFrame) Table of suggested flaws"""

        self.name = name
        self.skills = skills
        self.tools = tools
        self.languages = languages
        self.equipment = equipment
        self.features = features
        self.personality_trait = deepcopy(backgrounds_personality_traits[[self.name]])
        self.personality_trait.rename(columns={self.name: "Personality Trait" }, inplace=True)
        self.ideal = deepcopy(backgrounds_ideals[[self.name]])
        self.ideal.rename(columns={self.name: "Ideal"}, inplace=True)
        self.bond = deepcopy(backgrounds_bonds[[self.name]])
        self.bond.rename(columns={self.name: "Bond"}, inplace=True)
        self.flaw = deepcopy(backgrounds_flaws[[self.name]])
        self.flaw.rename(columns={self.name: "Flaw"}, inplace=True)


    def __str__(self):
        """Return formatted string of the Background instance."""
        string = f"{self.name}\nSkill Proficiencies: {self.skills}\n"

        if self.tools is not None:
            string += f"Tool Proficiencies: {self.tools}\n"

        if self.languages is not None:
            string += f"Laguages: {self.languages}\n"
            
        string += f"{format_text('Equipment: ' + self.equipment)}\n\n"
        
        for feature in self.features:
            string += str(feature) + "\n"
        
        string += f"\n{self.personality_trait}\n"
        string += f"{self.ideal}\n"
        string += f"{self.bond}\n"
        string += f"{self.flaw}\n"

        return string


    def roll_trait(self):
        """Return string of a roll on the background's personality trait table."""
        return format_text(self.personality_trait.at[d8(), self.name])


    def roll_ideal(self):
        """Return a string of a roll of the background's ideal table."""
        return format_text(self.ideal.at[d6(), self.name])
    

    def roll_bond(self):
        """Return string of a roll on the background's ideal table."""
        return format_text(self.bond.at[d6(), self.name])

    
    def roll_flaw(self):
        """Return a string of a roll on the background's flaw table."""
        return format_text(self.flaw.at[d6(), self.name])


class CharacterFeature:
    """Class returns an object representing a feature from a class.
    
    The class's level attribute allows for each CharacterFeature instance to be
    Checked againt a PlayerCharacter's level attribute to determine whether
    it is included in the PlayerCharacter's listed traits and features."""

    def __init__(self, name, text, sub_strings=None, level=None,
                 table=None, prerequisite=None):
        """Initialise the CharacterFeature instance.
        
        For features with multiple sub-features, store sub-features as
        as a list of CharacterFeature instances in the sub_string argument.

        Args:
            name (str): String of the class feature's name
            text (str): String describing the rules and traits of the feature
            sub_strings (lst): List of CharacterFeature instaces
            level (int): Number for the level at which the feature is received
            table (DataFrame): Table for any table attached to the feature
            prerequisite (str): String of prerequisite for feature"""
        self.name = name
        self.text = text
        self.sub_strings = sub_strings
        self.level = level
        self.table = table
        self.prerequisite = prerequisite


    def __str__(self):
        """Return a formatted string of the CharacterFeature instance."""
        string = f"{self.name.upper()}\n"
        if self.prerequisite is not None:
            if self.prerequisite[-5:] == "level":
                string += f"Prerequisite: {self.level}{self.prerequisite}\n"
            
            else:
                if self.level is not None: 
                    string += f"Prerequisite: {self.level}{self.prerequisite}\n"
                
                else:
                    string += f"Prerequisite: {self.prerequisite}\n"

        string += f"{format_text(self.text)}"
        string += f"\n{self.table}" if self.table is not None else ""
        
        if self.sub_strings is not None:
            for sub_string in self.sub_strings:
                string += str("\n\n" + str(sub_string))
        
        return string


#Race - Class containing strings of all features for a given race and subrace
class Race:
    """Class for and object representing a race with rollable height/weight.
    
    The class takes a race or subrace as a whole object and provides a method
    for a rolling a random height and weight."""

    def __init__(self, name, ability_increase, age, alignment, size, speed, 
                 languages, language_list, base_height, height_modifier, 
                 base_weight, weight_modifer, traits=None, skills=None, 
                 armour=None, weapons=None, tools=None):
        """Initialise the Race instance.
        
        Args:
            name (str): String of the race's name, with subrace in brackets
            ability_increase (str): String of race's the ability score increase
            age (str): String outlining typical lifespan of the race
            alignment (str): String outling the race's typical alignment
            size (str): String indicating the average size of the race
            speed (str): String of the race's average speed
            languages (str): String outling the race's language
            base_height (str): String for race's base height in feet and inches
            height_modifier (str): String of die roll to adjust height
            base_weight (str): String for race's base weight in pounds
            weight_modifer (str): string of die roll ro adjust weight
            traits (lst): List of CharacterFeature instances for race's traits
            skills
            armour
            weapons
            tools
            language_list"""
        self.name = name
        self.ability_increase = ability_increase
        self.age = age
        self.alignment = alignment
        self.size = size
        self.speed = speed
        self.languages = languages
        self.language_list = language_list
        self.base_height = base_height
        self.height_modifier = height_modifier
        self.base_weight = base_weight
        self.weight_modifier = weight_modifer
        self.traits = traits
        self.skills = skills
        self.armour = armour
        self.weapons = weapons
        self.tools = tools

  
    def roll_height_weight(self):
        """Return string of random height and weight for instance of race.
        
        The method makes use of an inner method, weight_roll, to handle Race
        Instances like halfling and gb=nome that do not have a die roll as 
        their weight_modifier."""
        feet = int(self.base_height[0])
        inches = int(self.base_height[2:])
        height_roll = roll_string(self.height_modifier)
        weight = int(self.base_weight)

        def weight_roll():
            """Return int based on die roll or number in weight_modifer"""
            try:
                weight_roll = roll_string(self.weight_modifer)

            except:
                weight_roll = int(self.weight_modifier)
            
            return weight_roll

        height_div = divmod(height_roll, 12)
        new_feet = feet + height_div[0]
        new_inches = inches + height_div[1]

        if new_inches > 12:
            new_inches -= 12
            new_feet += 1

        new_height = f"{new_feet}'{new_inches}\""
        new_weight = (height_roll * weight_roll()) + weight

        return f"Height {new_height}, Weight {new_weight} lb."


    def __str__(self):
        """Return a formatted string of the race's traits and features."""
        stringa = f"\n{self.name}\nAbility Score Increase. {self.ability_increase}"
        stringb = f"\n{format_text('Age. ' + self.age)}\n"
        stringc = f"{format_text('Alignment. ' + self.alignment)}\n"
        stringd = f"{format_text('Size. ' + self.size)}\n"
        stringe = f"Speed. Your base walking speed is {self.speed}"

        if self.traits is not None:
            for trait in self.traits:
                stringa += f"\n{trait}"

        stringf = f"\n{format_text('Languages' + self.languages)}"
        stringg = "\nBase Height\tHeight Modifier\tBase Weight\tWeight Modifier"
        stringh = f"\n{self.base_height}\t\t+{self.height_modifier}\t\t{self.base_weight} lb.\t\tx ({self.weight_modifier}) lb."
        
        return stringa + stringb + stringc + stringd + stringe + stringf + stringg +stringh


class CharacterClass:
    """A class containing all the attributes of a character class."""
    def __init__(self, name, table, hit_dice, hp_1st_level, hp_higher_levels, armour, 
                 weapons, tools, saving_throws, skills, equipment, starting_wealth, 
                 multiclass, features, archetypes, die_pool, resource):
        """Initialise the CharacterClass instance.

        Args:
            name (str): String of the class's name
            table (DataFrame): Table of the class's features by level
            hit_dice (str): String of the class's hit die
            hp_1st_level (str): String of class's total hit points at level 1
            hp_higher_levels (str): String of class's hit points level 2 and up
            armour (str): String of the class's armour proficiencies (if any)
            weapons (str): String of the class's weapon proficiencies
            tools (str): String of the class's tool proficiencies (if any)
            saving_throws (str): String for class's saving throw proficiencies
            skills (str): String of the skill proficiencies available to class
            equipment (lst): List of strings of class's starting equipment
            starting_wealth (str): String die roll for class's starting wealth
            multiclass (dict): Dictionary of multiclassing rules for class
            features (lst): List of CharacterFeature instances for class' features
            archetypes (lst): List of Archetype instances for the class
        
        Attributes:"""
        self.name = name
        self.table = table
        self.hit_dice = hit_dice
        self.hp_1st_level = hp_1st_level
        self.hp_higher_levels = hp_higher_levels
        self.armour = armour
        self.weapons = weapons
        self.tools = tools
        self.saving_throws = saving_throws
        self.skills = skills
        self.equipment = equipment
        self.starting_wealth = starting_wealth
        self.multiclass = multiclass
        self.features = features
        self.archetypes = archetypes
        self.die_pool = die_pool
        self.resource = resource

    
    def __str__(self):
        """Return formatted string of class features."""
        string = f"{self.name.upper()}\n"
        string += str(self.table) + "\n\n"
        string += f"As a {self.name.lower()}, you gain the following class features.\n"
        string += f"Hit Dice: {self.hit_dice} per {self.name.lower()} level\nHit Points at 1st Level: {self.hp_1st_level}\n"
        string += format_text(f"Hit Points at Higher Levels: {self.hp_higher_levels}") + "\n"
        string += f"\nPROFICIENCIES\nArmour: {self.armour}\n"
        string += format_text(f"Weapons: {self.weapons}") + "\n"
        string += format_text(f"Tools: {self.tools}") + "\n"
        string += f"\nSaving Throws: {self.saving_throws}\n"
        string += format_text(f"Skills: {self.skills}") + "\n"
        string += "\nEQUIPMENT\n"
        string += format_text("You start with the following equipment, in addition to the equipment granted by your background:") +"\n"
        
        for choice in self.equipment:
        
            string += format_text("\n* " + choice)
        
        string += "\n"
        string += f"\nMULTICLASSING\nWhen you gain a level in a class other than your first, you gain only some of that class's starting proficiencies.\n"
        
        for key, value in self.multiclass.items():

            string+= format_text(f"\n{key}: {value}")

        for feature in self.features:

            string += "\n\n" + str(feature)
        
        return string


class Archetype:
    """Class containing features of a class's archetype."""

    def __init__(self, name, character_class, armour, weapons, tools, 
                 skills, features, dice_pool=None):
        """Initialise the Archetype instance.
        
        Args:
            name (str): String of the archetype's name
            character_class (str): String of the class the archetype is from
            armour (str): String of the archetype's armour proficiencies
            weapons (str): String of the archetype's weapon proficiencies
            tools (str): String of the archetype's tool proficiencies
            skills (str): String of the archetype's skill proficiencies
            features (lst): List of CharacterFeature instances
            dice_pool (dict): Dictionary of values for archetype's dice pool
        """
        self.name = name
        self.character_class = character_class
        self.armour = armour
        self.weapons = weapons
        self.tools = tools
        self.skills = skills
        self.features = features
        self.dice_pool = dice_pool

    
    def __str__(self):
        """Return string of the Archetype's features"""
        string = ""

        for feature in self.features:

            string += "\n" + str(feature) + "\n" 

        return string
