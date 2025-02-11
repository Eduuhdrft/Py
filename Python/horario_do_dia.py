#imprima se é manhã, tarde ou noite
print("bem vindo")

horario=int(input("informe o horario do dia:"))

if horario >=6 and horario <=12:
    print("é manhã")

elif horario >12 and horario <=18:
    print("é tarde")

else:
    print("é noite")

if horario >24:
    print("informe horarios entre 00 e 24")