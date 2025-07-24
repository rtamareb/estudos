# Cálculo de frequência e nota
# Para um aluno passar de ano, ele precisa:
#     1. Ter frequência maior ou igual a 70%
#     2. Ter nota maior ou igual a 7.0
# Caso contrário, o aluno será reprovado

import sys
print ("")
print("Cálculo de frequência e notas")
# Validação do nome do aluno
valid_aluno = False
while valid_aluno == False:
    aluno = input("  Digite o nome do aluno: ")
    if aluno == '':
        print ("  *-*  Nome do aluno não pode ser espaços")
    else:
        valid_aluno = True

lista_materia = ('Física','Matemática', 'Estatística', 'Quantica')
valid_materia = False

# Validação da Matéria
while valid_materia == False:
    materia = input("  Digite a matéria: ")
    if materia not in lista_materia:
        print ("  *-* Matéria invalida")
    else:
        valid_materia = True

# Validação do total de aulas dadas
valid_aulas_dadas = False
while valid_aulas_dadas == False:
    aulas_dadas = input(f"  Digite o total de aulas dadas de {materia}: ")
    try:
        aulas_dadas = int(aulas_dadas)
        if aulas_dadas < 0:
            print ("  *-* Quantidade de aulas dadas não pode ser negativa. Tem que ser maior que 0")
        elif aulas_dadas > 100:
            print ("  *-* Quantidade de aulas dadas não pode ser maior que 100")
        else:
            valid_aulas_dadas = True
    except Exception as e:
        print ("  *-* Quantidade de aulas dadas não pode ter decimais. Tem que ser inteiras")

# Validação do limite de faltas
valid_limite_faltas = False
while valid_limite_faltas == False:
    limite_faltas = input(f"  Digite o limite de faltas de {materia}: ")
    try:
        limite_faltas = int(limite_faltas)
        if limite_faltas < 0:
            print ("  *-* Quantidade de limite de faltas não pode ser negativa. Tem que ser maior que 0")
        elif limite_faltas > aulas_dadas:
            print (f"  *-* Quantidade de limite de faltas não pode ser maior que a quantidade de aulas dadas de {materia}, que é de {aulas_dadas} ")
        else:
            valid_limite_faltas = True
    except  Exception as e:
        print ("  *-* Quantidade de limite de faltas não pode ter decimais. Tem que ser inteiras")


# Validação inicial da frequência
valid_faltas_aluno = False
resultado = ' '

while valid_faltas_aluno == False:
    faltas_aluno = input("  Digite o total de faltas do aluno: ")
    try:
        faltas_aluno = int(faltas_aluno)
        if faltas_aluno < 0:
            print ("  *-* Quantidade de faltas não pode ser negativa. Tem que ser maior que 0")
        elif faltas_aluno > aulas_dadas:
            print ("  *-* Quantidade de faltas não pode ser maior que a quantidade de aulas dadas de {materia}, que é de {aulas_dadas} ")
        elif faltas_aluno == aulas_dadas:
            print (f"  **==> {aluno} já é repetente por faltar à todas aulas dadas")
            valid_faltas_aluno = True
            sys.exit()
        elif faltas_aluno > limite_faltas:
            print (f"  **==> {aluno} já é repetente devido estourar quantidade máxima de faltas permitida ({limite_faltas}) faltas)")
            valid_faltas_aluno = True
#            sys.exit()
        else:
            valid_faltas_aluno = True
    except Exception as e:
        print ("  *-* Quantidade de faltas não pode ter decimais. Tem que ser inteiras")
        
# Validação da nota de corte
valid_nota = False
while  valid_nota == False:
    nota_corte = input(f"  Digite a nota de corte de {materia}: ")
    try:
        nota_corte = float(nota_corte)
        if nota_corte < 0:
            print ("  *-* Nota de corte inválida. Tem que ser positiva")
        elif nota_corte == 0:
            print ("  *-* Nota de corte inválida. Tem que ser maior que 0")
        elif nota_corte > 10:
            print ("  *-* Nova de corte inválida. Tem que ser menor ou igual a 10")
        else:
            valid_nota = True
    except Exception as e:
        print ("  *-* Nota de corte inválida. Tem que ser positivo, maior ou igual a zeros e menor que 10.")
        print ("         E se houverem casas decimais, devem ser separadas com '.'")

# Validação da nota da prova 1
valid_nota = False
while  valid_nota == False:
    nota_prova1 = input("  Digite a nota da prova 1: ")
    try:
        nota_prova1 = float(nota_prova1)
        if nota_prova1 < 0:
            print ("  *-* Nota 1 inválida. Tem que ser positiva")
        elif nota_prova1 > 10:
            print ("  *-* Nova 1 inválida. Tem que ser menor ou igual a 10")
        else:
            valid_nota = True
    except Exception as e:
        print ("  *-* Nota 1 inválida. Tem que ser positivo, maior ou igual a zeros e menor ou igual a 10.")
        print ("         E se houverem casas decimais, devem ser separadas com '.'")

# Validação da nota da prova 2
valid_nota = False
while  valid_nota == False:
    nota_prova2 = input("  Digite a nota da prova 2: ")
    try:
        nota_prova2 = float(nota_prova2)
        if nota_prova2 < 0:
            print ("  *-* Nota 2 inválida. Tem que ser positiva")
        elif nota_prova2 > 10:
            print ("  *-* Nova 2 inválida. Tem que menor ou igual a 10")
        else:
            valid_nota = True
    except Exception as e:
        print ("  *-* Nota 2 inválida. Tem que ser positivo, maior ou igual a zeros e menor ou igual a10.")
        print ("         E se houverem casas decimais, devem ser separadas com '.'")

# Cálculo da frequência do aluno
freq_aluno = aulas_dadas - faltas_aluno 
print (' ')

# Cálculo da frequência mínima
freq_min = aulas_dadas - limite_faltas
 
#print (f'A frequencia minima em {materia} é de {freq_min} aulas. {aluno} frequentou {freq_aluno} aulas')
if freq_aluno >= freq_min:  
    freq_ok = True
else:
    freq_ok = False

# Cálculo da média           
media = (nota_prova1 + nota_prova2) / 2
print ('')
#print (f'A nota de corte de {materia} é {nota_corte}. {aluno} teve a média {media}')
 

if media >= nota_corte:
    media_ok = True             
else:
    media_ok = False

# if freq_ok == True:
#     if media_ok == True:
#       print(f'O aluno {aluno} tirou média {media} em {materia}. Aprovado!!!')

#     else:
#       print(f'O aluno {aluno} tirou média {media} em {materia}. Reprovado devido à média')
 
# else:
#     print(f'O aluno {aluno} não atingiu a frequência mínima de {freq_min} aulas em {materia}. Reprovado devido à frequência')
    

if media_ok == True:
    if freq_ok == True:
        resultado = '  *** Aprovado ***'
    else:
        resultado = '  *-* Reprovado por frequência *-*'  
else:
    resultado = '  *-* Reprovado por média *-*'   


print("")       
print("**==> Resumo final")
print(f'        {aluno} em {materia} obteve média {media}. A nota de corte é {nota_corte} ')
print(f'        Foram dadas {aulas_dadas} aulas de {materia}. A frequência mínima é de {freq_min} podendo ter no máximo {limite_faltas}) faltas')
print(f'        {aluno} frequentou {freq_aluno} aulas, e faltou em {faltas_aluno} aulas')
print(f'        Resultado final: {resultado}')

