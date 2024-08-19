'''
    2. Escreva um algoritmo que leia o código de um determinado produto e
mostre a sua classificação. Utilize a seguinte tabela como referências.
'''
codigo_produto = int(input("Informe o Código do Produto: "))

if(codigo_produto == 1):
    print(f"Classificação {codigo_produto} ")
    print("Alimento Não-perecível")

elif (codigo_produto == 2 or codigo_produto == 3 or codigo_produto == 4):
    print(f"Classificação {codigo_produto} ")
    print("Alimento perecível")

elif (codigo_produto == 5 or codigo_produto ==6):
    print(f"Classificação {codigo_produto}")
    print("Vestuário")

elif (codigo_produto == 7):
     print(f"Classificação {codigo_produto}")
     print("Higiene Pessoal")

elif (codigo_produto == 8 or codigo_produto == 15):
    print(f"Classificação {codigo_produto}")
    print("Limpeza e Utensílios Domésticos")

else:
    print("Inválido")