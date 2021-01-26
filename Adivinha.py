import random

computador = random.randint(0, 10)
print('pensei em um numero entre 0 e 10 ')
print('Sera que você consegue acertar ? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite um numero de 0 a 10\n '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais...tente mais uma vez')
        elif jogador < computador:
            print('menos... tente outra vez')
print('Voce acertou com {} palpites'.format(palpite))


from random import randint
numsorteado = randint(1, 10)
print('Tente adivinhar um número sorteado de 1 à 10...')
jogada = int(input('Qual o seu palpite: '))
cont = 1
while jogada != numsorteado:
    if jogada > numsorteado:
        print('Informe um valor menor...')
    elif jogada < numsorteado:
        print('Informe um valor maior...')
    jogada = int(input('Tente novamente: '))
    cont += 1
print('Parabéns, com {} tentativas você venceu!!!' .format(cont))