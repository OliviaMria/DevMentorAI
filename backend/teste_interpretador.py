from interpretador import interpretar_mensagem


mensagem = "Estou trabalhando num projeto de uma loja online"

resultado = interpretar_mensagem(mensagem)

print("\nResultado:")
print("Tipo:", resultado["tipo"])
print("Valor:", resultado["valor"])