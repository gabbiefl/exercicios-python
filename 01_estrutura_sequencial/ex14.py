# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoPeixe = float(input("Digite o peso do peixe:"))
multa = 4.00

if pesoPeixe > 50:
    excessoPeso = pesoPeixe - 50
    multaTotal = excessoPeso * multa
    print(f"O peso do peixe corresponde a {pesoPeixe:.2f} kg, logo o limite de peso foi excedido por {excessoPeso:.2f} kg. Você deverá pagar uma multa de R$ {multaTotal:.2f} ")
else:
    print(f"O peso do peixe corresponde a {pesoPeixe:.2f} kg. O limite de peso não foi excedido, logo, não terá que pagar multa.")