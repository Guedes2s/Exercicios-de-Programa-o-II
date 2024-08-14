# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para personalizar a saída

def converter_12hrs(horas, minutos):
    if horas > 12 and horas < 24:
        horas -= 12
        print(f"{horas}:{minutos} P.M")
    elif horas <= 12:
        print(f"{horas}:{minutos} A.M")
    else:
        print("Hora inválida!")


horas = int(input("Quantas horas: "))
minutos = int(input("Quantos minutos: "))

converter_12hrs(horas, minutos)




