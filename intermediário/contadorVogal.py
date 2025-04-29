"""
Desafio 26 - Contagem de Vogais

Descrição:
Peça ao usuário que digite uma palavra ou frase. O programa deve contar quantas vogais (A, E, I, O, U) existem no texto, ignorando diferenças entre maiúsculas e minúsculas.

Exemplo:
Entrada: "Computação"
Saída: O texto contém 5 vogais.
"""

# Entrada do usuário
texto = input("Digite uma palavra ou frase: ")

# Contagem de vogais
vogais = "aeiou"
contador_vogais = sum(1 for char in texto.lower() if char in vogais)

print(f"O texto contém {contador_vogais} vogais.")
