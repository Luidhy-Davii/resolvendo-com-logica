"""
Desafio 06 - Par ou Ímpar

Descrição:
Dada uma lista de números inteiros, conte quantos números pares e quantos ímpares existem nela.

""" 
# Lista fixa de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Contadores
pares = 0
impares = 0

# Verificação
for numero in numeros:
    if numero % 2 == 0: 
        pares += 1
    else:
        impares += 1

# Resultado
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
