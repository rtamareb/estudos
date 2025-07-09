# Guessing number 
# Projeto 1: Jogo de advinhação
# No jogo, o usuário precisa advinhar um número secreto
# Ele pode tentar várias vezes até acertar

numero = 0
numero_secreto_ok = "nao"

while numero_secreto_ok != "sim":
    print ("")
    numero_secreto = float(input("Digite um número secreto positivo que seja maior que 0.00 e menor que 10.00: "))
    if numero_secreto < 0.01:    
        print ("O número secreto precisa ser maior que 0.00")
    elif numero_secreto > 9.99:
        print ("O número secreto precisa ser menor que 10.00")
    else:
        print ("O número secreto foi escolhido")
        numero_secreto_ok = "sim"

while numero != numero_secreto: 
    print ("")
    numero = float(input("Agora tente advinhar qual é o número secreto, e que seja positivo maior que 0.00 e menor que 10.00: "))
    if numero < 0.01:
        print ("O número precisa ser maior que 0.00")
    elif numero > 9.99:
        print ("O número precisa ser menor que 10.00")
    elif numero < numero_secreto:
        print ("O número secreto é maior")
    elif numero > numero_secreto:
        print ("O número secreto é menor")
    else:
        print ("")
        print (f"Parabéns. Você acertou. O número secreto é {numero_secreto}")
        print ("")
    

