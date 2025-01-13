# Faça um Programa que converta metros para centímetros.

print("=== Conversor de Medidas ===\n")

tipo_conversao = int(input("Bem-vindo(a)! Insira o número correspondente ao tipo de conversão desejada: \n [1] M → CM \n [2] CM → M "))


def metros_para_centimetros():
    valor = float(input("Insira o valor, em M, a ser convertido em CM: "))
    return valor * 100

def centimetros_para_metros():
    valor = float(input("Insira o valor, em CM, a ser convertido em M: "))
    return valor / 100

if tipo_conversao == 1:
    resultado = metros_para_centimetros()
    print(f"Resultado = {resultado:.2f} CM")
elif tipo_conversao == 2:
    resultado = centimetros_para_metros()
    print(f"Resultado = {resultado:.2f} M")
else:
    print("[ERRO]: Insira 1 ou 2.") 
    quit()