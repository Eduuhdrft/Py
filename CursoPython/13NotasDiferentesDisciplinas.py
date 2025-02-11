# Exercicio que verifica notas em diferentes disciplinas

nota1 = float(input("Informe a nota da primeira disciplina:"))
nota2 = float(input("Informe a nota da segunda disciplina: "))
nota3 = float(input("Informe a nota da terceira disciplina: "))

media = (nota1+nota2+nota3)/3

if media >= 7:
    print("Aprovado")

elif media >= 5 and media < 7:
    print("Em recuperação")

else:
    print("Reprovado")
