# Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")