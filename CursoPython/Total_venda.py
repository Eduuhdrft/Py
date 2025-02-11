# Aplicador de desconto em compras

total_vendas = 0

# Criando a estrutura de repetição

while True:
    venda = float(input("Digite o valor da venda ou '0' para sair: "))

    if venda == 0:
        break

    elif venda > 100:
        desconto = venda * 0.10
        total_vendas = venda - desconto
        print("O total de vendas com desconto foi: ", total_vendas)

    else:
        print("O total de vendas foi: ",venda)