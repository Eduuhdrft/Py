# Calculadora coma as operações basicas.

# Criando as variaveis

num1=float(input("Digite o primeiro numero:"))
num2=float(input("Digite o segundo numero:"))
#input é str por padrao
operacao=(input("Digite a operação desejada:"))

#condicionais

if operacao== "+":
    resultado= num1+num2

elif operacao== "-":
    resultado=num1-num2

elif operacao=="*":
    resultado=num1*num2

elif operacao=="/":
    if num2 !=0:
        resultado=num1/num2
    else:
        resultado="Erro: Divisão por zero!"

else:
    resultado="Operação invalida!"

print("Resultado:", resultado)


