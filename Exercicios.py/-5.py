'''Faça um programa que calcule e mostre a média aritmética de N de notas.
O usuário escolhe a quantidade de notas.'''

ListaNotas = []
media = 0
somaNotas = 0
tot = 0
while True:
    notas = float(input('Nota: '))
    ListaNotas.append(notas)
    somaNotas += notas
    tot += 1
    media = somaNotas / tot
    p = str(input('Quer continuar [S/N]? ')).upper()[0]
    while p not in 'SN':
        p = str(input('Opção inválida, quer continuar [S/N]? ')).upper()[0]
    if p in 'N': 
        break
ListaNotas.sort()
print('=-'*30)
print(f'Os números escolhidos foram {ListaNotas}.')
print(f'Você escolheu {tot} números e a média é {media}.')