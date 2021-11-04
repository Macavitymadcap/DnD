import json
import yaml

with open('MonsterManual.yaml', 'r') as yaml_file:
    yaml_monsters = yaml.safe_load(yaml_file)
json_monsters = json.dumps(yaml_monsters, indent=4)
