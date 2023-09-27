from main import * # importa tudo do arquivo main

# teste da Classe Bola
minha_bola = Bola("rosa", 30, "algodão_doce")
print(minha_bola.mostrarCor()) # utilizando o método mostrarCor
minha_bola.trocaCor("branco") # utilizando o método trocaCor
print(minha_bola.mostrarCor())