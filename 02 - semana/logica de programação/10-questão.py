'''
Um restaurante self-service de Palmares cobra R$ 20 por quilo nas refeições. Sabendo que, na
hora de determinar o valor da refeição, deve ser desconsiderado o peso do prato vazio (230
gramas), escreva um programa que receba como entrada o peso total do prato de um cliente
em gramas e exiba o preço cobrado com duas casas decimais. (Lembrete: 1 quilo = 1000
gramas)
'''

PRECO_KILO = 20.0

peso_prato = float(input("Informe o peso do seu prato (gramas): ")) / 1000
peso_prato = peso_prato - 0.230
total_pagar = peso_prato * PRECO_KILO

print(f"O valor total a ser pago é de R$ {total_pagar:.2f}")

