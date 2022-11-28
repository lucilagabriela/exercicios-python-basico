# Criar a class Carro e colocar, no mínimo, 3 propriedades e no min 3 metódos para ela

class Carro(): # criando a classe
    def __init__(self, cor, ano, marca):
        self.cor = cor
        self.ano = ano
        self.marca = marca
    
    def ligar(self):
        print('ligando...')
    
    def desligar(self):
        print('desligando...')
    
    def exibirInformacoes(self):
        print(self.cor, self.ano, self.marca)

Uno = Carro('Cinza', '2014', 'Fiat')
Uno.ligar()
Uno.desligar()
Uno.exibirInformacoes()