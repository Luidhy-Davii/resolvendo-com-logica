"""
Desafio 05 - Calcular a Média de uma Lista de Números

Descrição:
Peça ao usuário que informe uma quantidade de números. Em seguida, calcule e exiba a média aritmética desses números.

Exemplo de entrada:
Quantos números deseja informar? 4  
Digite o número 1: 10  
Digite o número 2: 20  
Digite o número 3: 30  
Digite o número 4: 40

Saída esperada:
A média dos números é: 25.0
"""

# Entrada da quantidade de números
quantidade = int(input("Quantos números deseja informar? "))

# Lista para armazenar os números
numeros = []

# Coletando os números
for i in range(quantidade):
    num = float(input(f"Digite o número {i + 1}: "))
    numeros.append(num)

# Calculando a média
media = sum(numeros) / len(numeros)

# Exibindo o resultado
print(f"A média dos números é: {media}")
