# Cálculo de frequência e nota
# Para um aluno passar de ano, ele precisa:
#     1. Ter frequência maior ou igual a 70%
#     2. Ter nota maior ou igual a 7.0
# Caso contrário, o aluno será reprovado

print ("")
print("Cálculo de frequência e nota")
aluno = input("  Digite o nome do aluno: ")
materia = input("  Digite a matéria: ")
aulas_dadas = int(input("  Digite o total de aulas dadas: "))
faltas_aluno = int(input("  Digite o total de faltas do aluno: "))
freq_perc = float(input("  Digite o percentual de frequência mínima: "))
nota_prova1 = float(input("  Digite a nota da prova 1: "))
nota_prova2 = float(input("  Digite a nota da prova 2: "))
nota_corte = float(input("  Digite a nota de corte: "))

# Cálculo da frequência do aluno
freq_aluno = aulas_dadas - faltas_aluno 
print (' ')
# Cálculo da frequência mínima
freq_min = freq_perc * aulas_dadas / 100
 
print (f'A frequencia minima em {materia} é de {freq_min} aulas. {aluno} frequentou {freq_aluno} aulas')
if freq_aluno >= freq_min:  
    freq_ok = True
else:
    freq_ok = False

# Cálculo da média           
media = (nota_prova1 + nota_prova2) / 2
print ('')
print (f'A nota de corte de {materia} é {nota_corte}. {aluno} teve a média {media}')
 

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
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado por frequência'  
else:
    resultado = 'Reprovado por média'   


print("")       
print("Resumo final")
print(f'  O/A aluno/a: {aluno} na matéria {materia} obteve média {media}. A nota de corte foi {nota_corte} ')
print(f'  A frequência foi de {freq_aluno} aulas, com {faltas_aluno} faltas. A frequência mínima era de {freq_min} aulas')
print(f'  Resultado final: {resultado}')

