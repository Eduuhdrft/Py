#criando meni simples de um restaurante
#usuario podera escolher diferentes pratos e tambem sair.

#criando a variavel lista para guardar os itens dos restaurantes.

menu=["coxinha","fogazza","pizza","joelho","hamburguer","cafe","suco","feijoada"]
print("Menu: ")

#varrendo o menu de opções "for" 

for prato in menu:
    print(prato)

    #criando sistema de escolhe de pratos

while True:
    escolha=input("Escolha um prato ou digite 'sair' para encerrar.")
   
    #Verificando se a pessoa digitar "sair" e encerrar o loop.

    #lower()==  serve para a palavra funcionar tanto no maisculo ou minisculo.

    if escolha.lower()== "sair":
        print("Até logo!")
        break

#"escolha" é a variavel input "inserivel"

    elif escolha in menu:
        print("Você escolheu: ", escolha)

    else:
        print("Prato não disponivel.")
