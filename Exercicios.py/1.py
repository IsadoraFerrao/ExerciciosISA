'''Tamanho da string. Faça um programa que leia 2 strings e informe o conteudo delas seguido do seu comprimento
informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
COMPARE AS DUAS STRINGS
1 BRASIL HEXA 2022!
2 BRASIL HEXA 2022'''

print('-='*30)
print('COMPARANDO AS STRINGS')
print('-='*30)

string1 = str(input('Escreva uma frase: '))
string2 = str(input('Escreve outra frase: '))
print(f'A primeira frase "{string1}" tem {len(string1)} caractéres.')
print(f'A segunda frase "{string2}" tem {len(string2)} caractéres.')
if len(string1) == len(string2):
    print('As duas frase são do mesmo tamanho.')
else:
    print('As duas frases são de tamanhos diferentes.')
if string1 == string2:
    print('As frases são iguais.')
else:
    print('As frases possuem conteúdos diferentes.')