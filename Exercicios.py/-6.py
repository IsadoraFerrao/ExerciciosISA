'''Faça um programa que leia cinco números e mostre o maior e menor deles.'''

lista = []
maior = 0
menor = 0

for c in range(0,5):
    n = int(input(f'Digite o número na {c}º posição: '))
    lista.append(n)
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'{lista}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
