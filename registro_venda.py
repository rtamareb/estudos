# Registro de Vendas
# Passos:
#   . Receber do usuário o nome do produto e o preço
#   . Adicionar à fatura
#   . Perguntar se ele quer comprar mais algum produto
#   . Se a resposta for "S" ou "SIM" ou "s" ou "sim" ou "Sim", repetir a operação. 
#   . Só parar quando a resposta for "n" ou "NÃO" ou "Não" ou "não" ou "NAO" ou "Nao" ou "nao" e neste caso imprimir a fatura
#   . A fatura deverá conter os produtos comprados e o preço 
#   . Ao final da fatura, apresentar o total
# Obs.: Para facilitar a resolução, considerar que só é possivel comprar uma unidade de cada produto de cada vez

print ("")
print ("Bem vindo ao Sistemas de Compras")
entrar = input("Deseja iniciar as compras? Digite S ou N ==> ")

while entrar not in ['n', 'N', 'Não', 'NÃO', 'não', 'Nao', 'NAO', 'nao', 's', 'S', 'Sim', 'SIM', 'sim']: 
    entrar = input ('Opção inválida. Digitar S para iniciar as comprar ou N para não comprar ==> ')

if entrar in ['n', 'N', 'Não', 'NÃO', 'não', 'Nao', 'NAO', 'nao']:
    print ('Saindo do Sistemas de Compras')
    print ('')
    exit()

print ("")
print ("Nosso catálogo de produtos contem:")
print ("  * A - R$ 5.50")
print ("  * B - R$ 4.30")
print ("  * C - R$ 2.87")
print ("  * D - R$ 9.76")
print ("  * E - R$ 12.93")
print ("*** Atenção. Só é permitido comprar 1 item de cada produto ***")
print (" ")

cod_prod = ('A', 'B', 'C', 'D', 'E')
compras = []
total = 0
while entrar in ['s', 'S', 'sim' , 'SIM' ,'Sim']:
    produto = input('Digite o código do produto ou N caso deseja encerrar a compra ==> ')
    if produto in ['n', 'N', 'Não', 'NÃO', 'não', 'Nao', 'NAO', 'nao']:
        if total == 0:
            print ('Lista de compras vazia')
            print ('')
            exit ()
        print ('1 Encerrando suas compras')
        print ('')
        break
    elif produto not in cod_prod:
        print('Código do produto inexistente')
        print ('')
    else:
        preco = float(input(' Digite o preço do produto ==> '))
        compras.append ([produto,preco])
        total += preco      
        entrar = input('** Digite S para continuar comprando ou N para parar de comprar ==> ') 
        while entrar not in ['s', 'S', 'sim' , 'SIM' ,'Sim', 'n', 'N', 'Não', 'NÃO', 'não', 'Nao', 'NAO', 'nao']:
                entrar = input('** Atenção: Digite S para continuar comprando ou N para parar de comprar ==> ') 
        if entrar in ['n', 'N', 'Não', 'NÃO', 'não', 'Nao', 'NAO', 'nao']:
            print ('2 Encerrando suas compras')
            print ('')
            break


print ('')
print ('.')
print ('..')
print ('...')
print ('.... Calculando suas compras')
print ('...')
print ('..')
print ('.')
print ('Sua compras consistem de: ')
for i in compras:
    print(f' ==> Produto {i[0]} - R$ {i[1]:.2f}')
          
print (f'O total de suas compras foi de R$ {total:.2f}')





    
    


