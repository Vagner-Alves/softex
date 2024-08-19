'''
3 - Escreva um programa que leia o nome e quantidade de horas que uma pessoa dorme por dia e calcule e exiba como saída o percentual de
 tempo ela passa dormindo (com duas casas decimais). 
 O resultado deve ser apresentado da seguinte forma: 
 “Fulano, você passa XX% do seu tempo de vida dormindo.” 
 Onde Fulano é o nome que o usuário informou e XX é o resultado do cálculo do percentual. 
 (Cálculo do percentual é dado pela fórmula= horas dormidas /24*100).

'''

nome = str(input("Informe seu Nome: ")).capitalize()
horas_dormidas = int(input("Quantas Horas voce dorme por noite?: "))

calculo = horas_dormidas / 24 * 100

print(f"{nome}, você passa {calculo:.2f}% do seu tempo de vida dormindo.")
