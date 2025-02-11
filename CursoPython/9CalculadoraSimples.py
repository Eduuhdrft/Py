# Exercicio de uma calculadora simples

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

operacao = input("Escolha a operação desejada: (soma, subtração, divisão e multiplicação): ")

if operacao == "soma":
    resultado = num1 + num2

elif operacao == "subtração":
    resultado = num1 - num2

elif operacao == "multiplicação":
    resultado = num1 * num2

elif operacao == "divisão":
    if num2 != 0 :
        resultado = num1 / num2
    else: 
        print("Erro: Divisão por zero!")


else:
    print("Operação inválida!!")


print("Resultado :", resultado)

