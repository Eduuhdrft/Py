# Bonus de Funcionário
print("---Bem vindo colaborador---")
print("---Vamos verificar se você possui direito ao bônus salarial:")
salario = float(input("Digite seu salário: "))
tempo_empresa = int(input("Digite o tempo de empresa: "))

if tempo_empresa > 5:
    print("Colaborador tem direito ao beneficio!")

else:
    print("Colaborador não tem direito ao beneficio!")