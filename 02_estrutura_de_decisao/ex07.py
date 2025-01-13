# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print("\n== Primeiro Produto: ==\nInsira as seguintes informações:\n")
nome_produto1 = input("Nome = ___")
valor_produto1 = float(input("Valor = ___"))

print("\n== Segundo Produto: ==\n Insira as seguintes informações:\n")
nome_produto2 = input("Nome = ___")
valor_produto2 = float(input("Valor = ___"))

print("\n== Terceiro Produto: ==\n Insira as seguintes informações:\n")
nome_produto3 = input("Nome = ___")
valor_produto3 = float(input("Valor = ___"))

if (valor_produto1 < valor_produto2) and (valor_produto1 < valor_produto3):
    produto_mais_barato = nome_produto1
    print(f"\nVocê deve comprar o produto {produto_mais_barato} por R$ {valor_produto1:.2f}")
elif (valor_produto2 < valor_produto1) and (valor_produto2 < valor_produto3):
    produto_mais_barato = nome_produto2
    print(f"\nVocê deve comprar o produto {produto_mais_barato} por R$ {valor_produto2:.2f}")
else:
    produto_mais_barato = nome_produto3
    print(f"\nVocê deve comprar o produto {produto_mais_barato} por R$ {valor_produto3:.2f}")
