#Program para verificar usuario e senha
#parac colocar um valor str prescisa ser entres aspas""

usuario= "teste"
senha= "@teste123"

input_usuario= input("informe o usuario:")

input_senha=input("informe a senha:")

#verifico se as variaveis inputs sao diferentes das que estao definidas no topotes

if input_usuario != usuario or input_senha != senha:
    print("usuario ou senha errado")

else:
    print("acesso liberado!")