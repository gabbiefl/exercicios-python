# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("=== Cálculo da Área de um Quadrado ===\n")

lado = float(input("Insira a medida de um dos lados do quadrado: "))

area = lado ** 2
dobro_area = area * 2

print(f"A área do quadrado é igual a: {area:.2f} cm²")
print(f"O DOBRO da área do quadrado é igual a: {dobro_area:.2f} cm² ")