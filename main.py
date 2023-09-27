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
        
