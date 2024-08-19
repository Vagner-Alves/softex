'''
Betina

trabalha em um escritório de advocacia e todos os dias analisa vários processos. Sabendo que
ela cumpre um expediente diário de 8h, escreva um programa que receba como entrada
quantos minutos ela leva para analisar cada processo, e exiba o total de processos revisados
em um dia de trabalho. (Dica: Uma hora tem 60 minutos) (Dica: um processo não pode ser
analisado parcialmente, apenas totalmente).
'''

HORA_TRABALHO = 8

tempo_revisao = int(input("Informa quantos minutos são necessário para revisar um processo: "))
revisoes_do_dia = (HORA_TRABALHO * 60) / tempo_revisao

print(f'Betina faz {revisoes_do_dia:.0f} revisões de processos por dia')