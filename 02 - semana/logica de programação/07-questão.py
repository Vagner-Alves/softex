'''
Todos os anos, os motoristas devem pagar ao Detran o IPVA (Imposto sobre a Propriedade de
Veículos Automotores) e uma taxa de trânsito. Caso paguem o IPVA com antecedência,
recebem um desconto de 5% apenas no valor desse imposto. Escreva um programa que
receba como entrada o valor do IPVA e o valor da taxa de trânsito, e exiba o total a ser pago
(com duas casas decimais de precisão) por um motorista que deseja quitar sua dívida cinco
dias antes do prazo.
'''

valor_ipva = float(input("Informe o valor do IPVA: "))
taxa_transito = float(input("Informe o valor da Taxa de trânsito: "))
desconto_antecipado = valor_ipva * 0.05

# valor a ser pago por um motorista que quitou a dívida antecipadamente ( - 5%)
valor_total = (valor_ipva - desconto_antecipado) + taxa_transito 
print(f"O total a ser Pago é de R${valor_total:.2f}")