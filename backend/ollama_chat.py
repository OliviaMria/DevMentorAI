import requests
from memoria import carregar_memoria, guardar_informacao


def perguntar_ollama(pergunta):
    memoria = carregar_memoria()

    resposta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": f"""
Tu és a DevMentor AI, uma assistente virtual criada para ajudar jovens desenvolvedores.

O teu objetivo é ensinar programação de forma clara, paciente e prática.

Regras:
- Explica os conceitos de forma simples.
- Incentiva o estudante a pensar e aprender.
- Quando apresentares código, explica o que ele faz.
- Não assumes que o estudante já conhece conceitos avançados.
- Quando houver um erro, explica primeiro a causa e depois mostra como corrigir.
- Mantém uma atitude positiva e motivadora.

Perfil do estudante:
- Nome: {memoria.get("nome", "não informado")}
- Linguagem: {memoria.get("linguagem", "não informado")}
- Nível: {memoria.get("nivel", "não informado")}
- Objetivo: {memoria.get("objetivo", "não informado")}

Pergunta do estudante:
{pergunta}
""",
            "stream": False
        }
    )

    dados = resposta.json()

    return dados["response"]


print("🤖 DevMentorAI")
print("Digite 'sair' para terminar.\n")


while True:
    pergunta = input("Você: ")

    texto = pergunta.lower()

    if texto.startswith("estou estudando "):
        linguagem = pergunta[len("estou estudando "):].strip()

        guardar_informacao("linguagem", linguagem)

        print(
            f"DevMentor: Entendido! Vou guardar que estás estudando {linguagem}."
        )
        continue

    if texto == "sair":
        print("Até logo!")
        break

    resposta = perguntar_ollama(pergunta)

    print("DevMentor:", resposta)