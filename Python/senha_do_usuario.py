#um programa que solicite ao usuário uma senha

usuario="eduardo"
senha=1234

print("Bem vindo!")

login_usuario=input("Digite seu usuario:")
if login_usuario == usuario:
    print("Usuario correto!")
else:
    print("Usuario incorreto!")

input_senha=input("Digite a senha do usuario:")
if input_senha == senha:
    print("Usuario e senha correto. Seja bem vindo!")
else:
    print("Senha incorreta!")