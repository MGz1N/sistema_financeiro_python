saldo = 0
historico = []
from datetime import datetime

while True:
    
    print("\n=== MENU ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Ver histórico de transações")
    print("5 - Sair")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        agora = datetime.now()
        try:
            valor = float(input("Valor para depósito: "))
        except ValueError:
            print("Valor inválido para depósito! Por favor, insira somente números.")
            continue

        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
            print(f"Depósito de R${valor:.2f} em {agora.strftime('%d/%m/%Y %H:%M')}")
            data = agora.strftime('%d/%m/%Y %H:%M')
            texto = f"{data} | Depósito | +R${valor:.2f} | Saldo: R${saldo:.2f}"
            historico.append(texto)
        else:
            print("Valor inválido para depósito!")

    elif opcao == "2":
        agora = datetime.now()
        try:
            valor = float(input("Valor para saque: "))
        except ValueError:
            print("Valor inválido para saque! Por favor, insira somente números.")
            continue
        if valor <= 0:
             print ("Valor inválido para saque!")
        elif valor <= saldo:
            saldo -= valor
            print("Saque realizado com sucesso!")
            print(f"Saque de R${valor:.2f} em {agora.strftime('%d/%m/%Y %H:%M')}")
            data = agora.strftime('%d/%m/%Y %H:%M')
            texto = f"{data} | Saque | -R${valor:.2f} | Saldo: R${saldo:.2f}"
            historico.append(texto)
        else:
            print("Saldo insuficiente!")


    elif opcao == "3":
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "4":
         if not historico:
          print ("Nenhuma transação realizada!")
         else:
            print("Histórico de transações:")
            for transacao in historico:
                print (transacao)
    

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")