from main import *
import math

rodar = True # condição
while rodar:
    try:
        # calcula a área de um comôdo com dados fornecidos pelo usuário
        print("Descubra a quantidade necessária de pisos para preencher seu cômodo.")
        comprimento_comodo = float(input("comprimento do cômodo: "))
        largura_comodo = float(input("largura do cômodo: "))

        # faz o cálculo e informa a área
        comodo = Retangulo(comprimento_comodo, largura_comodo)
        print(f'{comodo.areaRetangulo()}m² de área')
        area_comodo = comodo.areaRetangulo() # o resultado foi guardado em uma variável

        # pede as dimensões do piso ao usuário e calcula sua área
        print("\nQuais são as dimensões do piso que deseja utilizar?")
        comprimento_piso = float(input("comprimento do piso:"))
        largura_piso = float(input("largura do piso:"))
        piso = Retangulo(comprimento_piso, largura_piso)
        area_piso = piso.areaRetangulo()

        # divide a área do comodo pela area do piso e retorna o valor
        piso_necessário = area_comodo/area_piso
        piso_necessário = math.ceil(piso_necessário) # arredonda o número float para cima
        print(f'\nSerão necessários {piso_necessário}m² de piso.')

        # retorna a quantidade e metros de rodapé necessários (perímetro)
        print(f'Serão necessários {comodo.perimetroRetangulo()}m de rodapé')
        break
    except(ValueError):
        print("Valor inválido. Tente novamente")
