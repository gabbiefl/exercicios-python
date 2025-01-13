# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def verificar_letra():
    letra = input("Insira uma letra: ").upper()
    VOGAIS = ["A", "E", "I", "O", "U"] # lista de vogais

    if letra.isdigit():
        print("Valor inválido, insira uma 'letra'.")
        verificar_letra()
    elif letra in VOGAIS:
        print("A letra digitada é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")

verificar_letra()