/**
 * Delete a row of the table for a given index.
 * 
 * @param {number} num Index of row to be deleted.
 */
function deleteRow(num) {
    document.getElementById(`row${num}`).outerHTML = "";
}

/**
 * Add a new row to the table based on the user's input.
 */
function addRow() {
    var new_initiative = document.getElementById("new_initiative").innerHTML;
    var new_name = document.getElementById("new_name").innerHTML;
    var new_armour_class = document.getElementById("new_armour_class").innerHTML;
    var new_hit_points = document.getElementById("new_hit_points").innerHTML;
    var new_temp_hp = document.getElementById("new_temp_hp").innerHTML;
    var new_conditions = document.getElementById("new_conditions").innerHTML;

    var table = document.getElementById("encounter");
    var table_len = (table.rows.length);
    var row = table.insertRow(table_len).outerHTML = `
    <tr id="row${table_len}">
        <td id="initiative_row${table_len}" contenteditable="true">${new_initiative}</td>
        <td id="name_row${table_len}" contenteditable="true">${new_name}</td>
        <td id="armour_class_row${table_len}" contenteditable="true">${new_armour_class}</td>
        <td id="hit_points_row${table_len}" contenteditable="true">${new_hit_points}</td>
        <td id="temp_hp_row${table_len}" contenteditable="true">${new_temp_hp}</td>
        <td id="conditions_row${table_len}" contenteditable="true">${new_conditions}</td>
        <td><button onclick="deleteRow(${table_len})">Delete</button></td>
    </tr>`;

    document.getElementById("new_initiative").value = "";
    document.getElementById("new_name").value = "";
    document.getElementById("new_armour_class").value = "";
    document.getElementById("new_hit_points").value = "";
    document.getElementById("new_temp_hp").value = "";
    document.getElementById("new_conditions").value = "";
}
/**
 * Sort the table in descending initiative order.
 */
function sortTable() {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("encounter");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[0];
            y = rows[i + 1].getElementsByTagName("TD")[0];
            if (Number(x.innerHTML) < Number(y.innerHTML)) {
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}
/**
 * Highlight row of current initiative, starting with the first row
 * and working down the list, incrementing the round whenever the first
 * row is selected.
 */
function nextTurn() {
    var roundNum = Number(document.getElementById("round-num").innerHTML);
    var turnNum = Number(document.getElementById("turn-num").innerHTML);
    var tableLength = document.getElementById("encounter").rows.length
    if (roundNum === 0) {
        document.getElementById("encounter").rows[1].style.backgroundColor = "#8B0000";
        document.getElementById("round-num").innerHTML = roundNum + 1;
        document.getElementById("turn-num").innerHTML = turnNum + 1;
    }
    if (turnNum >= 1 && turnNum < tableLength - 1) {
        document.getElementById("encounter").rows[turnNum].style.backgroundColor = "#351431";
        document.getElementById("encounter").rows[turnNum + 1].style.backgroundColor = "#8B0000";
        document.getElementById("turn-num").innerHTML = turnNum + 1;
    } else {
        document.getElementById("encounter").rows[turnNum].style.backgroundColor = "#351431";
        document.getElementById("encounter").rows[1].style.backgroundColor = "#8B0000";
        document.getElementById("turn-num").innerHTML = 1;
        document.getElementById("round-num").innerHTML = roundNum + 1;
    }
}