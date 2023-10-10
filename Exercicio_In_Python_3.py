saldo = 1000

opcao = int(input("Informe a operacao desejada: "))

if  opcao == 1:
    saque = float(input("Informe o valor do saque: "))
    while saque > saldo:
        print("Saldo insuficiente")     
        saldo = float(input("Informe o valor do saque: "))
    saldo -= saque
    print("Seu saldo é: ", saldo)
elif  opcao == 2:
      deposito = float("Informe o valor do deposito: ")
      saldo = saldo + deposito
elif  opcao == 3:
      print("Seu saldo é: ", saldo)
else:
      print("Opcao invalida")             
