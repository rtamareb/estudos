# Média Simples
# Funções são blocos de código reutilizáveis que realizam uma tarefa específica
# Em vez de escrever o mesmo código várias vezes, criamos uma função e apenas chamamos sempre que necessário
# Estrutura:
#  def <nome_da_função> (parâmetro):
#    Código
#    return ***

#def saudacao(nome):
#    print (f"Olá, {nome}! Seja bem-vindo ao curso de Python. Este é um exemplo de uma função")
#
#saudacao("Rubens")

# Função com 2 parâmetros
#def somar (a, b):
#    return a + b
#
#resultado = somar (5, 3)
#print (f" O resultado da soma é {resultado}")

# Função com vários parâmetros

print ("")
print ("Cálculo de média simples")

materia = (input("Digite o nome da matéria: "))
aluno = (input("Digite o nome do aluno: "))
n1 = float(input("Digite a nota da 1ª prova: "))
n2 = float(input("Digite a nota da 2ª prova: "))
n3 = float(input("Digite a nota da 3ª prova: "))
  
nota_corte = float(input("Digite a nota de corte para a matéria: "))
def calcular_media (n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

media = calcular_media(n1, n2, n3)   
print (f"A média é {media:.2f}")
print (f"A nota final do/a {aluno}, na matéria {materia} foi de {media:.2f}")
print (f"A média para passar em {materia} é {nota_corte:.2f}")
print ("")
if media < nota_corte:
    print (f"{aluno} você precisa estudar mais no proximo ano. Repetiu. kkkk!!!") # Código a ser executado se a condição for verdadeira
elif media == nota_corte:
    print (f"{aluno} você terá uma 2ª chance, mas estude em vez de ficar no Whtasapp") # Código a ser executado se a 1ª condição for falsa e esta for verdadeira
else:
    print (f"Parabéns {aluno}, passou de ano. Pode ir pra Paúba") # Código a ser executado se nenhuma das condições for verdadeira

print ("")

