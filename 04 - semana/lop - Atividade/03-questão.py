'''
    Calcule a média aritmética das três notas de um aluno e mostre, além
do valor da média, uma mensagem de &quot;Aprovado&quot;, caso a média seja
igual ou superior a 7; a mensagem “em prova final” caso a média seja
menor que 7 e maior ou igual a 4; e &quot;reprovado&quot;, caso contrário.
'''

primeira_nota  =  float(input("Informa sua Primeira Nota: "))
segunda_nota   =  float(input("Informe sua Segunda Nota: "))
terceira_nota  =  float(input("Informe sua Terceira Nota: "))

media_aluno = ( primeira_nota + segunda_nota + terceira_nota ) / 3

if (media_aluno >= 7):
    print("Aprovado")

elif ( media_aluno < 7) or (media_aluno >= 4):
    print("Em prova final")

else:
    print("Reprovado")
