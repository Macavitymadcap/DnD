"""A module of functions for rolling on tables.

The module has functions that can verifiy if a number is a string of a range
and then roll on a given dataframe. These functions are then used to roll for 
art objects; gemstones; individual treasure; magic items; names and 
treasure hoards.
"""

from Data import art_objects_25gp
from Data import art_objects_250gp
from Data import art_objects_750gp
from Data import art_objects_2500gp
from Data import art_objects_7500gp
from Data import gemstones_10gp
from Data import gemstones_50gp
from Data import gemstones_100gp
from Data import gemstones_500gp
from Data import gemstones_1000gp
from Data import gemstones_5000gp
from Data import magic_items_a
from Data import magic_items_armour
from Data import magic_items_b
from Data import magic_items_c
from Data import magic_items_d
from Data import magic_items_e
from Data import magic_items_f
from Data import magic_items_figurines
from Data import magic_items_g
from Data import magic_items_h
from Data import magic_items_i
from Data import names_df
from Data
from DiceBox.dice import d4
from DiceBox.dice import d6
from DiceBox.dice import d8
from DiceBox.dice import d10
from DiceBox.dice import d12
from DiceBox.dice import d100
from DiceBox.dice import roll

def check_range(num, string):
    """Return True if num in string, False if not.

    Args:
        num (int): Number to be checked if in range
        string (str): String converted into range

    Attributes:
        get_range (func): Return a range from a given string
        check_num (func): Return True if num in range, False if not

    Returns:
        check_num(num, get_range(string)): True if num in String, False if not
    """

    def get_range(string):
        """Return a range from a given string.

        Args:
            string (str): String to be converted into a range object

        Returns:
            to_range: Range object from given string
        """
        hyphen = string.index("-")
        num1 = int(string[:hyphen])
        num2 = int(string[hyphen + 1:])
        to_range = range(num1, num2 + 1)

        return to_range

    def check_num(num, range):
        """Return True if num in range, False if not.

        Args:
            num (int): Number to be checked against given range
            range(func): Range object in which to serach for num

        Returns:
            bool: True if num in range, False if not
        """
        for i in range:

            if i is num:
                return True

        else:
            return False

    return check_num(num, get_range(string))


def roll_range(dataframe, die_roll, column):
    """Return roll on given dataframe column.

    Args:
        dataframe (DataFrame): Table of rollable strings
        die_roll (func): Roll of dice to be checked against the datafram's index
        column (str): String repsresenting the column to be returned

    Returns:
        dataframe.at[index, column]: String of roll on given table
    """
    for index in dataframe.index:

        if '-' in index:

            if check_range(die_roll, index):
                return dataframe.at[index, column]

        else:
            return dataframe.at[index, column]

def wild_magic():
    """"Return a roll on wild magic surge table."""
    
    return roll_range()

def art_object(value):
    """Return a roll on an art objects table of a given value.

    Args:
        value (int): Number representing gold value of returned object

    Returns:
        string: String of roll on art object table of given value
    """

    if value == 25:
        return art_objects_25gp.at[d10(), 'Object']

    elif value == 250:
        return art_objects_250gp.at[d10(), 'Object']

    elif value == 750:
        return art_objects_750gp.at[d10(), 'Object']

    elif value == 2500:
        return art_objects_2500gp.at[d10(), 'Object']

    elif value == 7500:
        return art_objects_7500gp.at[d8(), 'Object']


def gemstone(value):
    """Return a roll on a gemstone table of a given value.

    Args:
        value (int): Number representing gold value of returned gemstone

    Returns:
        string: String of roll on gemstone table of given value
    """

    if value == 10:
        return gemstones_10gp.at[d12(), 'Stone Description']

    elif value == 50:
        return gemstones_50gp.at[d12(), 'Stone Description']

    elif value == 100:
        return gemstones_100gp.at[d10(), 'Stone Description']

    elif value == 500:
        return gemstones_500gp.at[d6(), 'Stone Description']

    elif value == 1000:
        return gemstones_1000gp.at[d8(), 'Stone Description']

    elif value == 5000:
        return gemstones_5000gp.at[d4(), 'Stone Description']


def magic_item(table):
    """Return a magic item table rolled from a given table.

    Args:
        table (str): Letter for table from which the returned string is rolled

    Returns:
        string: String of roll on given magice item table
    """

    if table == 'a':
        return roll_range(magic_items_a, d100(), 'Magic Item')

    elif table == 'b':
        return roll_range(magic_items_b, d100(), 'Magic Item')

    elif table == 'c':
        return roll_range(magic_items_c, d100(), 'Magic Item')

    elif table == 'd':
        return roll_range(magic_items_d, d100(), 'Magic Item')

    elif table == 'e':
        return roll_range(magic_items_e, d100(), 'Magic Item')

    elif table == 'f':
        return roll_range(magic_items_f, d100(), 'Magic Item')

    elif table == 'g':
        roll_g = d100()
        if roll_g in range(12, 15):
            return roll_range(magic_items_figurines, d8(), 'Figurine of Wondrous Power')

        else:
            return roll_range(magic_items_g, roll_g, 'Magic Item')

    elif table == 'h':
        return roll_range(magic_items_h, d100(), 'Magic Item')

    elif table == 'i':
        roll_i = d100()
        if roll_i == 76:
            return roll_range(magic_items_armour, d12(), 'Magic Armour')

        else:
            return roll_range(magic_items_i, roll_i, 'Magic Item')


def treasure_tier1():
    """Return roll on Individual Treasure: Challenge 0-4.

    Attributes:
        coin_roll (int): Number between 1 and 100 checked against table ranges

    Returns:
        string: String of total money from roll on Individual Treasure: Challenge 0-4
    """
    coin_roll = d100()

    if coin_roll in range(1, 31):
        return f"{roll(5, d6)} cp"

    elif coin_roll in range(31, 61):
        return f"{roll(4, d6)} sp"

    elif coin_roll in range(61, 71):
        return f"{roll(3, d6)} ep"

    elif coin_roll in range(71, 96):
        return f"{roll(3, d6)} gp"

    else:
        return f"{d6()} pp"


def treasure_tier2():
    """Return roll on Individual Treasure: Challenge 7-10.

    Attributes:
        coin_roll (int): Number between 1 and 100 checked against table ranges

    Returns:
        string: String of total money from roll on Individual Treasure: Challenge 5-10
    """
    coin_roll = d100()

    if coin_roll in range(1, 31):
        return f"{roll(4, d6) * 100} cp, {d6() * 10} ep"

    elif coin_roll in range(31, 61):
        return f"{roll(6, d6) * 10} sp, {roll(2, d6) * 10} gp"

    elif coin_roll in range(61, 71):
        return f"{roll(3, d6) * 10} ep, {roll(2, d6) * 10} gp"

    elif coin_roll in range(71, 96):
        return f"{roll(4, d6) * 10} gp, {d6() * 10} pp"

    else:
        return f"{roll(2, d6) * 10} gp, {roll(3, d6)} pp"


def treasure_tier3():
    """Return roll on Individual Treasure: Challenge 11-16.

    Attributes:
        coin_roll (int): Number between 1 and 100 checked against table ranges

    Returns:
        string: String of total money from roll on Individual Treasure: Challenge 11-16
    """
    coin_roll = d100()

    if coin_roll in range(1, 21):
        return f"{roll(4, d6) * 100} sp, {d6() * 100} gp"

    elif coin_roll in range(21, 36):
        return f"{d6() * 100} ep, {d6() * 100} gp"

    elif coin_roll in range(36, 76):
        return f"{roll(2, d6) * 100} gp, {d6() * 10} pp"

    else:
        return f"{roll(2, d6) * 100} gp, {roll(2, d6) * 10} pp"


def treasure_tier4():
    """Return roll on Individual Treasure: Challenge 17+.

    Attributes:
        coin_roll (int): Number between 1 and 100 checked against table ranges

    Returns:
        string: String of total money from roll on Individual Treasure: Challenge 17+
    """
    coin_roll = d100()

    if coin_roll in range(1, 16):
        return f"{roll(2, d6) * 1000} ep, {roll(8, d6) * 100} gp"

    elif coin_roll in range(16, 56):
        return f"{d6() * 1000} gp, {d6() * 100} pp"

    else:
        return f"{d6() * 1000} gp, {roll(2, d6) * 100} pp"


def hoard_tier1():
    """Return roll on Treasure Hoard: Challenge 0-4.

    Attributes:
        hoard_roll (int): Number between 1 and 100 checked against table ranges
        copper (int): Number of total copper pieces
        silver (int): Number of total silver pieces
        gold (int): Number of total gold pieces
        coins (str): String of total money rolled for hoard
        gems_10 (lst): List of strings of 10 gp gemstones
        gems_50 (lst): List of strings of 50 gp gemstones
        art_25 (lst): List of strings of 25 gp art objects
        magic_items_a (lst): List of strings from magic items table a
        magic_items_b (lst): List of strings from magic items table b
        magic_items_c (lst): List of strings from magic items table c
        magic_items_f (lst): List of strings from magic items table a
        magic_items_g (str): String from magic items table g

    Returns:
        string: String of total treasure from roll on Treasure Hoard: Challenge 0-4
    """
    hoard_roll = d100()
    copper = roll(6, d6) * 100
    silver = roll(3, d6) * 100
    gold = roll(2, d6) * 10
    coins = f"{copper}cp, {silver}sp and {gold}gp"
    gems_10 = [gemstone(10) for i in range(roll(2, d6))]
    gems_50 = [gemstone(50) for i in range(roll(2, d6))]
    art_25 = [art_object(25) for i in range(roll(2, d4))]
    magic_items_a = [magic_item('a') for i in range(d6())]
    magic_items_b = [magic_item('b') for i in range(d4())]
    magic_items_c = [magic_item('c') for i in range(d4())]
    magic_items_f = [magic_item('f') for i in range(d4())]
    magic_items_g = magic_item('g')

    if hoard_roll in range(1, 7):
        return f"Coins: {coins}"

    elif hoard_roll in range(7, 17):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_10)}"

    elif hoard_roll in range(17, 27):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}"

    elif hoard_roll in range(27, 37):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_50)}"

    elif hoard_roll in range(37, 45):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_10)}\nMagic Items: {', '.join(magic_items_a)}"

    elif hoard_roll in range(45, 53):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_a)}"

    elif hoard_roll in range(53, 61):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_a)}"

    elif hoard_roll in range(61, 66):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_10)}\nMagic Items: {', '.join(magic_items_b)}"

    elif hoard_roll in range(66, 71):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_b)}"

    elif hoard_roll in range(71, 76):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_b)}"

    elif hoard_roll in range(76, 79):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_10)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(79, 81):
        return f"Coins: {coins}\Art Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(81, 86):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(86, 93):
        return f"Coins: {coins}\Art Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_f)}"

    elif hoard_roll in range(93, 98):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_f)}"

    elif hoard_roll in range(98, 100):
        return f"Coins: {coins}\Art Objects: {', '.join(art_25)}\nMagic Items: {magic_items_g}"

    elif hoard_roll == 100:
        return f"Coins: {coins}\nGemstones: {', '.join(art_25)}\nMagic Items: {magic_items_g}"


def hoard_tier2():
    """Return roll on Treasure Hoard: Challenge 5-10.

    Attributes:
        hoard_roll (int): Number between 1 and 100 checked against table ranges
        copper (int): Number of total copper pieces
        silver (int): Number of total silver pieces
        gold (int): Number of total gold pieces
        platinum (int): Number of total platinum pieces
        coins (str): String of total money rolled for hoard
        art_25 (lst): List of strings of 25 gp art objects
        art_250 (lst): List of strings of 250 gp art objects
        gems_50 (lst): List of strings of 50 gp gemstones
        gems_100 (lst): List of strings of 100 gp gemstones
        magic_items_a (lst): List of strings from magic items table a
        magic_items_b (lst): List of strings from magic items table b
        magic_items_c (lst): List of strings from magic items table c
        magic_items_d (str): String from magic items table d
        magic_items_f (lst): List of strings from magic items table f
        magic_items_g (lst): List of strings from magic items table g
        magic_items_h (lst): List of strings from magic items table h

    Returns:
        string: String of total treasure from roll on Treasure Hoard: Challenge 5-10
    """
    hoard_roll = d100()
    copper = roll(2, d6) * 100
    silver = roll(2, d6) * 1000
    gold = roll(6, d6) * 100
    platinum = roll(3, d6) * 10
    coins = f"{copper}cp, {silver}sp, {gold}gp and {platinum}pp"
    art_25 = [art_object(25) for i in range(roll(2, d4))]
    art_250 = [art_object(250) for i in range(roll(2, d4))]
    gems_50 = [gemstone(50) for i in range(roll(3, d6))]
    gems_100 = [gemstone(100) for i in range(roll(3, d6))]
    magic_items_a = [magic_item('a') for i in range(d6())]
    magic_items_b = [magic_item('b') for i in range(d4())]
    magic_items_c = [magic_item('c') for i in range(d4())]
    magic_items_d = magic_item('d')
    magic_items_f = [magic_item('f') for i in range(d4())]
    magic_items_g = [magic_item('g') for i in range(d4())]
    magic_items_h = magic_item('h')

    if hoard_roll in range(1, 5):
        return f"Coins: {coins}"

    elif hoard_roll in range(5, 11):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}"

    elif hoard_roll in range(11, 17):
        return f"coins: {coins}\nGemstones: {', '.join(gems_50)}"

    elif hoard_roll in range(17, 23):
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}"

    elif hoard_roll in range(23, 29):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}"

    elif hoard_roll in range(29, 33):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_a)}"

    elif hoard_roll in range(33, 37):
        return f"coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_a)}"

    elif hoard_roll in range(37, 41):
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}\nMagic Items: {', '.join(magic_items_a)}"

    elif hoard_roll in range(41, 45):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_a)}"

    elif hoard_roll in range(45, 50):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_b)}"

    elif hoard_roll in range(50, 55):
        return f"coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_b)}"

    elif hoard_roll in range(55, 60):
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}\nMagic Items: {', '.join(magic_items_b)}"

    elif hoard_roll in range(60, 64):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_b)}"

    elif hoard_roll in range(64, 67):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(67, 69):
        return f"coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(70, 73):
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(73, 75):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(75, 77):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}\nMagic Items: {magic_items_d}"

    elif hoard_roll in range(77, 79):
        return f"coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {magic_items_d}"

    elif hoard_roll == 79:
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}\nMagic Items: {magic_items_d}"

    elif hoard_roll == 80:
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {magic_items_d}"

    elif hoard_roll in range(81, 85):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_25)}\nMagic Items: {', '.join(magic_items_f)}"

    elif hoard_roll in range(85, 89):
        return f"coins: {coins}\nGemstones: {', '.join(gems_50)}\nMagic Items: {', '.join(magic_items_f)}"

    elif hoard_roll in range(89, 92):
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}\nMagic Items: {', '.join(magic_items_f)}"

    elif hoard_roll in range(92, 95):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_f)}"

    elif hoard_roll in range(95, 97):
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}\nMagic Items: {', '.join(magic_items_g)}"

    elif hoard_roll in range(97, 99):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_g)}"

    elif hoard_roll == 99:
        return f"coins: {coins}\nGemstones: {', '.join(gems_100)}\nMagic Items: {magic_items_h}"

    elif hoard_roll == 100:
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {magic_items_h}"


def hoard_tier3():
    """Return roll on Treasure Hoard: Challenge 11-17.

    Attributes:
        hoard_roll (int): Number between 1 and 100 checked against table ranges
        gold (int): Number of total gold pieces
        platinum (int): Number of total platinum pieces
        coins (str): String of total money rolled for hoard
        art_250 (lst): List of strings of 250 gp art objects
        art_750 (lst): List of strings of 750 gp art objects
        gems_500 (lst): List of strings of 500 gp gemstones
        gems_1000 (lst): List of strings of 1000 gp gemstones
        magic_items_a (lst): List of strings from magic items table a
        magic_items_b (lst): List of strings from magic items table b
        magic_items_c (lst): List of strings from magic items table c
        magic_items_d (lst): List of strings from magic items table d
        magic_items_e (str): String from magic items table e
        magic_items_f (str): String from magic items table f
        magic_items_g (lst): List of strings from magic items table g
        magic_items_h (lst): List of strings from magic items table h
        magic_items_i (str): String from magic items table i

    Returns:
        string: String of total treasure from roll on Treasure Hoard: Challenge 11-17
    """
    hoard_roll = d100()
    gold = roll(4, d6) * 1000
    platinum = roll(5, d6) * 100
    coins = f"{gold}gp and {platinum}pp"
    art_250 = [art_object(250) for i in range(roll(2, d4))]
    art_750 = [art_object(750) for i in range(roll(2, d4))]
    gems_500 = [gemstone(500) for i in range(roll(3, d6))]
    gems_1000 = [gemstone(1000) for i in range(roll(3, d6))]
    magic_items_a = [magic_item('a') for i in range(d4())]
    magic_items_b = [magic_item('b') for i in range(d6())]
    magic_items_c = [magic_item('c') for i in range(d6())]
    magic_items_d = [magic_item('d') for i in range(d4())]
    magic_items_e = magic_item('e')
    magic_items_f = magic_item('f')
    magic_items_g = [magic_item('g') for i in range(d4())]
    magic_items_h = [magic_item('h') for i in range(d4())]
    magic_items_i = magic_item('i')

    if hoard_roll in range(1, 4):
        return f"Coins: {coins}"

    elif hoard_roll in range(4, 7):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}"

    elif hoard_roll in range(7, 10):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}"

    elif hoard_roll in range(10, 13):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}"

    elif hoard_roll in range(13, 16):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}"

    elif hoard_roll in range(16, 20):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_a)}, {', '.join(magic_items_b)}"

    elif hoard_roll in range(20, 24):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}\nMagic Items: {', '.join(magic_items_a)}, {', '.join(magic_items_b)}"

    elif hoard_roll in range(24, 27):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}\nMagic Items: {', '.join(magic_items_a)}, {', '.join(magic_items_b)}"

    elif hoard_roll in range(27, 30):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_a)}, {', '.join(magic_items_b)}"

    elif hoard_roll in range(30, 36):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(36, 41):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(41, 46):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(46, 51):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(51, 55):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(55, 59):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(59, 63):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(63, 67):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(67, 69):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {magic_items_e}"

    elif hoard_roll in range(69, 71):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}\nMagic Items: {magic_items_e}"

    elif hoard_roll in range(71, 73):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}\nMagic Items: {magic_items_e}"

    elif hoard_roll in range(73, 75):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {magic_items_e}"

    elif hoard_roll in range(75, 77):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {magic_items_f}, {', '.join(magic_items_g)}"

    elif hoard_roll in range(77, 79):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}\nMagic Items: {magic_items_f}, {', '.join(magic_items_g)}"

    elif hoard_roll in range(79, 81):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}\nMagic Items: {magic_items_f} {', '.join(magic_items_g)}"

    elif hoard_roll in range(81, 83):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {magic_items_f}, {', '.join(magic_items_g)}"

    elif hoard_roll in range(83, 86):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(86, 89):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(89, 91):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(91, 93):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(93, 95):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_250)}\nMagic Items: {magic_items_i}"

    elif hoard_roll in range(95, 97):
        return f"Coins: {coins}\nArt Objects: {', '.join(art_750)}\nMagic Items: {magic_items_i}"

    elif hoard_roll in range(97, 99):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_500)}\nMagic Items: {magic_items_i}"

    elif hoard_roll in range(99, 101):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {magic_items_i}"


def hoard_tier4():
    """Return roll on Treasure Hoard: Challenge 17+.

    Attributes:
        hoard_roll (int): Number between 1 and 100 checked against table ranges
        gold (int): Number of total gold pieces
        platinum (int): Number of total platinum pieces
        coins (str): String of total money rolled for hoard
        art_2500 (lst): List of strings of 2500 gp art objects
        art_7500 (lst): List of strings of 7500 gp art objects
        gems_1000 (lst): List of strings of 1000 gp gemstones
        gems_5000 (lst): List of strings of 5000 gp gemstones
        magic_items_c (lst): List of strings from magic items table c
        magic_items_d (lst): List of strings from magic items table d
        magic_items_e (lst): List of strings from magic items table e
        magic_items_g (lst): List of strings from magic items table g
        magic_items_h (lst): List of strings from magic items table h
        magic_items_i (lst): List of strings from magic items table i

    Returns:
        (str): String of total treasure from roll on Treasure Hoard: Challenge 17+
    """

    hoard_roll = d100()
    gold = roll(12, d6) * 1000
    platinum = roll(8, d6) * 1000
    coins = f"{gold}gp and {platinum}pp"
    art_2500 = [art_object(2500) for i in range(d10())]
    art_7500 = [art_object(7500) for i in range(d4())]
    gems_1000 = [gemstone(1000) for i in range(roll(3, d6))]
    gems_5000 = [gemstone(5000) for i in range(d8())]
    magic_items_c = [magic_item('c') for i in range(d8())]
    magic_items_d = [magic_item('d') for i in range(d6())]
    magic_items_e = [magic_item('e') for i in range(d6())]
    magic_items_g = [magic_item('g') for i in range(d4())]
    magic_items_h = [magic_item('h') for i in range(d4())]
    magic_items_i = [magic_item('i') for i in range(d4())]

    if hoard_roll in range(1, 3):
        return f"Coins: {coins}"

    elif hoard_roll in range(3, 6):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(6, 9):
        return f"Coins: {coins}\nGemstones: {', '.join(art_2500)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(9, 12):
        return f"Coins: {coins}\nGemstones: {', '.join(art_7500)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(12, 15):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_5000)}\nMagic Items: {', '.join(magic_items_c)}"

    elif hoard_roll in range(15, 23):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(23, 31):
        return f"Coins: {coins}\nGemstones: {', '.join(art_2500)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(31, 39):
        return f"Coins: {coins}\nGemstones: {', '.join(art_7500)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(39, 47):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_5000)}\nMagic Items: {', '.join(magic_items_d)}"

    elif hoard_roll in range(47, 53):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_e)}"

    elif hoard_roll in range(53, 59):
        return f"Coins: {coins}\nGemstones: {', '.join(art_2500)}\nMagic Items: {', '.join(magic_items_e)}"

    elif hoard_roll in range(59, 64):
        return f"Coins: {coins}\nGemstones: {', '.join(art_7500)}\nMagic Items: {', '.join(magic_items_e)}"

    elif hoard_roll in range(64, 69):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_5000)}\nMagic Items: {', '.join(magic_items_e)}"

    elif hoard_roll == 69:
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_g)}"

    elif hoard_roll == 70:
        return f"Coins: {coins}\nGemstones: {', '.join(art_2500)}\nMagic Items: {', '.join(magic_items_g)}"

    elif hoard_roll == 71:
        return f"Coins: {coins}\nGemstones: {', '.join(art_7500)}\nMagic Items: {', '.join(magic_items_g)}"

    elif hoard_roll == 72:
        return f"Coins: {coins}\nGemstones: {', '.join(gems_5000)}\nMagic Items: {', '.join(magic_items_g)}"

    elif hoard_roll in range(73, 75):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(75, 77):
        return f"Coins: {coins}\nGemstones: {', '.join(art_2500)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(77, 79):
        return f"Coins: {coins}\nGemstones: {', '.join(art_7500)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(79, 81):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_5000)}\nMagic Items: {', '.join(magic_items_h)}"

    elif hoard_roll in range(81, 86):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_1000)}\nMagic Items: {', '.join(magic_items_i)}"

    elif hoard_roll in range(86, 91):
        return f"Coins: {coins}\nGemstones: {', '.join(art_2500)}\nMagic Items: {', '.join(magic_items_i)}"

    elif hoard_roll in range(91, 96):
        return f"Coins: {coins}\nGemstones: {', '.join(art_7500)}\nMagic Items: {', '.join(magic_items_i)}"

    elif hoard_roll in range(91, 101):
        return f"Coins: {coins}\nGemstones: {', '.join(gems_5000)}\nMagic Items: {', '.join(magic_items_i)}"


def name(kind, option):
    """Return string of name rolled on names_df for given kind and option.

    Args:
        kind (str): String of type of name to roll
        option (str): String to specify the type of name to roll

    Attributes:
        kind (str): arabic, celtic, chinese, dragonborn, dwarf, 
                    elf, english, egyptian, french, german, gnome, 
                    greek, halfling, half-orc, indian, japanese, 
                    mesoamerican, niger-congo, norse, polynesian, 
                    roman, slavic, spanish, or tiefling
        option (str): female, male or virtue for tiefling
    
    Returns:
        (str): Full name based on parameters
    """

    if kind == 'arabic':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'arabic, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'arabic, male')}"

    elif kind == 'celtic':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'celtic, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'celtic, male')}"

    elif kind == 'chinese':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'chinese, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'chinese, male')}"

    elif kind == 'dragonborn':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'dragonborn, female')}  {roll_range(names_df, d100(), 'dragonborn, clan')}"

        else:
            return f"{roll_range(names_df, d100(), 'dragonborn, male')} {roll_range(names_df, d100(), 'dragonborn, clan')}"

    elif kind == 'dwarf':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'dwarf, female')} {roll_range(names_df, d100(), 'dwarf, clan')}"

        else:
            return f"{roll_range(names_df, d100(), 'dwarf, male')} {roll_range(names_df, d100(), 'dwarf, clan')}"

    elif kind == 'egyptian':

        if option is 'female':
            return f"{roll_range(names_df, d100(), 'egyptian, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'egyptian, male')}"

    elif kind == 'elf':

        if option is 'female':
            return f"{roll_range(names_df, d100(), 'elf, female')} {roll_range(names_df, d100(), 'elf, child')} {roll_range(names_df, d100(), 'elf, family')}"

    elif kind == 'english':

        if option is 'female':
            return f"{roll_range(names_df, d100(), 'english, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'english, male')}"

    elif kind == 'french':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'french, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'french, male')}"

    elif kind == 'german':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'german, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'german, male')}"

    elif kind == 'gnome':

        if option is 'female':
            return f"{roll_range(names_df, d100(), 'gnome, female')} {roll_range(names_df, d100(), 'gnome, clan')}"

        else:
            return f"{roll_range(names_df, d100(), 'gnome, male')} {roll_range(names_df, d100(), 'gnome, clan')}"

    elif kind == 'greek':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'greek, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'greek, male')}"

    elif kind == 'halfling':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'halfling, female')} {roll_range(names_df, d100(), 'halfling, family')}"

        else:
            return f"{roll_range(names_df, d100(), 'halfling, male')} {roll_range(names_df, d100(), 'halfling, family')}"

    elif kind == 'half-orc':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'half-orc, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'half-orc, male')}"

    elif kind == 'indian':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'indian, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'indian, male')}"

    elif kind == 'japanese':

        if option is 'female':
            return f"{roll_range(names_df, d100(), 'japanese, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'japanese, male')}"

    elif kind == 'mesoamerican':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'mesoamerican, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'mesoamerican, male')}"

    elif kind == 'niger-congo':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'niger-congo, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'niger-congo, male')}"

    elif kind == 'norse':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'norse, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'norse, male')}"

    elif kind == 'polynesian':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'polynesian, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'polynesian, male')}"

    elif kind == 'roman':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'roman, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'roman, male')}"

    elif kind == 'slavic':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'slavic, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'slavic, male')}"

    elif kind == 'spanish':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'spanish, female')}"

        else:
            return f"{roll_range(names_df, d100(), 'spanish, male')}"

    elif kind == 'tiefling':

        if option == 'female':
            return f"{roll_range(names_df, d100(), 'tiefling, female')}"

        elif option == 'male':
            return f"{roll_range(names_df, d100(), 'tiefling, male')}"

        else:
            return f"{roll_range(names_df, d100(), 'tiefling, virtue')}"
