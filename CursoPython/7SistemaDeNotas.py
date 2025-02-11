# Programa de sistema de notas ( Aprovado, Reprovado e em recuperação)

nota = float(input("Informe a nota do aluno: "))

if nota >= 7:
    print("Aprovado")

elif nota >= 5 and nota <7:
    print("Em recuperação")

else:
    print("Reprovado")
