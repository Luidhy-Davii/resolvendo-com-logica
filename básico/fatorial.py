"""
Desafio 10 - Calcular Fatorial

Descrição:
Peça ao usuário que digite um número inteiro e exiba o fatorial desse número.

Exemplo:
Entrada: 5  
Saída: 5! = 120
"""

# Entrada do usuário
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

# Cálculo do fatorial
for i in range(2, n + 1):
    fatorial *= i

# Saída formatada
print(f"{n}! = {fatorial}")
