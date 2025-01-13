# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))

# verifica se os numeros sao iguais
if num1 == num2 == num3:
    print("Os números são iguais.")

# verifica o maior numero
if (num1 >= num2) and (num1 >= num3):
    maior = num1
elif (num2 >= num1) and (num2 >= num3):
    maior = num2
else:
    maior = num3

# verifica o menor numero
if (num1 <= num2) and (num1 <= num3):
    menor = num1
elif (num2 <= num1) and (num2 <= num3):
    menor = num2
else:
    menor = num3
    
print(f"\nMaior número inserido: {maior}\nMenor número inserido: {menor}")