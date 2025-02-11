#programa em Python que simule um sistema de login. 
login="eduardo"
senha:1234

#criando a variavel com numero de tentaivas.

tentativas=3

input_login=input("Digite o login:")
if input_login == login:
    while tentativas >0:
        input_senha=int(input("Digite a senha:"))
        if input_senha== senha:
            print("Acesso liberado.")
        else:
            tentativas -= 1
            print(f"Senha ou usuario incorretos. {tentativas} restantes.")

 