# Calculadora com as operações básicas

# Criando as váriaveis

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada: ")

# Condicionais

if operacao == '+':
    resultado = num1 + num2

elif operacao == '-':
    resultado = num1 - num2

elif operacao == '*':
    resultado = num1*num2

elif operacao == '/':
    if num2  !=0:
        resultado = num1/num2
    else:
        resultado = "Erro: Divisão por zero!"

else:
    resultado = "Operação inválida!"

print("Resultado: ",resultado)

