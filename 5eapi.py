# %%
from pprint import pprint
import requests

from DiceBox.dice import *

BASE_URL = "https://www.dnd5eapi.co/api/"

def get_monster_json(string: str) -> object:
    url = f"{BASE_URL}monsters/{string}/"
    json_data = requests.get(url).json()
    return json_data
# %%
