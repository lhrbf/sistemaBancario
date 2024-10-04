saldo = 2500

while True:
    print("\nBem-vindo ao Banco LHRBF!")
    print("1 - Depósito\n2 - Saque\n3 - Extrato\n0 - Sair")
    option = int(input("Escolha uma opção: "))

    if option == 1:
        deposito = float(input("Digite o valor do depósito: "))
        saldo += deposito
        print(f"Depósito de R${deposito:.2f} realizado com sucesso!")
    elif option == 2:
        saque = float(input("Digite o valor do saque: "))
        if saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= saque
            print(f"Saque de R${saque:.2f} realizado com sucesso!")
    elif option == 3:
        print(f"Seu saldo é: R${saldo:.2f}")
    elif option == 0:
        print("Obrigado por usar o Banco LHRBF! Até logo.")
        break
    else: 
        print("Número inválido!")