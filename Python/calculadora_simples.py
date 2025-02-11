#calculadora simples que opere com dois números, onde o usuário escolhe a operação.

print("Bem-vindo a calculadora")
print("Para fazer o calculo digite um numero, informe a operaçao e digite o proximo numero>")

num_1=float(input(":"))

operacao=input("digite a operação desejada:")

num_2=float(input(":"))

#criando as condicionais da operação

if operacao== "+":
    resultado=num_1+num_2

elif operacao=="-":
    resultado=num_1-num_2

elif operacao=="/":
    resultado=num_1/num_2

elif operacao=="*":
    resultado=num_1*num_2

else:
    print("operação invalida.")
    
print(f"{resultado} é o resultado da operação.")





