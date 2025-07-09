# Laços de repetição
# For ==> Quando sabemos quantas vezes queremos repetir um bloco de código.
#         Percorre uma sequência de valores, como uma lista, um intervalo de números
#         ou até mesmo letras de uma palavra
#         Estrutura:
#         for variável in sequência:
#             Instruções a serem executadas
# While ==> Quando queremos repetir algo até que uma condição se torne falsa
#           Usado quando não sabemos quantas vezes a ação será repetida, mas sabemos 
#           a condição que deve ser atendida para a ação ser repetida.
#           Estrutura:
#           while condição:
#              Instruções a serem executadas
              

# print ("Exemplo 01 de 'FOR'")
# print ("Contando de 1 a 6")
# print ("O comando 'range(a,b) significa que será gerado um número iniciando em a e terminando em b-1")
# print ("Atenção: Apesar do comando 'range (1,6)', vai variar de 1 a 5")
# print ("Início do FOR")
# for numero in range (1, 6):
#     print (f" {numero}")

# print("Acabou o FOR")

# print ("")
# print ("Exemplo 02 de 'FOR'")
# print ("Percorrendo uma lista de compras")
# compras = ["Arroz", "Feijão", "Leite", "Ovos"]
# for item in compras:
#     print (f" Comprar: {item}")

# print("Acabou o FOR")

# print ("")
# print ("Exemplo 03 de 'FOR'")
# print ("Percorrendo as letras de uma palavra")
# palavra = input("Digite qualquer palavra ")
# for letra in palavra:
#     print (f" A letra é: {letra}")

# print("Acabou o FOR")
# Se em uma palavra específica, tem a letra Y

# print ("")
# palavra = input("Por favor, digite uma palavra qualquer: ")
# letra = input ("Por favor, digite uma letra que você queira saber se ela está contida na palavra digitada anteriormente: ")
# chave = "Não"
# for letrap in palavra:
#     if letrap == letra:
#         chave = "Sim"

# if chave == "Sim":
#     print(f"A palavra digitada contem a letra {letra}")
# else:
#     print(f"Essa palavra não tem a letra {letra}")


# print ("")
# print ("Exemplo 01 de 'WHILE'")
# print ("Contagem Regressiva")
# contador = 10
# while contador > 0:
#     print (f" {contador}")
#     contador -= 1  # Diminui 1 do contador a cada repetição. Mesma coisa que "contador = contador - 1"

# print ("Fogo!!!!! Uhúúúúúúu!!!!!")
# print("Acabou o WHILE")

print ("")
print ("Exemplo 02 de 'WHILE'")
print ("Pedindo senha até acertar")
senha_correta = int(input("Digite qualquer número inteiro positivo: "))
senha = 0
while senha != senha_correta:
    senha = int(input("Digite a senha ou '0' para sair: "))
    if senha == 0:
        print ("")
        print("Você escolheu sair")
        exit()
    
print ("")
print ("Acesso permitido")
print("Acabou o WHILE")
