# Programa para verificar usuario e senha

usuario = "Teste"
senha = "@Teste123"

inputUsuario = input("Informe o usuário: ")
inputSenha = input("Informe a senha: ")

# Verifico se as variaveis inputs são diferentes das que
# estão definidas no topo
if inputUsuario != usuario or inputSenha != senha:
    print("Usuário ou senha incorretos!")

else:
    print("Acesso liberado!!")