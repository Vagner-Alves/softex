'''
Faça um programa para calcular o Índice de Massa Corporal (IMC) que é uma medida utilizada pela Organização Mundial de Saúde para avaliar o grau de obseidade de um indivíduo. 
O IMC é calculado pela relação entre o peso (em kg) dividido pelo quadrado da altura (em metros) do indivíduo. 
Uma vez calculdo o IMC, imprima-o e também informe a classificação resultante seundo a tabela fornecida pelo Sistema de Vigilância Alimentar Nutricional:

IMC < 18.5: Adulto com baixo peso.
18.5 <= IMC < 25: Adulto com peso adequado
25 <= IMC < 30. Adulto com sobrepeso
IMC >= 30: Adulto com obsesidade

'''

peso = float(input("Informe seu peso em KG: "))
altura = float(input("Informe sua Altura em metros: "))


IMC = peso / (altura ** 2)

if (IMC < 18.5):
    resultado_classificacao = "Adulto com baixo peso."

elif ( 18.5 <= IMC < 25):
    resultado_classificacao = "Adulto com peso adequado."

elif (25 <= IMC < 30 ):
    resultado_classificacao = "Adulto com sobrepeso."

else:
    resultado_classificacao = "Adulto com obesidade."

print(f"O seu IMC {IMC:.2f} é  considerado pela Organização Mundial da Saúde como: {resultado_classificacao}")