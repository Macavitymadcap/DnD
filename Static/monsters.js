import { readFileSync } from 'fs';
import YAML from 'yaml';

function searchMonsters(string) { 
    let rawdata = readFileSync('./MonsterManual.json');
    let monsters = JSON.parse(rawdata);
    return monsters[string.toLowerCase()]
}