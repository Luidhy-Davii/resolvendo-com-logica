"""
Desafio 13 - Gerador de Tabuada

Descrição:
Gerar a tabuada de um número informado pelo usuário, multiplicando-o de 1 a 10.

Exemplo:
Digite um número para gerar a tabuada: 7
Saída:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
"""

# Solicitar número ao usuário
numero = int(input("Digite um número para gerar a tabuada: "))

# Gerar e exibir a tabuada
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")