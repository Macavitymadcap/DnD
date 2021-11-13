from flask import Flask
from flask import render_template, json
import yaml

from StatBlock import monster_set

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


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