'''
Um edital de concorrência pública avaliará propostas considerando três critérios: qualidade, preço e prazo. Cada um dos três critérios recebe uma nota de 0 a 10. Escreva um programa que leia as notas de preço,
prazo e qualidade de uma proposta e escreva sua nota geral, 
baseando-se nos seguintes critérios:

Se a nota da qualidade for inferior a 7, a nota geral será 0 independentemente dos outros fatores.
Se a nota da qualidade for igual ou superior a 7, e a nota do preço for igual ou superior a 7, então a nota geral será a média das três notas, ou seja (qualidade + preço + prazo) / 3
Se a nota da qualidade for igual ou superior a 7 e a nota do preço for inferior a 7, então a nota geral será a média das três notas, mas com peso 2 para a nota do preço, ou seja, (qualidade + 2*preço + prazo)/4
'''

qualidade_nota  = float(input("Informe a nota / qualidade 0 a 10: "))
nota_preco      = float(input("Informe a nota / preço 0 a 10: "))
nota_prazo      = float(input("Informe a nota / Prazo 0 a 10: "))


if ( qualidade_nota < 7 ):
    nota_geral = 0

elif ( qualidade_nota >= 7 ) and ( nota_preco >= 7 ):
    nota_geral = (qualidade_nota + nota_preco + nota_prazo) / 3

else:
    nota_geral = (qualidade_nota + nota_preco * 2 + nota_prazo) / 4

print(f"Nota Geral da Proposta {nota_geral:.2f}")

