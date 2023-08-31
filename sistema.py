

menu = """

[d]Deposito
[s]Saque
[e]Extrato
[q]Sair


=> """

saldo = 0
limite = 500
extrato = ""
n_saques = 0
LIMETE_SAQUE = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é inválido.")    
    
    
    elif opcao == "s":
        valor = float(input("Informe valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limete = valor > limite
        
        excedeu_saques = n_saques >= LIMETE_SAQUE
        
        if excedeu_saldo:
            
            print("Operação falhou! Voce não tem saldo suficiente. ")
        
        elif excedeu_limete :
              
            print("Operação falhou! O valor do saque excede o limite . ")  
            
        elif excedeu_saques:
            
            
            print("Operação falhou! Número de saques execido. ")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n" 
            n_saques += 1
        
        
        else:
            print("Operação falhou! O valor informado é invalido. ")       
        
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == ("q"):
        break
    else:
        print("Opção ivalida, Por favor selecione novamente a operação desejada ")    
        
        
        
