"""
Desafio 08 - Verificar Palíndromo

Descrição:
Peça ao usuário que digite uma palavra ou frase. O programa deve informar se o texto é um palíndromo, ou seja, se pode ser lido da mesma forma de trás para frente (ignorando espaços e diferenças entre maiúsculas e minúsculas).

Exemplo:
Entrada: "arara"  
Saída: A palavra/frase é um palíndromo.
"""

#Entrada do usuário.
texto = input("Digite uma palavra ou frase: ")

#Remover espaços e converter para maiusculas.
texto_formatado = texto.replace(" ", "").lower()
#invertendo o texto.
invertido = texto_formatado[::-1]
#Verificação


if texto_formatado == invertido: 
    print("A palavra/frase é um palíndromo.")
else:
    print("A palavra/frase não é um palíndromo.")
