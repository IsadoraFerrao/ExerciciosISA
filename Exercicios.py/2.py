'''Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário 
de trás pra frente utilizando somente letras maiúsculas.
e também mostre o nome na vertical.'''

nome = str(input('Digite seu nome: ')).upper()
for i in range(len(nome)):
    c = nome[len(nome) - 1 - i]
    print(c)