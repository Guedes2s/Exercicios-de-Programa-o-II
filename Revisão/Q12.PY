# Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores.

quantidade = int(input('Digite a quantidade de números que você irá inserir: '))

lista = []

for i in range(quantidade):
    num = int(input(f"Insira o {i+1}° número: "))
    lista.append(num)

menor = min(lista)# MIN  vai percorrer toda a lista e me mostra o menor valor desta lista
maior = max(lista)# MAX  vai percorrer toda a lista e me mostra o maior valor desta lista
soma = sum(lista)# SUM  vai percorrer toda a lista e me mostra a soma de todos os valores desta lista
soma1 = menor + maior# soma entre o menor e maior

print(menor)
print(maior)
print(soma)
print(soma1)#resultado 