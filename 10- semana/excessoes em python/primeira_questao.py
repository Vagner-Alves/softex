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

    def __init__(self, lista):
        self.lista = lista

    def adicionar_numero(self, numero):

        try:
            self.lista.append(numero)
        
        except TypeError:
            print("A lista aceita apenas tipos inteiros")
            

numeros = []

listagem_numerica = Listagem_numerica(numeros)

resultado_busca = listagem_numerica.obter_numero_pelo_indice(12)