class Usuario:
    def __init__(self, nome, idade, sexo, endereco, documento_identificacao):
        self.nome = nome,
        self.idade = idade,
        self.sexo = sexo,
        self.endereco = endereco,
        self.documento_identificacao = documento_identificacao
    
    def exibir_informacao(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"endereço: {self.endereco}")
        print(f"documentos de identificação: {self.documento_identificacao}")


class Veiculo:
    def __init__(self, modelo, marca, hora_entrada, hora_saida, placa, cor):
        self.modelo = modelo,
        self.marca = marca,
        self.hora_entrada = hora_entrada,
        self.hora_saida = hora_saida,
        self.placa = placa
        self.cor = cor
    
    def exibir_informacao(self):
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Hora entrada: {self.hora_entrada}")
        print(f"Hora saida {self.hora_saida}")
        print(f"Placa do Veiculo: {self.placa}")
        print(f"cor do Veiculo: {self.cor}")


class Carro(Veiculo):
    pass

class Moto(Veiculo):
    pass


class Pagamento:
    def __init__(self,valor):
        self.valor = valor
    
    def pagamento_pix(self):
        chave_pix = 'abcbsasoodoe17ojdonad'
        print(f"Valor R$: {self.valor}")
        print(f"Chave PIX: {chave_pix}")
    
    def pagamento_cartao(self):
        selecionar = str(input("Digite 'C' para Crédito ou 'D' para Débito: ")).upper()
        if 'C' in selecionar:
            print(f"Cobrança Crédito:  {self.valor}")
        
        elif 'D' in selecionar:
            print(f"Cobrança Débito:  {self.valor}")
    
    def pagamento_boleto(self):
        print(f"Valor: R${self.valor}")
        print(f"Código Boleto: 111100000344008888677771112444")


class Estacionamento:
    def __init__(self, vagas_totais, valor_hora):
        self.vagas_totais = vagas_totais
        self.vagas_disponiveis = vagas_totais
        self.valor_hora = valor_hora
        self.lista_veiculos = []

    def registrar_entrada(self, veiculo):
        if self.vagas_disponiveis > 0:
            self.lista_veiculos.append(veiculo)
            self.vagas_disponiveis -= 1
            print(f"Veículo {veiculo.placa} estacionado.")
        else:
            print("Estacionamento lotado.")





