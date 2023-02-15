'''Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor,
a média de cada aluno, imprima o números de alunos com a média maior ou igual a 7.0.'''


cont = 0
soma = 0
media = 0

for aluno in range(0,10):
    aluno = str(input('\nDigite seu nome: '))
    for c in range(0,4):
        nota = float(input('Digite uma nota: '))
        soma += nota
        media = soma / 4
    if media >= 7:
        print(f'O aluno(a) {aluno} está com media superior a 7, por isso está aprovado(a).')
        cont +=1
    else:
        print(f'O aluno(a) {aluno} está com media inferior a 7, por isso está reprovado(a).')


print(f'\nForam {cont} Alunos com média superior a 7.')