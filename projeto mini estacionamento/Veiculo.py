class Veiculo:
    def __init__(self, modelo, marca, ano_lancamento, placa, cor):
        self.modelo = modelo,
        self.marca = marca,
        self.ano_lancamento = ano_lancamento
        self.placa = placa
        self.cor = cor
    
    def exibir_informacao(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano Lançamento: {self.ano_lancamento}")
        print(f"Placa do Veiculo: {self.placa}")
        print(f"cor do Veiculo: {self.cor}")


class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass

carro = Carro('Ferrari F40','Ferrari',2024,'BR-00000','Roxa-customizada')
carro.exibir_informacao()
print('-----------------')
moto = Moto('Bonneville T120 Black', 'Triumph',2024,'BR-111111','Preta')
moto.exibir_informacao()