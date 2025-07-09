# Nota Prova
# Condicionais
# São estruturas que permitem ao nosso programa tomar decisões com base
# em determinadas condições. Em outras palavras, o programa pode executar
# ações diferentes dependendo de uma situação específica
# Exemplo:
# Você está em uma cafeteria e está com pouca grana
# O capuccino custa R$ 10,00. Café com leite R$ 7,00. Café simples R$ 4,00
# Se você tiver R$ 10,00 ou mais na carteira, pode pedir um capuccino
# Se você tiver R$ 7,00 ou mais na carteira, pode pedir um café com leite
# Senão, só pode pedir um café simples

# Sintaxe básica no Python
# if   ==> Se
# else ==> Senão
# elif ==> Se + senão

print ("")
materia = (input("Digite o nome da matéria: "))
aluno = (input("Digite o nome do aluno: "))
nota_corte = float(input("Digite a nota de corte para a matéria: "))
nota = float(input("Digite a nota do aluno: "))

print (f"A nota final do/a {aluno}, na matéria {materia}, cuja nota de corte é {nota_corte}, foi de {nota}")
print ("")
print (f"O resultado final do/a {aluno} é")

if nota < nota_corte:
    print (f"{aluno} você precisa estudar mais no proximo ano. Repetiu. kkkk!!!") # Código a ser executado se a condição for verdadeira
elif nota == nota_corte:
    print (f"{aluno} você terá uma 2ª chance, mas estude em vez de ficar no Whtasapp") # Código a ser executado se a 1ª condição for falsa e esta for verdadeira
else:
    print (f"Parabéns {aluno}, passou de ano. Pode ir pra Paúba") # Código a ser executado se nenhuma das condições for verdadeira

print ("")

         
