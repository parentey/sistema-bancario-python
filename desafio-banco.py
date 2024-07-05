menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair 

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 3
LIMITE_SAQUES = 3

while True:

    opção = int(input(menu))

    if opção == 0:
        valor = float(input("Digite o valor para realizar o depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"+ Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado!")
        
        else:
            print("Operação não realizada. Por favor informe um valor válido para o depósito.")

    elif opção == 1:
        saque = float(input("Digite o valor para realizar o saque: "))

        if numero_saques > 0:

            if saque > 0 and saque <= saldo and saque <= limite:
                numero_saques -= 1
                saldo -= saque
                extrato += f"- Saque: R$ {saque:.2f}\n"
                print("Saque realizado!")

            else:
                if saque <= 0:
                    print("Operação não realizada. Valor inválido para saque.")

                elif saque > saldo:
                    print("Operação não realizada. Saldo indisponível para o saque.")

                elif saque > limite:
                    print("O valor do saque excede o valor limite para saques em sua conta. Por favor, tente novamente.")

        else:
            print("Você já realizou o número máximo de saques na data de hoje.")
    
    elif opção == 2:
        print(extrato)

        print(f"Seu saldo disponível no momento é: {saldo:.2f}\n")

        if numero_saques > 0:
            print(f"Você ainda possui {numero_saques} saques disponíveis.")
        
        else:
            print("Você não possui mais saques disponíveis para a data de hoje.")

    elif opção == 3:
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")

