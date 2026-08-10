perfil = {
    "nome": "Carlos",
    "idade": 21,
    "nivel": "iniciante",
    "linguagens": ["Python", "JavaScript"],
    "objetivo": "Tornar-me desenvolvedor"
}


def mostrar_perfil():
    print("\n===== PERFIL =====")
    print("Nome:", perfil["nome"])
    print("Idade:", perfil["idade"])
    print("Nível:", perfil["nivel"])
    print("Objetivo:", perfil["objetivo"])


def mostrar_linguagens():
    print("\n===== LINGUAGENS =====")

    for linguagem in perfil["linguagens"]:
        print("-", linguagem)


def motivacao():
    print("\n===== DEVMENTOR =====")
    print("Não precisas saber tudo para começar.")
    print("Precisas começar para aprender.")


def estudar():
    print("\n===== MODO ESTUDO =====")
    print("1 - Python")
    print("2 - JavaScript")
    print("3 - HTML/CSS")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("Hoje vamos estudar Python!")

    elif opcao == "2":
        print("Hoje vamos estudar JavaScript!")

    elif opcao == "3":
        print("Hoje vamos estudar HTML e CSS!")

    else:
        print("Opção inválida.")


def menu():

    while True:

        print("\n================================")
        print("          DEVMENTOR AI")
        print("================================")

        print("\n1 - Ver meu perfil")
        print("2 - Ver linguagens")
        print("3 - Receber motivação")
        print("4 - Estudar")
        print("5 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            mostrar_perfil()

        elif opcao == "2":
            mostrar_linguagens()

        elif opcao == "3":
            motivacao()

        elif opcao == "4":
            estudar()

        elif opcao == "5":
            print("DevMentor encerrada. Até logo!")
            break

        else:
            print("Opção inválida.")


menu()