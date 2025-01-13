# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Insira um número: "))

if 0 < valor:
    print("O número é positivo.")
elif 0 > valor:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")
