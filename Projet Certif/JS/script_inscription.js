// CCCC    RRRR    EEEEE   AAAAA   TTTTT   IIIII   OOOOO   N   N      CCCC    OOOOO   M   M   PPPP    TTTTT   EEEEE
// C       R   R   E       A   A     T       I     O   O   NN  N      C       O   O   MM MM   P   P     T     E
// C       RRRR    EEE     AAAAA     T       I     O   O   N N N      C       O   O   M M M   PPPP      T     EEE
// C       R  R    E       A   A     T       I     O   O   N  NN      C       O   O   M   M   P         T     E
// CCCC    R   R   EEEEE   A   A     T     IIIII   OOOOO   N   N      CCCC    OOOOO   M   M   P         T     EEEEE

document.querySelectorAll('input[type="checkbox"]').forEach(elt => {
    elt.disabled = true
});

let char_checked = false;
let min_checked = false;
let maj_checked = false;
let num_checked = false;
let spec_checked = false;

function checkPass() {
    let password = document.getElementById("password").value;
    let correct = 0
    const char = document.getElementById('char');
    const min = document.getElementById('min');
    const maj = document.getElementById('maj');
    const num = document.getElementById('num');
    const spec = document.getElementById('spec');
    const regexMin = new RegExp("[a-z]");
    const regexMaj = new RegExp("[A-Z]");
    const regexNum = new RegExp("[0-9]");
    const regexSpec = new RegExp("[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>\\/?]");
    if (password.length > 11) {
        char_checked = true;
        correct += 1;
    }
    else {
        char_checked = false
    }
    if (regexMin.test(password)) {
        min_checked = true;
        correct += 1;
    }
    else {
        min_checked = false
    }
    if (regexMaj.test(password)) {
        maj_checked = true;
        correct += 1;
    }
    else {
        maj_checked = false
    }
    if (regexNum.test(password)) {
        num_checked = true;
        correct += 1;
    }
    else {
        num_checked = false
    }
    if (regexSpec.test(password)) {
        spec_checked = true;
        correct += 1;
    }
    else {
        spec_checked = false
    }
    if (correct === 5) {
        return true
    } else { return false }
}
function updateCheckboxes() {
    if (char_checked) {
        document.getElementById('char').checked = true;
    }
    else {
        document.getElementById('char').checked = false;
    }
    if (min_checked) {
        document.getElementById('min').checked = true;
    }
    else {
        document.getElementById('min').checked = false;
    }
    if (maj_checked) {
        document.getElementById('maj').checked = true;
    }
    else {
        document.getElementById('maj').checked = false;
    }
    if (num_checked) {
        document.getElementById('num').checked = true;
    }
    else {
        document.getElementById('num').checked = false;
    }
    if (spec_checked) {
        document.getElementById('spec').checked = true;
    }
    else {
        document.getElementById('spec').checked = false;
    }
}

document.getElementById("password").addEventListener("input", () => {
    checkPass();
    updateCheckboxes();
});

document.querySelector("form").addEventListener("submit", function (e) {
    let password = document.getElementById("password").value;
    let confPass = document.getElementById("confPass").value;
    let email = document.getElementById('email').value;
    let confEmail = document.getElementById('confEmail').value;
    let tel = document.getElementById('tel').value.replace(/\D/g, '');
    const regexEmail = new RegExp("[A-Za-z0-9._-]+@[A-Za-z0-9-]+\\.[A-Za-z]{2,6}");
    const regexTel = new RegExp("0[0-9]{9}$");

    if (!checkPass()) {
        e.preventDefault();
        alert("Le mot de passe ne contient pas les minimus prérequis de sécurité");
        console.log("mdp invalide");
    } else if (password !== confPass) {
        e.preventDefault();
        alert("Les mots de passe ne sont pas identiques");
        console.log("mots de passe pas identiques");
    } else if (!regexEmail.test(email)) {
        e.preventDefault();
        alert("Le format de l'adresse email n'est pas valide");
        console.log("email invalide");
    } else if (email !== confEmail) {
        e.preventDefault();
        alert("Les adresses email ne sont pas identiques");
        console.log("email pas identiques");
    } else if (!regexTel.test(tel)) {
        e.preventDefault();
        alert("Le format du numéro de téléphone n'est pas valide");
        console.log("tel invalide");
    }
});