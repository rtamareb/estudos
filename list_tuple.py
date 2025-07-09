# List and tuple  
# Tipos de dados que armazenam múltiplos valores, mas com diferenças importantes:
# Listas (list):
#    . Modificável (adicionar, remover, alterar)
#    . Mais lenta
#    . Quando precisamos modificar dados
#    . Definida entre colchetes [] e pode armazenar diferentes tipos de dados
#    . Para acessar o elemento, basta indicar o índice []:
#        . frutas[0]
#    . Para alterar o elemento, basta usar o comando abaixo:
#        . frutas[1] = jabuticaba
#    . Para adicionar elemento:
#        . append() ==> adiciona um elemento ao final da lista
#             . frutas("caqui") ==> adiciona caqui ao final da lista frutas
#        . insert() ==> adiciona um elemento em uma posição específica
#            . frutas (1, "cereja") ==> adiciona cereja na posição 1 da lista frutas
#    . Para remover elemento:
#        . remove() ==> remove um item pelo valor
#        . pop() ==> remove um item pelo índice (ou o último item se nenhum índice for passado)

#
# Tuplas (tuple):
#    . Não é modificável (Uma vez criada, não pode ser alterada)
#    . Mais rápida
#    . Quando os dados não devem ser alterados e serão sempre fixos (Ex.: meses do ano, dias da semana, etc)
#    . Definida entre chaves () e pode armazenar diferentes tipos de dados
#    . Para acessar o elemento, basta indicar o índice:
#        . frutas[0]
#    . Para alterar os elementos de uma tupla:
#        . Converter a tupla para lista
#        . Alterar a lista
#        . Converter a lista para tupla
#        . Exemplo:
#          tupla = (1, 2, 3)
#          lista = list(tupla) # Converte a tuple/tupla para a list/lista
#          lista.append(4) # Incluir item 4 ao final da list
#          tupla = tuple(lista) # Converte a list/lista para tuple/tupla
#          print (tupla)
#
#


print ("")
print ("Tipos de Lista")
frutas = ["maçã","banana", "laranja"]  # lista
numeros = [1, 2, 3, 4, 5]  # lista
misturada = ["Python", 1, 3.14, True] # lista
tfrutas = ("maçã","banana", "laranja")  # tupla
tnumeros = (1, 2, 3, 4, 5)  # tupla
tmisturada = ("Python", 1, 3.14, True) # tupla
print (frutas)
print (numeros)
print (misturada)
print ("")
print ("")
print (f"lista frutas = {frutas}")
print ("Acessando elementos da lista Frutas")
print (f"frutas[0] = {frutas[0]}")  # índice 0 é o primeiro item da lista
print (f"frutas[1] = {frutas[1]}")  # indice 1 é o segundo item da lista, e assim por diante
print (f"frutas[2] = {frutas[2]}")  # indice 2 é o terceiro item da lista, e assim por diante
print (f"frutas[-1] = {frutas[-1]}")  # índice negativo conta de trás para a frente, sendo que o -1 é o último item da lista
print (f"frutas[-2] = {frutas[-2]}")  # índice negativo conta de trás para a frente, sendo que o -2 é o penúltimo item da lista
print (f"frutas[-3] = {frutas[-3]}")  # índice negativo conta de trás para a frente, sendo que o -3 é o antepenúltimo item da lista
print ("")
print ("")
print (f"lista frutas = {frutas}")
print ("Alterando o valor da lista frutas")
frutas[1] = "jabuticaba"
print ("Alterando de banana para jabuticaba") 
print (f"comando frutas[1] = jabuticaba  ==> {frutas[1]}")
print (frutas)

print ("")
print ("")
print (f"lista frutas = {frutas}")
print ("Comando append - adiciona item ao final da lista")
print (f"frutas.append(caqui) ==> adiciona caqui ao final da lista frutas")
frutas.append("caqui")
print (frutas)

print ("")
print ("")
print (f"lista frutas = {frutas}")
print ("Comando insert - adiciona item em uma posição específica da lista")
print (f"frutas.insert(1, cereja) ==> adiciona cereja na posição 1 da lista frutas")
frutas.insert(1, "cereja")
print (frutas)

print ("")
print ("")
print (f"lista frutas = {frutas}")
print ("Removendo cereja da lista frutas") 
print (f"comando frutas.remove(cereja) ==> remove cereja da lista frutas")
frutas.remove("cereja")
print (frutas)

print ("")
print ("")
print (f"lista frutas = {frutas}")
print ("Removendo item pelo índice ou o último ítem da lista se não passar o índice ") 
print (f"comando frutas.pop(3) ==> remove item do indice 3 (caqui)")
frutas.pop(3)
print (frutas)

print ("")
print ("")
print (f"lista frutas = {frutas}")
print ("Removendo item quando não se passa o índice") 
print (f"comando frutas.pop() ==> remove item do último indice (2 / laranja)")
frutas.pop()
print (frutas)

print ("")
print ("")
print (f"tupla tfrutas = {tfrutas}")
print ("Acessando um elemento da tupla tfrutas") 
print (f"comando tfrutas[1] ==> acessa o item com indice 1/banana)")
print (tfrutas[1])
print (tfrutas)

print ("")
print ("")
print ("Alterando uma tuple.")
tupla = (1, 2, 3)
print (f" Tuple antes da alteração {tupla}")
print (f" Convertendo de tuple para list")
lista = list(tupla) # Converte a tuple/tupla para a list/lista
print (f" Alterando a list com o comando lista.append(4)")
lista.append(4) # Incluir item 4 ao final da list
print (f" List após alteração {lista}")
print (f" Convertendo list para tuple")
tupla = tuple(lista) # Converte a list/lista para tuple/tupla
print (f" Tuple após conversão {tupla}")