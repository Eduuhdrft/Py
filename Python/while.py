senha= "54321"
leitura= ""
while (leitura != senha):
    leitura= input("Digite a senha:")
    if leitura == senha:
        print("Acesso Liberado!")
    else:
        print("Senha incorreta. Tente novamente.")