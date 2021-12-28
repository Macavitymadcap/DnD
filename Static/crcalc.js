/**
 * 
 * @param {*} challengeRating String or num of the challenge rating to be serached.
 * @returns Experience Points for given challenge rating.
 */
function getExperiencePoints(challengeRating) {
    const xpbycr = [
        [0, "1/8", "1/4", "1/2", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 39, 30],
        [10, 25, 50, 100, 200, 450, 700, 1100, 1800, 2300, 2900, 3900, 5000, 5900, 7200, 8400, 10000, 11500, 13000, 15000, 18000, 20000, 22000, 25000, 33000, 41000, 50000, 62000, 75000, 90000, 105000, 120000, 135000, 155000]
    ];
    return xpbycr[1][xpbycr[0].indexOf(challengeRating)];
};

/**
 * 
 * @param {array} monsters List of monster challenge ratings.
 * @returns Combined total of monster experience points
 */
function getTotalExperiencePoints(monsters) {
    let total = 0;

    for (let monster of monsters) {
        total += getExperiencePoints(monster);
    }

    return total;
};

/**
 * 
 * @param {number} level The player character's level.
 * @returns Easy, medium, hard and deadly xp threshold for given level.
 */
function getCharacterThresholds(level) {
    const thresholdsByXP = [
        [25, 50, 75, 100],
        [50, 100, 150, 200],
        [75, 150, 225, 400],
        [125, 250, 375, 500],
        [250, 500, 750, 1100],
        [300, 600, 900, 1400],
        [350, 750, 1100, 1700],
        [450, 900, 1400, 2100],
        [550, 1100, 1600, 2400],
        [600, 1200, 1900, 2800],
        [800, 1600, 2400, 3600],
        [1000, 2000, 3000, 4500],
        [1100, 2200, 3400, 5100],
        [1250, 2500, 3800, 5700],
        [1400, 2800, 4300, 6400],
        [1600, 3200, 4800, 7200],
        [2000, 3900, 5900, 8800],
        [2100, 4200, 6300, 9500],
        [2400, 4900, 7300, 10900],
        [2800, 5700, 8500, 12700]
    ];
    return thresholdsByXP[level - 1];
};

/**
 * 
 * @param {array} levels List of player character's class levels.
 * @returns Array of the party's combined xp thresholds.
 */
function getPartyThresholds(levels) {
    let easy = 0;
    let medium = 0;
    let hard = 0;
    let deadly = 0;

    for (let level of levels) {
        easy += getCharacterThresholds(level)[0];
        medium += getCharacterThresholds(level)[1];
        hard += getCharacterThresholds(level)[2];
        deadly += getCharacterThresholds(level)[3]
    };

    return [easy, medium, hard, deadly]
};

/**
 * 
 * @param {array} levels List of player character levels.
 * @param {array} monsters List of monster challenge ratings.
 * @returns Modified experience points for number of players and monsters.
 */
function modifyExperiencePoints(levels, monsters) {
    let xp = getTotalExperiencePoints(monsters);

    if (levels.length < 3) {
        switch (monsters.length) {
            case 1:
                return xp * 0.5;
                break;
            case 2:
                return xp * 1;
                break;
            case 3:
            case 4:
            case 5:
            case 6:
                return xp * 1.5;
                break;
            case 7:
            case 8:
            case 9:
            case 10:
                return xp * 2;
                break;
            case 11:
            case 12:
            case 13:
            case 14:
                return xp * 2.5;
                break;
            case 15:
                return xp * 3;
                break;
            default:
                return xp * 3;
        }
    } else if (levels.length >= 3 && levels.length <= 5) {
        switch (monsters.length) {
            case 1:
                return xp * 1;
                break;
            case 2:
                return xp * 1.5;
                break;
            case 3:
            case 4:
            case 5:
            case 6:
                return xp * 2;
                break;
            case 7:
            case 8:
            case 9:
            case 10:
                return xp * 2.5;
                break;
            case 11:
            case 12:
            case 13:
            case 14:
                return xp * 3;
                break;
            case 15:
                return xp * 4;
                break;
            default:
                return xp * 4;
        }
    } else {
        switch (monsters.length) {
            case 1:
                return xp * 1.5;
                break;
            case 2:
                return xp * 2;
                break;
            case 3:
            case 4:
            case 5:
            case 6:
                return xp * 2.5;
                break;
            case 7:
            case 8:
            case 9:
            case 10:
                return xp * 3;
                break;
            case 11:
            case 12:
            case 13:
            case 14:
                return xp * 4;
                break;
            case 15:
                return xp * 5;
                break;
            default:
                return xp * 5;
        }
    }
};

/**
 * 
 * @param {array} levels List of the party's character levels.
 * @param {array} monsters List of monster challenge ratings.
 * @returns String detailing the party's xp thresholds; base encounter XP;
 * modified encounter XP; XP per player and the level of difficulty.
 */
function getDifficulty(levels, monsters) {
    let modifiedExperiencePoints = modifyExperiencePoints(levels, monsters);
    let partyThresholds = getPartyThresholds(levels);
    let difficulty;

    if (modifiedExperiencePoints < partyThresholds[0]) {
        difficulty = 'Well Easy';
    } else if (modifiedExperiencePoints >= partyThresholds[0] && modifiedExperiencePoints < partyThresholds[1]) {
        difficulty = 'Easy';
    } else if (modifiedExperiencePoints >= partyThresholds[1] && modifiedExperiencePoints < partyThresholds[2]) {
        difficulty = 'Medium';
    } else if (modifiedExperiencePoints >= partyThresholds[2] && modifiedExperiencePoints < partyThresholds[3]) {
        difficulty = 'Hard';
    } else {
        difficulty = 'Deadly';
    };

    return difficulty;
}

function getPartyList() {
    if (document.getElementById('party-list').innerHTML.includes(',') === true) {
        const partyList = document.getElementById('party-list').innerHTML.split(',');
        for (let num = 0; num < document.getElementById('num-players').value; num++) {
            partyList.push(document.getElementById('player-level').value);
        };
        document.getElementById('party-list').innerHTML = partyList.join(', ');
        document.getElementById('total-players').innerHTML = partyList.length;
    } else {
        const partyList = [];
        for (let num = 0; num < document.getElementById('num-players').value; num++) {
            partyList.push(document.getElementById('player-level').value);
        };
        document.getElementById('party-list').innerHTML = partyList.join(', ');
        document.getElementById('total-players').innerHTML = partyList.length;
    };
};

function getMonsterCRs() {
    if (document.getElementById('cr-list').innerHTML.includes(',') === true) {
        const crList = document.getElementById('cr-list').innerHTML.split(', ');
        for (let num = 0; num < document.getElementById('num-monsters').value; num++) {
            if (document.getElementById('monster-cr').value.includes('/') === true) {
                crList.push(document.getElementById('monster-cr').value);
            } else {
                crList.push(parseInt(document.getElementById('monster-cr').value));
            };
        };
        document.getElementById('cr-list').innerHTML = crList.join(', ');
        document.getElementById('total-monsters').innerHTML = crList.length;
    } else {
        const crList = [];
        for (let num = 0; num < document.getElementById('num-monsters').value; num++) {
            if (document.getElementById('monster-cr').value.includes('/') === true) {
                crList.push(document.getElementById('monster-cr').value);
            } else {
                crList.push(parseInt(document.getElementById('monster-cr').value));
            };
        };
        document.getElementById('cr-list').innerHTML = crList.join(', ');
        document.getElementById('total-monsters').innerHTML = crList.length;
    };
};

function calculateDifficulty() {
    const thresholds = getPartyThresholds(document.getElementById('party-list').innerHTML.split(','));
    let numMonsters = document.getElementById('cr-list').innerHTML.split(',').length;
    let totalXP = getTotalExperiencePoints(document.getElementById('cr-list').innerHTML.split(', '));
    let modifiedXP = modifyExperiencePoints(document.getElementById('party-list').innerHTML.split(', '), document.getElementById('cr-list').innerHTML.split(', '));
    let xpPerPlayer = Math.floor(totalXP / numMonsters);

    document.getElementById('easy-threshold').innerHTML = thresholds[0];
    document.getElementById('medium-threshold').innerHTML = thresholds[1];
    document.getElementById('hard-threshold').innerHTML = thresholds[2];
    document.getElementById('deadly-threshold').innerHTML = thresholds[3];
    document.getElementById('total-xp').innerHTML = totalXP;
    document.getElementById('modified-xp').innerHTML = modifiedXP;
    document.getElementById('xp-per-player').innerHTML = xpPerPlayer;
    document.getElementById('difficulty').innerHTML = getDifficulty(document.getElementById('party-list').innerHTML.split(','), document.getElementById('cr-list').innerHTML.split(','));
};

function clearParty() {
    document.getElementById('party-list').innerHTML = '';
    document.getElementById('total-players').innerHTML = '';
};

function clearMonsters() {
    document.getElementById('cr-list').innerHTML = '';
    document.getElementById('total-monsters').innerHTML = '';
};

function clearResults() {
    document.getElementById('easy-threshold').innerHTML = '';
    document.getElementById('medium-threshold').innerHTML = '';
    document.getElementById('hard-threshold').innerHTML = '';
    document.getElementById('deadly-threshold').innerHTML = '';
    document.getElementById('total-xp').innerHTML = '';
    document.getElementById('modified-xp').innerHTML = '';
    document.getElementById('xp-per-player').innerHTML = '';
    document.getElementById('difficulty').innerHTML = '';
}