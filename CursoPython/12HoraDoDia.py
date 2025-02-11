# Exercicio que verifica o Horário do dia

hora = int(input("Digite a hora (0-23): "))

if hora <=  6 and hora < 12:
    print("Manha")

elif hora >= 12 and hora < 18:
    print("Tarde")

elif hora >= 18 and hora <=23:
    print("Boa Noite!")

else:
    print("Hora inválida!")