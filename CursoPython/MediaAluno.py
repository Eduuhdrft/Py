print("---Sistema de Notas do SENAI---")
print("   Seja Bem vindo!             ")

# Criando as variaveis para receber os dados
nome_aluno = input("Informe o nome do aluno: ")
ra_aluno = input("Informe o RA do aluno: "),
data_nasc = input("Informe a data de nascimento: ")

# Pedindo para informar as notas e aplicar calculo

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1+nota2+nota3)/3

# Mostrando os dados no terminal

print("O nome do aluno é: ",nome_aluno)
print("O RA do aluno é: ",ra_aluno)
print("A data de nascimento do aluno é: ",data_nasc)
print("A média final do aluno é: ",media)