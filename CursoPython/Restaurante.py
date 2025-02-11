# Criando um menu simples de um restaurante
# Usuário pode escolher diferente pratos e também sair.

# Criando a variavel lista para guardar os itens do restaurante

menu = ["Pizza","Hambúrguer", "Salada", "Sopa", "Feijoada","Lasanha"]
print("Menu: ")

# Varrendo o menu de opções
for prato in menu:
    print(prato)

# Criando o sistema de escolha de pratos

while True:
    escolha = input("Escolha um prato ou digite 'sair' para encerrar:")

    # Verificando se a pessoa digitar 'sair' e encerrar o loop
    if escolha.lower() == 'sair':
        print("Até logo!!")
        break
    
    elif escolha in menu:
        print("Você escolheu: ", escolha)

    else:
        print("Prato não está disponível!!")