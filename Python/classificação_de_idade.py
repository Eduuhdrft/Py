#solicitar ao usuario que informe a idade

input_idade=int(input("qual sua idade:"))
if input_idade <= 12:
    print("voce é criança.")

elif input_idade > 12 and input_idade <=17 : 
    print("voce é adolecente.")

elif input_idade >=18 and input_idade <=64:
    print("Voce é adulto.")

else:
    print("voce é idoso")
