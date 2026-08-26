const input = document.getElementById("messageInput");
const button = document.getElementById("sendButton");
const chat = document.querySelector(".chat");

button.addEventListener("click", enviarMensagem);

input.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    enviarMensagem();
  }
});

function enviarMensagem() {
  const mensagem = input.value.trim();

  if (mensagem === "") {
    return;
  }

  adicionarMensagem("Você", mensagem, "user");

  input.value = "";
}

function adicionarMensagem(nome, texto, tipo) {
  const mensagem = document.createElement("div");

  mensagem.classList.add("message", tipo);

  mensagem.innerHTML = `
        <strong>${nome}</strong>
        <p>${texto}</p>
    `;

  chat.appendChild(mensagem);

  chat.scrollTop = chat.scrollHeight;
}
