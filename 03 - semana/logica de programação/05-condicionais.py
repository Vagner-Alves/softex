'''
    Um ano é bissexto se for divisível por 4. Exceção a essa regra são os anos divisíveis por 100, os quais não são bissextos. 
    Exceção a essa segunda regra são os anos divisíves por 400, os quais são bissextos. 
    Escreva um programa que leia um número e escreva se ele corresponde ou não a um ano bissexto.
    É possíve usar um único "if" com condição composta para determinar se o ano é bissexto.
'''

ano = int(input("Informe o Ano para Saber se é ou não Bisexto: "))

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não se trata de um ano bissexto!")