'''
Faça um algoritmo que leia quatro números (Opção, Num1, Num2 e
Num3) e mostre a soma dos números se Opção for 2; o produto se
Opção for 3; e se a soma de Num1 com Num2 é maior, menor ou igual
a Num3 se Opção for 4. Os únicos valores aceitáveis para a variável
Opção são 2, 3 e 4.
'''

numero1  = int(input("Informe um Número: "))
numero2  = int(input("Informe um outro Número: "))
numero3  = int(input("Informe um outro Número: "))

print('''
2 - Somar os Números
3 - Multiplicar os Números (Produto)
4 - Comparar a os Números
1 - Para sair    ''')


opcao = int(input("Escolha uma Opção: "))

if (opcao == 2):
    soma = numero1 + numero2 + numero3
    print(soma)

elif (opcao == 3 ):
    produto =  numero1 * numero2 * numero3
    print(produto)

elif ( opcao == 4 ):
    
    if (numero1 + numero2 > numero3):
        print(f"{numero1 + numero2} é maior que {numero3}")
    
    elif (numero1 + numero2 <= numero3):
        print(f"{numero1 + numero2} é menor ou igual {numero3}")

    else:
        print("as opções aceitáveis são (2 , 3  e 4)")