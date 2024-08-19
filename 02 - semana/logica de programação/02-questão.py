'''
    Questões 2 , 3 e 4
'''


preco_brigadeiro = 0.9
preco_cajuzinho = 0.7

numero_brigadeiros = float(input("quantidade de Brigadeiros comprados: "))
custo_brigadeiros = numero_brigadeiros * preco_brigadeiro

numero_cajuzinhos = float(input("quantidade de cajuzinhos comprados: "))
custo_cajuzinhos = numero_cajuzinhos * preco_cajuzinho

quantidade_criancas = int(input("quantidade de crianças na festa:"))
brigadeiros_disponiveis = numero_brigadeiros / quantidade_criancas
cajuzinhos_disponiveis = numero_cajuzinhos / quantidade_criancas
total_doces = brigadeiros_disponiveis + cajuzinhos_disponiveis

print('-------------' * 10)
print(' ')
#print(f"O total gasto em Brigadeiros é R$ {custo_brigadeiros:.2f}")
#print(f"O total gasto em Cajuzinhos é R$ {custo_cajuzinhos:.2f}")
print(f"O Total gasto com Doces é R$: {custo_brigadeiros + custo_cajuzinhos:.2f}")
print(f"Cada Criança pode Comer {int(total_doces)} Doces")
