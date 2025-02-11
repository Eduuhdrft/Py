# PIN correto

PIN_CORRETO = "1234"


# Numero de tentativas:

TENTATIVAS = 3
TENTATIVAS_REALIZADAS = 0


while TENTATIVAS_REALIZADAS < TENTATIVAS:
    PIN_USUARIO = input("Informe o PIN para acessar: ")

    if PIN_USUARIO == PIN_CORRETO:
        print("SEJA BEM VINDO !!!!!")
        break

    else:
        print("PIN incorreto! Tente novamente!")
        TENTATIVAS_REALIZADAS += 1

    
if  TENTATIVAS_REALIZADAS == TENTATIVAS:
    print("PIN BLOQUEADO, NUMERO DE TENTATIVAS EXPIRADO!")
