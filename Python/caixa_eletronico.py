saldo=500

saque=""
deposito=""

print("Bem vindo ao Caixa  Eletronico!")

escolha_input=float(input("Sacar digite 1 e para deposito digite 2:"))
if escolha_input== 1:
    valor_do_saque=float(input("Digite o valor do saque:"))
    if valor_do_saque <= 500:
        print("saldo restante em conta:",saldo-valor_do_saque)

elif escolha_input == 2:
    valor_do_deposito=float(input("Digite o valor do deposito:"))
    if valor_do_deposito >0:
        print("Seu saldo atual é:",saldo+valor_do_deposito)
    else:
        print("o numero deve ser positivo!")

else:
    print("opção invalida!")

print("Obrigado por utilizar nosso serviço, Ate logo!")

       

    







     


    