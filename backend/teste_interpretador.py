from interpretador import interpretar_mensagem


mensagem = input("Escreve uma frase: ")

resultado = interpretar_mensagem(mensagem)

print("\nResultado:")
print("Tipo:", resultado["tipo"])
print("Valor:", resultado["valor"]) 