# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print("=== Conversão Celsius → Fahrenheit ===\n")

C = float(input("Digite a temperatura em Celsius: "))
F = (C * 9 / 5) + 32

print(f"A temperatura em Fahrenheit corresponde a: {F:.2f} °F")
