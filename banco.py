menu = """
[1] depositar
[2] sacar
[3] extrato
[0] sair
=> 
\n"""
saldo= 0.00
limite= 500
extrato= ""
limite_saques= 0
while True:
 
    opcao= input(menu)
    if opcao == "1":
        print("digite o valor a ser depositado: \n")
        deposito= float(input("R$"))
        while deposito <0 :
            print("valor invalido, digite um valor acima de zero.\n")
            deposito= float(input("R$"))
        if deposito >0:
            print("deposito realizado com sucesso \n")
            saldo+=deposito
            print(f"saldo atual: R${saldo:.2f}\n")
            extrato+=(f"deposito: R$ {deposito: .2f}\n")

    elif opcao == "2":
        if limite_saques <3:
            print("digite o valor a ser sacado: \n")
            saque= float(input("R$"))   
            if saque >0 and saque <= limite and saque <= saldo:
                print("saque realizado com sucesso \n")
                saldo -=saque
                print(f"saldo atual: R${saldo: .2f}\n")
                extrato+=(f"saque: R$ {saque:.2f}\n")
                limite_saques += 1
            elif saque <0:
                print("valor invalido,digite um valor acima de zero.\n")
            elif saque>limite:
                print("valor acima do limite, por favor insira um valor menor ou igual a R$ 500,00. \n")
            elif saque>saldo:
                print("saldo insuficiente\n")
        elif limite_saques==3:
            print("limite de saque atingido\n")
            

    elif opcao== "3":
        print(extrato)
    elif opcao== "0":
        break