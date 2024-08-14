# Crie um programa de câmbio.
# Nesse programa adicione funções que realizem conversões de real para dólar,
# real para euro e real para peso argentino, conforme o nome do país fornecido pelo usuário.

# Utilize os valores:
# 1,00 real = 0,18 dólar para Estados Unidos;
# 1,00 real = 0,16 euro para Portugal;
# 1,00 real = 165,38 peso para Argentina;


def Estados_Unidos (valor_real):
    conversao_dolar = valor_real * 0.18
    print(f'A conversão de {valor_real} R$ em dolar é {conversao_dolar}$')

def Portugal (valor_real):
    conversao_euro = valor_real * 0.16
    print(f'A conversão de {valor_real} R$ em euro é {conversao_euro}')

def Argentina (valor_real):
    conversao_peso = valor_real* 165.38
    print(f'A conversão de {valor_real} R$ em peso é {conversao_peso}')

nome_pais = input('Qual o nome do pais que você irá viajar: ')
lista = ['Estados Unidos','Portugal','Argentina']
while nome_pais not in lista:
    nome_pais = input('Qual o nome do pais que você irá viajar: ')

valor_real = float(input('Qual o valor em real: '))

if nome_pais == 'Estados Unidos':
    Estados_Unidos(valor_real)
elif nome_pais == 'Portugal':
    Portugal(valor_real)
elif nome_pais == 'Argentina':
    Argentina(valor_real)