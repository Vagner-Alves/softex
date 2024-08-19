'''
1 - Paula tem uma gráfica e cobra R$ 0.80 por folha impressa. Escreva um programa que leia a quantidade de folhas que alguém deseja imprimir e calcule e 
exiba (1 casa decimal) o valor a ser pago. 
'''

PRECO = 0.80

quantidade_folhas = int(input("Informe quantas folhas deseja imprimir: "))

total_pagar = quantidade_folhas * PRECO

print(f"O valor a ser pago R$: {total_pagar:.1f} ")