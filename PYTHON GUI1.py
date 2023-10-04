altura = float(input("Informe o valor da altura: "))
peso = float(input("Informe o peso: "))

imc = peso/(altura*altura)

print("IMC: ", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:   
    print("Peso normal")
elif imc < 29.9 :
    print("Sobrepeso")
else:
    print("Obeso")