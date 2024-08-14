#Escreva um código que receba o nome de uma pessoa e imprima uma saudação personalizada na tela com o nome do usuário.

def saudacao_personalizada(nome):
    print(f"Olá {nome}, bem-vindo(a)!")

nome = input("Olá! Por favor, digite seu nome: ")
saudacao_personalizada(nome)