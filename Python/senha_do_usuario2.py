#um programa que solicite ao usuário uma senha

usuario="eduardo"
senha="1234"

input_usuario=input("digite seu usuario: ")
input_senha=input("Digite a senha do usuario:")

if input_usuario == usuario and input_senha== senha:
    print("Acesso liberado, Seja bem vindo")
else:
    print("Usuario ou senha incorretos!")
