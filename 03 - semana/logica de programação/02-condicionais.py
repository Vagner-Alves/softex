'''
O circo chegou na cidade e estão sendo vendidos
ingressos a preços promocionais.

Todas as crianças até 5 anos pagam R$ 10, idosos com
60 anos ou mais pagam R$ 15, e os demais pagam R$ 25.

Escreva um programa que receba como entrada a idade
de uma pessoa e exiba o valor a ser pago pelo ingresso.

'''

INGRESSO = 25
INGRESSO_CRIANCA = 10
INGRESSO_IDOSO = 15

idade = int(input("Informa a sua Idade: "))

if ( idade <= 5 ):
    valor_ingresso = INGRESSO_CRIANCA

elif ( idade >= 60 ):
    valor_ingresso = INGRESSO_IDOSO

else:
    valor_ingresso = INGRESSO

print(f"Para pessoas com idade de até {idade} o Valor do ingresso é R$ {valor_ingresso}") 

