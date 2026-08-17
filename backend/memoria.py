import json
import os

ARQUIVO_MEMORIA = os.path.join( 
    os.path.dirname(__file__),
    "memoria.json"
)


def carregar_memoria():
    if os.path.exists(ARQUIVO_MEMORIA):
        with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return {}


def guardar_memoria(memoria):
    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as arquivo:
        json.dump(memoria, arquivo, indent=4, ensure_ascii=False)


def guardar_informacao(chave, valor):
    memoria = carregar_memoria()

    memoria[chave] = valor

    guardar_memoria(memoria)

def obter_informacao(chave):
    memoria = carregar_memoria()

    return memoria.get(chave)


def mostrar_perfil():
    memoria = carregar_memoria()

    print("\n===== PERFIL DO DEV =====")

    if not memoria:
        print("Ainda não existem informações.")
        return

    for chave, valor in memoria.items():
        print(f"{chave}: {valor}")

    print("=========================\n")
 