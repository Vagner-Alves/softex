'''
Todos os funcionários de uma empresa
precisam pagar impostos, mas o
percentual varia de acordo com o salário

Funcionários que ganham mais de R$
1000 pagam 17% de imposto, e os demais
pagam 8% de imposto

Escreva um programa que receba como
entrada o salário de um funcionário e
exiba o valor do imposto que ele terá
que pagar
'''
IMPOSTO_MAIOR = 0.17
IMPOSTO_MENOR = 0.08

salario = float(input("Informe o valor do seu Salário: "))

if salario >= 1000:
    imposto = salario * IMPOSTO_MAIOR
    
else:
    imposto = salario * IMPOSTO_MENOR

print(f"é preciso pagar um imposto de R$ {imposto:.2f}")