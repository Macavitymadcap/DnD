"""A package of functions for rolling various kinds of dice.

The module contains functions that replicate rolling polyhedral dice
(d4, d6, d8, d10, d12, d20, d100). that are used by the roll function to return
rolls of one or more of a type of die.

roll_string is a function that use the dice and roll functions to convert a
string of standard dice notation into rolls. This function is then used to
create functions for; rolling an array of dice; rolling with advantage or
disadvantage; rolling with disadvantage; rolling critical damage and rolling
an array of starting ability scores."""

from random import randint
import re
from typing import Callable

def roll_d(num: int) -> int:
    """Return a random number between 1 and num.
    
    Args:
        num (int): An int for the number of faces on the die
    
    Returns:
        roll (int): Int of the the number rolled."""
    return randint(1, num)

def d4() -> int:
    """Return a random number between 1 and 4."""
    return roll_d(4)


def d6() -> int:
    """Return a random number between 1 and 6."""
    return roll_d(6)


def d8() -> int:
    """Return a random number between 1 and 8."""
    return roll_d(8)


def d10() -> int:
    """Return a random number between 1 and 10."""
    return roll_d(10)


def d12() -> int:
    """Return a random number between 1 and 12."""
    return roll_d(12)


def d20() -> int:
    """Return a random number between 1 and 20."""
    return roll_d(20)


def d100() -> int:
    """Return a random number between 1 and 100."""
    return roll_d(100)


def roll(num: int, die: Callable[[None], int]) -> int:
    """Return a die or dice rolled a number of times.

    Args:
        num (int): The number of dice to roll
        die (func): A function that returns a random number

    Returns:
        roll_total: The combined total of all dice rolls"""
    roll_total = 0

    for i in range(num):
        roll_total += die()

    return roll_total


def roll_string(string: str) -> int:
    """Return a roll of a number of given dice with modifiers.

    Args:
        string (str): A string of a roll of dice with modifiers

    Attributes:
        string (str): The string is parsed for the operator and number of dice

    Returns:
        roll: A number returned from a call to the roll function"""
    # Regex patterns to be searched for in string.
    num_regex = r"\d*\s*"
    die_regex = r"[D|d]\d+"
    operator_regex = r"\s*[+|-|x|X|*|/|÷]\s*"

    # Locate number of dice, type of dice and modifier in string.
    num_dice = re.search(num_regex, string)
    num_dice_stripped = num_dice.group().strip()
    die = re.search(die_regex, string)
    modifier_from_string = string[-2:]
    modifier_no_operator = modifier_from_string.strip(operator_regex)
    modifier_stripped = modifier_no_operator.strip()

    # Return a roll of 1 die with any modifiers.
    if string.lower()[0] == "d":

        if "+" in string:
            return roll(1, eval(die.group().lower())) + int(modifier_stripped)

        elif "-" in string:
            return roll(1, eval(die.group().lower())) - int(modifier_stripped)

        elif "x" in string or "X" in string or "*" in string:
            return roll(1, eval(die.group().lower())) * int(modifier_stripped)

        elif "/" in string or "÷" in string:
            return int(roll(1, eval(die.group().lower())) / int(modifier_stripped))

        else:
            return roll(1, eval(die.group().lower()))

    # Return a roll of multiples of a die with any modifiers.
    else:

        if "+" in string:
            return roll(int(num_dice_stripped),
                        eval(die.group().lower())) + int(modifier_stripped)

        elif "-" in string:
            return roll(int(num_dice_stripped),
                        eval(die.group().lower())) - int(modifier_stripped)

        elif "x" in string or "X" in string or "*" in string:
            return roll(int(num_dice_stripped),
                        eval(die.group().lower())) * int(modifier_stripped)

        elif "/" in string or "÷" in string:
            return int(roll(int(num_dice_stripped),
                            eval(die.group().lower())) / int(modifier_stripped))

        else:
            return roll(int(num_dice_stripped), eval(die.group().lower()))


def roll_crit(dice: str, modifier: str = None) -> int:
    """Return a roll of doubled dice with modifiers.

    Args:
        dice (str): A string of a number of dice
        modifier (str): A string of an operator (+|-) and number
    
    Attributes:
        roll (int): Int of total dice rolled

    Returns:
        roll_string: A roll of double dice"""
    roll = 0
    if modifier is None:
        return roll_string(dice)

    elif modifier[0] == "+":
        for i in range(2):
            roll += roll_string(dice)

        return roll + int(modifier[1:])

    else:
        for i in range(2):
            roll += roll_string(dice)
            
        return roll - int(modifier[1:])


def roll_advantage(string: str) -> list[int]:
    """Return two calls to roll_string sorted highest to lowest.

    Args:
        string (str): A string of a roll of a number of dice with modifiers

    Returns:
        roll_list: A list of rolls sorted from highest [0] to lowest [1]"""
    roll_list = [roll_string(string) for i in range(2)]

    roll_list.sort(reverse=True)

    return roll_list


def roll_disadvantage(string: str) -> list[int]:
    """Return call to roll_advantage sorted lowest to highest.

    Args:
        string (str): A string of a roll of a number of dice with modifiers

    Returns:
        roll_list: A list of rolls sorted from lowest [0] to highest [1]"""
    roll_list = [roll_string(string) for i in range(2)]
    roll_list.sort()

    return roll_list


def roll_array(string: str) -> list[int]:
    """Return an array of a number of die rolls with modifiers.

    Args:
        string (str): A string of die with modifers to be rolled a number of times 

    Returns:
        rolls: An array of rolls"""
    d_index = string.index("d")
    num_dice = int(string[0:d_index])
    die_roll = string[d_index:]
    rolls = [roll_string(die_roll) for i in range(num_dice)]

    return rolls


def roll_ability_scores() -> list[int]:
    """Return a list of 6 4d6 minus the lowest for each group.

    Attributes:
        ability_die(func): Returns the total of 4d6 minus the lowest die

    Returns:
        abilities: An array of 6 calls to ability_die sorted highest to lowest"""

    def ability_die() -> int:
        ability = 0
        four_d6 = roll_array("4d6")
        four_d6.sort()
        four_d6.pop(0)

        for die_roll in four_d6:
            ability += die_roll

        return ability

    abilities = [ability_die() for i in range(6)]
    abilities.sort(reverse=True)

    return abilities
