# Rubens M. T. 06/08/2025
# Cálculo de IMC (Índice de Massa Corporal)
# Classificação do IMC
#    CONDIÇÃO            IMC em Mulheres     IMC em Homens
#    Abaixo do peso      <19.1               <20.7
#    Peso normal          19.1 - 25.8         20.7 - 26.4
#    Sobrepeso            25.8 - 27.3         26.4 - 27.8
#    Obesidade leve       27.3 - 32.3         27.8 - 31.1
#    Obesidade moderada   32.3 - 37.9         31.1 - 36.4
#    Obesidade severa    >37.9               >36.4  
# Usar funções para calcular o IMC e classificar o resultado. Não se esqueça de validar os input

print ("")
print ("*** Calculadora de IMC ***")
print ("")

# Validação do nome  
valid_nome = False
while valid_nome == False:
    nome = input("* Digite seu nome: ").capitalize()
    if nome.isspace(): 
        print ("  ** Nome não pode ser espaços em branco")
    elif nome.isnumeric(): 
        print ("  ** Nome não pode ser números")
    elif len(nome) < 3:
        print ("  ** Nome muito curto")
    else:
        valid_nome = True
        print ("")

# Validação do sexo
valid_sexo = False        
while valid_sexo == False:
    sexo = input("* Digite o seu sexo (M para masculino e F para feminino): ").upper()
    if sexo.isspace():
        print ("  ** Sexo não pode ser espaços em branco")
    elif sexo not in ['M', 'F']:
        print ("  ** Sexo inválido")
    else:
        valid_sexo = True
        print ("")

# Validação do peso
valid_peso = False  
while valid_peso == False:  
    peso = input("* Digite o seu peso em kilos: ")
    if peso.isspace():
        print ("  ** Peso não pode ser espaços em branco")
    else:
        try:
            peso = float(peso)    
            if peso < 0: 
                print ("  ** Peso não pode ser negativo")    
            elif peso == 0:
                print ("  ** Peso não pode ser zero")
            elif peso < 30:
                print ("  ** Peso não pode ser menor que 30 kilos")
            elif peso > 200:
                print ("  ** Peso não pode ser maior que 350 kilos")
            else:
                valid_peso = True
                print ("")
        except Exception as e:
            print ("  ** Peso deve ser um valor em kilos, numérico positivo, maior que 30 kilos e menor que 350 kilos ")    
            print ("     E se houverem casas decimais, devem ser separadas com '.'")

# Validação da altura
valid_altura = False
while valid_altura == False:
    altura = input("* Digite a sua altura em metros: ")
    if altura.isspace():
        print ("  ** Altura não pode ser espaços em branco")
    else:
        try:
            altura = float(altura)    
            if altura < 0:
                print ("  ** Altura não pode ser negativa")
            elif altura == 0:
                print ("  ** Altura não pode ser zero") 
            elif altura < 1.20:
                print ("  ** Altura não pode ser menor que 1.20 metros")
            elif altura > 2.50:
                print ("  ** Altura não pode ser maior que 2.50 metros")
            else:
                valid_altura = True
                print ("")
        except Exception as e:
            print ("  ** Altura deve ser um valor em metros, numérico positivo, maior que 1,20 m e menor que 2,50 m")
            print ("     E se houverem casas decimais, devem ser separadas com '.'")
    
# Cálculo do IMC
#    CONDIÇÃO            IMC em Mulheres     IMC em Homens
#    Abaixo do peso      <19.1               <20.7
#    Peso normal          19.1 - 25.8         20.7 - 26.4
#    Sobrepeso            25.8 - 27.3         26.4 - 27.8
#    Obesidade leve       27.3 - 32.3         27.8 - 31.1
#    Obesidade moderada   32.3 - 37.9         31.1 - 36.4
#    Obesidade severa    >37.9               >36.4  

def calcular_imc(sexo, peso, altura):
    imc = float(peso / (altura ** 2))
    if sexo == 'F':
        if imc < 19.1:
            classificacao = "Abaixo do peso"
        elif 19.1 <= imc < 25.8:
            classificacao = "Peso normal"
        elif 25.8 <= imc < 27.3:
            classificacao = "Sobrepeso"
        elif 27.3 <= imc < 32.3:
            classificacao = "Obesidade leve"
        elif 32.3 <= imc < 37.9:
            classificacao = "Obesidade moderada"
        else:
            classificacao = "Obesidade severa"
    else:
        if imc < 20.7:
            classificacao = "Abaixo do peso"
        elif 20.7 <= imc < 26.4:
            classificacao = "Peso normal"
        elif 26.4 <= imc < 27.8:
            classificacao = "Sobrepeso"
        elif 27.8 <= imc < 31.1:
            classificacao = "Obesidade leve"
        elif 31.1 <= imc < 36.4:
            classificacao = "Obesidade moderada"
        else:
            classificacao = "Obesidade severa"
    return (imc, classificacao)

imc, classificacao = calcular_imc(sexo, peso, altura)
print (f"{nome}, baseado no seu sexo ({sexo}), altura ({altura:.2f}m) e seu peso ({peso:.2f} kg), o seu IMC é {imc:.2f} e você está classificado como: {classificacao}.")