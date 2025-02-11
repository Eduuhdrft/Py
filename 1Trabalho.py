#Trabalho sistema gerenciador de reservas de quartos em hoteis SP

import os
os.system("cls")

reserva = ''
resultado = ""


quarto = ["Quarto 44", "Suite Master", "Suite", "Duplex", "Quarto 21"]

print("Bem-vindo ao sistema do Hotel.\n")

while True:
    print("O que gostaria de fazer?")
    print("1. Fazer uma reserva")
    print("2. Consultar reserva")
    print("3. Sair")
    
    opcao = input("\nEscolha uma opção (1, 2, ou 3): ")

    if opcao == '1':  
        print("\nOs quartos disponíveis são:")
        for i, comodo in enumerate(quarto, start=1):
            print(f"{i}. {comodo}") <, um número de quarto (1 a 5): "))
        if escolha < 1 or escolha > 5:
            print("\nEscolha inválida!")
        else:
            reserva = quarto[escolha - 1]
            print(f"\nReserva confirmada: {reserva}\n")

    elif opcao == '2':  
        if reserva:
            print(f"\nVocê tem uma reserva confirmada para: {reserva}\n")
        else:
            print("\nVocê não tem nenhuma reserva ativa.\n")

    elif opcao == '3':  
        print("\nAté logo! Obrigado por usar o sistema do Hotel.\n")
        break  

    else:
        print("\nOpção inválida! Tente novamente.\n")

        






