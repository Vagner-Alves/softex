'''
4 - Uma pequena pousada tem quartos disponíveis para uma e duas pessoas. Escreva um código que calcula o valor total a ser pago pelos hóspedes. 
Pergunte quantos dias o hóspede passou e quantas pessoas ocupou o quarto. 
Para uma pessoa o valor cobrado será 110,00 reais por diária e 130,00 reais se forem duas. 
Imprima o valor total a ser pago, com 2 casas decimais.
'''

PRECO_SOLO = 110
PRECO_CASAL = 130

quantidade_hospedes = int(input("Informe a quantidade de Hospodes na Pousada: "))
quantidade_dias = int(input("Informe a quantidade de Dias na Pousada: "))


if ( quantidade_hospedes == 1 ):
    valor_pagar = quantidade_dias * PRECO_SOLO

else:
    valor_pagar = quantidade_dias * PRECO_CASAL

print(f"O valor total a ser pago R${valor_pagar:.2f}")