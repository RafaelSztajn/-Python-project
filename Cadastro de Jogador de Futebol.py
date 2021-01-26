nome = input('Qual é o nome do jogador? ')
partidas = int(input('Quantas partidas ele jogou ? '))
campeonato = {'Nome': nome, 'Partidas': partidas}
s = 0
for c in range(1, partidas + 1):
    golss = int(input('Quantos gols na {} º partida ? '.format(c)))
    s += golss
    campeonato['Total de gols das partida'] = s
print('-=' * 30)
print('!!!Resultado!!!')
for i, v in campeonato.items():
    print('{} {}'.format(i, v))
print('-=' * 30)
