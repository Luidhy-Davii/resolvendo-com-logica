"""
Desafio 01 - Par ou Ímpar

Descrição:
Peça ao usuário que digite um número inteiro. Em seguida, informe se o número é par ou ímpar.

"""

# Entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verificação
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
