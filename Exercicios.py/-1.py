'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja invalido e continue
pedindo até que o usuario infome um valor valido.'''

while True:
    nota = int(input('Digite um valor entre 0 e 10: '))
    if nota >= 0 and nota <= 10:
        print(f'Você digitou o valor {nota}')
        break
    else:
        if nota > 10:
            print('Opção invalida tente novamente...')