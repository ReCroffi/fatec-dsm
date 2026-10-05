/*
descricao: Exercicio aula 12.
nome_arquivo: login.html
nome_exercicio: Exercício 12 - Formulário de Login
nome_aluno: Renan Croffi
email_aluno: renan.croffi@aluno.cps.sp.gov.br
turma: WEBI-ISW028-A
*/

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
