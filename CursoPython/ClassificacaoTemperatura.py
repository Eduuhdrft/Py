# Exercicio simulando o funcionamento de um classificador de temperatura.

# Criando a variavel Input

temperatura = float(input("Digite a temperatura: "))

if temperatura < 15:
    print(" O clima ta Frio!!")

elif temperatura <= 15 or temperatura <= 25:
    print("O clima está agradável!!")

else:
    print("O clima está quente!!")