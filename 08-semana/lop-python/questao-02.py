''' 
2. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas 
letras são vogais. 

'''
CAMINHO_ARQUIVO = r'softex\08-semana\lop-python\dados\questao-01.txt'

def contar_vogais(texto):
    vogais = 'aeiou'
    contador = 0

    for letras in texto.lower():
        if letras in vogais:
            contador += 1
    
    return contador

def abrir_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as arquivo:
            numero_vogais = contar_vogais(arquivo)
            print(f'o arquivo possui {numero_vogais} vogais.')
    except FileNotFoundError:
        print('arquivo não encontrado.')

abrir_arquivo(CAMINHO_ARQUIVO)
