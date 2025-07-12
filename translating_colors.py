# Translating colors
# Create a new dictionary with colors (in English) as keys and their translations (in Portuguese) as values.    
# Use the get method to retrieve the translation of a color input by the user. If the color is not found, return a default message.
cores = {'verde': 'green', 'vermelho': 'red', 'preto': 'black', 'branco': 'white', 'azul': 'blue', 'amarelo': 'yellow', 'roxo': 'purple', 'laranja': 'orange', 'cinza': 'gray', 'rosa': 'pink'}
cor = ' '
print ("")
print ("Traduzindo cores")
print ("")
while cor != '0':
    cor = str(input('Digite em letras minúsculas a cor que você deseja que seja traduzido para o inglês. Caso deseje sair, digite 0: ').lower())
    if cor == '0':
        print ("")
        print("Você escolheu sair")
        print ("")
        exit()
    traducao = cores.get(cor, 'Esta cor não consta no dicionário cores. Por favor, escolha uma cor válida.')
    print (f'A tradução da cor {cor} é: {traducao}')
    print ("")
    