from flask import Flask
from flask import render_template, json
import yaml

from StatBlock import monster_set

app = Flask(__name__)

@app.route("/")
def index():
    """Return index page of website."""
    return render_template("index.html")


@app.route("/dice")
def dice_roller():
    """Return html of dice roller page."""
    return render_template("dice.html")


@app.route("/monsters")
def monsterpedia():
    """Return html of searchable Monster Manual.yaml."""
    with open('Static\MonsterManual.yaml', 'r') as yaml_file:
        yaml_monsters = yaml.safe_load(yaml_file)
    json_monsters = json.dumps(yaml_monsters)
    
    return render_template("monstersearch.html", monsters=json_monsters)


@app.route("/initiative")
def initiative_tracker():
    """Return html of initiative tracker page."""
    return render_template("initiative.html")


if __name__ =="__main__":
    app.run()