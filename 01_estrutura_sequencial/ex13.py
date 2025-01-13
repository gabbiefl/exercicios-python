# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7

sexo = int(input("Digite o número correspondente ao seu sexo: 1- feminino, 2- masculino"))
altura = float(input("Digite a sua altura em metros:"))

if sexo == 1:
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal corresponde a: {pesoIdeal:.2f} kg")
elif sexo == 2:
    pesoIdeal = (72.7 * altura) - 58
    print(f"Seu peso ideal corresponde a: {pesoIdeal:.2f} kg")
else:
    print("[ERRO]: Insira 1 ou 2.")
    quit()
