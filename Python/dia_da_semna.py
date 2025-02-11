#Pergunte ao usuário um número de 1 a 7 e informe qual é o dia da semana correspondente.

semana=["opção invalida","Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]

dia=int(input("Informe o dia da semena de 1 a 7:"))
if dia == 1:
    print(semana[1])

elif dia == 2:
    print(semana[2])

elif dia == 3:
    print(semana[3])

elif dia == 4:
    print(semana[4])

elif dia == 5:
    print(semana[5])

elif dia == 6:
    print(semana[6])

elif dia == 7:
    print(semana[7])

else:
    ("informe somente numeros de '1 a 7'.")

