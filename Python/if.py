print("calculadora de Score")
print("Seja Bem-Vindo")

ale1 = float(input("digite um valor:"))
ale2 = float(input("digite um valor:"))
  
soma=ale1+ale2
  

  #if=se
if soma >=100:
    print("Score maximo!")

elif soma <=20:
    print("Score insuficiente!")

elif soma <=50:
    print("Score mediano")

#elif= se então
else :
    print("eu Score é:",soma)