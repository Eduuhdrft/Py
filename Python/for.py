#utilizando o for
#listas são por padrão Float
#para lista []
lista_notas= [3.4,6.6,8,9,10,9.5,8.8,4.3]
soma=0
for nota in lista_notas:
    soma = soma+nota
media=soma/len(lista_notas)
print(" média =", media)