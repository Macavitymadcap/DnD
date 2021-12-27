# %%
from pprint import pprint
import requests

BASE_URL = "https://www.dnd5eapi.co/api/"

def get_json(item: str, kind: str) -> object:
    url = f"{BASE_URL}{kind}/{item}/"
    json_data = requests.get(url).json()
    return json_data
# %%
bard = get_json("bard", "classes")
bard_features = [get_json(feature['index'], "features") for feature in get_json("features", "classes/bard")['results']]
bard_spells = [get_json(spell['index'], "spells") for spell in get_json("spells", "classes/bard")['results']]
# %%
def print_bard_features(level: int) -> None:
    for feature in bard_features:
        if int(feature['level']) <= level:
            if feature['name'][0:12] == "Spellcasting":
                spellcasting_string = ' '.join(feature['desc']).replace('  ', '\n')
                print(f"Spellcasting\n{spellcasting_string}\n")
                for item in bard['spellcasting']['info']:
                    item_string = ' '.join(item['desc']).replace('  ', '\n')
                    print(f"\t{item['name']}\n\t{item_string}\n")
            else:
                feature_string = ' '.join(feature['desc']).replace('  ', '\n')
                print(f"{feature['name']}\n{feature_string}\n")

def print_bard_spell_list(level: int) -> None:
    for i in range(level + 1):
        spell_list = [spell['name'] for spell in bard_spells if spell['level'] == i]
        if i == 0:
            print(f"Cantrips: {', '.join(spell_list).lower()}")
        else:
            print(f"Level {i}: {', '.join(spell_list).lower()}")

# %%
