import requests

def perguntar_ollama(pergunta):
    resposta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": pergunta,
            "stream": False
        }
    )

    dados = resposta.json()

    return dados["response"]


print("🤖 DevMentorAI")
print("Digite 'sair' para terminar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("Até logo!")
        break

    resposta = perguntar_ollama(pergunta)

    print("DevMentor:", resposta)