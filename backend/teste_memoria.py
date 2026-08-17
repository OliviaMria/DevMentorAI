from memoria import (
    guardar_informacao,
    obter_informacao,
    mostrar_perfil
)

guardar_informacao("nome", "Ana")
guardar_informacao("linguagem", "Python")
guardar_informacao("nivel", "iniciante")
guardar_informacao("objetivo", "Aprender desenvolvimento de software")

print("Nome:", obter_informacao("nome"))
print("Linguagem:", obter_informacao("linguagem"))

mostrar_perfil()
