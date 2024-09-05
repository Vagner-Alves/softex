class Listagem_numerica:

    def __init__(self, lista):
        self.lista = lista

    def obter_numero_pelo_indice(self, indice):
        
        try:
            print( self.lista[indice] )

        except IndexError:
            print("Indice Inválido")
            return None


class Adicionar_numeros:

    def __init__(self, lista, numero = 0):
        self.lista = lista
        self.numero = numero

    def adicionar_numero(self):

        try:
           self.numero = int(input("informe os números: "))
           self.lista.append(self.numero)

        except ValueError as error:
            print(error)
            print(f"\nA lista não aceita outros tipos de dados, apenas tipos inteiros são aceitos: ex 1, 2, 4 etc.")
        
        finally:
          
            print(self.lista)

numeros = []

listagem_numerica = Listagem_numerica(numeros)

#resultado_busca = listagem_numerica.obter_numero_pelo_indice(12)

adicionar = Adicionar_numeros(numeros)

adicionar.adicionar_numero()