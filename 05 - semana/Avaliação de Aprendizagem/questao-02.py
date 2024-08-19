'''
2 - IF Tech é uma empresa que paga seus funcionários pelas horas trabalhadas. 
Escreva um programa que pergunte quanto o funcionário ganha por hora e o número de horas trabalhadas por dia e calcule e exiba como saída o 
valor do salário desse funcionário no mês. (Considere que em um mês se trabalha 22 dias).
'''

MES_TRABALHO = 22

valor_hora = float(input("Informe o valor da Hora de Trabalho: "))
quantidade_hora = int(input("Informe a quantidade de Horas Trabalhadas: "))

valor_salario = quantidade_hora * valor_hora * MES_TRABALHO

print(f"O valor do Seu Salário Mensal é de R${valor_salario:.2f}")

