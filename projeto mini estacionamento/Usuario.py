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


usuario_teste = Usuario("vagner Alves",27,"masculino","Centro-Palmares",["xxx-xxx-xxx-yy","número RG aleatório"])

usuario_teste.exibir_informacao()