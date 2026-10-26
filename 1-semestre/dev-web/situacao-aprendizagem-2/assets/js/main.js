const loginForm = document.querySelector("#loginForm");
const loginMessage = document.querySelector("#loginMessage");

const demoUser = {
  username: "admin",
  password: "123456",
};

loginForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const username = document.querySelector("#username").value.trim();
  const password = document.querySelector("#password").value;

  if (
    username === demoUser.username &&
    password === demoUser.password
  ) {
    sessionStorage.setItem("authenticated", "true");
    window.location.href = "./perfil.html";
    return;
  }

  loginMessage.textContent = "Usuário ou senha inválidos.";
});