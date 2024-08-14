# Faça um programa que calcule a área de um terreno e imprima na tela.

#def area = base*largura
def calculo_area_terreno(comprimento, largura):
    area = comprimento*largura
    print(f'O valor da area é: {area}')

terreno_compr = int(input("Insira o comprimento do terreno: "))
terreno_larg = int(input("Insira a largura do terreno: "))

calculo_area_terreno(terreno_compr,terreno_larg)

