# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))


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

# verifica o numero do meio
if (num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
    meio = num1
elif (num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
    meio = num2
else:
    meio = num3

print(f"Em ordem decrescente: {maior}, {meio}, {menor}")