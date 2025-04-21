# Descrição: Dada uma lista de números inteiros, encontre o maior e o menor número da lista.

lista = [10, -5, 3, 8, 0, -2] #Lista de números inteiros
maior = lista[0] #Assume-se que o primeiro número da lista é o maior - 3
menor = lista[0] #Assume-se que o primeiro número da lista é o menor - 3

for numero in lista: #Faz um loop para cada número na lista
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("O maior número é:", maior)
print("O menor número é:", menor)
