if (sessionStorage.getItem("authenticated") !== "true") {
  window.location.href = "./index.html";
}

const profileForm = document.querySelector("#profileForm");
const profileFields = profileForm.querySelectorAll("input, textarea");
const editButton = document.querySelector("#editButton");
const saveButton = document.querySelector("#saveButton");
const cancelButton = document.querySelector("#cancelButton");
const profileMessage = document.querySelector("#profileMessage");
const logoutLink = document.querySelector("#logoutLink");
const photoInput = document.querySelector("#photo");
const profilePhoto = document.querySelector("#profilePhoto");

let originalValues = {};
const originalPhoto = profilePhoto.src;

logoutLink.addEventListener("click", () => {
  sessionStorage.removeItem("authenticated");
});

function setEditing(isEditing) {
  profileFields.forEach((field) => {
    field.disabled = !isEditing;
  });

  editButton.hidden = isEditing;
  saveButton.hidden = !isEditing;
  cancelButton.hidden = !isEditing;
}

editButton.addEventListener("click", () => {
  originalValues = Object.fromEntries(
    [...profileFields].map((field) => [field.id, field.value]),
  );
  profileMessage.textContent = "";
  setEditing(true);
});

cancelButton.addEventListener("click", () => {
  profileFields.forEach((field) => {
    field.value = originalValues[field.id];
  });
  photoInput.value = "";
  profilePhoto.src = originalPhoto;
  profileMessage.textContent = "";
  setEditing(false);
});

photoInput.addEventListener("change", () => {
  const [selectedPhoto] = photoInput.files;

  if (selectedPhoto) {
    profilePhoto.src = URL.createObjectURL(selectedPhoto);
  }
});

profileForm.addEventListener("submit", (event) => {
  event.preventDefault();
  profileMessage.textContent = "Alterações salvas com sucesso.";
  setEditing(false);
});
