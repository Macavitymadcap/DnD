"""A package of functions for rolling dice and tables. 

The package consists of two modules; dice and roll_table. The first 
contains functions for rolling polyhedral dice in various ways. The second
contains functions for rolling on tables rendered as DataFrames.

Functions:
    art_object: Return a roll on an art objects table of a given value
    check_range: Return True if num in string, False if not
    d4: Return a random number between 1 and 4
    d6: Return a random number between 1 and 6
    d8: Return a random number between 1 and 8
    d10: Return a random number between 1 and 10
    d12: Return a random number between 1 and 12
    d20: Return a random number between 1 and 20
    d100: Return a random number between 1 and 100
    gemstone: Return a roll on a gemstone table of a given value
    hoard_tier1: Return roll on Treasure Hoard: Challenge 0-4
    hoard_tier2: Return roll on Treasure Hoard: Challenge 5-10
    hoard_tier3: Return roll on Treasure Hoard: Challenge 11-17
    hoard_tier4: Return roll on Treasure Hoard: Challenge 17+
    magic_item: Return a magic item table rolled from a given table
    name: Return string of name rolled on names_df for given kind and option
    roll: Return a die or dice rolled a number of times
    roll_ability_scores: Return a list of 6 4d6 minus the lowest for each group
    roll_advantage: Return two calls to roll_string sorted highest to lowest
    roll_array: Return an array of a number of die rolls with modifiers
    roll_crit: Return a roll of doubled dice with modifiers
    roll_disadvantage: Return call to roll_advantage sorted lowest to highest
    roll_range: Return roll on given dataframe column
    roll_string: Return a roll of a number of given dice with modifiers
    treasure_tier1: Return roll on Individual Treasure: Challenge 0-4
    treasure_tier2: Return roll on Individual Treasure: Challenge 7-10
    treasure_tier3: Return roll on Individual Treasure: Challenge 11-16
    treasure_tier4: Return roll on Individual Treasure: Challenge 17+
"""

from DiceBox.dice import d4
from DiceBox.dice import d6
from DiceBox.dice import d8
from DiceBox.dice import d10
from DiceBox.dice import d12
from DiceBox.dice import d20
from DiceBox.dice import d100
from DiceBox.dice import roll
from DiceBox.dice import roll_ability_scores
from DiceBox.dice import roll_advantage
from DiceBox.dice import roll_array
from DiceBox.dice import roll_crit
from DiceBox.dice import roll_disadvantage
from DiceBox.dice import roll_string
from DiceBox.roll_table import art_object
from DiceBox.roll_table import check_range
from DiceBox.roll_table import gemstone
from DiceBox.roll_table import hoard_tier1
from DiceBox.roll_table import hoard_tier2
from DiceBox.roll_table import hoard_tier3
from DiceBox.roll_table import hoard_tier4
from DiceBox.roll_table import magic_item
from DiceBox.roll_table import name
from DiceBox.roll_table import roll_range
from DiceBox.roll_table import treasure_tier1
from DiceBox.roll_table import treasure_tier2
from DiceBox.roll_table import treasure_tier3
from DiceBox.roll_table import treasure_tier4
from DiceBox.roll_table import wild_magic
