"""
Desafio 11 - Verificar Ano Bissexto

Descrição:
Peça ao usuário que digite um ano. O programa deve informar se o ano é bissexto.

Exemplo:
Entrada: 2024  
Saída: O ano 2024 é bissexto.
"""

# Entrada do usuário
ano = int(input("Digite um ano: "))

# Verificação de ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
