import requests
import json


def interpretar_mensagem(mensagem):
    prompt = f"""
Analisa a mensagem de um estudante de programação.

Tu deves identificar se a mensagem contém uma destas informações:

1. nome
2. linguagem
3. nivel
4. objetivo
5. projeto
6. nenhuma

REGRAS IMPORTANTES:

- Se a pessoa disser que está trabalhando, desenvolvendo, criando ou fazendo um projeto, o tipo deve ser "projeto".
- "Estou trabalhando num projeto de uma loja online" significa:
  tipo = "projeto"
  valor = "uma loja online"
- Não respondas "nenhuma" quando a pessoa mencionar um projeto.

Exemplos:

Mensagem: "Estou aprendendo Python"
Resposta:
{{"tipo": "linguagem", "valor": "Python"}}

Mensagem: "Sou iniciante"
Resposta:
{{"tipo": "nivel", "valor": "iniciante"}}

Mensagem: "Meu objetivo é aprender desenvolvimento web"
Resposta:
{{"tipo": "objetivo", "valor": "aprender desenvolvimento web"}}

Mensagem: "Estou trabalhando num projeto de uma loja online"
Resposta:
{{"tipo": "projeto", "valor": "uma loja online"}}

Mensagem: "Estou criando um site para uma escola"
Resposta:
{{"tipo": "projeto", "valor": "um site para uma escola"}}

Se realmente não existir nenhuma informação relevante:
{{"tipo": "nenhuma", "valor": ""}}

Responde SOMENTE com JSON válido.

Mensagem do estudante:
{mensagem}
"""

    resposta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    dados = resposta.json()

    return json.loads(dados["response"])