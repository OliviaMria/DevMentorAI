import ollama

resposta = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Olá! Explica em uma frase o que é Python."
        }
    ]
)

print(resposta["message"]["content"])