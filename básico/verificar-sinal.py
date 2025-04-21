"""
Desafio 04 - Verificar se um número é positivo, negativo ou zero

Descrição:
Peça ao usuário para digitar um número. O programa deve informar se ele é positivo, negativo ou igual a zero.

Exemplo:
Digite um número: -7  
Saída: O número é negativo.
"""

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
