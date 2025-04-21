"""
Desafio 09 - Soma de 1 até N

Descrição:
Peça ao usuário para digitar um número inteiro N. Some todos os números de 1 até N e exiba o resultado.

Exemplo:
Entrada: 5  
Saída: A soma de 1 até 5 é: 15
"""

n = int(input("Digite um número inteiro: "))
soma = 0

for i in range(1, n + 1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")
