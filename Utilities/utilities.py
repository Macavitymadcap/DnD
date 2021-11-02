import json
import textwrap

def format_mod(num):
    """Return a string of a number as a positive or negative modfier.
    
    Args:
        num (int): Number evaluated and returned with prefix"""
    if int(num) >= 0:
        return f"+{num}"
    
    else:
        return num

def format_num(num):
    """Return int with st, nd, rd or th accordingly.
    
    Args:
        num (int): Number evaluated and returned with string suffix"""
    num_string = str(num)
    if num == 11 or num == 12 or num == 13:    
        return f"{num}th"

    elif num == 1 or num_string[-1] == "1":
        return f"{num}st"
    
    elif num_string[-1] == "2":
        return f"{num}nd"
    
    elif num_string[-1] == "3":
        return f"{num}rd"
    
    else:
        return f"{num}th"


def format_line(string):
    """Return a paragraph with 80 characters to a line.
    
    Args:
        string (str): String of a paragraph to be formatted
    
    Returns:
        string: String wrapped to 80 characters a line"""
    return textwrap.fill(str(string), 80)


def format_lines(string):
    """Return multiple paragraphs as string with 80 characters to a line.
    
    Args:
        string (str): String of paragraphs seperated by new line breaks
    
    Returns:
        new_string: String of paragraphs with 80 characters to a line"""
    text_list = string.split("\n")
    paragraph_list = [format_line(text) for text in text_list]
    new_string = "\n".join(paragraph_list)

    return new_string


def format_text(string):
    """Return string formatted 80 characters to a line with any paragraphs.
    
    Args:
        string (str): String of any number of lines to be formatted
    
    Returns:
        new_string: String of one or more paragraphs 80 characters to a line"""
    new_string = ""

    if "\n" in string:
        new_string = format_lines(string)
    
    else:
        new_string = format_line(string)
    
    return new_string


def name_stringer(string):
    """Returns string formatted to conventions for variable name.
    
    Args:
        string (str): String to have characters replaced with appropriate ones"""
    step1 = string.replace("'", "")
    step2 = step1.replace(" ", "_")
    step3 = step2.replace("(", "")
    step4 = step3.replace(")", "")
    step5 = step4.replace("-", "_")
    step6 = step5.replace(",", "")

    return step6.lower()

def search_monsters(monster):
    """Return formatted string of monster if found in Monster Manual.json.
    
    Args:
        monster (str): Name of monster fo which to search in json file.
    
    Returns:
        (str): Monster stat block if found, else error message"""
    with open('SRDjson\Monster Manual.json') as file:
        monster_manual = json.loads(file.read())
    
    for item in monster_manual:
        if item.lower() == monster.lower():
            string = f"{item}"
            for line in  monster_manual[item]['content'][0:4]:
                string += f"\n{line}"

            string += f"\nSTR\tDEX\tCON\tINT\tWIS\tCHA\n"
            string += f"{monster_manual[item]['content'][4]['table']['STR'][0]}\t"
            string += f"{monster_manual[item]['content'][4]['table']['DEX'][0]}\t"
            string += f"{monster_manual[item]['content'][4]['table']['CON'][0]}\t"
            string += f"{monster_manual[item]['content'][4]['table']['INT'][0]}\t"
            string += f"{monster_manual[item]['content'][4]['table']['WIS'][0]}\t"
            string += f"{monster_manual[item]['content'][4]['table']['CHA'][0]}\t"

            for line in  monster_manual[item]['content'][5:]:
                string += f"\n{line}"

            return format_text(f"\n{string}\n")
        
    return f"Monster '{monster}' not found."
