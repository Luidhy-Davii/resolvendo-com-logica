"""
Desafio 09 - Contador de Palavras

Descrição:
Peça ao usuário uma frase e informe quantas palavras ela possui.

Exemplo:
Entrada: "Olá, tudo bem com você?"
Saída: Número de palavras: 5
"""

# Entrada do usuário
frase = input("Digite uma frase: ")

# Quebra a frase em palavras usando split
palavras = frase.split()

# Exibe a quantidade de palavras
print(f"Número de palavras: {len(palavras)}")
