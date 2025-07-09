# Variable
# # variáveis e tipos de dados "básicos"
# Uma variável é um espaço na memória onde armazenamos um valor

# <nome_da_variavel) = <valor>

nome = "Rubens"  # variável do tipo string (text), sempre entre " " ou ' '
idade = 60       # variável do tipo inteiro (integer) , números inteiros
altura = 1.78    # variável do tipo float, números com casas decimais
dev = True       # variável do tipo booleana, valores lógicos (True / False) *** T e F maiúsculos

### no código abaixo, vai mostrar os dados conforme mocados acima.
#print (f"Olá, {nome}! Você tem {idade} anos e mvede {altura}m.")
# f ==> format

## no código abaixo, os valores serão inputados
nome = input("Digite o seu nome: ")   # entrada de texto
idade = int(input("Digite a sua idade: ")) # entrada de texto convertido para integer
altura =float(input("Digite a sua altura: ")) #entrada de texto convertido para float

print (f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")

