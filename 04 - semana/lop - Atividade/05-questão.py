'''
5. Escreva um algoritmo que determine o número de dias que uma
pessoa já viveu até a data de HOJE (26/06/2024). Considere que um
mês tenha 30 dias.
'''


DIA = 26
MES = 6
ANO = 2024

data_nascimento  =  str(input("Por favor, informe sua data de nascimento (Dd/Mm/Aa) ")).split('/')

dia_nascimento   =  int(data_nascimento[0])
mes_nascimento   =  int(data_nascimento[1])
ano_nascimento   =  int(data_nascimento[2])

idade = ANO - ano_nascimento
meses = ( MES * 30 ) - 4

idade_em_dias = (idade * 365) + meses 

print(f"Parabéns voce já viveu {idade_em_dias}")