"""
Desafio 12 - Calcular Índice de Massa Corporal (IMC)

Descrição:
Solicitar peso (em kg) e altura (em metros) do usuário, calcular o IMC e classificar o resultado em categorias como "Abaixo do peso", "Peso normal" e "Obesidade".

Exemplo:
Digite seu peso (kg): 70
Digite sua altura (m): 1.75
Saída: IMC: 22.9 → Peso normal
"""

# Solicitar peso e altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcular IMC
imc = peso / (altura ** 2)

# Classificar o resultado
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

# Exibir resultado
print(f"IMC: {imc:.1f} → {classificacao}")