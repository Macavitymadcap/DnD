from flask import Flask
from flask import render_template, json
import yaml

from gracie_lou import gracie
from Utilities import search_monsters
from StatBlock import monster_set

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sheet")
def character_sheet():
    """Return html of rendered character sheet for given character.
    
    Args:
        character(obj): Instance of the PlayerCharacter class"""
    return render_template("sheet.html")

@app.route("/dice")
def dice_roller():
    """Return html of dice roller page."""
    return render_template("dice.html")

@app.route("/monsters")
def monsterpedia():
    """Return html of searchable Monster Manual.yaml."""
    with open('MonsterManual.yaml', 'r') as yaml_file:
        yaml_monsters = yaml.safe_load(yaml_file)
    json_monsters = json.dumps(yaml_monsters)
    
    return render_template("monstersearch.html", monsters=json_monsters)

@app.route("/mm_<monster>")
def search_json_monsters(monster):
    monster_name = monster.replace("_", " ")
    return f"<pre>{search_monsters(monster_name)}</pre>"


@app.route("/statblock/<creature>")
def stat_block(creature):
    with open('MonsterManual.yaml', 'r') as yaml_file:
        yaml_monsters = yaml.safe_load(yaml_file)
    json_monsters = json.dumps(yaml_monsters)
    monster_name = creature.replace("_", " ")
    for item in monster_set:
        if monster_name == item.name.lower():
            monster = item

            return render_template("statblock.html", stats=monster, monsters=json_monsters)
        
    return render_template("statblock.html")


if __name__ =="__main__":
    app.run()