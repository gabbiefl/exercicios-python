"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

salario_inicial = float(input("Digite seu salário: "))

if salario_inicial <= 280:
    percentual_aumento = 0.20
    aumento = salario_inicial * percentual_aumento
    salario_final = salario_inicial + aumento
    print(f"Salário antes do reajuste: R$ {salario_inicial:.2f}\nPercentual de aumento aplicado: {percentual_aumento:.2f} %\nValor do aumento: R$ {aumento:.2f}\nSalário final: R$ {salario_final:.2f}")
elif 280 < salario_inicial <= 700:
    percentual_aumento = 0.15
    aumento = salario_inicial * percentual_aumento
    salario_final = salario_inicial + aumento
    print(f"Salário antes do reajuste: R$ {salario_inicial:.2f}\nPercentual de aumento aplicado: {percentual_aumento:.2f}%\nValor do aumento: R$ {aumento:.2f}\nSalário final: R$ {salario_final:.2f}")
elif 700 < salario_inicial <= 1500:
    percentual_aumento = 0.10
    aumento = salario_inicial * percentual_aumento
    salario_final = salario_inicial + aumento
    print(f"Salário antes do reajuste: R$ {salario_inicial:.2f}\nPercentual de aumento aplicado: {percentual_aumento:.2f}%\nValor do aumento: R$ {aumento:.2f}\nSalário final: R$ {salario_final:.2f}")
else:
    percentual_aumento = 0.05
    aumento = salario_inicial * percentual_aumento
    salario_final = salario_inicial + aumento
    print(f"Salário antes do reajuste: R$ {salario_inicial:.2f}\nPercentual de aumento aplicado: {percentual_aumento:.2f}%\nValor do aumento: R$ {aumento:.2f}\nSalário final: R$ {salario_final:.2f}")