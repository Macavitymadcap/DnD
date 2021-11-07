// Functions for rolling a die of x faces.
function rollD(num) {
    return Math.floor(Math.random() * num) +1;
}

function d4() {
    return rollD(4);
}

function d6() {
    return rollD(6);
}

function d8() {
    return rollD(8);
}

function d10() {
    return rollD(10);
}

function d12() {
    return rollD(12);
}

function d20() {
    return rollD(20);
}

function d100() {
    return rollD(100);
}

// Functions for ways of roll dice.
function rollMult(num, dice) {
    let rolls = 0;
    for (let i = 0; i < num; i++) {
        rolls += dice();
    }
    return rolls;
}

function rollString(string) {
    /* Patterns to be searched for in string operator & modifier set to NaN if
    none found.
    */
    numRegx = /\d*/;
    dieRegx = /[D|d]\d+/;
    opeRegx = /[-|+|x|X|*|/|÷]/;
    numDice = parseInt(numRegx.exec(string.trim())[0]);
    die = dieRegx.exec(string)[0].toLowerCase();
    try {
        operator = opeRegx.exec(string)[0];
        modifier = parseInt(string.slice(string.search(opeRegx) + 1).trim());
    }
    catch(err) {
        operator = NaN;
        modifier = NaN;
    }
    let roll;
    if (numDice >= 1) {
        /* Select call to rollD to be added to roll if numDice greater than
        or equal to 1.
        */
       roll = 0;
       for (let i = 0; i < numDice; i++) {
           roll += rollD(parseInt(die.slice(1)));
       }
    } else {
        /* Select call of rollD function to be added to roll if numDice is 0 or
        NaN.
        */
        roll = rollD(parseInt(die.slice(1)))
    }
    if (operator != NaN) {
        /* Return roll with operator and modified applied if they are not NaN,
        rounding down if division.
        */
        switch (operator) {
            case "-":
                return roll - modifier;
            case "+":
                return roll + modifier;
            case "*":
            case "x":
            case "X":
                return roll * modifier;
            case "/":
            case "÷":
                return Math.floor(roll / modifier);
        }
    }
    // Return roll if modifier is NaN.
    return roll;
}

function rollCrit(string) {
    /* Patterns to be searched for in string operator & modifier set to NaN if
    none found.
    */
    numRegx = /\d*/;
    dieRegx = /[D|d]\d+/;
    opeRegx = /[-|+|x|X|*|/|÷]/;
    numDice = parseInt(numRegx.exec(string.trim())[0]);
    die = dieRegx.exec(string)[0].toLowerCase();
    try {
        operator = opeRegx.exec(string)[0];
        modifier = parseInt(string.slice(string.search(opeRegx) + 1));
    }
    catch(err) {
        operator = "+";
        modifier = 0;
    }
    let roll = 0;
    for (let i = 0; i < 2; i++) {
        if (numDice > 1) {
            /* Select call to rollD to be added to roll if numDice greater than
            or equal to 1.
            */
            for (let i = 0; i < numDice; i++) {
                roll += rollD(parseInt(die.slice(1)));
        }
        } else {
            /* Select call of rollD function to be added to roll if numDice is 0 or
            NaN.
            */
            roll += rollD(parseInt(die.slice(1)))
        }
    }
    const list = [numDice, die, operator, modifier, roll];
    if (operator == "-") {
        return roll - modifier;
    } else if (operator = "+") {
        return roll + modifier;
    } else if (operator == "*" || operator == "x" || operator == "X" ) {
        return roll * modifier;
    } else if (operator == "/" || operator == "÷") {
        return roll / modifier;
    }
}

function rollArray(num, string) {
    let rolls = [];
    for (let i = 0; i < num; i++) { 
        rolls.push(rollString(string));
    }
    return rolls;
}

function rollAdvan(string) {
    rolls = rollArray(2, string);
    rolls.sort(function(a, b){return b - a});
    return rolls.join(' / ');
}

function rollDisad(string) {
    rolls = rollArray(2, string);
    rolls.sort(function(a, b){return a - b});
    return rolls.join(' / ');
}

function rollAbilityScores() {
    let rolls = [];
    for (let i = 0; i < 6; i++) {
        roll = rollArray(4, "d6");
        roll.sort(function(a, b){return a - b});
        roll.pop(3);
        rolls.push(roll.reduce(function(total, num){return total + num}));
    }
    rolls.sort(function(a, b){return b - a});
    return rolls.join(', ');
}