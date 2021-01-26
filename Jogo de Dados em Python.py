import random
import operator

f = 0
jogo = {'Jogador1 ': random.randint(1, 6),
        'Jogador2 ': random.randint(1, 6),
        'Jogador3 ': random.randint(1, 6),
        'Jogador4 ': random.randint(1, 6),
        'Jogador5 ': random.randint(1, 6), }
print('-=' * 30)
for i, d in jogo.items():
    print('{} tirou {} no dado'.format(i, d))
print('-=' * 30)
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('-=' * 30)
print('RANKING')
print('-=' * 30)
for i, v in ranking:
    f += 1
    print('{}º {}-{} '.format(f, i, v))
