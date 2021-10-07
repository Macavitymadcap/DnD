
"""Classes and functions for goods, items and other equipment.

The module has one function coinverter which is used to convert a value
from one type of coin into another.

The module contains four classes; Gear; Tool; Armour and Weapon. The first
is Gear,the base object from which all subsequent item classes inherit. 
The second, Tool, is used to represent tools. The third class Armour is used to 
represent armour and shields. The last, Weapon, is used to represent weapons."""
from copy import deepcopy

from Data import exchange_rates_df
from Utilities import format_text


class Gear:
    """Class returns an object representing an item.

    This class is the base from which all other item class inherit 
    attributes and methods.

    Attributes:
        equipment (set): Set of all instances of the Gear class
        name (str): String of the item's name
        cost (str): String of the item's value in gp or other coins
        weight (str): String of the item's weight in pounds
        description (str): String describing the item, default=None"""

    def __init__(self, name, cost, weight, description=None):
        """Inititalise the Gear instance.

        Args:
            name (str): String of the item's name
            cost (str): String of the item's value in gp or other coins
            weight (str): String of the item's weight in pounds
            description (str): String describing the item, default=None"""
        self.name = name
        self.cost = cost
        self.weight = weight
        self.description = description

    def __repr__(self):
        """Return a string representing the Gear instance."""
        return f'Gear("{self.name}", "{self.cost}", "{self.weight}", "{self.description}")'

    def __str__(self):
        """Return a formatted string for user-level representation."""
        string = f"{self.name}. {self.cost}, {self.weight}"
        if self.description == None:
            return string
        else:
            return f"{string}, {self.description}"


class Tool(Gear):
    """Class returns an object representing a tool.

    Attributes:
        name (str): String of the tool's name
        cost (str): String of the tool's value in gp or other coins
        weight (str): String of the tool's weight in pounds
        description (str): String describing the tool, default=None
        type (str): String identifying the kind of tool this instance is
        components (str) String listing the components of the tool
        skills (str) String listing skills that benefit from tool proficiency
        check_DCs (str): String of typical ability check DCs for using tool"""

    def __init__(self, name, cost, weight, description, type, components, skills, special, check_DCs):
        """Initialise the Tool instance.

        Args:
            name (str): String of the tool's name
            cost (str): String of the tool's value in gp or other coins
            weight (str): String of the tool's weight in pounds
            description (str): String describing the tool, default=None
            type (str): String identifying the kind of tool this instance is
            components (str) String listing the components of the tool
            skills (str) String listing skills that benefit from tool proficiency
            check_DCs (str): String of typical ability check DCs for using tool"""

        super().__init__(name, cost, weight, description)
        self.type = type
        self.components = components
        self.skills = skills
        self.special = special
        self.check_DCs = check_DCs

    def __repr__(self):
        """Return a string representing the Tool instance."""
        return f"Tool('{self.name}', '{self.cost}', '{self.weight}', '{self.description}', '{self.type}', '{self.components}', '{self.skills}', '{self.special}', '{self.check_DCs}')"

    def __str__(self):
        """Return a formatted string of the Tool instance for user-level."""
        stringa = f"{self.name}\n{self.cost}, {self.weight}\n"
        if self.components is not None:
            stringa += f"Components. {self.components}\n{self.skills}\n"

        if self.special is not None:
            stringa += self.special + "\n"

        checks = self.check_DCs.split(", ")
        check_string = ""
        for check in checks:
            check_string += check + "\n"
        stringb = f"Ability Check DCs:\n{check_string}"

        return stringa + stringb


class Armour(Gear):
    """Class returns an object representing a piece of armour or shield.

    Attributes:
        name (str): String of the armour's name
        cost (str): String of the armour's value in gp or other coins
        weight (str): String of the arour's weight in pounds
        type (str): String signifying the armour's kind, use to create don/doff
        armour_class (str): A string of the armour's bonus to armour class
        strength (str): A string noting the instance's strength requirements
        stealth (str): A string noting the instance's stealth penalties
        don (str): String detailing the time taken to put on the instance
        doff (str): String detailing the time taken to take off the instance"""

    def __init__(self, name, cost, weight, type, armour_class, strength, stealth):
        """Initialise the Armour instance.

        Args:
            name (str): String of the armour's name
            cost (str): String of the armour's value in gp or other coins
            weight (str): String of the arour's weight in pounds
            type (str): String signifying the armour's kind, use to create don/doff
            armour_class (str): A string of the armour's bonus to armour class
            strength (str): A string of the instance's strength requirements
            stealth (str): A string of the instance's stealth penalties

        Attributes:
            don (str): String of the time taken to put on the instance
            doff (str): String of the time taken to take off the instance"""

        super().__init__(name, cost, weight)
        self.type = type
        self.armour_class = armour_class
        self.strength = strength
        self.stealth = stealth

        if self.type == "Light":
            self.don = "1 minute"
            self.doff = "1 minute"

        elif self.type == "Medium":
            self.don = "5 minutes"
            self.doff = "1 minute"

        elif self.type == "Heavy":
            self.don = "10 minutes"
            self.doff = "5 minutes"

        else:
            self.don = "1 action"
            self.don = "1 action"

    def __repr__(self):
        """Return a string representing the Armour instance."""
        return f"Armour('{self.name}', '{self.cost}', '{self.weight}', '{self.type}', '{self.armour_class}', '{self.strength}', '{self.stealth}')"

    def __str__(self):
        """Return a formatted string of the Armour instance for user-level."""
        string = f"{self.name}. {self.type}, {self.cost}, {self.armour_class}, {self.strength}, {self.stealth}, {self.weight}"
        return string


class Weapon(Gear):
    """Class returns an object representing a weapon.

    Attributes:
        name (str): String of the weapon's name
        cost (str): String of the weapon's value in gp or other coins
        weight (str): String of the weapon's weight in pounds
        description (str): String describing the weapon, default=None
        type (str): String signifying the kind of weapon it is
        damage_die (str): String of the damage die or number dealt by weapon
        damage_type (str): String of the weapon's kind of damage 
        range (str): String for range of weapon if any"""

    def __init__(self, name, cost, weight, description, type, damage_die,
                 damage_type, range):
        """Initialise the Weapon instance.

        Args:
            name (str): String of the weapon's name
            cost (str): String of the weapon's value in gp or other coins
            weight (str): String of the weapon's weight in pounds
            description (str): String describing the weapon, default=None
            type (str): String signifying the kind of weapon it is
            damage_die (str): String of the damage die or number dealt by weapon
            damage_type (str): String of the weapon's kind of damage 
            range (str): String for range of weapon if any"""

        super().__init__(name, cost, weight, description)
        self.type = type
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.range = range

    def __repr__(self):
        """Return a string representing the Weapon instance."""
        return f"Weapon('{self.name}', '{self.cost}', '{self.weight}', '{self.description}', '{self.type}', '{self.damage_die}', '{self.damage_type}', '{self.range}')"

    def __str__(self):
        """Return a formatted string of the Weapon instance for user-level."""
        stringa = f"{self.name}. {self.type}, {self.cost}, {self.damage_die} {self.damage_type}"
        if self.range is None:
            return f"{stringa}, {self.description}"
        else:
            return f"{stringa}, {self.range}, {self.description}"


class MagicItem(Gear):
    """An object representing a magic item."""

    def __init__(self, name, weight, description, kind, rarity,
                attunement=None, charges=None, regain=None,
                armour=None, weapon=None, modifier=None):
        """Initialise the MagicItem instance.

        Args:
            name (str)
            weight (str)
            description (str)
            kind (str)
            rarity (str)
            attunement (str)
            charges (int)
            regain (str)
            armour (obj)
            weapon (obj)
            modifier (int)"""
        super().__init__(name, weight, description)
        self.kind = kind
        self.rarity = rarity
        self.description = description
        self.attunement = attunement
        self.charges = charges
        self.current_charges = deepcopy(self.charges)
        self.regain = regain
        self.armour = armour
        self.weapon = weapon
        self.modifier = modifier

    def __str__(self):
        string = f"{self.name.upper()}\n"
        string += f"{self.kind.capitalize()}, {self.rarity}"
        if self.attunement is not None:
            string += f" ({self.attunement})"

        if self.armour is not None:
            string += f"\n{self.armour.weight}, AC {self.armour.armour_class}"

        if self.weapon is not None:
            string += f"\n{self.weapon.weight}, {self.weapon.damage_die} {self.weapon.damage_type}"

            if self.weapon.range is not None:
                string += f", {self.weapon.range}"

            if self.weapon.description is not None:
                string += f", {self.weapon.description}"

        string += f"\n{self.description}"

        return format_text(string)


    def use_charges(self, num):
        """Decrement current_charges attribute by given number.
        
        Args:
            num (int): Number by which to decrease current_charges"""
        if self.current_charges - num < 0:
            pass

        else:
            self.current_charges -= num


    def add_charges(self, num):
        """Increment current_charges attribute by given number.
        
        Args:
            num (int): Number to increment current charges by, up to charges"""
        if self.current_charges + num > self.charges:
            self.current_charges = deepcopy(self.charges)
        
        else:
            self.current_charges += num


def coinverter(amount, from_unit, to_unit):
    """Return a string of coin value converted into another coin value.

    Args:
        amount (int): Number to be converted from one unit to another
        from_unit (str): String of the base coin type
        to_unit (str): String of the target coin type

    Attributes:
        multiplier (int): Number derived from exchange_rates_df
        value (int): Value of target coins as int or float

    Returns:
        value: Int or float of target coins"""
    multiplier = exchange_rates_df.loc[from_unit, to_unit]
    value = amount * multiplier
    return value
