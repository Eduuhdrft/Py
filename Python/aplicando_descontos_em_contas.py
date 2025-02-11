#aplicando descontos em venda
#criando programa que pergunte o valor da venda


#digitando valor da venda
total_vendas=0


while True:
    valor=float(input("digite o valor da venda ou '0' para sair: "))
    if valor ==0:
        break


    elif valor > 100:
         desconto= valor * 0.10
         total_vendas=valor - desconto
         print("Voce ganhou 10% de desconto:", total_vendas)

    else:
        print("O total de vendas foi:",valor)


        

