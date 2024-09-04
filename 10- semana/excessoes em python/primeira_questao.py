numeros = [1,2,3,4,5,6,7,8,9,10]


def listagem(lista_numero, n):

    try:

        print( lista_numero[n])
    
    except IndexError:
        print("indice Inválido")
        return None


listagem(numeros, 12)