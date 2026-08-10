print("==============================")
print("       DevMentor AI")
print("==============================")

nome = input("Qual é o teu nome? ")
idade = input("Qual é a tua idade? ")
linguagem = input("Qual linguagem estás a estudar? ")
nivel = input("Qual é o teu nível? ")
objetivo = input("Qual é o teu objetivo? ")

perfil = {
    "nome": nome,
    "idade": idade,
    "linguagem": linguagem,
    "nivel": nivel,
    "objetivo": objetivo
}

print()
print("Perfil criado!")
print("------------------------------")

print("Nome:", perfil["nome"])
print("Idade:", perfil["idade"])
print("Linguagem:", perfil["linguagem"])
print("Nível:", perfil["nivel"])
print("Objetivo:", perfil["objetivo"])