'''
A biblioteca de Palmares empresta gratuitamente seus livros a alunos, professores e
funcionários de todo o campus. Entretanto, sempre que um usuário atrasa a entrega de um
livro, ele tem que pagar uma multa de R$ 0,75 por cada dia de atraso. Escreva um programa
que receba como entrada a quantidade de dias de atraso do empréstimo de um livro, e exiba
o valor da multa a ser paga pelo usuário com duas casas decimais.
'''

VALOR_MULTA = 0.75

quantidade_dias_atraso = int(input("Informa a quantidade de dias de atraso: "))

valor_total = quantidade_dias_atraso * VALOR_MULTA
print(f"Valor Total a ser Pago R$ {valor_total:.2f}")