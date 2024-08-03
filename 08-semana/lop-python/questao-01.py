'''
1. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas 
linhas esse arquivo possui.
'''

CAMINHO_ARQUIVO = r'softex\08-semana\lop-python\dados\questao-01.txt'

def contador_linha(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            num_linhas = sum(1 for _ in arquivo)
            print(f'O arquivo possui {num_linhas} linhas.')
    except FileNotFoundError:
        print('Arquivo não encontrado.')

# Exemplo de uso:
arquivo_usuario = str(input("digite o caminho ( relativo ) do arquivo de texto: "))
contador_linha(CAMINHO_ARQUIVO)
