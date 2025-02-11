# Exercicio para verificar se o numer é multiplo de outro numero

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 % numero2 == 0:
    print(f"{numero1} é multiplo de {numero2}")

else:
    print(f"{numero1} não é multiplo de {numero2}")