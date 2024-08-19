'''
    Sabendo que uma Copiadora cobra R$ 0,08 por cada cópia feita, escreva um programa que
receba como entrada a quantidade de folhas de um livro e exiba o valor total a ser pago para
copiá-lo com duas casas decimais. (Lembrete: cada folha corresponde a duas páginas – frente
e verso)
'''

PRECO_COPIA = 0.08

quantidade_folhas = int(input("Informa a quantidade de folhas para impressão: "))
total_pagar = ( quantidade_folhas * 2 ) * PRECO_COPIA

print(f"O valor total a ser pago é R$ {total_pagar:.2f}")