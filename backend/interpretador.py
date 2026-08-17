import requests
import json


def interpretar_mensagem(mensagem):
    prompt = f"""
Analisa a mensagem de um estudante de programação.

Determina se ele forneceu alguma destas informações:

- nome
- linguagem
- nivel
- objetivo
- projeto
- nenhuma

Responde SOMENTE com JSON válido neste formato:

{{
    "tipo": "nome",
    "valor": "Ana"
}}

Se não houver nenhuma informação relevante:

{{
    "tipo": "nenhuma",
    "valor": ""
}}

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