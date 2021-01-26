ficha = []
while True:
    nome = (input('Qual é o nome?'))
    nota = float(input('Qual é a nota ?'))
    nota01 = float(input('Qual é a segunda nota ?'))
    media = (nota + nota01) / 2
    ficha.append([nome, [nota, nota01], media])
    p = str(input('Deseja continuar?')).upper()[0]
    if p == 'N':
        break
print('-=' * 30)
print('{:<4}{:<10}{:>8}'.format('NO', 'Nome', 'Media'))
print('-' * 26)
for i, a in enumerate(ficha):
    print('{:<4}{:<10}{:>8.1f}'.format(i, a[0], a[2]))
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno?(999 interompe)'))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) - 1:
        print('Notas de {} são {}'.format(ficha[opc][0], ficha[opc][1]))
print('<<<VOLTE SEMPRE>>>')
