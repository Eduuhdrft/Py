# Saldo Inicial

saldo = 1000
print("Bem-vindo ao caixa 24 horas!")
print("O seu saldo é de R$: ", saldo)

# Informando as opções do caixa eletronico

opcao = int(input("Escolha a operação desejada (1- Depósito, 2- Saque):"))

# Verificar a opção desejada
if opcao == 1:
    # Realização do deposito
    valor_depositado = float(input("Digite o valor a ser depositado : R$"))
    saldo += valor_depositado
    print(f"Deposito de R$ {valor_depositado} realizado com sucesso. Seu novo saldo é de R$: {saldo}")

elif opcao == 2:
    # Realizando saque
    valor_saque = float(input("Digite o valor a ser sacado: R$"))
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque} realizado com sucesso. Seu novo saldo é de R$ {saldo}")

    else:
        print("Saldo insuficiente!")

else:
    print("Opção invalida!")


print(" Obrigado por utilizar nosso caixa eletrônico!")