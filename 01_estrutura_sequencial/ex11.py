# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # o produto do dobro do primeiro com metade do segundo;
    # a soma do triplo do primeiro com o terceiro;
    # o terceiro elevado ao cubo.

n1 = int(input("Digite um número inteiro:"))
n2 = int(input("Digite outro número inteiro:"))
n3 = float(input("Agora, digite um número real:"))
print(f"n1: {n1}, n2: {n2}, n3: {n3}")

resultado1 = (2 * n1) * (n2 / 2)
print(f"O produto do dobro do primeiro com metade do segundo resulta em: {resultado1:.2f}")

resultado2 = (3 * n1) + n3
print(f"A soma do triplo do primeiro com o terceiro resulta em: {resultado2:.2f}")

resultado3 = n3 ** 3
print(f"O terceiro elevado ao cubo resulta em: {resultado3:.2f}")