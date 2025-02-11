pin=1234
tentativas=3

#criando o input do pin

while tentativas >0:
    input_pin=int(input("Digite o PIN:"))
    
    if input_pin == pin:
        print("Seja bem vindo, acesso liberado!")
        break

    else:
        tentativas -= 1
        print(" Oin incorreto.")

if tentativas ==0:
    print("numero de tentativas exedido")