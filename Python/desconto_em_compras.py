# Pergunte ao usuário o valor de uma compra e se ele é estudante. 

desconto=0.15


print("Bem vindo.")

input_valor=float(input("Digite o valor da sua compra:")) 
if input_valor >0:
    print("o valor da compra é:",input_valor)
else:
    print("O valor deve ser maior que 0!")



    estudante=input("Voce é estudante? Digite sim ou não:")
    if estudante=="sim":
        valor_total=input_valor*desconto
        print("Voce ganhou 15% de desconto, o valor final da compra é:",input_valor-valor_total)
