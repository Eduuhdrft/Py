


def soma (a,b):
    return a + b

def subtracao (a,b):
    return a-b

def multiplicacao (a,b):
    return a*b

def divisao (a,b):
    if b ==0:
        return "Divisao por 0 erro."
    return a/b


# criando a funçao da calculadora que ira utilizar as outras funcoes

def calculadora():
    print("Bem vindo a calculadora do SENAI!")
    print("Escolha a operação:")
    print("1. Soma")
    print("2. subtração.")
    print("3. multplicação.")
    print("4. divisão")

    escolha = input("Digite o numero da opção:")

    if escolha in ["1","2","3","4"]:
        num1=float(input("Digite o primeiro valor:"))
        num2=float(input("Digite o segundo valor:"))

        if escolha == "1":
            print("resultado", soma(num1, num2))

        elif escolha == "2":
            print("Resultado:", subtracao(num1, num2))

        elif escolha == "3":
            print("Resultado", multiplicacao(num1, num2))

        elif escolha == "4":
            print("Resultado", divisao(num1< num2))

    else:
        print("Esolha invalida")

        #chamando função calculadora

calculadora()