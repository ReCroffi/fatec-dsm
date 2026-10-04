

function validateForm() {
    let x = document.forms['login']['email'].value;
    if (x == '') {
        alert('Email deve ser preenchido');
        return false;
    }
    let y = document.forms['login']['password'].value;
    if (y == '') {
        alert('Senha deve ser preenchida');
        return false;
    }
}
