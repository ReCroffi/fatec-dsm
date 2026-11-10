/*
descricao: Exercicio aula 13.
nome_arquivo: main.js
nome_exercicio: Exercício 13 - Formulários de Perfil e Cadastro
nome_aluno: Renan Croffi
email_aluno: renan.croffi@aluno.cps.sp.gov.br
turma: WEBI-ISW028-A
*/

function validarPerfil() {
  let form = document.forms['perfil'];

  if (form['email'].value == '') {
    alert('Email deve ser preenchido');
    return false;
  }
  if (form['senha'].value == '') {
    alert('Senha deve ser preenchida');
    return false;
  }
  if (form['senha'].value.length < 6) {
    alert('Senha deve ter pelo menos 6 caracteres');
    return false;
  }
  if (form['sexo'].value == '') {
    alert('Escolha uma opção de sexo');
    return false;
  }
  if (!form.querySelector('input[name="interesses"]:checked')) {
    alert('Marque pelo menos um interesse');
    return false;
  }
  if (form['curso'].value == '') {
    alert('Selecione um curso');
    return false;
  }
  if (form['sobre'].value == '') {
    alert('Escreva algo sobre você');
    return false;
  }
}

function validarCadastro() {
  let form = document.forms['cadastro'];

  if (form['nome'].value == '') {
    alert('Nome deve ser preenchido');
    return false;
  }
  if (form['email'].value == '') {
    alert('Email deve ser preenchido');
    return false;
  }
  if (form['senha'].value.length < 6) {
    alert('Senha deve ter pelo menos 6 caracteres');
    return false;
  }
  if (form['senha'].value != form['confirma'].value) {
    alert('As senhas não são iguais');
    return false;
  }
  if (!form['termos'].checked) {
    alert('Aceite os termos de uso');
    return false;
  }
}
