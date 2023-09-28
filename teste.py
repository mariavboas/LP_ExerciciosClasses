from main import * # importa tudo do arquivo main

# teste da Classe Bola
minha_bola = Bola("rosa", 30, "algodão_doce")
print(minha_bola.mostrarCor()) # utilizando o método mostrarCor
minha_bola.trocaCor("branco") # utilizando o método trocaCor
print(minha_bola.mostrarCor())

# teste da Classe Quadrado
meu_quadrado = Quadrado(10)
print(meu_quadrado.retonarLado())
meu_quadrado.mudarLado(20)
print(meu_quadrado.retonarLado())

# teste da classe Retângulo
meu_retangulo = Retangulo(12, 8)
print(meu_retangulo.retornarComprimento())
print(meu_retangulo.retonarLargura())
print(f'o perímetro é: {meu_retangulo.perimetroRetangulo()}')
print(meu_retangulo.areaRetangulo())
