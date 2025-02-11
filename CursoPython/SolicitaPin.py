# Pin correto

PIN_CORRETO = "1234"

# Numero de tentativas

TENTATIVAS = 3
TENTATIVAS_REALIAZADAS = 0

while   TENTATIVAS_REALIAZADAS <    TENTATIVAS:
    PIN_USUARIO = input("Informe o PIN para acessar: ")

    # Verificando se o pin informado está correto!

    if PIN_USUARIO == PIN_CORRETO:
        print("Seja bem vindo, acesso liberado!")
        break

    else:
        print("PIN incorreto! Tente novamente!")

        TENTATIVAS_REALIAZADAS += 1

if TENTATIVAS_REALIAZADAS == TENTATIVAS:
    print("PIN BLOQUEADO!! NUMERO DE TENTATIVAS EXPIRADO!!")

