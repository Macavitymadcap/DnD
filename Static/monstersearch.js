const fs = require('fs');
// Return number with + if 0 or higher
function addOperator(num) {
    if (num >= 0) {
        return "+" + num;
    } else {
        return num;
    }
}
// Return modifier of score prefixed with + or -
function getModifier(num) {
    let mod = Math.floor((num - 10) / 2);
    return addOperator(mod)
}
// Search json_data for matching monster
function searchMonsters() {
    let string = document.getElementById('monster_name').value;
    let monsters = JSON.parse(document.getElementById("json_data").innerHTML);
    let stats = monsters[string.toLowerCase()];
    if (stats) {
        let statblock = `
        <table>
            <tr>
                <td><h3>${stats["Name"].toUpperCase()}</h3></td>
            </tr>
            <tr>
                <td><i>${stats["Size"]} ${stats["Kind"]}, ${stats["Alignment"]}</i></td>
            </tr>`;
        if (stats["Armour Class"] instanceof Array) {
            statblock += `
            <tr>
                <td><b>Armour Class</b> ${stats["Armour Class"][0]} (<i>${stats["Armour Class"][1]}</i>)</td>
            </tr>`;
        } else {
            statblock += `
            <tr>
                <td><b>Armour Class</b> ${stats["Armour Class"]}</td>#
            </tr>`;
        }
        statblock += `
        <tr>
            <td><div class="flex_line">
                <span><div class="dropdown" id="damage_heal">
                    <button onclick="showDropDown('damDropdown')" class="dropbtn">Hit Points</button>
                    <div id="damDropdown" class="dropdown-content">
                        <button onclick="document.getElementById('hit_points').innerHTML = parseInt(document.getElementById('hit_points').innerHTML) + parseInt(document.getElementById('mod_hp').value)">Heal</button>
                        <button onclick="document.getElementById('hit_points').innerHTML = parseInt(document.getElementById('hit_points').innerHTML) - parseInt(document.getElementById('mod_hp').value)">Damage</button>
                    </div>
                </div>
                </span>
                <span id="hit_points">${stats["Hit Points"][0]}</span> 
                <span><input type="number" id="mod_hp"></span>
                <span><b id="name">Temp HP</b> <input type="number"></span>
                <span><button onclick="document.getElementById('hit_points').innerHTML = rollString(document.getElementById('hit_dice').innerHTML)">Hit Dice</button> <span id="hit_dice">${stats["Hit Points"][1]}</span></span>            
            </div></td>
        </tr>
        <tr>
            <td><b id="name">Speed</b> ${stats["Speed"]}</td>
        </tr>
        <tr><td>
        <table class="abilities_table">
            <tr>
                <td><div class="dropdown">
                        <button onclick="showDropDown('strDropdown')" class="dropbtn">STR</button>
                        <div id="strDropdown" class="dropdown-content">
                        <button onclick="document.getElementById('score_roll').innerHTML = rollString('d20' + '${getModifier(stats["Abilities"][0])}')">Roll</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollAdvan('d20' + '${getModifier(stats["Abilities"][0])}')">Advn</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollDisad('d20' + '${getModifier(stats["Abilities"][0])}')">Disad</button>
                    </div>
                </div>
                </td>
                <td><div class="dropdown">
                        <button onclick="showDropDown('dexDropdown')" class="dropbtn">DEX</button>
                        <div id="dexDropdown" class="dropdown-content">
                        <button onclick="document.getElementById('score_roll').innerHTML = rollString('d20' + '${getModifier(stats["Abilities"][1])}')">Roll</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollAdvan('d20' + '${getModifier(stats["Abilities"][1])}')">Advn</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollDisad('d20' + '${getModifier(stats["Abilities"][1])}')">Disad</button>
                    </div>
                </div>
                </td>
                <td><div class="dropdown">
                        <button onclick="showDropDown('conDropdown')" class="dropbtn">CON</button>
                        <div id="conDropdown" class="dropdown-content">
                        <button onclick="document.getElementById('score_roll').innerHTML = rollString('d20' + '${getModifier(stats["Abilities"][2])}')">Roll</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollAdvan('d20' + '${getModifier(stats["Abilities"][2])}')">Advn</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollDisad('d20' + '${getModifier(stats["Abilities"][2])}')">Disad</button>
                    </div>
                </div>
                </td>
                <td><div class="dropdown">
                        <button onclick="showDropDown('intDropdown')" class="dropbtn">INT</button>
                        <div id="intDropdown" class="dropdown-content">
                        <button onclick="document.getElementById('score_roll').innerHTML = rollString('d20' + '${getModifier(stats["Abilities"][3])}')">Roll</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollAdvan('d20' + '${getModifier(stats["Abilities"][3])}')">Advn</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollDisad('d20' + '${getModifier(stats["Abilities"][3])}')">Disad</button>
                    </div>
                </div>
                </td>
                <td><div class="dropdown">
                        <button onclick="showDropDown('wisDropdown')" class="dropbtn">WIS</button>
                        <div id="wisDropdown" class="dropdown-content">
                        <button onclick="document.getElementById('score_roll').innerHTML = rollString('d20' + '${getModifier(stats["Abilities"][4])}')">Roll</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollAdvan('d20' + '${getModifier(stats["Abilities"][4])}')">Advn</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollDisad('d20' + '${getModifier(stats["Abilities"][4])}')">Disad</button>
                    </div>
                </div>
                </td>
                <td><div class="dropdown">
                        <button onclick="showDropDown('chaDropdown')" class="dropbtn">CHA</button>
                        <div id="chaDropdown" class="dropdown-content">
                        <button onclick="document.getElementById('score_roll').innerHTML = rollString('d20' + '${getModifier(stats["Abilities"][5])}')">Roll</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollAdvan('d20' + '${getModifier(stats["Abilities"][5])}')">Advn</button>
                        <button onclick="document.getElementById('score_roll').innerHTML = rollDisad('d20' + '${getModifier(stats["Abilities"][5])}')">Disad</button>
                    </div>
                </div>
                </td>
                <td rowspan="3" id="score_roll"></td>
            </tr>
            <tr>
                <td>${stats['Abilities'][0]}</td>
                <td>${stats['Abilities'][1]}</td>
                <td>${stats['Abilities'][2]}</td>
                <td>${stats['Abilities'][3]}</td>
                <td>${stats['Abilities'][4]}</td>
                <td>${stats['Abilities'][5]}</td>
            </tr>
            <tr>
                <td id="str_mod">${getModifier(stats["Abilities"][0])}</td>
                <td id="dex_mod">${getModifier(stats["Abilities"][1])}</td>
                <td id="con_mod">${getModifier(stats["Abilities"][2])}</td>
                <td id="int_mod">${getModifier(stats["Abilities"][3])}</td>
                <td id="wis_mod">${getModifier(stats["Abilities"][4])}</td>
                <td id="cha_mod">${getModifier(stats["Abilities"][5])}</td>
            </tr>
        </table>
        </td></tr>`;
        if (stats["Saving Throws"]) {
            statblock += `
            <tr>
                <td><div class="flex_line">
                    <div><b>Saving Throws</b></div>`;
            var saves = stats["Saving Throws"];
            for (const save in saves) {
                statblock += `<div class="dropdown">
                    <button onclick="showDropDown('${save}Dropdown')" class="dropbtn">${save}</button>
                    <div id="${save}Dropdown" class="dropdown-content">
                    <button onclick="document.getElementById('saving_throw').innerHTML = rollString('d20+' + '${saves[save]}')">Roll</button>
                    <button onclick="document.getElementById('saving_throw').innerHTML = rollAdvan('d20+' + '${saves[save]}')">Advn</button>
                    <button onclick="document.getElementById('saving_throw').innerHTML = rollDisad('d20+' + '${saves[save]}')">Disad</button>
                </div>
            </div>
            <div>${addOperator(saves[save])}</div> `;
            }
            statblock += `
            <div id="saving_throw"></div>
            </div></td>
        </tr>`;
        }
        if (stats["Skills"]) {
            statblock += `
            <tr>
                <td><div class="flex_line">
                    <div><b>Skills</b></div>`;
            var skills = stats["Skills"];
            for (const skill in skills) {
                statblock += `<div class="dropdown">
                    <button onclick="showDropDown('${skill}Dropdown')" class="dropbtn">${skill}</button>
                    <div id="${skill}Dropdown" class="dropdown-content">
                    <button onclick="document.getElementById('skill_check').innerHTML = rollString('d20+' + '${skills[skill]}')">Roll</button>
                    <button onclick="document.getElementById('skill_check').innerHTML = rollAdvan('d20+' + '${skills[skill]}')">Advn</button>
                    <button onclick="document.getElementById('skill_check').innerHTML = rollDisad('d20+' + '${skills[skill]}')">Disad</button>
                </div>
            </div>
            <div>${addOperator(skills[skill])}</div> `;
            }
            statblock += `<div id="skill_check"></div>
        </div></td>
        </tr>`;
        }
        if (stats["Damage Vulnerabilities"]) {
            statblock += `
            <tr>
                <td><b>Damage Vulnerabilities</b> ${stats["Damage Vulnerabilities"]}</td>
            </tr>`;
        }
        if (stats["Damage Resistances"]) {
            statblock += `
            <tr>
                <td><b>Damage Resistances</b> ${stats["Damage Resistances"]}</td>
            </tr>`;
        }
        if (stats["Damage Immunities"]) {
            statblock += `
            <tr>
                <td><b>Damage Immunities</b> ${stats["Damage Immunities"]}</td>
            </tr>`;
        }
        if (stats["Condition Immunities"]) {
            statblock += `
            <tr>
                <td><b>Condition Immunities</b> ${stats["Condition Immunities"]}</td>
            </tr>`;
        }
        statblock += `
        <tr>
            <td><b>Senses</b> ${stats["Senses"]}</td>
        </tr>
        <tr>
            <td><b>Languages</b> ${stats["Languages"]}</td>
        </tr>
            <td><b>Challenge</b> ${stats["Challenge"]}</td>
        </tr>`
        if (stats["Special Traits"]) {
            var traits = stats["Special Traits"];
            for (const trait in traits) {
                statblock += `
                <tr>
                    <td><i><b>${trait}.</b></i> ${traits[trait]}</td>
                </tr>`;
            }
        }
        if (stats["Actions"]) {
            statblock += `
            <tr>
                <td><h4>ACTIONS</h4></td>
            </tr>`
            var actions = stats["Actions"];
            if (actions["Multiattack"]) {
                statblock += `
                <tr>
                    <td><i><b>Multiattack.</b></i> ${actions["Multiattack"]}</td>
                </tr>`
            }
            for (const action in actions) {
                if (action === "Multiattack") {
                        continue; 
                }
                // put spellcasting

                if (typeof actions[action]["to hit"] === 'undefined') {
                    statblock += `
                    <tr>
                        <td><div><i><b>${action}</b></i>`;
                        if (actions[action]["recharge"]) {
                            statblock += `<b><i> (${actions[action]["recharge"]}). </i></b>`;
                        }
                        statblock += `${actions[action]["text"]}</td></tr>`
                } else {
                    statblock += `
                    <tr>
                        <td><div class="flex_line">
                        <div><i><b>${action}.</b></i></div>
                        <div><i>${actions[action]["kind"]}</i></div>
                        <div>${addOperator(actions[action]["to hit"])}</div>
                        <div class="dropdown">
                            <button onclick="showDropDown('${action}ToHitDropdown')" class="dropbtn">To Hit</button>
                            <div id="${action}ToHitDropdown" class="dropdown-content">
                                <button onclick="document.getElementById('${action}-to-hit-roll').innerHTML = rollString('d20' + '${addOperator(actions[action]["to hit"])}')">Roll</button>
                                <button onclick="document.getElementById('${action}-to-hit-roll').innerHTML = rollAdvan('d20' + '${addOperator(actions[action]["to hit"])}')">Advn</button>
                                <button onclick="document.getElementById('${action}-to-hit-roll').innerHTML = rollDisad('d20' + '${addOperator(actions[action]["to hit"])}')">Disad</button>
                            </div>
                        </div>
                        <div><span id="${action}-to-hit-roll"></span></div>`;
                    if (actions[action]["reach"]) {
                        statblock += `<div>reach ${actions[action]["reach"]},</div>`;
                    }
                    if (actions[action]["range"]) {
                        statblock += `<div>range ${actions[action]["range"]},</div>`;
                    }
                    statblock += `<div>${actions[action]["target"]}.</div>`
                    if (actions[action]["hit"]) {
                        statblock += `<div class="dropdown">
                            <button onclick="showDropDown('${action}HitDropdown')" class="dropbtn">Hit</button>
                                <div id="${action}HitDropdown" class="dropdown-content">
                                    <button onclick="document.getElementById('${action}-damage-roll').innerHTML = rollString('${actions[action]["damage roll"]}')">Roll</button>
                                    <button onclick="document.getElementById('${action}-damage-roll').innerHTML = rollCrit('${actions[action]["damage roll"]}')">Crit</button>
                                </div>
                            </div>
                            <div> ${actions[action]["hit"]}</div>
                            <div>(${actions[action]["damage roll"]})</div>
                            <div>${actions[action]["damage type"]} damage <span id="${action}-damage-roll"></span></div>`;
                    } else {
                        statblock += `<div><i>Hit: </i>`
                    }
                    if (actions[action]["plus hit"]) {
                        statblock += `<div>, plus ${actions[action]["plus hit"]}</div>
                        <div class="dropdown">
                            <button onclick="showDropDown('${action}PlusHitDropdown')" class="dropbtn">Hit</button>
                            <div id="${action}PlusHitDropdown" class="dropdown-content">
                                <button onclick="document.getElementById('${action}-plus-damage-roll').innerHTML = rollString('${actions[action]["plus damage roll"]}')">Roll</button>
                                <button onclick="document.getElementById('${action}-plus-damage-roll').innerHTML = rollCrit('${actions[action]["plus damage roll"]}')">Crit</button>
                            </div>
                        </div>
                        <div>(${actions[action]["plus damage roll"]})</div>
                        <div>${actions[action]["plus damage type"]} damage <span id="${action}-plus-damage-roll"></span></div>`;
                    }
                    if (actions[action]["text"]) {
                        statblock += `<span>${actions[action]["text"]}</span>`;
                    }
                    statblock += `</div></td></tr>`
                }
            }
        }
        if (stats["Legendary Actions"]) {
            var legendaryText = `The ${stats["Name"].toLowerCase()} can take 3 legendary actions, choosing from the options below. Only one legendary action can be used at a time and only at the end of another creature's turn. The ${stats["Name"].toLowerCase()} regains spent legendary actions at the start of its turn.`

            statblock += `
            <tr>
                <td><h4>LEGENDARY ACTIONS</h4></td>
            </tr>`
            statblock += `
            <tr>
                <td>${legendaryText}</td>
            </tr>`
        }
        statblock += `</table>`
        return statblock;
    } else {
        return `<h3>404</h3>
            <p>'${string}' not found, Check your spelling and try again. <p>`;
    }
}