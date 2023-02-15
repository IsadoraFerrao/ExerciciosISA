'''Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
1: Quantos espaços em branco existem na frase.
2: Quantas vezes aparecem as vogais A,E,I,O,U...'''

vogais = 0
frase = str(input('Digite uma frase: ')).upper()
print(f'Na frase "{frase}" temos {frase.count(" ")} espaços vazios,',end=' ')
for letra in frase:
    if letra in 'AEIOU':
        vogais += 1
print(f'e temos {vogais} vogais.')