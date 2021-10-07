from flask import Flask
from flask import render_template

from gracie_lou import gracie
from Utilities import search_monsters
from StatBlock import monster_set

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sheet")
def character_sheet():
    """Return html of rendered chatacter sheet for given character.
    
    Args:
        character(obj): Instance of the PlayerCharacter class"""
    return render_template("sheet.html")


@app.route("/mm_<monster>")
def search_json_monsters(monster):
    monster_name = monster.replace("_", " ")
    return f"<pre>{search_monsters(monster_name)}</pre>"


@app.route("/statblock/<creature>")
def stat_block(creature):
    monster_name = creature.replace("_", " ")
    for item in monster_set:
        if monster_name == item.name.lower():
            monster = item

            return render_template("statblock.html", stats=monster)
        
    return render_template("statblock.html")


@app.route("/sheet_<character>")
def sheet(character):
    try:
        if character == "gracie":
            return f"<pre>{gracie.get_sheet(full=True)}</pre>"
    
    except:
        return f"<p>Character '{character}' not found.</p>"


if __name__ =="__main__":
    app.run()