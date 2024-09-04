class listagem_numerica:

    def __init__(self, lista):
        self.lista = lista

    def obter_numero_pelo_indice(self, indice):
        
        try:
            self.lista[indice]

        except IndexError:
            print("Indice Inválido")
            return None






numeros = [1,2,3,4,5,6,7,8,9,10]
