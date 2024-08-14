#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data_inserida = input("Digite uma data no formato dd/mm/aaa: ")
dia,mes, ano = map(int, data_inserida.split('/'))

if mes <1 or mes>12:
    print("Data inválida! O mes deve estar entre 1 e 12.")
else:
    if mes in[1,3,5,7,10,12]:
        max_dias = 31
    elif mes in[4,6,9,11]:
        max_dias = 30
    elif ano %4 == 0 and(ano%100!=0 or ano% 400==0):
        max_dias = 29
    else:
        max_dias = 28

        if dia <1 or dia> max_dias:
            print("Data inválida!O dia inserido não é válido para o mes informado.")
        else:
            print("Data válida!")
            print("Formato de data inválido.Certifique-se de digitar no formato dd/mm/aaaa.")
