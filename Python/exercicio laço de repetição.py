#crie um programa e peça para o usuario informar o  PIN (1234)

pin=1234
tentativas=3

while tentativas >0 :
    input_pin=int(input("Digite o PIN: "))

    if input_pin== pin:
        print("Acesso liberado")
        break

    else:
        tentativas -=1
        print("Pin incorreto, numero de tentativas restantes:",tentativas)

        if tentativas ==0:
            print("numero de tentaivas exedido!")

    

