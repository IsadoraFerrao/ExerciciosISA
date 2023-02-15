'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e 
a soma entre eles.'''
lista = []
soma = 0

print('-='*30)
print('Se digitar 999 o programa irá encerrar...')
print('=-'*30)
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    lista.append(n)

print(f'A soma entre os números {sum(lista)}')
print(f'O menor entre os números {min(lista)}')
print(f'O maior entre os números {max(lista)}')