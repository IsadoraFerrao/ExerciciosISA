'''Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 digítos
adicionando o 9 na frente. O usuário pode informar o número com ou sem traço separador.'''

while True:
    phone = str(input('Digite o número do seu telefone: '))
    if len(phone) < 9:
        print('Faltou algum número, por favor digite novamente....')
    if phone[0] not in '9':
        print('Por favor, inicie o número com 9, tente novamente...')
    else:
        if len(phone) >= 9 and phone[0] in '9':
            print('=-'*30)
            print(f'\033[33mVocê digitou o número {phone}, parabéns, número foi digitado corretamente!!!\033[m')
            break