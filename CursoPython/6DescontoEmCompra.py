# Exercicio que aplica desconto em compras caso for estudante

print("---Seja bem vindo ao mercadinho SENAI---")

valor_compra = float(input("Informe o valor da compra: "))
estudante = int(input("Você é estudante? (1 -estudante ou 2 - não)"))

if estudante == 1:
    desconto = valor_compra * 0.15
    print(f"Valor final com desconto: R$ {valor_compra-desconto}")

else: 
    print(f"Valor total: R$ {valor_compra}")