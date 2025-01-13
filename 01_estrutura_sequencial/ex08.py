# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("=== Cálculo de Sálario Mensal ===\n")

ganho_por_hora = float(input("Insira seu ganho por hora: "))
horas_trabalhadas = float(input("Insira o total de horas trabalhadas no mês: "))
salario = ganho_por_hora * horas_trabalhadas

print(f"O seu salário no mês é: R$ {salario:.2f}")