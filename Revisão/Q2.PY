#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

list1 = ['A','E','I','O','U']
list2 = ['B','C','D','F','G','J','K','L','M','N','P','Q','R','S','T','V','W','X','Z']
letra = input('Digite uma letra: ').upper()#SERVE PARA TRANSFORMA A LETRA EM MAISCULA
print()

for i in list1:
     if letra == i:
         print(f'A letra {letra} é uma vogal')

for i in list2:
    if letra == i:
        print(f'A letra {letra} é uma consoante')

else:
    print(f'Digite uma letra, e não um número')