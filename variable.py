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


#Variáveis

print ('A variável nome cujo conteúdo é ',nome,' é do tipo', type(nome))

print ('A variável idade cujo conteúdo é ',idade,' é do tipo', type(idade))

print ('A variável altura cujo conteúdo é ',altura ,' é do tipo', type(altura))

var_booleana = False
print ('A variável var_booleana cujo conteúdo é ',var_booleana ,' é do tipo', type(var_booleana))

num1 = 100.25
num2 = 350.50

print ('O resultado de ',num1, '+', num2, 'é:', num1+num2,'. E o tipo é',type(num1 + num2))


num1 = 200
num2 = 450

print ('O resultado de ',num1, '+', num2, 'é:', num1+num2,'. E o tipo é',type(num1 + num2))
