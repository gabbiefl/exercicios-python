# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print("=== Conversão Fahrenheit → Celsius ===\n")

F = float(input("Digite a temperatura em graus Fahrenheit:"))
C = 5 * ((F - 32) / 9)

print(f"A temperatura em Celsius corresponde a {C:.2f} °C")