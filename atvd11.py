# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)
idade = int(input('qual a sua idade: '))

# Classificação de faixa etária.
if idade <= 12:
    print('você é uma criança.')
elif idade > 12 and idade <= 17:
    print("você é um adolescente.")
elif idade >= 18 and idade < 60:
    print("você é um adulto.")
else:
    print("você é um idoso.")