print("==============================")
print("🤖 DevMentor AI")
print("==============================")


nome = input("Olá! Qual é o teu nome? ")

nivel = input(
    "Qual o teu nível? (iniciante/intermedio/avancado): "
)


if nivel == "iniciante":

    print(
        "Ótimo", nome,
        "Vamos começar pelos fundamentos."
    )


elif nivel == "intermedio":

    print(
        "Muito bem", nome,
        "Vamos trabalhar projetos."
    )


elif nivel == "avancado":

    print(
        "Excelente", nome,
        "Vamos estudar arquitetura e IA."
    )


else:

    print(
        "Ainda não conheço esse nível."
    )

    personalidade = """
Sou uma assistente paciente,
explico programação de forma simples
e incentivo jovens desenvolvedores.
"""
