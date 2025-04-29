"""
Desafio 24 - Verificar Anagrama

Descrição:
Solicite duas palavras ao usuário e verifique se elas são anagramas, ou seja, se possuem as mesmas letras em quantidade igual, mas em ordem diferente.

Exemplo:
Entrada: "amor" e "roma"  
Saída: As palavras são anagramas.
"""

# Entrada do usuário
palavra1 = input("Digite a primeira palavra: ").lower().replace(" ", "")
palavra2 = input("Digite a segunda palavra: ").lower().replace(" ", "")

# Verificação
if sorted(palavra1) == sorted(palavra2):
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")
