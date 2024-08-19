'''
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagems de até 200km, 
e R$ 0,45 para viagens mais longas.
'''

MAIOR_PRECO = 0.50
MENOR_PRECO = 0.45

distancia = float(input("Informe a distancia que deseja percorre: "))

if (distancia <= 200):
    valor_passagem = distancia * MAIOR_PRECO

else:
    valor_passagem = distancia * MENOR_PRECO

print(f"{valor_passagem:.2f}")