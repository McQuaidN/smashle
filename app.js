import { characters } from './Characters.js';

var form = document.getElementById('mainForm');
var textbox = document.getElementById('tbxCharacter');
let x = Math.floor((Math.random() * characters.length));
var randChar = characters[x];
let errorBox = document.getElementById("errors").innerText;

for (let i=0; i < characters.length; i++){
    characters[i].Name = characters[i].Name.toLowerCase();
}


form.addEventListener('submit', function(event){
    event.preventDefault();
    submitButton();
});

function submitButton(){
    textbox.value = textbox.value.toLowerCase();
    var flag = false;
    for (let i=0; i < characters.length; i++){
        var char = characters[i];
        if (textbox.value == char.Name){
            flag = true;
        }
    }

    if(flag == true){
        errorBox = "Valid character";
        newRow()
    }
    else{
        console.log("am i getting here")
        errorBox = "invalid character";
    }
    textbox.value = '';
}

function newRow(){
    let table = document.getElementById("tableBody");
    let row = document.createElement("tr");
    let cell = document.createElement("td");
    cell.innerText = textbox.value;
    textbox.value = "";
    row.appendChild(cell);
    table.appendChild(row);
}

function clearButton(){
    document.getElementById("tableBody").innerHTML = '';
}

document.getElementById("clear").addEventListener("click", clearButton());