# lista de exercicios 2

# Classe Bola
class Bola:
    # construtor de classe. é chamado quando uma nova instância da classe Bola for criada
    def __init__ (self, cor, circunferencia, material):
        # cada argumento é designado a um atributo da instância
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    # métodos de classe. os métodos trocaCor e mostraCor só podem ser utilizados por instâncias da classe Bola.
    def trocaCor(self, nova_cor):
        self.cor = nova_cor # o atributo cor da instância recebe o valor do argumento nova_cor
    
    def mostrarCor(self):
        return self.cor # retorna o valor cor da instância
    
# Classe Quadrado
class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado
    
    def mudarLado(self, novo_Lado):
        self.tamanho_do_lado = novo_Lado # método que irá trocar o valor do lado
    
    def retonarLado(self):
        return self.tamanho_do_lado
    
    def AreaQuadrado(self):
        areaQuadrado = self.tamanho_do_lado * 2 # calcula a area

# Classe Retangulo
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def areaRetangulo(self): # calcula a área
        areaRetangulo = self.comprimento * self.largura
        return areaRetangulo
    
    def perimetroRetangulo(self): # calcula o perímetro
        perimetroRetangulo = (self.comprimento * 2) + (self.largura * 2)
        return perimetroRetangulo
    
    def mudarComprimento(self, novo_comprimento): # define novo comprimento
        self.comprimento = novo_comprimento
    
    def mudarLargura(self, nova_largura): # define nova largura
        self.largura = nova_largura
    
    def retornarComprimento(self): # retorna o valor do comprimento
        return self.comprimento
    
    def retonarLargura(self): # retorna o valor da largura
        return self.largura
    