'''
Soraia foi fazer compras no supermercado de seu bairro e tomou um susto!! A dúzia de
laranjas está caríssima, custando R$ 9,00!! Escreva um programa que receba como entrada a
quantidade de laranjas que Soraia deseja comprar, e exiba o valor total necessário para
realizar a compra com duas casas decimais de precisão. (Dica: uma dúzia corresponde a 12
laranjas, mas cada laranja também pode ser vendida separadamente).
'''

VALOR_LARANJA  = 0.75

quantidade_laranja = float(input("Informe a quantidade de laranjas que deseja comprar: "))
total = quantidade_laranja * VALOR_LARANJA

print(f"Valor Total de {quantidade_laranja:.0f} Laranjas R$ {total:.2f}")