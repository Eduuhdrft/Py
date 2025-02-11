usuario = "Teste"
senha ="@Teste123"

inputUsuario = input("Informe o usuário: ")
inputSenha = input("Informe a senha: ")

if inputUsuario != usuario or inputSenha != senha:
    print("Usuário ou senha incorretos!")

else: 
    print("Acesso liberado!")