# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

if num1 == num2 == num3:
    print("Todos números são iguais.")
elif num1 > num2 and num1 > num3:
    print("O primeiro número é maior.")
elif num2 > num1 and num2 > num3:
    print("O segundo número é maior.")
else:
    print("O terceiro número é maior.")