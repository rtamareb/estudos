# ATM - Automatic Teller Machine - Caixa Eletrônico
# Projeto 2: Simulando um Caixa Eletrônico
#
# O usuário tem um saldo inicial de R$ 500.00 e pode sacar o dinheiro até zerar o saldo, ou encerrar
#
print ("")
print ("ATM - Automatic Teller Machine - Caixa Eletrônico")
saldo = float(input("Digite o saldo inicial da conta: R$ "))
if saldo < 0.00:
    print ("O saldo inicial precisa ser maior que R$ 0.00")
    exit()

while saldo > 0.00:
    saque = float(input("Digite o valor do saque ou digite 0 para sair "))
    if saque == 0:
        break
    if saque > saldo:
        print ("")
        print ("Saque não é possível. Saldo não é suficiente")
        print (f"Seu saldo é de R$ {saldo:.2f}")
    else:        
        saldo = saldo - saque
        #round(saldo, 2)
        print ("") 
        #saldo = round(saldo)
        print (f"Saque de R$ {saque:.2f} efetuado com sucesso")
        print (f"O seu saldo é de R$ {saldo:.2f}")
        round
print ("Operação finalizada")
