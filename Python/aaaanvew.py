pin=9823
tentativas=4

while tentativas > 0 :
    input_pin=int(input("Digite o PIN:"))

    if input_pin == pin:
        print("Acesso liberado")
        break

    else:
        tentativas -=1
        print(f"PIN incorreto, {tentativas} tentativas restantes.")

if tentativas ==0:
    print("Numero de tentativas execido!")






