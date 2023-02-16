'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
*Telefonou para a vítima?
*Esteve no local do crime?
*Mora perto da vítima?
*Devia para a vítima?
*Ja trabalhou com a vítima?
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a duas questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "cúmplice", e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente". '''
cont = 0

p1 = str(input('Telefonou para a vítima? [S/N] ')).upper()[0]
p2 = str(input('Esteve no local do crime? [S/N] ')).upper()[0]
p3 = str(input('Mora perto da vítima? [S/N] ')).upper()[0]
p4 = str(input('Devia para a vítima? [S/N] ')).upper()[0]
p5 = str(input('Ja trabalhou com a vítima? [S/N] ')).upper()[0]

if p1  in 'S':
    cont += 1
if p2  in 'S':
    cont += 1
if p3  in 'S':
    cont += 1
if p4  in 'S':
    cont += 1
if p5  in 'S':
    cont += 1
    
if cont == 1:
    print('Inocente...')
elif cont == 2:
    print('Suspeita...')
elif cont == 3 or cont == 4:
    print('Cúmplice...')
else:
    print('Assassino...')
