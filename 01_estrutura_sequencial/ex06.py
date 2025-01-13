# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print("=== Cálculo da Área de um Círculo ===\n")

raio = float(input("Insira o raio do círculo: "))
PI = 3.14 # constante
area = PI * (raio ** 2)

print(f"A área do círculo é igual a: {area:.2f}")