menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("Operação inválida, tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        acima_saldo = valor > saldo
        
        acima_limite = valor > limite
        
        acima_saque = numero_saques >= LIMITE_SAQUES
        
        if acima_saldo:
            print("Saldo insuficente! ")
        if acima_limite:
            print("Valor excede o limite de saque")
        if acima_saque:
            print("Quantidade máxima de saques atingida")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação inválida, tente novamente.")

    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Saldo anterior: R${:.2f}".format(saldo))
        print(extrato)
        print("Saque realizado: {}".format(numero_saques))
        print("================================")
        
    elif opcao == "4":
        break
    
    else:
        print("Operação inválida. Gentileza escolher 1outra opção!")
    

    