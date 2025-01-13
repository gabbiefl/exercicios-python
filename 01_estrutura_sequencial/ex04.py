# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

import time

print("=== Cálculo de Notas Bimestrais ===")
print("\nBem-vindo(a)!")

primeiro_bimestre = float(input("Insira a nota do 1° Bimestre: "))
segundo_bimestre = float(input("Insira a nota do 2° Bimestre: "))
terceiro_bimestre = float(input("Insira a nota do 3° Bimestre: "))
quarto_bimestre = float(input("Insira a nota do 4° Bimestre: "))

print("Calculando a média bimestral...\n")
time.sleep(2)

media = (primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre) / 4

print(f"A média bimestral do aluno é igual a: {media:.2f}")

if media >= 6:
    print("Parabéns! Você foi aprovado. =)")
else: 
    print("Não foi dessa vez! Você está de recuperação! =(")