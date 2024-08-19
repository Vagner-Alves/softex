'''
    Escreva um programa que receba como entrada dois números inteiros e exiba a soma e o
produto entre eles.
'''

primeiro_numero = int(input("informe um número (inteiro): "))
segundo_numero = int(input("informe um número (inteiro) novamente: "))

soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero

print(f"{primeiro_numero} + {segundo_numero} = {soma}")
print(f"{primeiro_numero} * {segundo_numero} = {produto}")

