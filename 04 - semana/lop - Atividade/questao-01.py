'''
    Claro! Aqui está um algoritmo em Python que lê três valores
     inteiros diferentes e os mostra em ordem decrescente:
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

maior_valor = valor1

if ( valor2 > maior_valor):
    maior_valor = valor2

if (valor3 > maior_valor):
    maior_valor = valor3


menor_valor = valor1

if ( valor2 < menor_valor):
    menor_valor = valor2

if (valor3 < menor_valor):
    menor_valor = valor3

valor_meio = valor1 + valor2 + valor3 - maior_valor - menor_valor

print(f"Números em ordem decrescente: {maior_valor}, {valor_meio}, {menor_valor}")