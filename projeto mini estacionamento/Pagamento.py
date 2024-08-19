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


teste = Pagamento(80.00)

teste.pagamento_cartao()
print('--------------------------------------')
teste.pagamento_boleto()
print('--------------------------------------')
teste.pagamento_pix()